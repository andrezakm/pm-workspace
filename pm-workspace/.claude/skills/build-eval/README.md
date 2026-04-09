# Build Eval

Orchestrator: Brief → Spec + Eval + lauffähiger Prototyp in einem Lauf.

Shortcut für den gesamten Spec-Eval-Zyklus. Prüft ob Spec/Eval bereits existieren und überspringt Schritte wenn ja.

## Input
Pfad zum Brief wird beim Aufruf übergeben

## Invocation
`/build-eval input/case/brief.md`

## Output
- `output/YYYY-MM-DD/spec-eval/spec.md`
- `output/YYYY-MM-DD/spec-eval/eval.md`
- `output/YYYY-MM-DD/prototyping/app.py`

## Weiter mit
`/eval-runner`
