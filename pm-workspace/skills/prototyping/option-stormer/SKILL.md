---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: Option Stormer

Du nimmst eine Spec und baust 3 verschiedene Prototypen — nicht einen und dann iterieren, sondern drei parallel, dann vergleichen.

## Input

- `output/spec-eval/spec.md`
- Datendateien die in der Spec referenziert werden (via Glob finden)

## Vorgehen

1. **Spec lesen** — Lies output/spec-eval/spec.md vollständig. Identifiziere alle UI-Komponenten und Constraints.
2. **Kern-UI-Entscheidung identifizieren** — Was ist die zentrale Design-Entscheidung? Layout, Interaktionsmodell, oder Informationshierarchie?
3. **3 Varianten bauen** — Schreibe drei vollständige Streamlit-Apps:
   - **Variante A** — Die naheliegendste Lösung
   - **Variante B** — Eine Alternative die ein anderes Interaktionsmuster nutzt
   - **Variante C** — Die unerwartete Variante: Was wäre wenn man das Problem ganz anders angeht?
4. **Vergleich schreiben** — Schreibe eine Vergleichstabelle: Was unterscheidet die drei? Welche Trade-offs?

## Qualitätskriterien

- Alle 3 Apps sind lauffähig mit `streamlit run`
- Alle 3 erfüllen die Spec (gleiche Funktionalität, andere UX)
- Die Unterschiede sind strukturell, nicht kosmetisch
- Nur streamlit + pandas. Kein matplotlib, kein plotly, kein altair. Für Diagramme: `st.bar_chart`, `st.line_chart` etc.
- Kein `@st.cache_data` — CSV direkt mit `pd.read_csv()` laden
- Echte Daten aus Datendatei, kein Hardcoding
- Sonderfälle behandelt (z.B. leerer Filter → Hinweis statt leere Tabelle)

## Output

- `output/prototyping/option-a/app.py`
- `output/prototyping/option-b/app.py`
- `output/prototyping/option-c/app.py`
- `output/prototyping/option-comparison.md`

## Format: option-comparison.md

```
# Option Vergleich

## Kern-UI-Entscheidung
[Was ist die zentrale Entscheidung die die drei Varianten unterscheidet?]

## Übersicht

| Kriterium | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Interaktionsmodell | ... | ... | ... |
| Informationshierarchie | ... | ... | ... |
| Lernkurve für Nutzer | niedrig/mittel/hoch | ... | ... |
| Eignet sich für | ... | ... | ... |

## Trade-offs
**Option A:** [Stärken und Schwächen]
**Option B:** [Stärken und Schwächen]
**Option C:** [Stärken und Schwächen]

## Empfehlung
[Welche Variante für welchen Kontext? Keine pauschale Empfehlung — Bedingungen benennen.]
```
