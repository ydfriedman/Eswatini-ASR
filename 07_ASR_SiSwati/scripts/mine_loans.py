"""Mine real siSwati text (SADiLaR Monolingual + Bilingual EN-SS corpora, CC BY 4.0) for how English loan stems are written.
Writes aggregate evidence only: data/synth_text/loan_evidence.tsv (per generator stem) and loan_prefix_totals.json.
Usage: python mine_loans.py   (reads ../data/raw/ssw_text, ../synth/lexicon.py)"""
import re, glob, json, collections, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "synth"))
import lexicon as L

RAW = os.path.join(HERE, "..", "data", "raw", "ssw_text"); OUT = os.path.join(HERE, "..", "data", "synth_text")
files = glob.glob(f"{RAW}/mono*/*.ss.txt") + glob.glob(f"{RAW}/bilingual*/*BilingualCorpus*.ss.txt")
txt = "\n".join(open(f, encoding="utf-8", errors="replace").read() for f in files)
tok = collections.Counter(re.findall(r"[A-Za-z][A-Za-z'\-]*", txt.lower()))

pre = re.compile(r"\b(i|ema|ti|tin|in|im|imi|um|bo|ku|se|ye|we|ne|nge|le|kwe|na)-([a-z]{4,})\b")
prefix_totals = collections.Counter(m.group(1) for m in pre.finditer(txt.lower()))
json.dump({"n_tokens": sum(tok.values()), "prefix_totals": dict(prefix_totals.most_common())}, open(f"{OUT}/loan_prefix_totals.json", "w"), indent=1)

stems = {}
for slot, d in L.NOUNS.items():
    for s, v in d.items(): stems[s] = (slot, v["cls"])
for slot, lst in L.BARE.items():
    for s in lst: stems.setdefault(s, (slot, "bare"))
rows = []
for s, (slot, cls) in sorted(stems.items()):
    w = s.lower().replace(" ", "-") if " " in s else s.lower()
    if " " in s: bare = txt.lower().count(s.lower())          # multi-word: count phrase only
    else: bare = tok.get(w, 0) + tok.get(w + "s", 0)
    pref = {p: tok.get(f"{p}-{w}", 0) + tok.get(f"{p}-{w}s", 0) for p in ("i", "ema", "ti", "ku", "ne", "se", "nge", "kwe", "ye")}
    rows.append((slot, s, cls, bare, *pref.values()))
with open(f"{OUT}/loan_evidence.tsv", "w") as f:
    f.write("slot\tstem\tgenerator_class\tbare_count\ti-\tema-\tti-\tku-\tne-\tse-\tnge-\tkwe-\tye-\n")
    for r in rows: f.write("\t".join(map(str, r)) + "\n")
seen = sum(1 for r in rows if sum(r[3:]) > 0)
print(f"{len(files)} files, {sum(tok.values()):,} tokens; {seen}/{len(rows)} generator stems attested in any form")
print("prefix totals:", dict(prefix_totals.most_common(10)))

# evidence for the nativised-form table (lexicon.NATIVISED): how often written siSwati uses the nativised form vs the English word
with open(f"{OUT}/native_evidence.tsv", "w") as f:
    f.write("english\tform_type\tnativised_form\tcount_nativised\tcount_english_any_form\n")
    for eng, forms in L.NATIVISED.items():
        eng_n = sum(c for t, c in tok.items() if re.fullmatch(r"(?:[a-z]+-)?" + re.escape(eng.lower()) + r"(?:s|ed|ing)?", t))
        for ftype, form in forms.items():
            f.write(f"{eng}\t{ftype}\t{form}\t{tok.get(form, 0)}\t{eng_n}\n")
print(open(f"{OUT}/native_evidence.tsv").read())
