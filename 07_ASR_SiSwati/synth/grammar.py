"""Frame + lexicon grammar for synthetic siSwati-matrix / English-embedded clinic utterances.

Frames are siSwati text with English spans in [[...]]. {SLOT} tokens expand from LEX; a slot inside [[ ]] is English,
outside is siSwati. Frames are adapted from data/codeswitch_sentences.tsv (authored by Claude, NOT native-reviewed;
agreement/orthography must be checked by a native speaker before any scale-up). Everything here is plain data so a
reviewer can edit it without touching code.
"""
import random, re

LEX = {
    # English content words/phrases that clinic speakers typically keep in English
    "ITEM":   ["prescription", "medication", "treatment", "medicine", "sick note", "referral letter", "lab form", "appointment card", "identity card", "clinic card"],
    "TEST":   ["blood test", "viral load", "CD4 count", "TB test", "HIV test", "pregnancy test", "sugar test", "scan", "x-ray", "urine test"],
    "SYMP":   ["fever", "headache", "cough", "diarrhoea", "rash", "chest pain", "back pain", "nausea", "dizziness", "high blood pressure"],
    "DRUG":   ["pills", "tablets", "ARVs", "antibiotics", "painkillers", "insulin", "cotrimoxazole", "TB treatment"],
    "PLACE":  ["clinic", "hospital", "pharmacy", "laboratory", "outpatient department", "health centre"],
    "STAFF":  ["nurse", "doctor", "pharmacist", "counsellor", "lab technician", "community health worker"],
    "COND":   ["diabetes", "tuberculosis", "hypertension", "asthma", "malaria", "anaemia", "epilepsy"],
    "MISC":   ["side effects", "queue", "transport", "message", "lunch", "taxi", "phone", "form", "refill", "booking"],
    "RESULT": ["negative", "positive", "normal", "high", "low", "undetectable"],
    "REL":    ["next week", "next month", "this week", "tomorrow morning", "after lunch"],
    # siSwati-side slots (day names, durations, relatives) - to be checked by native speaker
    "DAY":    ["ngelisontfo", "ngeMsombuluko", "ngelesibili", "ngelesitsatfu", "ngelesine", "ngelesihlanu", "ngeMgcibelo"],
    "DUR":    ["emalanga lamabili", "emalanga lamatsatfu", "emaviki lamabili", "emaviki lamane", "inyanga", "emaviki lamatsatfu"],
    "WHO":    ["umntfwana wami", "make wami", "babe wami", "umnakwetfu", "umkami", "indvodzana yami"],
    "TIME":   ["ekuseni", "emini", "kusasa", "lamuhla", "izolo", "ebusuku"],
}

FRAMES = [
    "{TIME} ngitawuya ku [[{PLACE}]]",
    "[[{STAFF}]] utsite ngitsatse le [[{ITEM}]] kabili ngelilanga",
    "ngikhohliwe kutsatsa ema[[{DRUG}]] ami {TIME}",
    "i [[appointment]] yami lelandzelako ingu [[{REL}]] {DAY}",
    "[[{STAFF}]] ucele kutsi ngente i [[{TEST}]]",
    "i [[{TEST}]] yami ibe [[{RESULT}]] nyalo",
    "ngicela ungiphe i [[{ITEM}]] lensha",
    "{WHO} une [[{SYMP}]] kusukela {TIME}",
    "ngiva buhlungu ngine [[{SYMP}]] {DUR}",
    "kufanele ugcine i [[{ITEM}]] yakho",
    "sicela ulete i [[{ITEM}]] yakho nawuta ku [[{PLACE}]]",
    "ngitsenge ema[[{DRUG}]] ku [[{PLACE}]]",
    "ema[[results]] ami alungile yini",
    "ngisebenta ku [[{PLACE}]] ngingu [[{STAFF}]]",
    "le mali ye [[{MISC}]] iyabiza kakhulu",
    "{WHO} une [[{COND}]]",
    "sitaku [[phone]] nangabe ema[[results]] sewafikile",
    "ngitsatsa i [[{ITEM}]] yami ngesikhatsi sonkhe",
    "i [[{MISC}]] beyinde kakhulu {TIME}",
    "ngi [[busy]] kakhulu kulelisontfo",
    "utsite i [[{TEST}]] itawentiwa {DAY}",
    "ngicela u [[explain]] kahle ngobe angiva",
    "umntfwana udzinga i [[vaccine]] yakhe yesibili",
    "ngine [[{MISC}]] ngema[[{DRUG}]] lamasha",
    "i [[{STAFF}]] utsite ngiphumule {DUR}",
    "ngiyacela u [[refill]] le [[{ITEM}]] yami",
    "sitawuhlangana {DAY} emva kwe [[{MISC}]]",
    "ngifuna ku [[book]] i [[appointment]] ye [[{REL}]]",
    "ngiyacela ungibhalele i [[sick note]]",
    "ema[[condoms]] atfolakala mahhala lapha ku [[{PLACE}]]",
    "kufanele udle kahle ngaphambi kwekutsatsa i [[{DRUG}]]",
    "[[{STAFF}]] utsite ngibuye emva kwe{DUR}",
    "angitfolanga i [[{ITEM}]] yami ku [[{PLACE}]]",
    "ngicela u [[check]] i [[{TEST}]] yami",
    "ngiphatsa kabi ngobe nginesifo se [[{COND}]]",
    "sicela ulandzele i [[treatment]] kahle",
    "ngitsatsa i [[{DRUG}]] {TIME} nakusihlwa",
    "i [[{TEST}]] ibonisa kutsi une [[{COND}]]",
    "ngifike ku [[{PLACE}]] ngi [[late]] ngoba i [[taxi]] ibe [[late]]",
    "ngesikhatsi se [[{TEST}]] ngiva [[{SYMP}]]",
    "{WHO} utsatsa i [[{DRUG}]] njalo {TIME}",
]

def expand(frame, rng):
    """Return list of (lang, text) segments for one filled frame."""
    def fill(m):
        return rng.choice(LEX[m.group(1)])
    out, pos = [], 0
    for m in re.finditer(r"\[\[(.+?)\]\]", frame):
        if m.start() > pos: out.append(("ssw", frame[pos:m.start()]))
        out.append(("eng", m.group(1)))
        pos = m.end()
    if pos < len(frame): out.append(("ssw", frame[pos:]))
    segs = []
    for lang, t in out:
        t = re.sub(r"\{(\w+)\}", fill, t)
        # a siSwati-side slot may carry English text only if it came from an English lexicon; those are always inside [[ ]]
        # glue prefix like "ema[[x]]": keep as separate segments (prefix is siSwati, stem English)
        if t.strip(): segs.append((lang, t.strip()))
    return segs
