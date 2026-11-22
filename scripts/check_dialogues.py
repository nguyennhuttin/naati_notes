#!/usr/bin/env python3
"""Validate NAATI-CCL-style dialogues in topic markdown files.

Segment line format (one line), followed by a translation line:
  **[3] Advisor — EN, 27 words:** English source text
  → *Vietnamese translation*
  **[4] Client — VI, 31 words:** Vietnamese source text
  → *English translation*

Word count = English words (source for EN, translation for VI), as NAATI does.
"""
import re
import sys

SEG = re.compile(r'^\*\*\[(\d+)\] (.+?) — (EN|VI), (\d+) words?:\*\* (.+)$')
VI_CHARS = re.compile(r'[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]')


def words(s):
    return len(s.replace('*', '').split())


def check(path):
    errs = []
    lines = open(path, encoding='utf-8').read().split('\n')
    dialogues = []
    for i, l in enumerate(lines):
        if l.startswith('## Dialogue'):
            dialogues.append({'title': l, 'segs': [], 'line': i + 1})
        m = SEG.match(l)
        if m:
            if not dialogues:
                errs.append(f'{path}:{i+1}: segment before any "## Dialogue" heading')
                continue
            n, spk, lang, stated, src = m.groups()
            tr = lines[i + 1] if i + 1 < len(lines) else ''
            if not tr.startswith('→ *') or not tr.rstrip().endswith('*'):
                errs.append(f'{path}:{i+2}: translation line must be "→ *...*"')
            tr = tr[2:].strip().strip('*')
            eng = src if lang == 'EN' else tr
            vi = tr if lang == 'EN' else src
            actual = words(eng)
            if abs(actual - int(stated)) > 2:
                errs.append(f'{path}:{i+1}: stated {stated} words but English has {actual}')
            if actual > 35:
                errs.append(f'{path}:{i+1}: segment has {actual} English words (>35)')
            if not VI_CHARS.search(vi.lower()):
                errs.append(f'{path}:{i+1}: Vietnamese side has no Vietnamese diacritics')
            if VI_CHARS.search(eng.lower()):
                errs.append(f'{path}:{i+1}: English side contains Vietnamese diacritics')
            dialogues[-1]['segs'].append((int(n), lang, actual, i + 1))
    for d in dialogues:
        s = d['segs']
        where = f"{path}:{d['line']} {d['title']!r}"
        if not s:
            errs.append(f'{where}: no segments found')
            continue
        if not 12 <= len(s) <= 16:
            errs.append(f'{where}: {len(s)} segments (want 12-16)')
        if [x[0] for x in s] != list(range(1, len(s) + 1)):
            errs.append(f'{where}: segment numbers not 1..N')
        if s[0][1] != 'EN':
            errs.append(f'{where}: first segment must be EN')
        for a, b in zip(s, s[1:]):
            if a[1] == b[1]:
                errs.append(f'{where}: segments {a[0]} and {b[0]} are both {a[1]} (must alternate)')
        en = sum(x[2] for x in s if x[1] == 'EN')
        vi = sum(x[2] for x in s if x[1] == 'VI')
        if not 280 <= en + vi <= 330:
            errs.append(f'{where}: total {en+vi} words (want 280-330)')
        if not 130 <= en <= 175 or not 130 <= vi <= 175:
            errs.append(f'{where}: EN {en} / VI {vi} (each should be ~150, 130-175)')
        if not any(x[2] <= 12 for x in s):
            errs.append(f'{where}: no short segment (<=12 words); real tests mix short and long')
        print(f'{where}: {len(s)} segs, EN {en} + VI {vi} = {en+vi}, max {max(x[2] for x in s)}')
    return errs


if __name__ == '__main__':
    all_errs = []
    for p in sys.argv[1:]:
        all_errs += check(p)
    for e in all_errs:
        print('ERROR', e)
    sys.exit(1 if all_errs else 0)
