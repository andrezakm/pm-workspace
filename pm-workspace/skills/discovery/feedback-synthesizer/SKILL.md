---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools (`mcp__filesystem__*`).

# Skill: Feedback Synthesizer

Du analysierst rohes Kundenfeedback und verdichtest es zu strukturierten Clustern.

## Input

Der Pfad zum Feedback-Ordner wird beim Aufruf übergeben. Verwende Glob um alle .md-Dateien im Ordner zu finden.

## Vorgehen

1. **Lesen ohne werten** — Lies alle Dateien vollständig. Notiere dir wiederkehrende Themen, aber urteile noch nicht.
2. **Clustern** — Identifiziere 3–6 thematische Cluster. Jeder Cluster fasst ein Muster zusammen, das in mehreren Quellen vorkommt.
3. **Belegen** — Weise jedem Cluster mindestens 2 Direktzitate zu. Zitate immer mit Quelle (Datei + Absender, wenn verfügbar).
4. **Sonstiges** — Erwähnungen die in keinen Cluster passen, sammle unter "Sonstiges / Einzelfälle".

## Qualitätskriterien

- Mindestens 2 Belege pro Cluster (Direktzitat oder konkrete Paraphrase mit Quellenangabe)
- Kein Cluster mit weniger als 2 unabhängigen Nennungen
- Keine Interpretation die nicht direkt aus dem Datenmaterial ableitbar ist
- Widersprüche explizit dokumentieren, nicht glätten

## Output-Format

Schreibe `output/discovery/feedback-clusters.md` mit folgendem Format:

```
# Feedback-Cluster

## Cluster 1: [Name]
**Häufigkeit:** [Anzahl Nennungen, Quellen]
**Zusammenfassung:** [1-2 Sätze]
**Belege:**
- "[Direktzitat]" — [Quelle]
- "[Direktzitat]" — [Quelle]

## Cluster 2: ...

## Sonstiges / Einzelfälle
- [Einzelnennung 1] — [Quelle]
- [Einzelnennung 2] — [Quelle]
```

## Output

Schreibe die fertige Analyse nach `output/discovery/feedback-clusters.md`.
