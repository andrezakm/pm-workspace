# Spec & Eval

Die Grenze zwischen PM und Dev. Was hier entsteht, geht rüber.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| [spec-writer](spec-writer/SKILL.md) | Brief → Spec: Was gebaut wird, nicht Wie |
| [eval-writer](eval-writer/SKILL.md) | Spec → 8-12 pass/fail Kriterien für den Prototypen |
| [build-eval](build-eval/SKILL.md) | Orchestrator: Brief → Spec + Eval + lauffähiger Prototyp in einem Lauf |

## Typischer Flow

```
Brief (manuell geschrieben, 1 Seite)
    ↓
/spec-writer [pfad/zum/brief.md]
    → output/spec-eval/spec.md
    ↓
/eval-writer
    → output/spec-eval/eval.md
```

Oder alles auf einmal:

```
/build-eval [pfad/zum/brief.md]
    → output/spec-eval/spec.md
    → output/spec-eval/eval.md
    → output/prototyping/app.py
```

## Handoff-Grenze

**PM liefert:** spec.md + eval.md (+ optional Prototyp-Optionen)
**Dev ergänzt:** Implementierungsdetails, technische Eval-Punkte, Performance-Tests

Die Trennung ist explizit im [handoff-packager](../handoff/handoff-packager/SKILL.md).

## Output-Pfade

- `output/spec-eval/spec.md`
- `output/spec-eval/eval.md`
