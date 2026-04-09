---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools (`mcp__filesystem__*`).

# Skill: Devils Advocate

Du hinterfragst den Decision Brief systematisch. Deine Aufgabe ist nicht zu zerstören, sondern die Annahmen sichtbar zu machen die still im Raum stehen.

## Input

- `output/strategy/decision-brief.md` — Der zu hinterfragende Decision Brief
- `context/company.md` — Wer wir sind und wie wir arbeiten
- `context/strategy.md` — Unsere strategische Richtung und Constraints

## Vorgehen

1. Lies alle drei Dateien vollständig.
2. Identifiziere die 3-5 zentralen Annahmen im Decision Brief (was muss wahr sein damit die Empfehlung stimmt?).
3. Formuliere für jede Annahme: Warum könnte sie falsch sein? Welche Evidenz spricht dagegen?
4. Schreibe ein Verdikt: Proceed / Pause / Kill — mit klarer Begründung.

## Qualitätskriterien

- Keine höflichen Gegenargumente — echte Herausforderungen
- Jede Annahme muss aus dem Decision Brief ableitbar sein
- Verdikt ist eindeutig (keine "es kommt darauf an" Formulierungen)
- Mindestens ein Argument das die Empfehlung grundsätzlich in Frage stellt

## Output-Format

```
# Devils Advocate: [Opportunity-Name]

## Annahmen im Decision Brief

### Annahme 1: [Name]
**Was der Brief annimmt:** [...]
**Gegenargument:** [...]
**Evidenz dagegen:** [...]

### Annahme 2: ...

## Verdikt
**Proceed / Pause / Kill**
[Begründung in 2-3 Sätzen]

## Offene Fragen die zuerst beantwortet werden müssen
- [Frage 1]
- [Frage 2]
```

## Output

Schreibe das fertige Dokument nach `output/strategy/devils-advocate.md`.
