---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools (`mcp__filesystem__*`).

# Skill: Opportunity Scorer

Du bewertest die identifizierten Feedback-Cluster als Produktmöglichkeiten. Lies zuerst `context/company.md` und `context/strategy.md` um den Bewertungsrahmen zu verstehen.

## Input

- `output/discovery/feedback-clusters.md` — Ergebnis des Feedback-Synthesizers
- `context/company.md` — Wer wir sind und wie wir arbeiten
- `context/strategy.md` — Unsere strategische Richtung und Constraints

## Vorgehen

1. Lies alle drei Eingabedateien vollständig.
2. Erstelle für jeden Cluster (außer "Sonstiges") eine Scorecard.
3. Bewerte anhand von drei Dimensionen (je 1–5):
   - **Fit mit Vision** — Passt das zur Produktrichtung laut `context/strategy.md`?
   - **Wiederholbarkeit** — Taucht dieses Muster branchenübergreifend auf, oder ist es ein Einzelfall?
   - **Baubarkeit** — Können wir das mit unserem Team und unseren Constraints realistisch bauen?
4. Jede Begründung muss explizit auf `context/company.md` oder `context/strategy.md` verweisen.

## Qualitätskriterien

- Jede Punktzahl hat eine Begründung
- Jede Begründung referenziert mindestens eine konkrete Aussage aus `context/company.md` oder `context/strategy.md`
- Keine Punktzahlen ohne Evidenz aus den Input-Dateien
- Scores sind differenziert (nicht alle 3/5)

## Output-Format

Schreibe `output/strategy/opportunity-scorecard.md` mit folgendem Format:

```
# Opportunity Scorecard

## [Cluster-Name]

| Dimension | Score | Begründung |
|-----------|-------|-----------|
| Fit mit Vision | X/5 | [Verweis auf context/company.md oder context/strategy.md] |
| Wiederholbarkeit | X/5 | [Verweis auf Feedback-Daten] |
| Baubarkeit | X/5 | [Verweis auf context/strategy.md Constraints] |
| **Gesamt** | **X/15** | |

**Fazit:** [1-2 Sätze Einschätzung]

---
```

## Output

Schreibe die fertige Scorecard nach `output/strategy/opportunity-scorecard.md`.
