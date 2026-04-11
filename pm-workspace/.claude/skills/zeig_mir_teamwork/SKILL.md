---
disable-model-invocation: true
---

# Kurs: Teamwork in Claude Code

Wie ein PM-Team mit demselben System zusammenarbeitet — ohne sich gegenseitig in die Quere zu kommen.

Der Kurs hat 12 Schritte. Du navigierst mit "weiter" (nächster Schritt) oder "Schritt X" (direkt springen).

**Hinweis:** Dieser Kurs setzt voraus, dass du weißt wie das System aufgebaut ist (Woche 5, Kurs 1). Für die Git-Mechanik — Branches, Pull Requests, Merge — gibt es einen separaten Mini-Git-Kurs. Hier geht es um das Prinzip, nicht um die Kommandos.

**Was dieser Kurs zeigt — und was nicht:** Die Schritte hier sind Prinzipien, kein Pflichtprogramm. Auf welcher Granularität ihr übergebt, wie schnell ihr reviewt, wer merged, wann ein Artefakt "geteilt genug" ist — das müsst ihr in eurem Team aushandeln. Es gibt keine universelle Antwort. Es gibt nur die Antwort die zu eurer Kultur, eurer Größe, eurem Tempo passt.

---

## Lernziele

Nach diesem Kurs weißt du:
- Was im Team geteilt wird — und was privat bleibt
- Wie mehrere PMs mit demselben Repo arbeiten ohne zu kollidieren
- Wie Änderungen an Skills und Context kontrolliert ins Team gelangen
- Wie Artefakte (Decision Briefs, Handoffs) geteilt werden
- Wie das System durch Teamnutzung besser wird

---

## Schritt 1: Das Grundprinzip — Zimmer und Wohnzimmer

Jeder Workspace hat zwei Bereiche.

**Dein Zimmer — persönlicher Workspace:**
Sandbox. Hier probierst du aus. Hier denkst du nach. Deine drei Prototyp-Varianten, dein erster Entwurf vom Decision Brief, dein halbfertiger Skill. Niemand sieht das. Niemand muss das sehen. Das ist der Raum fürs Denken.

**Das Wohnzimmer — geteilte Infrastruktur:**
Truth. Hier gelten die Familienregeln. Was hier liegt, gilt für alle. Skills die alle nutzen. Context-Files die den Stand der Wahrheit abbilden. Learnings die das Team gesammelt hat.

**Der Übergang wird bewacht:**
Aus dem Zimmer ins Wohnzimmer kommt etwas nur durch Interaktion — synchron (Meeting, Review) oder asynchron (Slack, PR). Dasselbe Prinzip wie ein Pull Request: aus meinem Branch geht etwas in den Trunk, aber nur nach Review. Nicht automatisch. Nicht heimlich.

**Reflexion:** Was liegt in deiner aktuellen Arbeit im "Zimmer" — und was wäre reif fürs "Wohnzimmer"?

> **Tipp:** Notier dir deine Antwort — am Ende des Kurses bauen wir daraus zusammen einen konkreten Plan.

Sag "weiter" für Schritt 2.

---

## Schritt 2: Die drei Schichten

Das System hat drei Schichten:

```
Schicht 1: Geteilte Infrastruktur   → Git Repo
Schicht 2: Geteilte Quellen         → MCPs (Slack, Granola, Linear...)
Schicht 3: Persönlicher Workspace   → Lokal, dein Zimmer
```

Schicht 1 ist das Wohnzimmer. Schicht 3 ist dein Zimmer. Schicht 2 ist dazwischen — die Quellen sind geteilt, die Verarbeitung ist individuell.

Ein PM und ein Designer lesen denselben Slack-Thread. Der PM sieht ein Feature-Signal. Der Designer sieht ein UX-Problem. Beide haben Recht. Geteilte Quelle, persönliche Verarbeitung.

**Reflexion:** Welche dieser drei Schichten ist bei euch heute am schwächsten? Was fehlt?

> **Tipp:** Notier dir deine Antwort — am Ende des Kurses bauen wir daraus zusammen einen konkreten Plan.

Sag "weiter" für Schritt 3.

---

## Schritt 3: Schicht 1 — Geteilte Infrastruktur (Git)

Das gemeinsame Repo enthält drei Dinge:

**`CLAUDE.md`**
Der System-Kern. Kontext-Regeln, Handoff-Grenze, Navigation.
Gilt für alle. Änderungen nur per PR.

**`context/`**
company.md, strategy.md, product.md, team.md, metrics.md, learnings.md, roadmap.md.
Das ist der Stand der Wahrheit über euer Unternehmen.
Wenn sich die Strategie ändert, ändert sich strategy.md. Eine Quelle, alle lesen dasselbe.

**`.claude/skills/`**
Alle SKILL.md Files. Das sind die Werkzeuge des Teams.
Wenn jemand den eval-writer verbessert, profitieren alle — aber nur nach Review.

**Was NICHT ins Repo gehört:**
`output/` — das ist persönlich. Drafts, Prototypen, halbfertige Analysen. Privat bis zum bewussten Teilen.

**Wie es funktioniert:**
Jeder klont das Repo. Jeder hat lokal eine Kopie. Änderungen an Skills, Context oder CLAUDE.md laufen über Branches und Pull Requests. Skills sind jetzt quasi Code. Selber Prozess, selbes Tool.

**Git-Begriffe kurz erklärt** *(für alle die das noch nicht täglich nutzen):*
- **Branch** = deine eigene Arbeitskopie — du änderst, ohne den Stand der anderen zu berühren
- **Pull Request (PR)** = du sagst dem Team: "Ich habe etwas geändert, bitte schaut drüber"
- **Review** = jemand liest die Änderungen und gibt grünes Licht (oder macht Kommentare)
- **Merge** = die Änderungen sind drin — für alle, sofort beim nächsten `git pull`

Für den genauen Ablauf gibt es einen eigenen Mini-Git-Kurs.

**Reflexion:** Was in eurem aktuellen PM-Prozess würde in `context/` gehören? Was würde sich ändern wenn alle dasselbe context/strategy.md lesen?

> **Tipp:** Notier dir deine Antwort — am Ende des Kurses bauen wir daraus zusammen einen konkreten Plan.

Sag "weiter" für Schritt 4.

---

## Schritt 4: Schicht 2 — Geteilte Quellen (MCPs)

Slack, Granola, Gong, Jira, Linear, Analytics. Die Quellen sind geteilt — alle sehen denselben Slack-Kanal, dieselben Meetings, dieselben Tickets.

MCP-Verbindungen werden pro Person eingerichtet. Wer Slack-Zugang hat, verbindet Slack. Wer Granola nutzt, verbindet Granola. Kein Zwang — jeder verbindet was für seinen Workflow relevant ist.

**Das Wichtige:** Geteilte Quelle bedeutet nicht geteilte Interpretation. Ein PM zieht aus demselben Feedback-Pool andere Cluster als ein anderer PM — weil ihr `context/` unterschiedlich ausgefüllt ist, oder weil ihr verschiedene Fragen stellt.

Das ist kein Problem. Das ist das Ziel. Dann teilt ihr was relevant ist — über Git (ins Repo) oder direkt (Slack, Meeting).

**Reflexion:** Welche Quelle würde euer Team als erstes anbinden? Wo verliert ihr heute am meisten Zeit mit manuellem Kopieren?

Sag "weiter" für Schritt 5.

---

## Schritt 5: Schicht 3 — Persönlicher Workspace

Dein Zimmer. Hier passiert die eigentliche Arbeit.

`output/YYYY-MM-DD/` — alle Artefakte die du produzierst. Prototypen, Decision Briefs, Eval-Ergebnisse, Synthesen, Drafts. Alles privat bis du es teilst.

`scripts/` — deine Skill-Werkstatt. Hier entwickelst du neue Skills bevor sie ins Team gehen. Kein Format-Zwang, keine Reviews. Wenn etwas fertig ist, wird es zu einer SKILL.md und geht per PR ins Repo.

Was hier passiert:
- Du probierst drei Prototyp-Varianten aus (`/option-stormer`)
- Du schreibst einen Decision Brief und lässt den Devil's Advocate drüber laufen
- Du synthetisierst Feedback und sortierst Cluster
- Du schreibst eine Spec und testest sie gegen die Eval

Nichts davon muss sofort im Team sichtbar sein. Das schützt den Denkraum. Nicht alles was du produzierst, muss sofort im Teamkontext stehen.

**Wann etwas rausgeht:**
- Decision Brief ist fertig → in Slack posten oder im Weekly zeigen
- Skill verbessert → PR ins Repo
- Learning gemacht → in `context/learnings.md` eintragen, per PR
- Handoff-Package fertig → dem Dev übergeben

**Reflexion:** Welcher Schritt in deinem aktuellen Prozess "geht zu früh raus" — bevor du selbst zufrieden bist?

Sag "weiter" für Schritt 6.

---

## Schritt 6: Was geteilt wird — und wie

Fünf Typen von Inhalten, fünf Wege:

| Was | Wo | Wie | Beispiel |
|-----|-----|-----|---------|
| **Neuer Skill** | `scripts/` → `.claude/skills/` | Entwickeln in scripts/ → SKILL.md → Branch → PR → Merge | Du entwickelst einen neuen Skill lokal. Wenn er gut ist, machst du einen PR. Ab Merge gehört er allen. |
| **Skills (verbessert)** | `.claude/skills/` im Repo | Branch → PR → Review → Merge | Du ergänzt eine Risk-Sektion im decision-brief Skill. Ab jetzt hat das ganze Team sie. |
| **Context** | `context/` im Repo | Branch → PR → Review → Merge | Strategie-Meeting ergibt neuen Fokus. PM updated strategy.md. Alle Skills arbeiten ab jetzt mit neuem Kontext. |
| **CLAUDE.md** | Root im Repo | Branch → PR → Review → Merge | Team beschließt neue Output-Konvention. Jemand updated CLAUDE.md. |
| **Artefakte** | Persönlich → Slack / Meeting | Bewusste Entscheidung | Decision Brief fertig → Slack oder Weekly. |
| **Learnings** | `context/learnings.md` | Branch → PR → Merge | "FAQ-Pattern war klar besser als Chat." Eingetragen. Das System weiß es beim nächsten Mal. |

**Reflexion:** Welcher dieser Typen fehlt bei euch am meisten? Was geht heute verloren weil es keinen Weg zurück ins System findet?

> **Tipp:** Notier dir deine Antwort — am Ende des Kurses bauen wir daraus zusammen einen konkreten Plan.

Sag "weiter" für Schritt 7.

---

## Schritt 7: Beispiel — Anna macht Discovery

Setting: PM-Team, 2 PMs. Anna macht Discovery, Ben übernimmt ab Spec/Eval. Geteiltes Repo. Beide haben Slack und Granola verbunden.

**Anna — in ihrem Zimmer:**

Anna verbindet den Slack-MCP, zieht Nachrichten aus `#kundenfeedback` und `#retros`:

> "Führe /feedback-synthesizer aus auf die letzten 3 Monate aus #kundenfeedback und #retros"

Ergebnis: `output/2026-04-11/discovery/feedback-clusters.md`
4 Cluster. Onboarding dominiert mit 8 Erwähnungen.

Anna lässt `/feedback-synthesizer` auch über die letzten Granola-Meeting-Transkripte laufen:

> "Führe /feedback-synthesizer aus auf die Sales Calls der letzten 4 Wochen aus Granola"

Ergebnis: `output/2026-04-11/discovery/feedback-clusters-granola.md`
Bestätigt: Onboarding ist das stärkste Signal.

Alles noch in Annas Zimmer. Niemand sieht es.

**Reflexion:** Wann ist ein Discovery-Output "gut genug" um ihn zu teilen? Wer entscheidet das?

Sag "weiter" für Schritt 8.

---

## Schritt 8: Beispiel — Anna teilt (Zimmer → Wohnzimmer)

Anna läuft noch weiter:

> "Führe /opportunity-scorer aus"

Ergebnis: `output/2026-04-11/strategy/opportunity-scorecard.md`
Onboarding: 14/15. Meeting-Summarizer: 11/15.

> "Führe /decision-brief aus"

Ergebnis: `output/2026-04-11/strategy/decision-brief.md`
Empfehlung: BUILD.

Anna ist nicht sicher. Devil's Advocate:

> "Führe /devils-advocate aus"

Stärkstes Gegenargument: "Onboarding-Agents gibt es von der Stange. Warum custom bauen?"
Annas Antwort: Weil wir die Brücke zum Produkt suchen, nicht die schnellste Lösung.

**Anna teilt — zwei Varianten:**

*Synchron:* Anna zeigt Decision Brief + Devil's Advocate im Team-Weekly. Diskussion. Team sagt: "Go."

*Asynchron:* Anna postet Decision Brief in Slack `#produktteam`. Ben liest, kommentiert, sagt: "Nehme ich für die Spec."

In beiden Fällen: die Entscheidung ist jetzt im Team. Der Brief kann optional ins Repo (als Referenz), muss aber nicht.

**Was ins Repo MUSS:** Wenn Anna dabei den decision-brief Skill verbessert hat — Branch, PR, Review, Merge. Ben bekommt den verbesserten Skill automatisch beim nächsten `git pull`.

**Reflexion:** Wie würde diese Übergabe bei euch heute konkret aussehen? Slack, Meeting, E-Mail, Ticket — was passt zu eurer Kultur?

> **Tipp:** Notier dir deine Antwort — am Ende des Kurses bauen wir daraus zusammen einen konkreten Plan.

Sag "weiter" für Schritt 9.

---

## Schritt 9: Beispiel — Ben macht Spec, Eval, Prototyp

Ben nimmt Annas Decision Brief als Ausgangspunkt und schreibt einen Feature-Brief.

> "Führe /spec-writer aus für input/case/onboarding-brief.md"

Ergebnis: `output/2026-04-11/spec-eval/spec.md`
Was der Agent können muss, welche Fragen er beantworten muss, welche Datenquellen er braucht.

Ben reviewt die Spec. Passt zwei Punkte an. Dann die Eval:

> "Führe /eval-writer aus"

Ergebnis: `output/2026-04-11/spec-eval/eval.md`
10 Kriterien, alle pass/fail.

Ben will drei Varianten sehen:

> "Führe /option-stormer aus"

Ergebnis:
```
output/2026-04-11/prototyping/option-a/app.py  — Chat-Interface
output/2026-04-11/prototyping/option-b/app.py  — FAQ mit Suchfeld
output/2026-04-11/prototyping/option-c/app.py  — Guided Flow
output/2026-04-11/prototyping/option-comparison.md
```

Ben zeigt Variante B einem Kollegen auf Zoom. Variante B gewinnt.

Eval-Runner über Variante B:

> "Führe /eval-runner aus für output/2026-04-11/spec-eval/eval.md und output/2026-04-11/prototyping/option-b/app.py"

8 PASS, 1 FAIL, 1 UNKLAR. FAIL: "Agent antwortet auf Fragen außerhalb des Onboarding-Kontexts." Ben schärft die Spec nach, baut neu. 9 PASS, 1 UNKLAR. Gut genug.

**Reflexion:** An welchem Punkt in Bens Flow wäre der natürliche Checkpoint für ein kurzes Alignment mit Anna?

Sag "weiter" für Schritt 10.

---

## Schritt 10: Beispiel — Handoff (Zimmer → draußen)

> "Führe /handoff-packager aus"

Ergebnis: `output/2026-04-11/handoff/handoff.md`

Enthält:
- Feature: Onboarding-Agent
- Links zu Spec, Eval, Prototyp, Decision Brief
- 5 konkrete nächste Schritte für Dev
- Explizite Trennung: was PM evaluiert hat (Funktionalität) vs. was Dev ergänzen soll (Latenz, Halluzinations-Rate, Security, HR-Integration)

Ben übergibt das Package an die Entwicklerin. Sie nimmt Spec + Eval, ergänzt ihre technische Schicht, und baut.

Die PM-Eval bleibt bestehen. Wenn der Production-Code fertig ist, muss er beide Evals bestehen — Bens PM-Eval UND die technische Eval der Entwicklerin.

**Das ist der Punkt wo das System die Team-Grenze überschreitet.** PM → Dev. Die Artefakte wandern. Das Handoff-Package ist das Vehikel.

**Reflexion:** Was gibt es bei euch heute anstelle eines Handoff-Packages? Was geht dabei verloren?

Sag "weiter" für Schritt 11.

---

## Schritt 11: Learnings zurückfließen lassen

Das System wird besser durch Benutzung — aber nur wenn Learnings auch eingetragen werden.

**Was ins Repo zurückfließt:**

`context/learnings.md` (per PR):
> "Onboarding-Agent: FAQ-Pattern (Variante B) war klar besser als Chat-Interface. User wollen suchen, nicht chatten. Guided Flow zu einschränkend."

Ab jetzt weiß das System beim nächsten Onboarding-ähnlichen Projekt: FAQ-Pattern bevorzugen.

`.claude/skills/` (per PR, falls verbessert):
> Ben hat den eval-writer angepasst — ein neues Kriterium für Agent-Scope-Begrenzung eingebaut. PR, Review, Merge. Ab jetzt prüft jede Eval automatisch ob der Agent seinen Scope einhält.

**Das ist der Unterschied zu einem Tool:** Ein Tool lernt nicht. Ein System das durch Benutzung besser wird, tut es — aber nur wenn Menschen die Schleife schließen.

Das ist auch das Schwierigste. Der Flow ist fertig, das Handoff ist draußen. Niemand hat mehr Energie für Learnings. Das muss deshalb ein expliziter Schritt sein — kein Nachgedanke.

**Reflexion:** Was war das letzte Mal dass euer Team ein Learning explizit festgehalten hat? Wo ist es gelandet?

Sag "weiter" für Schritt 12.

---

## Schritt 12: Zusammenfassung und nächste Schritte

```
WOHNZIMMER (Repo)           ZIMMER (Lokal)
──────────────────           ──────────────
CLAUDE.md                   output/YYYY-MM-DD/
context/                    Drafts
.claude/skills/             Prototypen
                            scripts/ ← Skill-Werkstatt
                            Experimente

Übergang: PR oder Meeting    Übergang: bewusstes Teilen
Familienregeln:              Deine Regeln:
Kein PR ohne Review          Mach was du willst
Skills sind Code             Probier drei Varianten
Context ist Truth            Bau in scripts/, promote per PR
Änderungen sind sichtbar     Teile wenn's gut ist
```

**Wenn ihr heute anfangen wollt:**

1. Repo aufsetzen — einer erstellt, alle klonen
2. `context/` gemeinsam befüllen — das ist die erste Konversation die zählt
3. Eine Spielregel festlegen: wie läuft ein Skill-PR ab? Wer reviewed, wie schnell?
4. Ersten gemeinsamen Flow durchlaufen — einer macht Discovery, anderer Spec/Eval
5. Learning eintragen — bewusst, als letzten Schritt des Flows

**Die eine Frage die ihr beantworten müsst:**
Wer ist der Guardian des Wohnzimmers? Wer merged PRs, wer achtet darauf dass context/ aktuell bleibt, wer hat die Übersicht über die Skills? Das muss jemand sein — kein Tool.

---

**Kurs abgeschlossen. Jetzt: euren Plan bauen.**

Du weißt wie das Zimmer aussieht. Du weißt wie das Wohnzimmer aussieht. Du weißt wie der Übergang funktioniert.

Wenn du dir während des Kurses Notizen gemacht hast — jetzt ist der Moment. Sag Claude:

> "Ich habe den Teamwork-Kurs durchgearbeitet. Hier sind meine Notizen: [deine Notizen]. Hilf mir einen konkreten Plan zu erstellen: wie setze ich das System mit meinem Team auf, was passe ich an, welche Spielregeln legen wir fest, wer übernimmt was?"

Claude arbeitet dann mit dir durch: was ihr schon habt, was ihr aufbauen müsst, welche Spielregeln ihr festlegen solltet, wer den Guardian des Wohnzimmers macht.

**Für den Überblick:** Die Präsentation `doc/PM-System-Übersicht.html` zeigt alles nochmal komprimiert — Struktur, Flows, Bereiche. Nützlich als Referenz im Team-Gespräch oder beim Onboarding neuer Kollegen.

---

## Zusatzmaterial

- `doc/PM-System-Übersicht.html` — Präsentation: Struktur, Flows, alle Skills im Überblick
- `README.md` — Skill-Übersicht
- Mini-Git-Kurs — Branches, PRs, Merge für PM-Teams (separater Kurs)
- `../TeamworkinClaude.md` — Vollständiges Referenz-Dokument mit Beispielen
