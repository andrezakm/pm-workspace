# Eval Runner

Eval + App → PASS / FAIL / UNKLAR pro Kriterium, mit Begründung aus dem Code.

## Input
`output/YYYY-MM-DD/spec-eval/eval.md` + `output/YYYY-MM-DD/prototyping/app.py` (oder option-a/b/c)

## Invocation
`/eval-runner`
Mit expliziten Pfaden: `/eval-runner output/YYYY-MM-DD/spec-eval/eval.md output/YYYY-MM-DD/prototyping/option-b/app.py`

## Output
`output/YYYY-MM-DD/prototyping/eval-results.md`

## Weiter mit
`/handoff-packager`
