"""Switch-point statistics from the SADiLaR soap-opera English-isiZulu transcripts (research-only data: only AGGREGATES are written).
Usage: python cs_stats.py ../data/raw/soapies_engzul/balanced_engzul.xml ../data/synth_text/soap_engzul_stats.json
"""
import sys, json, collections
import xml.etree.ElementTree as ET

root = ET.parse(sys.argv[1]).getroot()
utts = []
for u in root.iter("utterance"):
    segs = [(s.findtext("lang_id", "").strip(), (s.findtext("transcription") or "").strip(), float(s.findtext("duration") or 0)) for s in u.iter("utterance_segment")]
    segs = [s for s in segs if s[1]]
    if segs: utts.append(segs)

lang_words, lang_dur = collections.Counter(), collections.Counter()
types = collections.Counter(); nseg_hist = collections.Counter(); seg_len = collections.defaultdict(list)
pairs = collections.Counter(); first_lang = collections.Counter(); last_lang = collections.Counter()
eng_in_zul_w = collections.Counter(); zul_after_eng_w = collections.Counter(); eng_start = collections.Counter()
eng_seg_len_in_cs = []
for segs in utts:
    langs = [l for l, _, _ in segs]
    for l, t, d in segs: lang_words[l] += len(t.split()); lang_dur[l] += d; seg_len[l].append(len(t.split()))
    nseg_hist[min(len(segs), 6)] += 1
    uniq = set(langs)
    types["mono_" + langs[0] if len(uniq) == 1 else "mixed"] += 1
    if len(uniq) > 1:
        first_lang[langs[0]] += 1; last_lang[langs[-1]] += 1
        for (a, _, _), (b, tb, _) in zip(segs, segs[1:]):
            if a != b: pairs[f"{a}->{b}"] += 1
        for l, t, _ in segs:
            if l == "eng":
                w = t.split(); eng_seg_len_in_cs.append(len(w)); eng_in_zul_w[" ".join(w) if len(w) <= 2 else "<long>"] += 1
        for l, t, _ in segs:
            if l == "eng": eng_start[t.split()[0]] += 1
n_mixed = types["mixed"]
total_words = sum(lang_words.values())
out = {
    "n_utterances": len(utts), "hours_by_lang_ms": {k: round(v / 3.6e6, 2) for k, v in lang_dur.items()},
    "word_share": {k: round(v / total_words, 3) for k, v in lang_words.items()},
    "utterance_types": dict(types), "mixed_share": round(n_mixed / len(utts), 3),
    "segments_per_utt_hist": dict(sorted(nseg_hist.items())),
    "switch_direction_counts": dict(pairs.most_common(10)),
    "mixed_utts_starting_lang": dict(first_lang), "mixed_utts_ending_lang": dict(last_lang),
    "median_words_per_segment": {k: sorted(v)[len(v) // 2] for k, v in seg_len.items()},
    "english_segments_in_mixed_utts": {"n": len(eng_seg_len_in_cs), "share_1_word": round(sum(x == 1 for x in eng_seg_len_in_cs) / max(1, len(eng_seg_len_in_cs)), 3),
                                        "share_2_3_words": round(sum(2 <= x <= 3 for x in eng_seg_len_in_cs) / max(1, len(eng_seg_len_in_cs)), 3),
                                        "share_4plus_words": round(sum(x >= 4 for x in eng_seg_len_in_cs) / max(1, len(eng_seg_len_in_cs)), 3)},
    "top_english_single_or_double_word_insertions": dict(eng_in_zul_w.most_common(40)),
    "top_english_segment_initial_words": dict(eng_start.most_common(30)),
}
json.dump(out, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in out.items() if not k.startswith("top_")}, indent=1)); print("top English insertions:", list(out["top_english_single_or_double_word_insertions"].items())[:25])
