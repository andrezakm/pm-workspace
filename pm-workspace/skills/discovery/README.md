# Discovery

Rohdaten strukturieren. Muster sichtbar machen. Bevor du bewertest, musst du verstehen.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| [feedback-synthesizer](feedback-synthesizer/SKILL.md) | Mehrere Feedback-Quellen → 3-6 thematische Cluster mit Direktzitaten |
| [interview-analyzer](interview-analyzer/SKILL.md) | Interview-Transkripte → Einzel-Analyse (6 Dimensionen) + Cross-Interview-Synthese |
| [slack-importer](slack-importer/SKILL.md) | Slack-Export → strukturiertes Feedback (Platzhalter, ans eigene Format anpassen) |

## Typischer Flow

```
Rohdaten (Slack, Emails, Interviews, Docs)
    ↓
/feedback-synthesizer [pfad-zum-ordner]
    → output/discovery/feedback-clusters.md

Interviews
    ↓
/interview-analyzer [pfad-zum-ordner]
    → output/discovery/interview-synthesis.md
```

## Output-Pfade

- `output/discovery/feedback-clusters.md` — Cluster aus dem feedback-synthesizer
- `output/discovery/interview-synthesis.md` — Synthese aus dem interview-analyzer
- `output/discovery/interview-individual-[nachname].md` — Einzel-Analysen pro Interview
- `output/discovery/slack-feedback.md` — Strukturiertes Slack-Feedback

## Weiter mit

`output/discovery/feedback-clusters.md` ist der Input für den [opportunity-scorer](../strategy/opportunity-scorer/SKILL.md).
