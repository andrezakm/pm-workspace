# scripts/ — Persönliche Sandbox

Hier entwickelst du neue Funktionalität — bevor sie ein Skill wird.

## Workflow

```
scripts/mein-neuer-skill.md     ← hier entwickeln, testen, iterieren
        ↓
.claude/skills/mein-neuer-skill/SKILL.md   ← wenn fertig: als Skill verpacken
        ↓
Branch → PR → Review → Merge   ← ins Team über Git
```

## Spielregeln

- **Kein Format-Zwang.** Hier darf es chaotisch sein. Notizen, Fragmente, Experimente.
- **Kein Review nötig.** Das ist dein Zimmer. Niemand schaut rein.
- **Eigene Outputs.** Teste in `output/YYYY-MM-DD/scripts/` — damit nichts mit echten Runs kollidiert.
- **Promotion bewusst.** Wenn etwas gut genug ist, verpackst du es als SKILL.md und machst einen PR.

## Was hier typischerweise liegt

- Neue Skills in Entwicklung
- Angepasste Versionen bestehender Skills
- Experimentelle Flows (mehrere Skills verkettet)
- Prompt-Fragmente die noch nicht fertig sind
