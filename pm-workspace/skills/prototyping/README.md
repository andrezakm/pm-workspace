# Prototyping

Aus der Spec wird Code. Aus Code wird Evidenz.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| /prototype-builder | Spec → lauffähige Streamlit-App (eine Variante) |
| /option-stormer | Spec → 3 strukturell verschiedene Prototypen + Vergleichstabelle |
| /eval-runner | Eval + App → PASS/FAIL/UNKLAR pro Kriterium mit Begründung |

## Typischer Flow

```
output/spec-eval/spec.md
    ↓
/option-stormer                   oder          /prototype-builder
    → output/prototyping/option-a/app.py            → output/prototyping/app.py
    → output/prototyping/option-b/app.py
    → output/prototyping/option-c/app.py
    → output/prototyping/option-comparison.md
    ↓
[beste Variante wählen]
    ↓
/eval-runner
    → output/prototyping/eval-results.md
```

## Technische Constraints (alle Prototypen)

- Nur `streamlit` + `pandas` — kein matplotlib, plotly, altair
- Diagramme: `st.bar_chart`, `st.line_chart`, `st.scatter_chart`
- Kein `@st.cache_data` — `pd.read_csv()` direkt
- Python 3.8+, streamlit >= 1.0

## Output-Pfade

- `output/prototyping/app.py`
- `output/prototyping/option-a/app.py`, `option-b/`, `option-c/`
- `output/prototyping/option-comparison.md`
- `output/prototyping/eval-results.md`
