# PM Workspace

Ein modulares System für Product Manager die mit Claude Code arbeiten.
7 Bereiche, 14+ Skills, ein gemeinsames Kontext-Fundament.
Alle Outputs auf Deutsch mit korrekten Umlauten (ä, ö, ü, ß).

## Kontext-Regel

Bevor du irgendeinen Skill ausführst, lies die relevanten Context-Files:
- `context/company.md` + `context/strategy.md` — immer
- `context/product.md` — bei Spec, Prototyping, Handoff
- `context/team.md` + `context/roadmap.md` — bei Priorisierung
- `context/metrics.md` — bei Scoring und Tracking

Ohne Kontext kein Output.

## Ordnerstruktur

```
context/        — permanenter Kontext (company, strategy, product, team, metrics, learnings, roadmap)
.claude/skills/ — ausführbare Skills, Invocation: /skill-name
skills/         — Navigation und Flows, Details in skills/README.md
output/         — Artefakte, gespiegelt nach Bereichen
input/          — eigene Daten (Feedback, Interviews, Briefs)
```

## Handoff-Grenze

`spec-eval/` Skills (spec-writer, eval-writer, build-eval) sind die Grenze zwischen PM und Dev.

## Navigation

Für Skills: lies zuerst `skills/README.md`
