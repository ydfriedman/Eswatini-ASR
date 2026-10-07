// Builds SiSwati_ASR_Evaluation.docx from tables.json + fig_*.png
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun, AlignmentType,
  HeadingLevel, WidthType, ShadingType, BorderStyle, LevelFormat, Footer, PageNumber, TableOfContents,
} = require("docx");

const T = JSON.parse(fs.readFileSync(path.join(__dirname, "tables.json")));
const FONT = "Arial";
const INK = "1F1F1F", MUTED = "5A5A55", ACCENT = "1C5CAB", HEAD_FILL = "E8EEF7", NOTE_FILL = "F4F1EA", WARN_FILL = "FBEFE6";
const PAGE_W = 12240, MARGIN = 1296, CONTENT_W = PAGE_W - 2 * MARGIN; // 9648 DXA

// ---------- helpers ----------
function runs(text, base = {}) {
  // **bold** inline markup
  return text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(s =>
    s.startsWith("**") ? new TextRun({ text: s.slice(2, -2), bold: true, font: FONT, ...base })
                       : new TextRun({ text: s, font: FONT, ...base }));
}
const P = (text, opts = {}) => new Paragraph({ children: runs(text, opts.run || {}), spacing: { after: 120, line: 276 }, ...opts.para });
const H1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT })] });
const H2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT })] });
const bullet = (t, level = 0) => new Paragraph({ numbering: { reference: "bullets", level }, children: runs(t), spacing: { after: 60, line: 264 } });
const numbered = (t, ref = "numbers") => new Paragraph({ numbering: { reference: ref, level: 0 }, children: runs(t), spacing: { after: 80, line: 264 } });
const caption = t => new Paragraph({ children: runs(t, { italics: true, size: 18, color: MUTED }), spacing: { before: 60, after: 200 } });

function shadedBlock(title, lines, fill, borderColor) {
  // callout: paragraphs with shading + left border
  const border = { left: { style: BorderStyle.SINGLE, size: 18, color: borderColor, space: 8 } };
  const out = [new Paragraph({ shading: { type: ShadingType.CLEAR, fill, color: "auto" }, border,
    spacing: { before: 120, after: 60 }, children: [new TextRun({ text: title, bold: true, font: FONT, color: borderColor, size: 22 })] })];
  lines.forEach((l, i) => out.push(new Paragraph({ shading: { type: ShadingType.CLEAR, fill, color: "auto" }, border,
    numbering: { reference: "callout", level: 0 }, spacing: { after: i === lines.length - 1 ? 200 : 60, line: 264 }, children: runs(l) })));
  return out;
}

function table(header, rows, widths, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: "C9C8C2" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cell = (text, w, isHead, align) => new TableCell({
    width: { size: w, type: WidthType.DXA }, borders,
    shading: isHead ? { type: ShadingType.CLEAR, fill: HEAD_FILL, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ alignment: align, children: runs(String(text), { size: 18, bold: isHead, color: INK }) })],
  });
  const alignFor = i => (opts.leftCols || 1) > i ? AlignmentType.LEFT : AlignmentType.RIGHT;
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, widths[i], true, alignFor(i))) }),
           ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, widths[i], false, alignFor(i))) }))],
  });
}
function figure(file, wPx, hPx, widthIn = 6.4) {
  const data = fs.readFileSync(path.join(__dirname, file));
  const w = Math.round(widthIn * 96), h = Math.round(w * hPx / wPx);
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120 },
    children: [new ImageRun({ type: "png", data, transformation: { width: w, height: h },
      altText: { title: file, description: file, name: file } })] });
}
const gap = () => new Paragraph({ children: [], spacing: { after: 60 } });

// ---------- dynamic numbers ----------
const swEn = T.simbaw_en || [];
const findRow = (lab, model) => (swEn.find(r => r[0].startsWith(lab) && r[1] === model) || [])[2] || "n/a";
const swZulAuto = findRow("Zulu", "Simba-W (auto language)"), swZulEn = findRow("Zulu", "Simba-W (English forced)"), whZul = findRow("Zulu", "Whisper-large-v3");
const swSswAuto = findRow("SiSwati", "Simba-W (auto language)"), swSswEn = findRow("SiSwati", "Simba-W (English forced)"), whSsw = findRow("SiSwati", "Whisper-large-v3");

// ---------- content ----------
const children = [];
children.push(
  new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: "Speech Recognition for siSwati and SiSwati-Accented English", font: FONT, size: 40, bold: true, color: INK })] }),
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "An evaluation of open ASR models, and what it means for testing Intron Health's ASR", font: FONT, size: 24, color: MUTED })] }),
  new Paragraph({ spacing: { after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 6 } },
    children: [new TextRun({ text: "Eswatini CMIS project  ·  26 September 2026  ·  Prepared with Claude (Anthropic)", font: FONT, size: 18, color: MUTED })] }),
);

children.push(...shadedBlock("Bottom line", [
  "**No single open model handles all three situations we care about.** Simba-S is clearly best on siSwati (19% word error rate, 3% character error rate on read speech). Whisper-large-v3 is clearly best on SiSwati- and Zulu-accented English (15–20% after discounting spoken punctuation). No model handles siSwati–English code-switching: English words inside siSwati sentences are lost 91–100% of the time.",
  "**How these models perform in real Eswatini clinics is still unknown.** Every real recording we could test is read-aloud speech. No public spontaneous, noisy, or code-switched siSwati recordings exist, so our code-switching results come from synthetic audio and are qualitative.",
  "**Our English benchmark cannot be used to judge Intron Health.** AfriSpeech-200, the source of all our accented-English audio, was created by Intron Health, so Intron's models have very likely been trained on it. A fair comparison needs a new, private, Eswatini-specific test set (Section 4).",
], NOTE_FILL, ACCENT));

// 1. Key findings
children.push(H1("1. Key findings"));
children.push(
  numbered("**siSwati: models trained on siSwati are far ahead.** On 500 real NCHLT clips, the three UBC Simba models, all fine-tuned on siSwati, reach 3–5% character error. Models without siSwati training reach 8–39%. SeamlessM4T-v2 has no siSwati, so it rewrites siSwati as Zulu (\"utsite ngitsatse\" becomes \"uthi ngithathe\"). Whisper splits long siSwati words into fragments. **Caveat:** the Simba models probably saw these prompts during training, so their siSwati numbers are an upper bound."),
  numbered("**Accented English: Whisper-large-v3 wins clearly.** On 2,835 Zulu-accented clips from 100 speakers, its lenient word error rate is 14.8%. SeamlessM4T-v2 scores 38.2%, Simba-S 50.1% and Simba-W 52.8%. On the smaller siSwati-accent set (96 clips, 5 speakers) the ranking is the same: Whisper 19.5%, Seamless 35.3%, Simba-S 41.4%."),
  numbered(`**Simba-W is the one model that is reasonable at both siSwati and English, if it is told the language.** Simba-S returns nothing at all for 8–14% of English clips. Simba-W keeps most of its English, but its automatic language detection often decides that Zulu-accented English is Swahili and outputs looping Swahili text. With English forced, Simba-W improves from ${swZulAuto} to ${swZulEn} lenient WER on a 300-clip Zulu-accent sample (Whisper: ${whZul}), and from ${swSswAuto} to ${swSswEn} on the siSwati-accent set (Whisper: ${whSsw}). It still trails Whisper on English, and forcing a single language defeats the purpose in code-switched speech.`),
  numbered("**The clinical prompt does not help recognition.** Giving Whisper a medical-vocabulary prompt lowers standard WER by about 4 points, but only because it changes formatting (punctuation written as symbols rather than spoken words). Lenient WER is unchanged: 14.8% without the prompt, 14.9% with it. Medical vocabulary itself costs Whisper about 4.5 points: 17.3% on clinical sentences versus 12.8% on general ones."),
  numbered("**Code-switching is unsolved.** Models that must pick an output language translate the whole utterance (SeamlessM4T with an English target) or distort the English words (Zulu target, Simba). CTC models (Simba-M, MMS) never translate; they spell English words as they sound (\"lemedicatun\", \"tebetulosis\"). But this does not make the words more recoverable. A fuzzy dictionary match could recover only about one third of English words from any model's output."),
  numbered("**Synthetic audio is a poor stand-in for real speech.** On identical siSwati text, the models trained on siSwati make roughly 6–10× more character errors when the audio is synthetic (for example Simba-S: 2.8% real vs 27.6% synthetic). The mismatch between the Xhosa TTS voice and siSwati dominates the errors, so code-switching conclusions rest on qualitative failure patterns, not the numbers."),
);

// 2. Unknowns — emphasized
children.push(H1("2. What we still don't know: remaining unknowns and weak spots"));
children.push(P("These gaps limit how far the results above can be trusted for clinical deployment decisions. Each should be closed before choosing a vendor or model."));
const U = [
  ["No real code-switched audio", "Code-switching is how clinic conversations actually sound, and the English words (drugs, tests, numbers) are often the clinically critical ones. Our code-switched set is synthetic: a Xhosa TTS voice reading sentences written by Claude, never reviewed by a native speaker.", "Record real code-switched speech (Section 4). Have a native siSwati speaker correct the 40 prompt sentences first."],
  ["Read speech only", "Real consultations are spontaneous: hesitations, restarts, overlapping speakers, long pauses. All real test audio here is people reading prompts, which flatters every model.", "Collect role-played and (with consent) real consultations."],
  ["No clinic acoustics", "Busy outpatient waiting areas, phone or tablet microphones, masks and distance all raise error rates. Our audio is mostly quiet, close-microphone recordings.", "Record in real facilities on the devices that will be used."],
  ["siSwati test set likely seen in training", "NCHLT reuses prompts across its train and test splits, and the Simba models were trained on NCHLT. Simba's 3–5% character error is an upper bound.", "Evaluate on newly recorded siSwati that no model has seen."],
  ["Thin siSwati-accent English data", "Only 96 clips from 5 speakers, and one speaker accounts for 58 of them. Zulu-accented English (100 speakers) was used as a proxy. The two accents are close but not identical.", "Record 20+ Eswatini speakers across regions, ages and genders."],
  ["Domain mismatch", "AfriSpeech's \"clinical\" sentences are textbook passages read aloud. They lack the drug names, doses, lab values, dates and personal and place names used in Eswatini clinics.", "Build test scripts from real CMIS vocabulary: formulary, lab tests, facility names."],
  ["Metrics miss clinical impact", "WER treats \"the\" and \"dolutegravir\" as equally important. Word-level scoring also over-penalises siSwati's long compound words, and siSwati spelling of English loanwords is not standardised.", "Add an entity-level metric (drugs, doses, numbers, dates) and agree transcription conventions."],
  ["Short clips only", "All clips are under 33 seconds. Real consultations run for minutes, and long recordings bring segmentation errors and models inventing text during silence.", "Test on full-length consultations, including silent stretches."],
  ["Limited decoding and models", "Greedy decoding only, no language-model rescoring, and no Omnilingual ASR or commercial systems (Intron, Lelapa, Google, Azure). Simba-S's empty-output problem might be fixable by forcing a minimum output length; this was not tested.", "Add these as follow-up conditions on the new test set."],
  ["Deployment unknowns", "Speed, cost, offline operation and data-residency requirements were not assessed. Everything ran on one Apple M4 laptop.", "Assess once a shortlist exists."],
];
children.push(table(["Weak spot", "Why it matters", "How to close it"], U, [2000, 4424, 3224], { leftCols: 3 }));
children.push(gap());

// 3. Intron
children.push(H1("3. Implications for evaluating Intron Health's ASR"));
children.push(...shadedBlock("Data contamination warning", [
  "AfriSpeech-200 was created and published by Intron Health. Their commercial ASR has very likely been trained on it, possibly including the exact siSwati- and Zulu-accented clips used here. Intron's scores on this data would therefore be optimistic and not comparable with the other models.",
  "Ask Intron directly which datasets their model was trained on. Evaluate all vendors only on newly recorded audio that has never been published or shared.",
], WARN_FILL, "B4531F"));
children.push(P("The open-model results still set a useful bar. To be worth adopting for English, Intron needs to beat Whisper-large-v3 (free, about 15–20% lenient WER here) on Eswatini audio. For siSwati it needs to beat Simba-S. And it needs to show real code-switching ability, which no open model has. The test set in Section 4 is designed so all systems can be compared on the same tricky real-world cases."));

// 4. Proposed test set
children.push(H1("4. Proposed Eswatini clinic test set"));
children.push(P("A private, held-out test set built around the situations clinicians will actually face. Start with role-played consultations recorded by clinic staff, which avoids patient-privacy issues. Add consented real consultations once governance is in place."));
const S = [
  ["1", "siSwati consultation", "Nurse and patient discuss symptoms and adherence entirely in siSwati", "Core siSwati recognition on spontaneous speech", "60"],
  ["2", "Code-switched consultation", "\"Ngitsatsa i-TLD yami every morning, kodvwa ngiva i-headache\"", "Keeping English terms inside siSwati sentences, without translating", "60"],
  ["3", "English dictation (SiSwati accent)", "Clinician dictates a note, including \"full stop\" and \"new line\"", "Accent, medical terms, handling of dictation commands", "30"],
  ["4", "Drugs, doses and results", "\"Dolutegravir 50 mg\", \"viral load less than 50 copies\", \"HbA1c 8.2\"", "The words alerts depend on: drug names, numbers, units", "30"],
  ["5", "Names, places, dates", "Patient names; Manzini, Hlathikhulu, Siteki; \"next appointment 14 October\"", "Proper nouns and dates, where models tend to invent text", "20"],
  ["6", "Clinic acoustics", "The same scripts recorded in a busy outpatient area, on a phone, through a mask", "Robustness to real recording conditions", "30"],
  ["7", "Speaker diversity", "Older patients, caregivers, all four regions, men and women", "Fairness across groups; per-speaker variation", "(across 1–6)"],
  ["8", "Long-form and silence", "Full 5–10 minute consultations with pauses", "Segmentation, drift, text invented during silence", "30"],
];
children.push(table(["#", "Scenario", "Example", "What it tests", "Min."], S, [400, 1900, 3048, 3500, 800], { leftCols: 4 }));
children.push(caption("Target minutes are an initial suggestion (about 4–5 hours of audio in total), enough for speaker-level confidence intervals."));
children.push(H2("Evaluation protocol"));
[
  "**Same audio for every system.** Keep the originals private. Send vendors only through an evaluation interface with agreed terms on data retention and training use.",
  "**Reference transcripts:** two native siSwati speakers transcribe independently and reconcile differences, following written conventions for loanword spelling, numbers (digits), and marking code-switches.",
  "**Metrics:** WER and CER with lenient normalisation. **Clinical entity accuracy**: were the drug, dose, number, date and test name captured correctly? Empty-output rate, invented-text rate on silence, and correct language labelling.",
  "**Statistics:** confidence intervals that resample speakers rather than clips, and paired comparisons of systems on the same clips.",
  "**Decision criteria agreed in advance,** e.g. the minimum entity accuracy acceptable for drug names before any alert relies on transcribed speech.",
].forEach(t => children.push(bullet(t)));

// 5. Results detail
children.push(H1("5. Detailed results"));
children.push(H2("5.1 Real siSwati (NCHLT, 500 clips)"));
children.push(figure("fig_siswati_cer.png", 1440, 720));
children.push(caption("Character error rate with 95% bootstrap intervals. CER is shown because word-level scores punish models that split siSwati's long words."));
children.push(table(["Model", "WER", "CER", "Exact match"], T.siswati, [4848, 1600, 1600, 1600]));
children.push(caption("WER can exceed 100% when a model inserts extra words. Whisper, for example, splits \"inganekwane\" into \"inga nikuwane\"."));

children.push(H2("5.2 Accented English (AfriSpeech-200)"));
children.push(figure("fig_english_wer.png", 1440, 1120));
children.push(caption("Lenient WER (spoken \"comma\"/\"full stop\" words ignored), with 95% intervals that resample speakers."));
children.push(P("**SiSwati accent (96 clips, 5 speakers)**"));
children.push(table(["Model", "WER", "Lenient WER", "CER", "Empty output"], T.eng_ssw, [3848, 1450, 1450, 1450, 1450]));
children.push(gap());
children.push(P("**Zulu accent (2,835 clips, 100 speakers)**"));
children.push(table(["Model", "WER", "Lenient WER", "CER", "Empty output"], T.eng_zul, [3848, 1450, 1450, 1450, 1450]));
children.push(gap());
children.push(P("**Clinical vs general sentences (Zulu accent, lenient WER)**"));
children.push(table(["Model", "Clinical", "General"], T.domain, [5648, 2000, 2000]));
children.push(gap());
if (swEn.length) {
  children.push(P("**Simba-W: automatic language detection vs English forced (same clips)**"));
  children.push(table(["Clips", "Model", "Lenient WER", "CER", "Empty"], swEn, [2400, 3248, 1400, 1300, 1300], { leftCols: 2 }));
  children.push(caption(`With automatic detection, Simba-W labels many Zulu-accented clips as Swahili and outputs Swahili text. Forcing English largely fixes this (${swZulAuto} → ${swZulEn}), though it remains behind Whisper (${whZul}).`));
}

children.push(H2("5.3 Code-switched siSwati–English (synthetic, 40 sentences)"));
children.push(P("All figures here come from synthetic audio (Xhosa TTS voice). Read the \"siSwati TTS control\" column as the baseline error that synthesis alone causes."));
children.push(table(["Model", "CER (code-switched)", "CER (siSwati TTS control)", "siSwati words wrong", "English words wrong", "English words recoverable*"], T.cs, [2848, 1360, 1360, 1360, 1360, 1360]));
children.push(caption("*Share of English words that a fuzzy dictionary match (≥60% character similarity) could recover from the output. The chance level, matching against a different sentence's output, is 0–3%."));
children.push(P("**Real vs synthetic audio of identical siSwati text (40 sentences)**"));
children.push(table(["Model", "CER real", "CER synthetic", "WER real", "WER synthetic"], T.tts_gap, [3648, 1500, 1500, 1500, 1500]));
children.push(gap());

children.push(H2("5.4 Failure modes to test for in any system"));
const F = [
  ["Empty output", "Simba-S returns nothing for 8–14% of English clips", "Silently dropped speech; nothing flags the gap"],
  ["Wrong language detected", "Simba-W reads Zulu-accented English as Swahili; Whisper (auto) output Portuguese for at least one siSwati clip", "Plausible-looking text that is wrong, and may be in another language"],
  ["Translation instead of transcription", "SeamlessM4T turns siSwati into Zulu, or code-switched speech into English", "Content paraphrased or altered; \"medication\" becomes \"imithi\""],
  ["Invented text / loops", "Repetition loops (\"kwamba kwamba…\"), made-up English sentences", "Fabricated clinical content"],
  ["Word splitting", "Whisper splits long siSwati words", "Inflated WER; harder downstream parsing"],
  ["Spoken punctuation", "\"coma\" written for \"comma\", which clashes with the medical term coma", "Naive cleanup could delete real clinical words"],
  ["Stray characters", "ɛ, ɔ and other non-siSwati letters in Simba outputs (mostly on synthetic audio)", "Needs output filtering"],
];
children.push(table(["Failure mode", "Where we saw it", "Clinical risk"], F, [2200, 4048, 3400], { leftCols: 3 }));
children.push(gap());

// 6. Methods
children.push(H1("6. Methods"));
children.push(H2("Models"));
const M = [
  ["Simba-S (UBC-NLP)", "SeamlessM4T-v2 speech-to-text, fine-tuned on SimbaBench (43 African languages)", "Yes", "No language tag (as in the model card)"],
  ["Simba-W (UBC-NLP)", "Whisper-large-v3, fine-tuned on SimbaBench", "Yes", "Auto language; English forced on a subset"],
  ["Simba-M (UBC-NLP)", "MMS-1b-all CTC, fine-tuned on SimbaBench", "Yes", "\"multilingual_african\" adapter"],
  ["SeamlessM4T-v2-large (Meta)", "Multitask speech/text model", "No", "Zulu target for siSwati; English target for English"],
  ["MMS-1b-all (Meta)", "CTC with per-language adapters", "No (no siSwati adapter exists)", "Zulu adapter"],
  ["Whisper-large-v3 (OpenAI)", "Weakly supervised multilingual encoder-decoder", "No", "English (± clinical prompt); Swahili or auto for siSwati"],
];
children.push(table(["Model", "Type", "siSwati in training?", "How run"], M, [2300, 3348, 1600, 2400], { leftCols: 4 }));
children.push(gap());
children.push(H2("Evaluation data"));
const D = [
  ["Real siSwati", "NCHLT siSwati test split (via SimbaBench)", "500 clips, 35 min", "Read prompts, ~3 words each"],
  ["SiSwati-accented English", "AfriSpeech-200 \"siswati\" accent, all splits", "96 clips, 23 min, 5 speakers", "90% clinical textbook sentences"],
  ["Zulu-accented English", "AfriSpeech-200 \"zulu\" + \"isizulu\", all splits", "2,835 clips, 7.9 h, 100 speakers", "49% clinical, 51% general"],
  ["Code-switched", "40 sentences written by Claude, voiced by Simba-TTS-xho", "40 clips, 2.4 min", "Synthetic; not native-reviewed"],
  ["TTS controls", "Same voice reading NCHLT siSwati text / AfriSpeech English text", "40 + 40 clips", "Isolate the effect of synthesis"],
];
children.push(table(["Set", "Source", "Size", "Notes"], D, [2100, 3548, 2000, 2000], { leftCols: 4 }));
children.push(gap());
children.push(P("**Excluded:** SimbaBench's \"siSwati Lwazi\" test file is mislabelled; its content is Afrikaans."));
children.push(H2("Scoring"));
[
  "Corpus-level WER and CER after normalisation: lowercase, punctuation removed, hyphens split, NCHLT noise tags removed.",
  "**Lenient WER** additionally ignores spoken punctuation words (comma/coma, full stop, period), which AfriSpeech readers often voiced.",
  "95% bootstrap confidence intervals: speaker-level for real English sets, clip-level otherwise. Paired bootstrap for model-vs-model differences.",
  "All models run with greedy decoding on an Apple M4 (MPS, fp16). Whisper uses eager attention, because the default attention kernel on Apple GPUs produced corrupted output (\"!!!!\"). Simba-S's empty outputs were reproduced in fp32, so they are genuine.",
].forEach(t => children.push(bullet(t)));
children.push(H2("Reproducibility"));
children.push(P("Code, manifests, raw transcripts and per-clip scores are in 07_ASR_SiSwati/ (scripts/, data/, results/). Model weights were deleted after the runs and are re-downloaded automatically when a script is re-run. Data licences: NCHLT (CC-BY 3.0), AfriSpeech-200 (CC-BY-NC-SA 4.0), SimbaBench and Simba models (CC-BY 4.0)."));

// ---------- document ----------
const doc = new Document({
  creator: "Prepared with Claude", title: "SiSwati ASR Evaluation",
  styles: {
    default: { document: { run: { font: FONT, size: 21, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: FONT, color: ACCENT }, paragraph: { spacing: { before: 360, after: 140 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: FONT, color: INK }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
    { reference: "callout", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
    { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 15840 }, margin: { top: 1296, bottom: 1296, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
      new TextRun({ text: "SiSwati ASR evaluation  ·  page ", font: FONT, size: 16, color: MUTED }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: MUTED })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => { const out = path.join(__dirname, "SiSwati_ASR_Evaluation.docx"); fs.writeFileSync(out, b); console.log("wrote", out, b.length); });
