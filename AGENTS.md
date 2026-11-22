# Agent instructions – NAATI CCL Vietnamese ⇄ English study pack

This repo is a **study pack** (Markdown only, no app) for the NAATI CCL test. The owner is a native Vietnamese speaker with strong English (PTE superior) who wants **rapid, exam-realistic interpreting practice**. Every piece of content is judged against one bar: *does it look and sound like a real CCL dialogue?*

## Validate

```bash
python3 scripts/check_dialogues.py topics/*.md          # all topics
python3 scripts/check_dialogues.py topics/04-health.md  # one file
```

It prints one summary line per dialogue and `ERROR …` lines. Done = exit 0 and **zero ERROR lines**. Piping through `tail`/`head` hides the exit code, so grep for `ERROR` instead. Run it after any edit to a dialogue.

## How the pieces fit

The layers go from general to specific. Each fact lives in one place:

1. `README.md`: exam format and marking rules, how to study, the 2-week plan, topic index, note-taking symbols. **Exam rules live here only.**
2. `00-core-vocab.md`: vocabulary used in every topic (politeness, numbers and dates, connectors, Vietnamese fillers, the North/South/diaspora word table, Australian organisations). Put a term here only if it applies to all topics. Otherwise it goes in a topic file.
3. `official-samples-notes.md`: analysis of the official NAATI samples, a phrase bank showing how NAATI's model answers translate by meaning, and a list of errors in third-party material. It explains **why** the dialogue format is what it is.
4. `topics/NN-<topic>.md`: one file per official CCL domain, all 12, numbered 01–12 in the README order.
5. `materials/`: the **source of truth for realism**. It contains:
   - Official NAATI Vietnamese samples (`Vietnamese - <Topic>.pdf` plus `Vietnamese_<Topic>.mp3`).
   - Third-party practice PDFs (`10.-…`, `11.-…`, `14.-…`), which have known errors.
   - `CCL_Booklet_v_9_PP.pdf`, a third-party rules booklet.

   Extract text with `pip install pypdf` and `pypdf.PdfReader`. Extract audio timing with `ffprobe` or `ffmpeg -af silencedetect`. Never copy official dialogue text into topic files; analyse it and write original content.

If you add or rename a file, update the README's links and topic table.

## Topic file layout

Every topic file has exactly these sections, in this order:

```
# NN – Topic
Typical scenarios: …
## Core vocabulary                      (EN | VI table; health uses ### sub-tables)
## Key phrases (rapid drill)            (EN→VI rows, then colloquial VI→EN rows)
## Dialogue 1 – <title> (<role>)        denser vocabulary
## Dialogue 2 – <title> (<role>)        denser vocabulary
## Dialogue 3 – <title> (<role>)        simple, warm, official-sample style – closest to the real test
## Traps
```

- Append vocabulary rows; never duplicate an existing row.
- **Traps** are one-line bullets on false friends and register pitfalls. Examples:
  - excess ≠ *dư thừa*
  - rates = council rates ≠ *lãi suất*
  - bond ≠ *trái phiếu*
  - *chích ngừa* = *tiêm chủng*
  - idioms rendered by meaning
- When a dialogue introduces a new pitfall, add it to Traps.

## Dialogue format (the validator parses this exactly)

```
## Dialogue 3 – Painful hand joints (GP)

| Domain | Health |
|---|---|
| English speaker | Dr Collins, GP (male) |
| Vietnamese speaker | Mr Pham, patient (male, 45) |
| Scenario | One or two sentences of setting. |

*The dialogue begins now.*

**[1] Doctor — EN, 15 words:** Hi, Mr Pham, I'm Dr Andrew Collins. Come on in. What brings you here today?
→ *Chào anh Phạm, tôi là bác sĩ Andrew Collins. Mời anh vào. Hôm nay anh đến khám vì chuyện gì?*

**[2] Patient — VI, 32 words:** Dạ, chào bác sĩ. …
→ *Hello, doctor. …*

*End of dialogue — 14 segments · EN 159 + VI 160 = 319 words*
```

- Each segment is one source line in the form `**[N] <Role> — EN|VI, <n> words:** …`, using an em dash, followed by one line in the form `→ *translation*`.
- `<n>` is the number of **English** words in the segment: the source for EN segments, the translation for VI segments. This is how NAATI counts.
- Hard limits, all enforced by the validator:
  - 12–16 segments per dialogue.
  - The first segment is EN, and turns strictly alternate.
  - Each segment has ≤ 35 English words.
  - 280–330 words total, with about 150 per language (130–175 each).
  - At least one short segment (≤ 12 words).
- Mix the lengths the way the official samples do: several segments of 20–35 words, several of 10–20, and one or two very short ones ("How does 3.30 sound?", *Vâng, thế thì tuyệt quá.*).
- Update the end line whenever the counts change.

## Writing approach: realism over jargon

Copy the shape of the official samples:
- **Arc.** The professional greets the client by name and introduces themselves. The Vietnamese speaker explains their situation **with feelings and family details**. The professional asks questions and gives requirements, often as a **list** of documents or steps, because lists are where candidates lose marks. Close with arrangements and pleasantries, often with a touch of humour (kids "always starving", a new shirt for the interview).
- **Detail density.** Each dialogue carries a few critical numbers, dates, times and conditions. That is enough; it should not read like a lecture.
- **Speakers.** The English speaker is a professional with a name and role. The Vietnamese speaker is a client, parent or patient. Vary genders across dialogues and record them in the header.
- **Register.** The client addresses the professional as *ông/bà (+ name)* or *thưa ông/bà*, with *dạ/vâng/ạ*. Render the professional's English with *ông/bà* or *anh/chị*, consistent within a dialogue. **Address is always ông/bà/anh/chị** (or *bác sĩ*, *thầy/cô* where natural), never *bạn* or *ngài*.
- **Vietnamese voice.** Write Vietnamese-Australian community speech that mixes Northern and Southern/diaspora forms (*đô, ngàn, ba/má, ngày mốt, chích ngừa, Bộ … hay sao, tiệm, xài*), with idioms and colloquialisms that must be translated by meaning.
- **Translations.** Translate by meaning, idiomatically, and **completely**. Every number, date, time, name, list item, condition, negation and qualifier ("about", "probably", "only if") must appear on the other side. Anything left out or added is a mark lost in the real exam, so it is a bug here.
- **Facts.** Australian facts must be plausible and current. Prefer general wording ("a small fee", "usually within a few weeks") over fast-changing, state-specific figures. When a program is renamed, update it everywhere it appears and add a Trap noting the old name. Past examples:
  - jobactive → Workforce Australia
  - AAT → ART
  - Home Care Packages → Support at Home
  - NSW-only courts → "court"
- **Third-party material.** Treat the numbered third-party PDFs as topic ideas only. `official-samples-notes.md` §3 lists their known errors (*bạn* register, 38–47-word segments, tenderness = *yếu ớt*, scene = *cảnh*, …). Use the corrected renderings.

## Workflow for bulk content work

- **Preserve user edits.** The owner edits translations by hand. Before rewriting a file, run `git diff` on it and carry the user's wording into the new version.
- **Split by file.** For changes across many topics, give one agent per 3 files and a shared spec (the format and approach above). Each agent validates its own files until the checker is clean, then you run the checker across all files.
- **Final check**, beyond the validator, grep for:
  - *bạn* used as a form of address
  - leftover old-format lines (e.g. `> *You will hear a dialogue…*`)
  - renamed programs that still appear
  - README links that no longer resolve
- Commit only when the owner asks.
