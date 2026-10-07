"""Morphotactic siSwati-English code-switched TEXT generator (no audio; audio needs a GPU/TTS step run elsewhere).

What it does beyond the old synth/grammar.py:
  * English loan nouns get a noun-class prefix chosen from the word's class (i-/ema-, i-/ti-, bo-, ...): "ema-[[pills]]".
  * Agreement is generated from that class, so possessives / concords / demonstratives / 'new' follow the noun
    ("i-blood test yami ibe ..." but "i-viral load lami libe ..." if the word were class 5).
  * Switch points are explicit and logged per sentence in `switch_type`:
      insertion      English noun/verb stem inside a siSwati clause (intra-word prefix + stem)
      dm_initial     English discourse marker, then siSwati clause           ("so ngicela ...")
      conj_inter     siSwati clause, English conjunction, siSwati clause      ("... but ...")
      alternational  siSwati clause, optional English conjunction, full English clause
      eng_first      full English clause, then siSwati clause
      tag            siSwati clause + English tag                             ("... you know")
  * Train/val split is by CLAUSE, so no clause in val appears in train.

Template syntax (see CLAUSES): {SLOT:num:attr} for class-bearing nouns (num = sg|pl; attr = noun|poss1|poss2|dem|sc|new),
{SLOT:bare} for the bare English stem, {SLOT} for plain slots, {V:inf|subj} for verb loans. `#id` after the slot name
(e.g. {TEST#a:sg:noun}) makes repeated mentions share one lexical choice.

Usage: python textgen.py --n 2000 --out ../data/synth_text --seed 0
NOTE: every siSwati clause, class assignment and concord below is unreviewed by a native speaker.
"""
import argparse, json, os, random, re
import lexicon as L, morph as M

CLAUSES = [
    "{TIME} ngitawuya {PLACE:loc}",
    "{STAFF:bare} utsite ngitsatse {ITEM#a:sg:dem} {ITEM#a:bare} kabili ngelilanga",
    "ngikhohliwe kutsatsa {DRUG#a:pl:noun} {DRUG#a:pl:poss1} {TIME}",
    "{STAFF:bare} ucele kutsi ngente {TEST#a:sg:noun}",
    "{TEST#a:sg:noun} {TEST#a:sg:poss1} {TEST#a:sg:sc}be {RESULT} nyalo",
    "ngicela ungiphe {ITEM#a:sg:noun} {ITEM#a:sg:new}",
    "{WHO} une {SYMP} kusukela {TIME}",
    "ngiva buhlungu ngine {SYMP} {DUR}",
    "kufanele ugcine {ITEM#a:sg:noun} {ITEM#a:sg:poss2}",
    "sicela ulete {ITEM#a:sg:noun} {ITEM#a:sg:poss2} nawuta {PLACE:loc}",
    "ngitsenge {DRUG#a:pl:noun} {PLACE:loc}",
    "{RES#a:pl:noun} {RES#a:pl:poss1} {RES#a:pl:sc}lungile yini",
    "ngisebenta {PLACE:loc} {TIME}",
    "le mali ye-{MISC:bare} iyabiza kakhulu",
    "{WHO} une {COND}",
    "ngitsatsa {ITEM#a:sg:noun} {ITEM#a:sg:poss1} ngesikhatsi sonkhe",
    "{TEST#a:sg:noun} {TEST#a:sg:sc}tawentiwa {DAY}",
    "ngicela u-{V:bare} kahle ngobe angiva",
    "ngicela {V:subj} {ITEM#a:sg:dem} {ITEM#a:bare}",
    "ngiyafuna {V:inf} {APPT#a:sg:noun} ye-{REL:bare}",
    "ngiyacela ungibhalele {ITEM#a:sg:noun}",
    "kufanele udle kahle ngaphambi kwekutsatsa {DRUG#a:pl:noun}",
    "{STAFF:bare} utsite ngibuye {REL:bare}",
    "angitfolanga {ITEM#a:sg:noun} {ITEM#a:sg:poss1} {PLACE:loc}",
    "ngicela {V:subj} {TEST#a:sg:noun} {TEST#a:sg:poss1}",
    "ngiphatsa kabi ngobe nginesifo se-{COND:bare}",
    "ngitsatsa {DRUG#a:pl:noun} {TIME} nakusihlwa",
    "{TEST#a:sg:noun} ibonisa kutsi une {COND}",
    "{WHO} utsatsa {DRUG#a:pl:noun} njalo {TIME}",
    "sidzinga {ITEM#a:sg:noun} {ITEM#a:sg:new} {TIME}",
    "{APPT#a:sg:noun} {APPT#a:sg:poss1} {APPT#a:sg:sc}fika {DAY}",
    "ngifuna kubona {STAFF:bare} {DAY}",
    "{STAFF:bare} ubhale {ITEM#a:sg:noun} {ITEM#a:sg:new}",
    "{MISC#a:sg:noun} {MISC#a:sg:sc}bekade {MISC#a:sg:sc}nde {TIME}",
    "umntfwana wami udzinga {ITEM#a:sg:noun} {ITEM#a:sg:new}",
    "ngelula {PLACE:loc} {TIME}",
    "ngitfole {RES#a:pl:noun} {RES#a:pl:poss1} {TIME}",
    "sitawuhlangana {DAY} emva kwe-{MISC:bare}",
    "ngiyakhumbula kutsatsa {DRUG#a:pl:noun} {DRUG#a:pl:poss1}",
    "kunayo {STAFF:bare} lapha {PLACE:loc} lamuhla",
    "{WHO} ukhale {SYMP} {TIME}",
    "ngitsenge {ITEM#a:sg:noun} {ITEM#a:sg:poss1} kuphela",
    "ngifike nge-{VEH:bare} {TIME}",
    "ngilethe {ITEM#a:sg:noun} ne-{ITEM#b:bare}",
    "ngiphume {PLACE:loc} emva kwe-{TEST:bare}",
    "ngisebente ne-{STAFF:bare} lamuhla",
]

PLURAL_STEM = lambda s: s + "s"
P_NATIVE = 0.5     # probability a stem with an attested nativised form (lexicon.NATIVISED) is written in that form
SLOT_RE = re.compile(r"\{(\w+)(?:#(\w+))?(?::(\w+))?(?::(\w+))?\}")


def realize(clause, rng):
    """Fill a clause template -> tagged string, English spans in [[ ]]."""
    chosen = {}

    def pick(name, ident):
        key = (name, ident)
        if key not in chosen:
            if name in L.NOUNS: stem = rng.choice(sorted(L.NOUNS[name])); chosen[key] = (stem, L.NOUNS[name][stem]["cls"])
            elif name in L.BARE: chosen[key] = (rng.choice(L.BARE[name]), None)
            elif name in L.SSW: chosen[key] = (rng.choice(L.SSW[name]), None)
            elif name == "V": chosen[key] = (rng.choice(L.VERBS), None)
            else: raise KeyError(f"unknown slot {name}")
        return chosen[key]

    def native(name, ident, stem, field):
        """Nativised form for this slot mention (decided once per mention so repeats agree), or None."""
        nat = L.NATIVISED.get(stem)
        if not nat or field not in nat: return None
        key = (name, ident, "nat")
        if key not in chosen: chosen[key] = rng.random() < P_NATIVE
        return nat[field] if chosen[key] else None

    def fill(m):
        name, ident, f1, f2 = m.group(1), m.group(2), m.group(3), m.group(4)
        stem, cls = pick(name, ident)
        if name in L.SSW: return stem
        if name in L.BARE: return f"[[{stem}]]"
        if name == "V":
            if f1 == "bare": return f"[[{stem}]]"
            return native(name, ident, stem, f1) or M.verb(stem, f1)
        if f1 == "bare": return native(name, ident, stem, "sg") or f"[[{stem}]]"
        if f1 == "loc": return native(name, ident, stem, "loc") or f"ku-[[{stem}]]"
        num, attr = f1, f2
        if attr == "noun": return native(name, ident, stem, num) or M.nominal(PLURAL_STEM(stem) if num == "pl" else stem, cls, num)
        return M.agree(cls, num, attr)

    return SLOT_RE.sub(fill, clause)


def merge_english(tagged):
    """Adjacent English spans are one span: '[[and then]] [[I left]]' -> '[[and then I left]]'."""
    return re.sub(r"\]\] \[\[", " ", tagged)


def plain(tagged):
    return tagged.replace("[[", "").replace("]]", "")


def segments(tagged):
    """Language segments for a later TTS step. A siSwati prefix glued to an English stem ('ema-' + 'pills') is flagged glue."""
    segs, pos = [], 0
    for m in re.finditer(r"\[\[(.+?)\]\]", tagged):
        pre = tagged[pos:m.start()]
        glued = bool(pre) and not pre.endswith(" ")
        if pre.strip():
            head, _, tail = pre.rpartition(" ") if glued else (pre, "", "")
            if glued:
                if head.strip(): segs.append({"lang": "ssw", "text": head.strip()})
                segs.append({"lang": "ssw", "text": tail, "glue_next": True})
            else: segs.append({"lang": "ssw", "text": pre.strip()})
        segs.append({"lang": "eng", "text": m.group(1)}); pos = m.end()
    if tagged[pos:].strip(): segs.append({"lang": "ssw", "text": tagged[pos:].strip()})
    return segs


def split_clauses(items, rng, val_frac):
    idx = list(range(len(items))); rng.shuffle(idx)
    n_val = max(1, round(len(items) * val_frac))
    return {"val": [items[i] for i in idx[:n_val]], "train": [items[i] for i in idx[n_val:]]}


# weights informed by the soap-opera English-isiZulu transcripts (data/synth_text/soap_engzul_stats.json): 40% of utterances mixed,
# 48% of mixed utterances have 3+ language segments, English segments are mostly 1-3 words. Real siSwati-only and English-only
# utterances are included so the model does not learn that every utterance is code-switched.
MODES = [("mono_ssw", 0.15), ("mono_eng", 0.05), ("insertion", 0.25), ("dm_initial", 0.16), ("conj_inter", 0.10), ("multi", 0.10),
         ("alternational", 0.07), ("eng_first", 0.04), ("tag", 0.08)]


def make_sentence(mode, pool_c, pool_e, rng, pool_r=None, pool_m=None):
    if mode == "mono_ssw":
        s = rng.choice(pool_r); return mode, s, [s]
    if mode == "mono_eng":
        e = rng.choice(pool_m or pool_e); return mode, f"[[{e}]]", [e]
    c1 = rng.choice(pool_c)
    if mode == "multi":      # 3+ segments: ssw clause, English conjunction, ssw clause, English tag
        c2 = rng.choice(pool_c)
        return mode, f"{realize(c1, rng)} [[{rng.choice(L.CONJ_EN)}]] {realize(c2, rng)} [[{rng.choice(L.DM_TAG)}]]", [c1, c2]
    if mode == "insertion":
        return "insertion", realize(c1, rng), [c1]
    if mode == "dm_initial":
        return mode, f"[[{rng.choice(L.DM_INITIAL)}]] {realize(c1, rng)}", [c1]
    if mode == "conj_inter":
        c2 = rng.choice(pool_c)
        return mode, f"{realize(c1, rng)} [[{rng.choice(L.CONJ_EN)}]] {realize(c2, rng)}", [c1, c2]
    if mode == "alternational":
        e = rng.choice(pool_e); conj = rng.choice(L.CONJ_EN + [""])
        return mode, f"{realize(c1, rng)} {f'[[{conj}]] ' if conj else ''}[[{e}]]", [c1, e]
    if mode == "eng_first":
        e = rng.choice(pool_e)
        return mode, f"[[{e}]] {realize(c1, rng)}", [c1, e]
    if mode == "tag":
        return mode, f"{realize(c1, rng)} [[{rng.choice(L.DM_TAG)}]]", [c1]
    raise ValueError(mode)


def load_real(raw_dir, lang="ssw", max_n=20000, seed=0):
    """Short real sentences (SADiLaR Monolingual siSwati / Bilingual EN-SS corpora, CC BY 4.0) for monolingual utterances.
    Lowercased, punctuation stripped, ASCII only, 4-9 words, no digits/acronyms/hyphens."""
    import glob
    f = glob.glob(os.path.join(raw_dir, "mono*", "*.ss.txt")) if lang == "ssw" else glob.glob(os.path.join(raw_dir, "bilingual*", "*BilingualCorpus*.en.txt"))
    if not f: return None
    out = []
    for line in open(f[0], encoding="utf-8", errors="replace"):
        if re.search(r"[0-9]|\b[A-Z]{2,}\b|-", line): continue
        s = re.sub(r"\s+", " ", re.sub(r"[^A-Za-z' ]", " ", line)).strip().lower()
        if 4 <= len(s.split()) <= 9 and re.fullmatch(r"[a-z' ]+", s): out.append(s)
    out = sorted(set(out)); random.Random(seed).shuffle(out)
    return out[:max_n]


def generate(n, seed=0, val_frac=0.1, max_tries=50, real_ssw=None, real_eng=None, p_native=None):
    global P_NATIVE
    if p_native is not None: P_NATIVE = p_native
    rng = random.Random(seed)
    cl, ec = split_clauses(CLAUSES, rng, val_frac), split_clauses(L.ESHORT + L.ECLAUSES, rng, val_frac)
    ec = {k: [e for e in v for _ in range(3 if e in L.ESHORT else 1)] for k, v in ec.items()}   # weight short segments 3:1, AFTER the split
    rl = split_clauses(real_ssw, rng, val_frac) if real_ssw else None
    if real_eng: ec_mono = split_clauses(real_eng, rng, val_frac)
    modes = [(m, w) for m, w in MODES if rl or m != "mono_ssw"]
    out, seen = [], set()
    for split, quota in (("val", max(1, round(n * val_frac))), ("train", n - max(1, round(n * val_frac)))):
        got, tries = 0, 0
        while got < quota and tries < quota * max_tries:
            tries += 1
            mode = rng.choices([m for m, _ in modes], [w for _, w in modes])[0]
            mode, tagged, src = make_sentence(mode, cl[split], ec[split], rng, rl[split] if rl else None, ec_mono[split] if real_eng else None)
            tagged = merge_english(tagged)
            text = plain(tagged)
            if text in seen: continue
            seen.add(text); got += 1
            eng_w = sum(len(s["text"].split()) for s in segments(tagged) if s["lang"] == "eng")
            out.append({"id": f"cst{len(out):06d}", "split": split, "switch_type": mode, "text": text, "tagged": tagged,
                        "segments": segments(tagged), "n_words": len(text.split()), "n_eng_words": eng_w, "source": src, "synthetic": True})
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2000); ap.add_argument("--out", default="../data/synth_text"); ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    raw = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "raw", "ssw_text")
    rows = generate(a.n, a.seed, real_ssw=load_real(raw, "ssw", seed=a.seed), real_eng=load_real(raw, "eng", seed=a.seed))
    with open(os.path.join(a.out, "cs_text.jsonl"), "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    rng = random.Random(a.seed + 1)
    with open(os.path.join(a.out, "review_sample.tsv"), "w") as f:     # for the native-speaker reviewer
        f.write("id\tswitch_type\ttagged\tcorrect_text\tnotes\n")
        for r in rng.sample(rows, min(120, len(rows))): f.write(f"{r['id']}\t{r['switch_type']}\t{r['tagged']}\t\t\n")
    with open(os.path.join(a.out, "review_lexicon.tsv"), "w") as f:     # class assignments to confirm
        f.write("slot\tenglish_stem\tclass_pair\tconf\tsg\tpl\tcorrect_class\tnotes\n")
        for slot, d in L.NOUNS.items():
            for stem, v in sorted(d.items()):
                f.write(f"{slot}\t{stem}\t{v['cls']}\t{v['conf']}\t{M.nominal(stem, v['cls'], 'sg')}\t{M.nominal(PLURAL_STEM(stem), v['cls'], 'pl')}\t\t\n")
    from collections import Counter
    c = Counter(r["switch_type"] for r in rows); ew = sum(r["n_eng_words"] for r in rows); w = sum(r["n_words"] for r in rows)
    print(f"{len(rows)} sentences ({sum(r['split']=='val' for r in rows)} val); English word share {ew/w:.0%}; switch types {dict(c)}")
