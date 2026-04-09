# PM Workspace

Ein modulares System für Product Manager die mit Claude Code arbeiten.
Von rohem Feedback bis zum Dev-Handoff — in einem Repo, mit einem gemeinsamen Kontext.

## Wie starten

1. Repo klonen
2. Claude Code öffnen im `pm-workspace/` Ordner
3. `context/` befüllen — dein Unternehmen, deine Strategie, dein Team
4. Starte mit: `/system-auditor`

## Die 7 Bereiche

### Discovery
Du hast Feedback — aus Slack, Interviews, Emails, internen Docs. Discovery strukturiert dieses Rohmaterial in thematische Cluster mit Belegen. Erst verstehen, dann bewerten.

### Strategy
Aus Clustern werden Entscheidungen. Der opportunity-scorer bewertet Muster systematisch. Der decision-brief destilliert die Empfehlung auf eine Seite. Der devils-advocate greift sie an. Der business-case-debater führt eine vollständige Analyse durch — mit Web-Research, Hypothesen und einer 5-Rollen-Debatte.

### Roadmap
Erweiterungspunkt. Hier leben Skills die aus Entscheidungen eine priorisierte Roadmap machen — mit Anbindung an Tools wie Linear oder Jira.

### Spec & Eval
Die Grenze zwischen PM und Dev. Der spec-writer übersetzt einen Brief in eine Spec: Was gebaut wird, nicht Wie. Der eval-writer schreibt die Kriterien mit denen der Prototyp bewertet wird. Was hier entsteht, geht rüber.

### Prototyping
Aus der Spec wird Code. Der option-stormer baut drei strukturell verschiedene Prototypen — nicht eine Lösung und dann hoffen, sondern drei Richtungen und dann entscheiden. Der eval-runner prüft den Code gegen die Eval.

### Handoff
Alles was Dev braucht, gebündelt. Kein Copy-Paste — nur ein Cover-Sheet mit Verweisen, konkreten nächsten Schritten, und der expliziten Trennung was PM bereits evaluiert hat und was Dev noch prüfen soll.

### Meta
Das System über sich selbst. Der system-auditor prüft was ausgefüllt ist, was fehlt, und was als nächstes sinnvoll ist. Starte hier wenn du nicht weißt wo du stehst.

## Architektur-Entscheidung

Diese CLAUDE.md ist bewusst kurz gehalten.
Details zu einzelnen Skills leben in den README.md Files der jeweiligen `skills/`-Unterordner.
Die Skills selbst liegen in `.claude/skills/` und werden mit `/skill-name` aufgerufen.

Claude lädt die CLAUDE.md bei jeder Session. Je größer sie ist, desto weniger Kontext
bleibt für die eigentliche Arbeit. Folder-Indexes werden nur geladen wenn Claude navigiert.

Wenn du das System erweiterst: neuen Skill in `.claude/skills/[name]/SKILL.md`,
Folder-Index updaten, fertig. Die CLAUDE.md bleibt unberührt.

*(Claude wird versuchen, alles zentral reinzupacken. Lass es nicht.)*
