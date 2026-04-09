---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: System Auditor

Du prüfst den aktuellen Zustand des pm-workspace. Welche Context-Files sind ausgefüllt, welche leer? Welche Skills existieren? Welche Output-Ordner haben Artefakte?

## Input

Der gesamte pm-workspace/ Ordner. Verwende Glob intensiv.

## Vorgehen

1. **context/ prüfen** — Lies jede Datei in context/. Prüfe ob der Abschnitt `## Dein Kontext` nur den HTML-Kommentar enthält (leer) oder echten Inhalt hat.
2. **skills/ prüfen** — Verwende Glob um alle SKILL.md Files zu finden. Prüfe ob sie existieren und nicht leer sind.
3. **output/ prüfen** — Verwende Glob um alle Dateien in output/ zu finden (außer .gitkeep). Gruppiere nach Unterordner.
4. **CLAUDE.md prüfen** — Lies CLAUDE.md. Prüfe ob sie unter 500 Tokens ist und die wichtigsten Sektionen enthält.
5. **Bericht schreiben** — Schreibe output/meta/system-audit.md.

## Qualitätskriterien

- Ampelsystem konsequent anwenden: ✅ ausgefüllt / ⚠️ nur Template / ❌ fehlt
- Heuristik für "ausgefüllt": `## Dein Kontext` Sektion hat mehr als nur den HTML-Kommentar `<!-- ... -->`
- Empfehlung am Ende ist priorisiert: was ist der sinnvollste nächste Schritt?

## Output: output/meta/system-audit.md

```
# System Audit
**Datum:** [Heute]

## Context Files

| File | Status | Hinweis |
|------|--------|---------|
| context/company.md | ✅ / ⚠️ / ❌ | [leer / ausgefüllt / fehlt] |
| context/strategy.md | ... | ... |
| context/product.md | ... | ... |
| context/team.md | ... | ... |
| context/metrics.md | ... | ... |
| context/learnings.md | ... | ... |
| context/roadmap.md | ... | ... |

## Skills

| Bereich | Skill | Status |
|---------|-------|--------|
| discovery | feedback-synthesizer | ✅ / ❌ |
| discovery | interview-analyzer | ✅ / ❌ |
| discovery | slack-importer | ✅ / ❌ |
| strategy | opportunity-scorer | ✅ / ❌ |
| strategy | decision-brief | ✅ / ❌ |
| strategy | devils-advocate | ✅ / ❌ |
| strategy | business-case-debater | ✅ / ❌ |
| spec-eval | spec-writer | ✅ / ❌ |
| spec-eval | eval-writer | ✅ / ❌ |
| spec-eval | build-eval | ✅ / ❌ |
| prototyping | prototype-builder | ✅ / ❌ |
| prototyping | eval-runner | ✅ / ❌ |
| prototyping | option-stormer | ✅ / ❌ |
| handoff | handoff-packager | ✅ / ❌ |
| meta | system-auditor | ✅ |

## Output-Artefakte

| Ordner | Artefakte |
|--------|-----------|
| output/discovery/ | [Liste der Dateien oder "leer"] |
| output/strategy/ | ... |
| output/roadmap/ | ... |
| output/spec-eval/ | ... |
| output/prototyping/ | ... |
| output/handoff/ | ... |
| output/meta/ | ... |

## CLAUDE.md

| Prüfpunkt | Status |
|-----------|--------|
| Datei existiert | ✅ / ❌ |
| Unter 500 Tokens | ✅ / ⚠️ |
| Kontext-Regel vorhanden | ✅ / ❌ |

## Empfehlung

**Als nächstes solltest du:**
1. [Höchste Priorität — meistens: context/ ausfüllen wenn leer]
2. [Zweite Priorität]
3. [Optional]
```
