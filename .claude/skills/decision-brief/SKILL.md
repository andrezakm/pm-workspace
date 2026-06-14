---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools (`mcp__filesystem__*`).

# Skill: Decision Brief

Du schreibst einen 1-Pager der aus den Scores eine klare Produktempfehlung ableitet.

## Schritt 0: Run-Verzeichnis bestimmen

Berechne das heutige Datum im Format YYYY-MM-DD. Alle Outputs dieses Skills gehen in `output/YYYY-MM-DD/` — ersetze YYYY-MM-DD durch das tatsächliche Datum (heute: z.B. `output/2026-04-09/`). Erstelle dieses Verzeichnis implizit durch den ersten Write-Aufruf.

## Input

- `output/YYYY-MM-DD/strategy/opportunity-scorecard.md` — Scorecard der Opportunities
- `context/strategy.md` — Strategische Richtung und Constraints

## Vorgehen

1. Lies beide Eingabedateien vollständig.
2. Identifiziere die Opportunity mit dem höchsten Gesamt-Score.
3. Schreibe den 1-Pager gemäß Output-Format.
4. Die Empfehlung muss eindeutig sein: BUILD, SKIP oder MEHR DATEN. Kein "es kommt darauf an".
5. Verwende echte Zahlen aus dem Feedback (Stunden, Nennungen, Häufigkeiten) — keine vagen Formulierungen.

## Qualitätskriterien

- Empfehlung ist eindeutig (BUILD / SKIP / MEHR DATEN)
- Enthält mindestens eine konkrete Zahl aus dem Feedback-Material
- Jede Aussage ist rückverfolgbar auf Quell-Dateien
- Keine Spekulationen über Dinge die nicht in den Daten stehen

## Output-Format

Schreibe `output/YYYY-MM-DD/strategy/decision-brief.md` mit folgendem Format:

```
# Decision Brief: [Opportunity-Name]

**Empfehlung:** BUILD / SKIP / MEHR DATEN
**Datum:** [Heutiges Datum]

## Das Muster
[Was haben wir beobachtet? Welches Muster taucht in den Daten auf?]

## Für wen
[Welche Kunden oder Nutzergruppen haben dieses Problem geäußert? Mit konkreten Namen/Quellen.]

## Warum jetzt
[Was macht diesen Moment relevant? Zahlen, Dringlichkeit, strategischer Fit.]

## Empfehlung
[BUILD / SKIP / MEHR DATEN — mit klarer Begründung. Kein Wenn-Dann.]

## Offene Fragen
- [Frage 1]
- [Frage 2]
```

## Output

Schreibe den fertigen Brief nach `output/YYYY-MM-DD/strategy/decision-brief.md`.
