# Call Highlights — Woche 5: The System

## Eröffnung: Was ist diese Woche passiert?

Wir haben ein System gebaut. Nicht einen Skill. Nicht einen Prompt. Ein ganzes System.

Alles was wir in den letzten 4 Wochen einzeln gemacht haben — Interviews analysieren, Opportunities scoren, Specs schreiben, Prototypen bauen — das lebt jetzt zusammen in einem Repo. Mit einem Kontext-Fundament. Mit Flows die ineinandergreifen.

Das ist der Moment wo es klickt. Oder wo es Fragen gibt. Beides ist gut.

---

## Block 1: Aufbau des Systems — die Architektur

**Kernfrage an die Gruppe:** Was ist der Unterschied zwischen "ich habe 14 Skills" und "ich habe ein System"?

Die Antwort: **Kontext.**

Das System hat 4 Säulen:

**context/** — Das Fundament. 7 Files: company, strategy, product, team, metrics, learnings, roadmap. Jeder Skill liest diese Files bevor er irgendwas tut. Ohne Kontext kein Output. Das ist die Regel. Nicht optional.

**skills/** — Die Werkzeuge. 14+ Skills in 7 Bereichen. Jeder Skill hat ein SKILL.md das genau beschreibt was er nimmt, was er liefert, und was Qualität bedeutet.

**output/** — Die Ergebnisse. Ein Ordner pro Run. Alles was ein Skill produziert, landet hier. Strukturiert nach Bereichen: discovery, strategy, spec-eval, prototyping, handoff, meta.

**input/** — Das Rohmaterial. Feedback, Interviews, Briefs, Datendateien. Was reinkommt.

**Didaktischer Move:** Zeig die Ordnerstruktur. Lass die Leute sehen wie simpel das ist. Das ist kein Rocket Science — das ist Ordnung. Aber Ordnung die Claude versteht und nutzt.

**Wichtiger Punkt:** Die CLAUDE.md ist bewusst kurz. Unter 500 Tokens. Warum? Weil Claude die bei JEDER Session lädt. Je größer die wird, desto weniger Kontext bleibt für die echte Arbeit. Die Details leben in den SKILL.md Files. Das ist Architektur, nicht Faulheit.

---

## Block 2: Die Hauptflows — wie alles zusammenhängt

**Kernfrage:** Was passiert wenn ich sage "Analysiere das Feedback und sag mir was wir bauen sollen"?

Der Flow:

```
Rohes Feedback → /feedback-synthesizer → Cluster
                                            ↓
                              /opportunity-scorer → Scorecard
                                            ↓
                               /decision-brief → BUILD / SKIP / MEHR DATEN
                                            ↓
                              /devils-advocate → Gegenargumente
                                            ↓
                                /spec-writer → Spec (Was, nicht Wie)
                                            ↓
                              /option-stormer → 3 Prototypen + Vergleich
                                            ↓
                                /eval-runner → PASS / FAIL / UNKLAR
                                            ↓
                           /handoff-packager → Alles gebündelt für Dev
```

**Didaktischer Move:** Geh den Flow einmal durch. Nicht abstrakt — am NeoEmployee-Beispiel. "Onboarding-Agent" als roter Faden. Die Leute kennen den Case aus den letzten Wochen.

**Neue Skills diese Woche die den Flow vervollständigen:**

- **option-stormer** — Das ist der Willison-Move. Drei Prototypen bauen statt einen. Weil es fast nichts kostet. "Ich baue nicht eine Lösung und hoffe. Ich baue drei, schau sie an, und entscheide welche lebt." Strukturell verschieden, nicht kosmetisch.

- **handoff-packager** — Die Brücke zum Dev. Kein Copy-Paste. Cover-Sheet mit Links zu Spec, Eval, Prototyp. Konkrete nächste Schritte. PM-Eval vs. Dev-Eval explizit getrennt.

- **system-auditor** — Der Gesundheitscheck. Ampelsystem: was ist ausgefüllt, was fehlt, was als nächstes. "Führe /system-auditor aus" ist der erste Befehl nach dem Klonen.

**Highlight für den Call:** Der Flow ist kein starrer Wasserfall. Du kannst an jedem Punkt einsteigen. Du hast schon eine Hypothese? Spring direkt zum decision-brief. Du hast schon eine Spec? Direkt zum option-stormer. Das System zwingt dich nicht in eine Reihenfolge — aber es gibt dir eine wenn du eine brauchst.

---

## Block 3: Teamwork — Zimmer und Wohnzimmer

**Kernfrage:** Was passiert wenn 2 PMs mit demselben System arbeiten?

Die Metapher: **Dein Zimmer und das Wohnzimmer.**

**Dein Zimmer** = dein lokaler output/-Ordner. Hier denkst du nach. Hier probierst du aus. Hier scheitert keiner. Drei Prototyp-Varianten, ein halbfertiger Decision Brief, ein wilder Devil's Advocate — alles privat. Dein Denkraum. Dein Tempo.

**Das Wohnzimmer** = das Git-Repo. CLAUDE.md, context/, skills/. Was hier liegt, gilt für alle. Skills sind Code. Context ist Truth. Änderungen laufen über PRs.

**Der Übergang wird bewacht.** Aus dem Zimmer ins Wohnzimmer geht nichts automatisch. Du entscheidest wann du teilst. Synchron im Weekly. Asynchron über Slack oder PR. Aber bewusst. Immer bewusst.

**Die drei Schichten:**

1. **Geteilte Infrastruktur (Git)** — Skills, Context, CLAUDE.md. Familienregeln. PR und Review.

2. **Geteilte Quellen (APIs/MCPs)** — Slack, Granola, Jira. Alle sehen denselben Kanal. Aber jeder extrahiert was er braucht. Geteilte Quelle, persönliche Verarbeitung.

3. **Persönlicher Workspace (Lokal)** — Dein Output. Deine Drafts. Deine Experimente. Privat bis du bereit bist.

**Didaktischer Move:** Das Anna-und-Ben-Beispiel aus dem Teamwork-Doc erzählen. Anna macht Discovery, Ben übernimmt bei Spec. Anna teilt im Weekly. Ben baut weiter. Am Ende fließen Learnings ins Repo zurück. Das macht es greifbar.

**Wichtiger Punkt für die Diskussion:** Learnings zurückschreiben. Das System wird besser durch Benutzung — aber NUR wenn Learnings auch eingetragen werden. context/learnings.md ist das Gedächtnis. Wenn da nichts reinkommt, lernt das System nichts.

---

## Block 4: Was die Teilnehmer diese Woche tun sollen

Klar machen: Das System klonen reicht nicht. Es muss befüllt werden.

**Schritt 1:** context/ ausfüllen. Alle 7 Files. Eigenes Unternehmen, eigene Strategie, eigenes Team. Die NeoEmployee-Beispiele sind Orientierung — aber sie müssen raus und durch eigenen Kontext ersetzt werden. Ziel: unter 30 Minuten.

**Schritt 2:** /system-auditor ausführen. Der zeigt was fehlt und was als nächstes kommt.

**Schritt 3:** Einen Flow durchspielen. Von vorne bis hinten. Mit eigenem Kontext, eigenen Daten. Nicht NeoEmployee — das eigene Ding.

**Schritt 4 (optional, für Fortgeschrittene):** Einen Skill anpassen oder einen neuen bauen. Der scripts/-Ordner ist die Sandbox dafür.

---

## Block 5: Kurse im System — Selbstlern-Material

Das System hat drei eingebaute Kurse als HTML-Präsentationen:

- **/kurs** → PM-System-Übersicht. Das System verstehen.
- **/zeig_mir_teamwork** → Teamwork-Prinzipien. Zimmer/Wohnzimmer.
- **/mini_git_kurs** → Git-Grundlagen. Branches, PRs, warum das wichtig ist.

Die Teilnehmer können die jederzeit selbst durchgehen. Die Kurse sind im System, nicht extern. Das heißt: Claude erklärt das System — im System.

---

## Mögliche Fragen vorbereiten

**"Muss ich Git können?"**
Für alleine arbeiten: nein. Für Teamwork: ja, die Basics. Dafür gibt's den /mini_git_kurs. Branches, PRs, Merge — mehr brauchst du erstmal nicht.

**"Was wenn mein Context sich ändert?"**
Dann änderst du die Context-Files. Das ist der Punkt. strategy.md ist kein Tattoo. Wenn sich die Strategie ändert, ändert sich das File. Und ab dem nächsten Skill-Aufruf arbeitet das System mit dem neuen Kontext.

**"Kann ich eigene Skills bauen?"**
Ja. scripts/-Ordner nutzen zum Experimentieren. Wenn der Skill funktioniert: SKILL.md schreiben, in .claude/skills/ packen, fertig.

**"Was ist der Unterschied zu den einzelnen Skills aus den letzten Wochen?"**
Kontext. Die Skills aus Woche 3 und 4 waren standalone. Die haben funktioniert, aber sie wussten nichts voneinander. Jetzt lesen sie alle dasselbe Kontext-Fundament. Das macht den Unterschied zwischen Werkzeugkasten und System.

---

## Closing

Das System ist ein Starter-Kit. Nicht das Endprodukt. Es wird besser je mehr die Teilnehmer damit arbeiten, eigenen Kontext reinfüllen, Skills anpassen, Learnings zurückschreiben.

Der Kern: **Ein PM braucht kein perfektes System. Ein PM braucht ein System das mit ihm wächst.**

Diese Woche ist der Punkt wo das passiert.
