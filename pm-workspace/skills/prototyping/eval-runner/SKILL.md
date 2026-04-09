---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools.

# Skill: Eval Runner

Du liest eine Eval.md und eine app.py und beurteilst jeden Eval-Punkt — soweit aus dem Code entscheidbar.

## Input

Zwei Pfade werden beim Aufruf übergeben. Standardpfade: `output/spec-eval/eval.md` und `output/prototyping/app.py`

## Vorgehen

1. Lies beide Dateien vollständig.
2. Gehe jeden Eval-Punkt durch.
3. Entscheide für jeden Punkt:
   - **PASS** — aus dem Code eindeutig erkennbar dass das Kriterium erfüllt ist
   - **FAIL** — aus dem Code erkennbar dass das Kriterium nicht erfüllt ist
   - **UNKLAR** — nicht aus dem Code entscheidbar (visuelles Layout, subjektive UX, Laufzeitverhalten)
4. Schreibe eine Begründung pro Punkt.

## Qualitätskriterien

- Keine Urteile über Dinge die nur zur Laufzeit sichtbar sind (z.B. ob der Browser öffnet)
- UNKLAR ist kein Ausweichen — nur wenn der Code wirklich keine Aussage erlaubt
- Begründungen sind kurz und konkret (1-2 Sätze, Verweis auf Code-Zeile wenn möglich)
- Gesamtbewertung am Ende: Anzahl PASS / FAIL / UNKLAR

## Output-Format

```
# Eval-Ergebnis: [Feature-Name]

**Datum:** [Heute]
**Eval-Datei:** [Pfad]
**Prototyp:** [Pfad]

## Ergebnisse

| ID | Kriterium | Status | Begründung |
|----|-----------|--------|------------|
| E1 | ... | PASS | ... |
| E2 | ... | UNKLAR | ... |

## Zusammenfassung

PASS: X / FAIL: X / UNKLAR: X

[1-2 Sätze Gesamteinschätzung]
```

## Output

Schreibe das Ergebnis nach `output/prototyping/eval-results.md`.
