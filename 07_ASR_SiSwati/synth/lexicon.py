"""Lexicon for the morphotactic generator. conf: 'default' = 5/6 (i-/ema-), the pattern real siSwati text overwhelmingly uses for English loans (see data/synth_text/loan_evidence.tsv:
ema- 916 vs ti- 2 in 2.2M tokens); 'guess' = author's choice with no evidence (persons only); 
'ok' would mean a native speaker confirmed it (none are, yet). Plain data; edit freely."""

# English noun -> noun-class pair. Default 5/6 (i-/ema-); persons 1a/2a.
def _n(words, cls="5/6"): return {w: {"cls": cls, "conf": "default" if cls == "5/6" else "guess"} for w in words}

NOUNS = {
    "ITEM":  {**_n(["prescription", "sick note", "referral letter", "lab form", "appointment card", "identity card", "clinic card"]),
              **_n(["medication", "treatment", "medicine"])},
    "TEST":  {**_n(["blood test", "viral load", "CD4 count", "TB test", "HIV test", "pregnancy test", "sugar test", "x-ray", "urine test"]),
              **_n(["scan"])},
    "DRUG":  _n(["pill", "tablet", "antibiotic", "painkiller", "ARV"]),     # singular stems; plural via ema-
    "PLACE": _n(["clinic", "hospital", "pharmacy", "laboratory", "health centre"]),
    "STAFF": _n(["nurse", "doctor", "pharmacist", "counsellor", "lab technician"], "1a/2a"),
    "APPT":  _n(["appointment"]),
    "RES":   _n(["result", "condom", "side effect"]),
    "MISC":  {**_n(["queue", "message", "refill", "booking", "form", "taxi", "phone"]), **_n(["transport"])},
}

# slots that stay bare English (no prefix): after 'une' (has), 'se' (of), etc.
BARE = {
    "SYMP":   ["fever", "headache", "cough", "diarrhoea", "rash", "chest pain", "back pain", "nausea", "dizziness", "high blood pressure"],
    "COND":   ["diabetes", "tuberculosis", "hypertension", "asthma", "malaria", "anaemia", "epilepsy"],
    "VEH":    ["taxi", "bus", "ambulance"],
    "RESULT": ["negative", "positive", "normal", "high", "low", "undetectable"],
    "REL":    ["next week", "next month", "this week", "tomorrow morning", "after lunch"],
}

# siSwati-side slots (unreviewed)
SSW = {
    "DAY":  ["ngelisontfo", "ngeMsombuluko", "ngelesibili", "ngelesitsatfu", "ngelesine", "ngelesihlanu", "ngeMgcibelo"],
    "DUR":  ["emalanga lamabili", "emalanga lamatsatfu", "emaviki lamabili", "emaviki lamane", "inyanga", "emaviki lamatsatfu"],
    "WHO":  ["umntfwana wami", "make wami", "babe wami", "umnakwetfu", "umkami", "indvodzana yami"],
    "TIME": ["ekuseni", "emini", "kusasa", "lamuhla", "izolo", "ebusuku"],
}

VERBS = ["explain", "check", "book", "refill", "phone", "confirm", "cancel", "collect", "submit"]

# English discourse markers that speakers keep when switching (clause-initial) and tag phrases (clause-final)
DM_INITIAL = ["so", "but", "and", "okay", "right", "sure", "no", "well", "actually", "sorry", "please", "listen", "if", "why", "look"]   # most frequent English segment starts in the soap-opera transcripts
DM_TAG     = ["you know", "right", "okay", "sure", "hey"]
CONJ_EN    = ["but", "so", "and", "because", "and then", "or"]

# whole English clauses used for alternational switches (switch point at the clause boundary)
# short English segments (real English segments in mixed utterances: 55% one word, 23% 2-3 words, 22% 4+)
ESHORT = ["no problem", "of course", "I know", "it is fine", "not now", "thank you", "I am sorry", "just wait", "it is okay", "I understand"]
ECLAUSES = [
    "I waited for two hours", "they said I must come back", "I did not get my results",
    "the queue was very long", "I do not have transport", "I took my pills this morning",
    "I will call you tomorrow", "it is not working", "I have a bad headache", "I need to see the doctor",
    "I lost my clinic card", "the nurse is not here",
]

# Established nativised forms (siSwati-spelled loans) that written siSwati prefers over the English word. Counts are occurrences in the
# SADiLaR siSwati text (2.2M tokens; formal register) - see ../data/synth_text/native_evidence.tsv. Spoken clinic speech probably uses
# English more than written text does, so the generator uses these with probability P_NATIVE (textgen.py), not always.
# sg/pl: noun forms; loc: locative ('at the X'); inf: infinitive. Missing key -> fall back to the English stem.
NATIVISED = {
    "doctor":   {"sg": "dokotela", "pl": "bodokotela"},                       # dokotela 281, bodokotela 152 vs 'doctors' 2
    "nurse":    {"sg": "nesi"},                                              # nesi 9 vs nurse 2 (weak evidence)
    "condom":   {"sg": "ikhondomu", "pl": "emakhondomu"},                     # 21 / 18 vs English 0
    "hospital": {"sg": "sibhedlela", "pl": "tibhedlela", "loc": "esibhedlela"},   # 79 / 161 / 305 vs 'hospital' 12
    "cancel":   {"inf": "kukhansela"},                                        # kukhansela 40, khansela 33 vs cancel 1
}
