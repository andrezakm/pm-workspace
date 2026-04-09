# PM Workspace

Ein modulares System für Product Manager die mit Claude Code arbeiten.
Von rohem Feedback bis zum Dev-Handoff — in einem Repo, mit einem gemeinsamen Kontext.

## Wie starten

1. **Repo klonen**
2. **Claude Code öffnen** im `pm-workspace/` Ordner
3. **context/ befüllen** — dein Unternehmen, deine Strategie, dein Team
4. **Starte mit:** `Führe den system-auditor aus`

Der system-auditor sagt dir was noch fehlt und was als nächstes sinnvoll ist.

## Die 7 Bereiche

| Bereich | Was passiert hier |
|---------|-----------------|
| **Discovery** | Rohes Feedback und Interviews → strukturierte Cluster |
| **Strategy** | Cluster → Opportunities → Entscheidung → Business Case |
| **Roadmap** | Entscheidungen → Priorisierung (Erweiterungspunkt) |
| **Spec & Eval** | Brief → Spec → Eval-Kriterien (Grenze zu Dev) |
| **Prototyping** | Spec → 1 oder 3 Streamlit-Prototypen → Evaluation |
| **Handoff** | Alle Artefakte → gebündeltes Cover-Sheet für Dev |
| **Meta** | System-Audit: was ist fertig, was fehlt, was als nächstes |

## Typischer Durchlauf

```
Feedback/Interviews
    → /feedback-synthesizer
    → /opportunity-scorer
    → /decision-brief
    → /spec-writer
    → /option-stormer
    → /eval-runner
    → /handoff-packager
```

## Architektur-Entscheidung

Diese CLAUDE.md ist bewusst kurz gehalten — unter 500 Tokens.
Details zu einzelnen Skills leben in den README.md Files
der jeweiligen `skills/`-Unterordner. Das ist keine Faulheit,
das ist Architektur.

Claude lädt die Root-CLAUDE.md bei jeder Session.
Je größer sie ist, desto weniger Kontext bleibt für die
eigentliche Arbeit. Die Folder-Indexes werden nur geladen
wenn Claude in den Bereich navigiert.

Wenn du das System erweiterst: neuen Skill in den richtigen
Unterordner, den Folder-Index updaten, fertig. Die Root
bleibt unberührt.

*(Claude wird versuchen, alles zentral reinzupacken. Lass es nicht.)*
