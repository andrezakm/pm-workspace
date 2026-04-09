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
context/   — permanenter Kontext (company, strategy, product, team, metrics, learnings, roadmap)
skills/    — Skill-Bibliothek, Details in skills/README.md
output/    — Artefakte, gespiegelt nach Bereichen
input/     — Live-Quellen (MCP oder eigene Daten), kein fester Ordner
```

## Handoff-Grenze

`skills/spec-eval/` ist die Grenze zwischen PM und Dev.

## Navigation

Für Skills: lies zuerst `skills/README.md`
