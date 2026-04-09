# Strategy

Aus Mustern Entscheidungen machen. Von Clustern zur Empfehlung.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| [opportunity-scorer](opportunity-scorer/SKILL.md) | Feedback-Cluster bewerten: Vision-Fit × Wiederholbarkeit × Baubarkeit |
| [decision-brief](decision-brief/SKILL.md) | Top-Opportunity → 1-Pager mit eindeutiger Empfehlung (BUILD/SKIP/MEHR DATEN) |
| [devils-advocate](devils-advocate/SKILL.md) | Decision Brief angreifen: Annahmen aufdecken, Verdikt (Proceed/Pause/Kill) |
| [business-case-debater](business-case-debater/SKILL.md) | Vollständige Business Case Analyse in 6 Phasen (Research → Debatte → Synthese) |

## Typischer Flow

```
output/discovery/feedback-clusters.md
    ↓
/opportunity-scorer
    → output/strategy/opportunity-scorecard.md
    ↓
/decision-brief
    → output/strategy/decision-brief.md
    ↓
/devils-advocate          oder          /business-case-debater
    → output/strategy/devils-advocate.md    → output/strategy/eval-run-[timestamp]/
```

## business-case-debater — Hinweis

Der business-case-debater ist ein eigenständiges Subsystem mit 6 Phasen und Web-Research.
Vor dem Start: `skills/strategy/business-case-debater/input.yaml` befüllen.
Läuft interaktiv — nach jeder Phase Checkpoint.

## Output-Pfade

- `output/strategy/opportunity-scorecard.md`
- `output/strategy/decision-brief.md`
- `output/strategy/devils-advocate.md`
- `output/strategy/eval-run-[timestamp]/` (business-case-debater, 10+ Dateien)
