# Slack Importer

Slack-Export → strukturiertes Feedback im cluster-ready Format.

> Platzhalter: Slack-Exportformate variieren. Skill an das eigene Format anpassen.

## Input
Ordner mit Slack-Export-Dateien (JSON, CSV, oder Markdown/Text)

## Invocation
`/slack-importer input/slack-export/`

## Output
`output/YYYY-MM-DD/discovery/slack-feedback.md`

## Weiter mit
`/feedback-synthesizer` (slack-feedback.md als zusätzliche Quelle)
