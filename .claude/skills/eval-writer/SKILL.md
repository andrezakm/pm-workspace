---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools.

# Referenz: Eval schreiben

## Was eine Eval ist

Eine Eval ist eine Tabelle mit 8–12 pass/fail-Kriterien. Sie prüft ob der Prototyp die Spec erfüllt. Die Ergebnis-Spalte bleibt leer — die füllt der Mensch (oder der eval-runner).

## Schritt 0: Run-Verzeichnis bestimmen

Berechne das heutige Datum im Format YYYY-MM-DD. Alle Outputs dieses Skills gehen in `output/YYYY-MM-DD/` — ersetze YYYY-MM-DD durch das tatsächliche Datum (heute: z.B. `output/2026-04-09/`). Erstelle dieses Verzeichnis implizit durch den ersten Write-Aufruf.

## Input

- `output/YYYY-MM-DD/spec-eval/spec.md`

## Format

```
# Eval: [Feature-Name]

## Anleitung
PASS = Bedingung ist erfüllt. FAIL = nicht erfüllt. UNKLAR = nicht aus Code oder Output entscheidbar.

## Kriterien

| ID | Kriterium | Wie testen | Pass-Bedingung | Ergebnis |
|----|-----------|------------|----------------|----------|
| E1 | ...       | ...        | ...            | FAIL     |
```

## Qualitätskriterien

- Jedes Kriterium ist eindeutig pass/fail entscheidbar — kein "sieht gut aus"
- "Wie testen" beschreibt eine konkrete Handlung (klicken, filtern, lesen)
- "Pass-Bedingung" ist eindeutig (was muss sichtbar/nicht sichtbar sein?)
- UNKLAR nur wenn das Kriterium visuell oder subjektiv ist und nicht aus dem Code entschieden werden kann
- Keine Doppelungen — jedes Kriterium prüft etwas anderes

## Output

`output/YYYY-MM-DD/spec-eval/eval.md`
