"""Run: python test_textgen.py   (plain asserts; also works under pytest)"""
import re, textgen as T, morph as M, lexicon as L

def test_prefixes():
    assert M.nominal("pills", "5/6", "pl") == "ema-[[pills]]"
    assert M.nominal("test", "9/10", "sg") == "i-[[test]]" and M.nominal("test", "9/10", "pl") == "ti-[[test]]"
    assert M.nominal("nurse", "1a/2a", "sg") == "[[nurse]]" and M.nominal("nurses", "1a/2a", "pl") == "bo-[[nurses]]"

def test_agreement_follows_class():
    assert M.agree("5/6", "sg", "poss1") == "lami" and M.agree("9/10", "sg", "poss1") == "yami"
    assert M.agree("5/6", "pl", "poss1") == "ami" and M.agree("9/10", "pl", "poss1") == "tami"
    assert M.agree("5/6", "sg", "sc") == "li" and M.agree("5/6", "pl", "sc") == "a"

def test_every_clause_realises():
    import random
    for c in T.CLAUSES:
        for s in range(30):
            out = T.realize(c, random.Random(s))
            assert "{" not in out and "}" not in out, (c, out)
            assert out.count("[[") == out.count("]]")

def test_agreement_in_output():
    # one noun class per mention: poss on a class-5 'prescription' must be lami, on class-9 'medication' yami
    import random
    for s in range(200):
        out = T.realize("{ITEM#a:sg:noun} {ITEM#a:sg:poss1}", random.Random(s))
        stem = re.search(r"\[\[(.+?)\]\]", out).group(1)
        want = M.agree(L.NOUNS["ITEM"][stem]["cls"], "sg", "poss1")
        assert out.endswith(" " + want), out

def test_corpus_properties():
    rows = T.generate(1500, seed=3)
    assert len(rows) == 1500 and len({r["text"] for r in rows}) == 1500
    assert {r["switch_type"] for r in rows} == {m for m, _ in T.MODES}
    src = lambda rs: {x for r in rs for x in r["source"]}
    assert not src([r for r in rows if r["split"] == "train"]) & src([r for r in rows if r["split"] == "val"]), "clause leaked across splits"
    assert all("]] [[" not in r["tagged"] for r in rows)
    assert all(re.fullmatch(r"[A-Za-z0-9' \-]+", r["text"]) for r in rows), [r["text"] for r in rows if not re.fullmatch(r"[A-Za-z0-9' \-]+", r["text"])][:3]
    # switch points: dm_initial sentences start with an English DM; tag sentences end in an English tag
    for r in rows:
        if r["switch_type"] == "dm_initial": assert r["segments"][0]["lang"] == "eng"
        if r["switch_type"] == "tag": assert r["segments"][-1]["lang"] == "eng"
    assert T.generate(50, seed=3) == T.generate(50, seed=3)

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"): f(); print("ok", n)
