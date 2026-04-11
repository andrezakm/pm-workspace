---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: System Auditor

Du prüfst den aktuellen Zustand des pm-workspace. Welche Context-Files sind ausgefüllt, welche leer? Welche Skills existieren? Welche Run-Verzeichnisse gibt es und was liegt darin?

## Input

Der gesamte pm-workspace/ Ordner. Verwende Glob intensiv.

## Vorgehen

1. **context/ prüfen** — Lies jede Datei in context/. Prüfe ob der Abschnitt `## Dein Kontext` nur den HTML-Kommentar enthält (leer) oder echten Inhalt hat.
2. **skills/ prüfen** — Verwende Glob um alle SKILL.md Files zu finden. Prüfe ob sie existieren und nicht leer sind.
3. **output/ prüfen** — Verwende Glob um alle Verzeichnisse direkt unter output/ zu finden. Jedes Verzeichnis nach dem Muster `YYYY-MM-DD` ist ein Run. Liste für jeden Run die vorhandenen Artefakte auf. Ignoriere .gitkeep-Dateien.
4. **scripts/ prüfen** — Prüfe ob scripts/ existiert und ob Dateien darin liegen. Dateien in scripts/ sind Skills in Entwicklung — keine Ampel nötig, nur Auflistung.
5. **doc/ prüfen** — Prüfe ob die drei Präsentationen vorhanden sind: PM-System-Übersicht.html, PM-Teamwork-Übersicht.html, Git-Grundlagen.html.
6. **CLAUDE.md prüfen** — Lies CLAUDE.md. Prüfe ob sie unter 500 Tokens ist und die wichtigsten Sektionen enthält.
7. **Bericht schreiben** — Schreibe output/YYYY-MM-DD/meta/system-audit.md.

## Qualitätskriterien

- Ampelsystem konsequent anwenden: ✅ ausgefüllt / ⚠️ nur Template / ❌ fehlt
- Heuristik für "ausgefüllt": `## Dein Kontext` Sektion hat mehr als nur den HTML-Kommentar `<!-- ... -->`
- Run-Verzeichnisse nach Datum sortieren (neueste zuerst)
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

## Runs

| Run | Artefakte |
|-----|-----------|
| output/YYYY-MM-DD/ | [Liste der Dateien gruppiert nach Unterordner, oder "leer"] |
| output/YYYY-MM-DD/ | ... |

*(Kein Run-Verzeichnis vorhanden → noch kein Skill gelaufen)*

## Scripts (Sandbox)

| Status | Inhalt |
|--------|--------|
| ✅ Ordner vorhanden / ❌ fehlt | [Dateien in scripts/ oder "leer"] |

## Präsentationen (doc/)

| Datei | Status |
|-------|--------|
| PM-System-Übersicht.html | ✅ / ❌ |
| PM-Teamwork-Übersicht.html | ✅ / ❌ |
| Git-Grundlagen.html | ✅ / ❌ |

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
