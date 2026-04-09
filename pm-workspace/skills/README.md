# Skills — Master-Index

Alle Skills im pm-workspace. Invocation: `/skill-name` in Claude Code.
Details in den jeweiligen Folder-READMEs. SKILL.md Files liegen in `.claude/skills/`.

## Discovery

| Skill | Was er tut |
|-------|-----------|
| /feedback-synthesizer | Rohes Kundenfeedback → thematische Cluster mit Belegen |
| /interview-analyzer | Interview-Transkripte → Einzel-Analysen + Synthese |
| /slack-importer | Slack-Export → strukturiertes Feedback (Platzhalter) |

## Strategy

| Skill | Was er tut |
|-------|-----------|
| /opportunity-scorer | Feedback-Cluster → Opportunity-Scorecard (Vision/Wiederholbarkeit/Baubarkeit) |
| /decision-brief | Scorecard → 1-Pager mit klarer Empfehlung (BUILD/SKIP/MEHR DATEN) |
| /devils-advocate | Decision Brief → Annahmen-Kritik + Verdikt (Proceed/Pause/Kill) |
| /business-case-debater | Vollständige Business Case Analyse: Research → Hypothesen → 5-Rollen-Debatte → Synthese |

## Roadmap

Noch keine Skills. Erweiterungspunkt — Plugin-Kandidaten: Linear, Jira.
Siehe [roadmap/README.md](roadmap/README.md).

## Spec & Eval

| Skill | Was er tut |
|-------|-----------|
| /spec-writer | Brief → Spec (Was, nicht Wie) |
| /eval-writer | Spec → Eval-Tabelle (8-12 pass/fail Kriterien) |
| /build-eval | Orchestrator: Brief → Spec + Eval + Prototyp in einem Lauf |

## Prototyping

| Skill | Was er tut |
|-------|-----------|
| /prototype-builder | Spec → lauffähige Streamlit-App |
| /eval-runner | Eval + App → PASS/FAIL/UNKLAR pro Kriterium |
| /option-stormer | Spec → 3 strukturell verschiedene Prototypen + Vergleich |

## Handoff

| Skill | Was er tut |
|-------|-----------|
| /handoff-packager | Alle Artefakte → Cover-Sheet mit Links und nächsten Schritten |

## Meta

| Skill | Was er tut |
|-------|-----------|
| /system-auditor | Workspace-Audit: was ist ausgefüllt, was fehlt, was als nächstes tun |
