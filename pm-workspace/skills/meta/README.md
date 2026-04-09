# Meta

Das System über sich selbst. Starte hier wenn du nicht weißt wo du stehst.

## Skills

| Skill | Beschreibung |
|-------|-------------|
| /system-auditor | Workspace-Audit: context ausgefüllt? Skills vollständig? Artefakte vorhanden? |

## Wann ausführen

- **Beim ersten Start** — um zu sehen was noch fehlt
- **Nach dem Befüllen von context/** — um zu verifizieren dass alles erkannt wird
- **Nach einem Durchlauf** — um zu sehen welche Artefakte erzeugt wurden
- **Wenn etwas nicht funktioniert** — als Diagnose-Tool

## Ampelsystem

```
✅ ausgefüllt / vorhanden
⚠️ nur Template (context/ noch nicht befüllt)
❌ fehlt
```

## Output-Pfade

- `output/meta/system-audit.md`
