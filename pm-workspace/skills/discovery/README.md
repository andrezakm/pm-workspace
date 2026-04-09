# Discovery

Rohdaten strukturieren. Muster sichtbar machen. Bevor du bewertest, musst du verstehen.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| /feedback-synthesizer | Mehrere Feedback-Quellen → 3-6 thematische Cluster mit Direktzitaten |
| /interview-analyzer | Interview-Transkripte → Einzel-Analyse (6 Dimensionen) + Cross-Interview-Synthese |
| /slack-importer | Slack-Export → strukturiertes Feedback (Platzhalter, ans eigene Format anpassen) |

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

- `output/discovery/feedback-clusters.md`
- `output/discovery/interview-synthesis.md`
- `output/discovery/interview-individual-[nachname].md`
- `output/discovery/slack-feedback.md`

## Weiter mit

`output/discovery/feedback-clusters.md` ist der Input für `/opportunity-scorer`.
