---
disable-model-invocation: true
---

# Kurs: Woche 5 — Das System

Willkommen in Woche 5. Heute baust du nichts. Du schaust zu — und verstehst, wie das System das du vor dir hast aufgebaut ist, was es kann, und wie du es auf deine Realität anpasst.

Der Kurs hat 12 Schritte. Du navigierst mit "weiter" (nächster Schritt) oder "Schritt X" (direkt springen).

**Kein Hands-on erforderlich.** Aber: Alles hier ist live. Wenn du etwas ausprobieren willst, kannst du jederzeit aus dem Kurs heraus einen Skill aufrufen — und dann weitermachen.

---

## Lernziele

Nach diesem Kurs weißt du:
- Wie der pm-workspace aufgebaut ist und was wo liegt
- Welche Flows für welche PM-Situationen relevant sind
- Wie du das System auf deinen Kontext anpasst
- Wie du es lokal erweiterst — manuell, halbautomatisch, automatisch
- Wo du neue Skills findest und wie du sie integrierst
- Den Unterschied zwischen persönlichem Assistenten und Team-Interface

**Was dieser Kurs nicht ist:** Eine Tool-Demo. Das Ziel ist nicht "ich weiß wie man /feedback-synthesizer aufruft" — sondern "ich verstehe warum das System so gebaut ist und wo ich eingreifen würde."

---

## Schritt 1: Warum ein System — und nicht nur ein Prompt?

Du hast in den letzten Wochen einzelne Skills kennengelernt: Feedback analysieren, Specs schreiben, Prototypen bauen. Das Problem mit einzelnen Skills: sie arbeiten nicht zusammen. Jeder kennt seinen Kontext nicht. Jeder fängt von vorn an.

Ein System löst das. Nicht durch mehr Automatisierung — sondern durch **gemeinsamen Kontext**.

Das ist der Kern des pm-workspace:

```
context/ + input/  →  Skills  →  output/YYYY-MM-DD/
```

Die Skills kennen dein Unternehmen. Deine Strategie. Dein Team. Dein Produkt. Sie lesen das vor jedem Lauf. Was rauskommt ist nicht generisch — es ist auf dich kalibriert.

**Die zweite Idee:** Ein Run = ein Verzeichnis. Alles was heute entsteht liegt in `output/2026-04-11/`. Morgen in `output/2026-04-12/`. Kein Überschreiben. Kein Verlust. Du kannst Runs vergleichen.

**Reflexion:** Was passiert bei dir heute wenn du eine Entscheidung vorbereiten willst? Wie viel Zeit geht für Strukturierung drauf — bevor du überhaupt anfängst zu denken?

Sag "weiter" für Schritt 2.

---

## Schritt 2: Anatomie — Was liegt wo

Der pm-workspace hat drei Schichten:

```
pm-workspace/
│
├── context/          ← Das Hirn des Systems
│   ├── company.md    Wer ihr seid, wie ihr arbeitet
│   ├── strategy.md   Wohin ihr wollt, was euch begrenzt
│   ├── product.md    Was ihr baut, für wen
│   ├── team.md       Wer da ist, welche Fähigkeiten
│   ├── metrics.md    Woran ihr Erfolg messt
│   ├── roadmap.md    Was geplant ist
│   └── learnings.md  Was ihr gelernt habt
│
├── input/            ← Rohdaten rein
│   ├── raw_feedback/ Slack, Emails, Interview-Notizen
│   ├── interviews/   Qualitative Interview-Dateien
│   └── case/         Briefs und Datendateien
│
├── output/           ← Artefakte raus
│   └── YYYY-MM-DD/   Ein Verzeichnis pro Run
│
└── .claude/
    └── skills/       ← Die Skills (flach, aber konzeptuell gegliedert)
```

Die `.claude/skills/`-Struktur ist technisch flach — Claude Code braucht das so. Konzeptuell sind die Skills in 7 Bereiche gegliedert: Discovery, Strategy, Roadmap, Spec & Eval, Prototyping, Handoff, Meta.

**Das Wichtigste:** `context/` wird von jedem Skill automatisch gelesen. Du befüllst es einmal. Danach kennt das System deinen Kontext — bei jedem Aufruf, bei jedem Skill.

**Reflexion:** Was würdest du in `context/strategy.md` schreiben? Was sind die zwei, drei Dinge die jeder Output über eure Strategie wissen müsste?

Sag "weiter" für Schritt 3.

---

## Schritt 3: Wie ein Skill funktioniert

Ein Skill ist eine Markdown-Datei mit Instruktionen. Du rufst ihn mit `/skill-name` auf. Claude Code liest die Datei, führt sie aus, schreibt den Output.

Was passiert unter der Haube:

1. Claude liest `CLAUDE.md` — Kontext-Regel, Handoff-Grenze, Navigation
2. Claude liest den relevanten `context/`-Files (je nach Skill)
3. Claude liest die `SKILL.md` des aufgerufenen Skills
4. Claude liest den Input (Feedback-Ordner, Brief, vorherige Outputs)
5. Claude schreibt in `output/YYYY-MM-DD/[bereich]/`

Kein Zauberei. Keine Black Box. Alles liegt offen in `.claude/skills/[name]/SKILL.md`. Du kannst jeden Skill öffnen und lesen — und verstehen warum er das tut was er tut.

**Das ist der Unterschied zu einem Tool:** Du bist nicht Nutzer einer Plattform. Du bist Eigentümer der Instruktionen. Du kannst sie ändern. Ergänzen. Löschen.

**Reflexion:** Welchen Skill würdest du als erstes öffnen und lesen? Warum?

Sag "weiter" für Schritt 4.

---

## Schritt 4: Die 7 Bereiche und ihre Flows

```
Discovery          → Verstehen: Was sagen Kunden, Nutzer, Daten?
Strategy           → Entscheiden: Was bauen wir — und warum?
Roadmap            → Planen: In welcher Reihenfolge, mit wem? (Erweiterungspunkt)
Spec & Eval        → Übergeben: Was genau wird gebaut, wann ist es gut?
Prototyping        → Validieren: Funktioniert die Idee als Artefakt?
Handoff            → Abschließen: Was braucht Dev zum Starten?
Meta               → Navigieren: Wo stehe ich, was fehlt?
```

Der natürliche Flow durch diese Bereiche ist die PM-Kernaufgabe — von Rohdaten zur Entscheidung zur Übergabe. Aber du musst nicht immer den ganzen Weg gehen. Manchmal fängst du bei Strategy an. Manchmal brauchst du nur einen Handoff.

**Die drei häufigsten Flows im PM-Alltag:**

**Flow 1: Discovery → Entscheidung**
Rohes Feedback liegt vor. Du willst wissen: was steckt drin, was ist die wichtigste Opportunity?
`/feedback-synthesizer` → `/opportunity-scorer` → `/decision-brief` → `/devils-advocate`

**Flow 2: Entscheidung → Dev-Ready**
Du weißt was gebaut werden soll. Du brauchst Spec, Prototyp, Handoff.
`/spec-writer` → `/option-stormer` → `/eval-runner` → `/handoff-packager`

**Flow 3: Strategische Analyse**
Du willst einen Business Case durchleuchten — mit Web-Research und strukturierter Debatte.
`/business-case-debater` (eigenständiges Subsystem, läuft interaktiv)

**Reflexion:** Welcher dieser Flows wäre heute in deinem Alltag am nützlichsten? Was liegt gerade auf deinem Tisch das du damit angehen könntest?

Sag "weiter" für Schritt 5.

---

## Schritt 5: Output-Qualität — Immer prüfen, immer iterieren

Das System produziert schnell. Das ist kein Grund, alles unkritisch zu übernehmen.

**Die Grundregel:** Jeden Output lesen. Verstehen was drin steht. Dann entscheiden: passt es, oder muss etwas korrigiert werden?

Wenn etwas nicht stimmt — nicht von vorne anfangen. Stattdessen:

> "In der Scorecard bei Cluster 3 fehlt der Bezug zu unserem Team-Constraint. Ergänze das."

Claude überarbeitet genau das. Du liest nochmal. Passt es jetzt? Dann weiter.

**Dieses Iterationsprinzip ist keine Schwäche des Systems — es ist das Design.** Der Mensch behält das Urteil. Claude macht die Arbeit. Die Übergabe passiert bewusst, nicht automatisch.

Das gilt auch für Übergaben zwischen Skills: wenn `/decision-brief` etwas produziert das nicht stimmt, korrigierst du es bevor du `/spec-writer` aufrufst. Fehler pflanzen sich fort. Je früher du eingreifst, desto kleiner die Korrektur.

**Die Faustregel:** Fixe immer so früh wie möglich in der Kette.
Brief → Spec → Eval → Code. Ein Fehler im Brief kostet zehnmal so viel wenn er erst im Code auftaucht.

**Reflexion:** Wann hast du zuletzt einen AI-Output unkritisch übernommen? Was wäre passiert wenn du ihn gründlicher gelesen hättest?

Sag "weiter" für Schritt 6.

---

## Schritt 6: Kontext ist alles — context/ anpassen

Das Stärkste am System ist nicht die Skill-Sammlung. Es ist der gemeinsame Kontext.

**Wie du den Kontext befüllst:**

Öffne `context/company.md`. Du siehst einen Template-Abschnitt `## Dein Kontext`. Ersetze den Platzhalter mit echten Informationen — so viel oder wenig wie du willst, aber spezifisch genug dass Claude daraus etwas ableiten kann.

Nicht: *"Wir sind ein innovatives Tech-Unternehmen."*
Sondern: *"Wir haben 12 Personen. Engineering: 4. Wir deployen wöchentlich. Unser größter Constraint ist Bandbreite, nicht Budget."*

**Was wenn der Standard-Kontext nicht reicht?**

Du kannst eigene Context-Files hinzufügen. Beispiele:
- `context/competitors.md` — Wettbewerbslandschaft
- `context/customers.md` — Kundensegmente und ihre Jobs-to-be-done
- `context/tech-stack.md` — Was gebaut werden kann und was nicht

Damit Claude diese Files liest, ergänzt du die Kontext-Regel in `CLAUDE.md`:

```
- context/competitors.md — bei Discovery und Strategy
- context/customers.md — immer
```

Einfach eine Zeile hinzufügen. Claude liest es beim nächsten Skill-Aufruf.

**Reflexion:** Welche Information fehlt in den Standard-Context-Files die für euch besonders relevant wäre? Habt ihr etwas das die meisten PM-Teams nicht haben — und das in den Kontext sollte?

Sag "weiter" für Schritt 7.

---

## Schritt 7: Lokal erweitern — Input automatisieren, Output weiterleiten

Das System läuft lokal. Das heißt: du entscheidest wo Input herkommt und wo Output landet.

**Input automatisieren — Beispiele mit MCPs:**

Wenn du Slack-Nachrichten direkt ins System ziehen willst:
```
/slack-importer  →  liest input/slack-export/  →  output/YYYY-MM-DD/discovery/slack-feedback.md
```

Mit dem Slack-MCP kannst du den Export-Schritt überspringen — Nachrichten landen direkt in `input/`. Gleiches gilt für Notion-Seiten, Linear-Tickets, E-Mail-Postfächer.

Das ist die Integration die jeden Flow kürzer macht: **nicht mehr kopieren, sondern verbinden.**

**Output weiterleiten — Beispiele:**

Der Handoff landet in `output/YYYY-MM-DD/handoff/handoff.md`. Du könntest ihn:
- Als Notion-Seite exportieren (Notion-MCP)
- Als Linear-Dokument anlegen (Linear-MCP)
- Als E-Mail-Entwurf vorbereiten (Gmail-MCP)

**Aber:** Mach das nicht als erstes. Mach es wenn du dem Flow vertraust.

**Reflexion:** Welche Datenquelle würdest du als erstes anbinden? Wo verlierst du heute am meisten Zeit mit Copy-Paste?

Sag "weiter" für Schritt 8.

---

## Schritt 8: Manuell → Übergabe → Automatisch

Das ist die Reife-Kurve die für jede Integration gilt:

**Stufe 1 — Manuell**
Du rufst jeden Skill selbst auf. Du liest jeden Output. Du entscheidest was weitergeht. Kein Schritt ohne dein Urteil.

*Wann:* Immer am Anfang. Auch wenn du das System schon kennst — bei einem neuen Flow, einem neuen Kontext, einem neuen Team.

**Stufe 2 — Mit Übergabe**
Du automatisierst Teile des Flows, aber baust bewusste Haltepunkte ein. Beispiel:

> `/feedback-synthesizer` läuft automatisch über Nacht.
> Morgens liest du die Cluster.
> Erst wenn du sagst "weiter" läuft `/opportunity-scorer`.

Das 4-Augen-Prinzip als Design-Entscheidung: nicht weil du dem System nicht vertraust, sondern weil du die Kontrolle behalten willst ohne alles selbst zu machen.

**Stufe 3 — Automatisch**
Der gesamte Flow läuft. Output landet wo er soll. Du greifst nur ein wenn etwas auffällt.

*Wann:* Wenn du den Flow kennst. Wenn der Kontext stabil ist. Wenn die Outputs konsistent gut genug sind.

**Wichtig:** Stufe 3 bedeutet nicht "kein Mensch mehr". Es bedeutet: der Mensch entscheidet wo er eingreift — bewusst, nicht reaktiv.

**Und: Zielformulierung zuerst.** Bevor du automatisierst, frage: für wen ist dieser Output? Ein Handoff für Dev sieht anders aus als ein Summary für dein Management, anders als ein Briefing für dich selbst. Das System kann unterschiedliche Formate für unterschiedliche Audiences erzeugen — aber du musst es ihm sagen.

**Reflexion:** Welcher Flow in deinem Alltag würde von Stufe 2 profitieren — automatisch laufen, aber mit einem bewussten Haltepunkt bevor er weitergeht?

Sag "weiter" für Schritt 9.

---

## Schritt 9: Skills klauen und anpassen

Das System ist open-ended. Die interessanteste Erweiterung kommt nicht von dir allein — sondern von der Community.

**Wo du Skills findest:**

- **Pawel Huryn** (pawelonasubstack.com) — PM-Prozesse, Roadmaps, Stakeholder-Management
- **Aakash Gupta** (aakashg.com) — Growth, Metrics, Feature-Priorisierung  
- **Claude Code Community** — github.com/anthropics/claude-code, Discord
- **Eigene Vorwochen** — die Skills aus Woche 1–4 sind alle übernehmbar

**Wie du einen fremden Skill integrierst:**

1. Skill lesen — vollständig. Was macht er? Was setzt er voraus?
2. Kontext prüfen — braucht er Informationen die du nicht hast?
3. Pfade anpassen — Input und Output auf `output/YYYY-MM-DD/` umbiegen
4. Context-Regel prüfen — welche `context/`-Files muss er lesen?
5. Testen — einmal manuell laufen lassen, Output beurteilen

**Niemals:** Einen fremden Skill blind übernehmen und in einen automatisierten Flow einbauen. Erst verstehen, dann vertrauen, dann automatisieren.

**Reflexion:** Welchen PM-Prozess in deinem Alltag würdest du gerne als Skill formulieren? Was würde er lesen, was würde er schreiben?

Sag "weiter" für Schritt 10.

---

## Schritt 10: Persönlicher Assistent vs. Team-Interface

Das ist der konzeptuell wichtigste Schritt dieses Kurses.

**Zwei fundamental verschiedene Nutzungsweisen:**

**Persönlicher Assistent**
Du arbeitest allein. Das System kennt deinen Kontext, deine Denkweise, deine Sprache. Die Outputs sind für dich — du entscheidest was du damit machst. Kein anderer sieht den Prozess, nur das Ergebnis.

Skills für diesen Modus: `/decision-brief`, `/devils-advocate`, `/business-case-debater`. Alles was dir hilft, schärfer zu denken.

**Team-Interface**
Das System produziert Artefakte die andere lesen. Specs die Dev bekommt. Handoffs die ins Ticket-System gehen. Scorecards die im Review-Meeting stehen.

Hier gelten andere Anforderungen: Nachvollziehbarkeit, Konsistenz, Formatierung für Nicht-Nutzer.

Skills für diesen Modus: `/spec-writer`, `/handoff-packager`, `/eval-writer`. Alles was eine Übergabe vorbereitet.

**Warum die Trennung wichtig ist:**

Ein Kollege der deine Spec liest, will nicht wissen wie sie entstanden ist. Er will wissen: was wird gebaut, wann ist es fertig, was ist außerhalb des Scope.

Ein Stakeholder der deinen Decision Brief bekommt, will nicht wissen dass Claude ihn mitgeschrieben hat. Er will wissen: was empfehlt ihr, warum.

Das System produziert beides — aber du musst wissen welchen Modus du gerade brauchst, und den Output entsprechend behandeln.

**Reflexion:** Was von dem was du heute mit Claude machst ist "persönlicher Assistent"? Was wäre "Team-Interface"? Wo ist die Grenze in deinem konkreten Alltag?

Sag "weiter" für Schritt 11.

---

## Schritt 11: Was dieses System nicht ist

Drei Grenzen die wichtig sind um offen zu benennen:

**1. Kein Entscheidungsersatz**
Das System hilft dir, schneller zu einer besseren Entscheidungsgrundlage zu kommen. Die Entscheidung selbst — ob ihr etwas baut, ob ihr eine Opportunity verfolgt, ob ihr einen Kurs korrigiert — die triffst du. Niemand anderes.

Ein `/decision-brief` sagt "BUILD". Das heißt nicht: ihr baut es. Es heißt: die Daten unterstützen diese Richtung. Du weißt was die Daten nicht wissen.

**2. Kein Todo-System**
Das System verwaltet keine Aufgaben, keine Deadlines, keine Zuständigkeiten. Es produziert Artefakte — Dokumente, Analysen, Prototypen. Was du damit machst, wie du es priorisierst, wer es umsetzt: das ist dein Prozess.

Der Unterschied ist wichtig weil viele PM-Tools versuchen beides zu sein. Der pm-workspace ist bewusst nur das erste — damit er das gut macht.

**3. Kein statisches Tool**
Das System ist ein Ausgangspunkt. In sechs Monaten werden andere Skills da sein. Andere Kontexte. Andere Flows. Was heute gut funktioniert, wirst du anpassen. Was heute fehlt, wirst du hinzufügen.

Das ist kein Fehler — das ist das Design. Ein System das du nicht ändern kannst, kannst du nicht besitzen.

**Reflexion:** Welche Erwartung hattest du vor diesem Kurs die dieser Abschnitt korrigiert? Was ist die ehrlichste Einschränkung die du jemandem in deinem Team nennen würdest der das System nutzen soll?

Sag "weiter" für Schritt 12.

---

## Schritt 12: Nächste Schritte

Du hast jetzt ein vollständiges Bild: Struktur, Flows, Anpassung, Erweiterung, Grenzen.

**Wenn du heute anfangen willst:**

1. `context/` befüllen — fang mit `company.md` und `strategy.md` an
2. `/system-auditor` aufrufen — er zeigt dir was noch fehlt
3. Einen Flow wählen der heute relevant ist — und ihn manuell einmal durchlaufen
4. Den Output beurteilen — und einmal korrigieren lassen

**Wenn du das System mit deinem Team nutzen willst:**

Das ist Woche 6. Dort geht es um: wie führe ich Kollegen ein, wie teilen wir einen Workspace, was sind die Spielregeln wenn mehrere Menschen mit demselben System arbeiten.

**Wenn du experimentieren willst — jetzt:**

Das System läuft live. Du kannst jeden Skill direkt aufrufen:
- `/system-auditor` — Workspace-Audit
- `/feedback-synthesizer input/raw_feedback/` — falls Testdaten vorhanden
- `/business-case-debater` — nach Befüllen von `input.yaml`

Kein Setup nötig. Kein Durchlauf 2 der auf dich wartet. Einfach ausprobieren.

---

**Kurs abgeschlossen.**

Du weißt wie es aufgebaut ist. Du weißt wo die Hebel sind. Der Rest ist Praxis.

---

## Zusatzmaterial

- `README.md` — Übersicht aller Skills und Flows
- `.claude/skills/[name]/README.md` — Kurzreferenz pro Skill
- `.claude/skills/[name]/SKILL.md` — Vollständige Instruktionen (für wenn du anpassen willst)
