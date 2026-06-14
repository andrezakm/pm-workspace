# PTW-Workshop Skill
*Ein Facilitation-Werkzeug von überproduct*

---

> **Dieses Werkzeug erzeugt einen Ausgangspunkt für ein Gespräch, keine Schlussfolgerung. Sein Wert liegt darin, was es diskutierbar macht.**

---

## Was das ist

Ein Claude-Code-Skill, der aus rohen Organisationsdokumenten einen vollständigen Play-to-Win-(PTW)-Strategie-Workshop simuliert. Er erzeugt einen qualifizierten ersten PTW-Choice-Cascade-Entwurf — Winning Aspiration, Where to Play, How to Win, Capabilities, Management Systems — plus Spannungen, Mehrdeutigkeiten, reverse-engineerte Annahmen und Experiment-Designs, über sechs strukturierte Schritte mit verpflichtenden menschlichen Checkpoints.

Aufruf mit `/PTW-workshop`.

---

## Woher die Dokumente kommen (drei Quellen)

Der Workshop kann aus drei Quellen gespeist werden — einzeln oder kombiniert:

- **(A) `context/`** — das Kontext-Fundament des Workspace (company, strategy, product, team, metrics, roadmap, learnings). Standard, um die *eigene* Strategie zu schärfen. Entspricht der System-Regel „Ohne Kontext kein Output".
- **(B) Eigene Dokumente** — Strategiepapiere, Pitch-Decks, Board-Updates etc. direkt in den Chat einfügen oder in `input/ptw-workshop/` ablegen.
- **(C) Öffentliche Recherche** — eine Firma nennen; der Skill recherchiert per WebSearch öffentlich bekannte Muster (Geschäftsmodell, Positionierung, Märkte, Wettbewerber) und destilliert daraus eine Dokumentenbasis. Macht jede Organisation zu einem Case — auch ohne interne Unterlagen.

---

## Wofür es gut ist

**Facilitator-Vorbereitung.** Führe den Workshop vor dem Workshop. Komm an und weißt schon, wo die Cascade bricht, welche Entscheidungen umstritten sind, welche Personas worüber aneinandergeraten. Nutze den Entwurf als Probe, nicht als Ergebnis.

**Framework-Demonstration.** Zu zeigen, was PTW produziert, überzeugt mehr als zu erklären, was PTW ist. Eine aus echten Dokumenten gebaute Choice Cascade ist eine bessere Einführung als ein Foliensatz.

**Executive Dry Run.** Lass Führungskräfte die Form eines PTW-Workshops sehen, bevor sie in einem sitzen. Sie kommen mit kalibrierten Erwartungen an.

**Teaching und Case-Work.** Über Quelle (C) lässt sich der Skill mit öffentlicher Recherche füttern, wenn keine Kundendokumente existieren — jede Organisation wird zum tragfähigen Fallbeispiel.

---

## Wofür es nicht gut ist

**„Das ist deine Strategie."** In dem Moment, in dem jemand den KI-Output als Antwort statt als Ausgangspunkt behandelt, hat das Framework seinen Zweck verfehlt. Die Gespräche *sind* die Strategiearbeit. Der Entwurf ist nur gut genug, um diese Gespräche schärfer zu machen.

Der Skill kann keinen echten Workshop mit echten Menschen ersetzen. Er sieht keine interne Kultur, keine informelle Macht, keine gelebte organisationale Erfahrung — nichts von dem, was Menschen wissen, aber nicht aufschreiben. Er arbeitet aus Dokumenten und produziert einen Entwurf, der kohärent genug ist, um nützlich zu sein, und unvollständig genug, um ehrlich zu sein.

---

## Wie es funktioniert

Der Skill läuft in sechs Schritten, jeder baut auf dem vorigen auf, mit User-Checkpoints durchgehend:

**Schritt 1 — Individuelle Analyse („1" in 1-2-4-All)**
Fünf Personas (CEO, CFO, Head of Product, Tech Lead, Employee Rep) analysieren die Quell-Dokumente unabhängig durch ihre spezifische Linse. Fünf parallele Agenten, fünf Output-Dateien.

**Schritt 2 — Paar-Diskussionen („2/3" in 1-2-4-All)**
Personas diskutieren in Paaren oder kleinen Gruppen, um Gemeinsamkeiten zu finden und Spannungen sichtbar zu machen. Drei Paarungs-Modi:
- *Affinität* (Default): Natürliche Linsen-Gruppen — CEO+CFO (strategisch), Product+Tech (Delivery)
- *Divers*: Cross-Linsen-Paarungen — CFO+Employee Rep, CEO+Tech Lead. Am besten, um Spannungen früh sichtbar zu machen.
- *Zufall*: Reine Auslosung. Bringt manchmal die unerwartetsten Konvergenzen.

**Schritt 3 — Gruppen-Synthese („All" in 1-2-4-All)**
Alle individuellen und Paar-Analysen werden zu einem ersten PTW-Entwurf (v0.1) verdichtet. Der User prüft und korrigiert, bevor es weitergeht.

**Schritt 4 — Remember the Future**
Jede Persona stellt sich vor, die Organisation hat in drei Jahren wirklich Erfolg gehabt, und arbeitet rückwärts. Das cross-validiert den Entwurf und löst oft Fragen, die die Vorwärts-Analyse offen lässt. Der generativste Schritt — er bringt Commitment-Fragen zutage, die Dokumente nicht beantworten können.

**Schritt 5 — Reverse Engineering**
Auf Basis aller bisherigen Outputs fragt ein Synthese-Agent: „Was müsste wahr sein, damit diese Strategie erfolgreich ist?" Er erzeugt die vollständige Menge an Annahmen, auf denen die Cascade ruht, und bewertet jede auf zwei Dimensionen:
- *Importance* (0–20): Wie abhängig ist die Strategie davon, dass diese Annahme wahr ist? (20 = existenziell kritisch)
- *Knowledge* (0–20): Wie viel Daten/Evidenz haben wir aktuell, dass dies wahr ist? (0 = keine Daten, 20 = starke Evidenz)

Nur Annahmen mit Importance > 10 qualifizieren. Aus der qualifizierenden Menge werden je Quadrant die Top 5 dokumentiert:
- **Quadrant A — Wichtig & Bekannt**: Aussagen, die im Angebot behauptet werden müssen
- **Quadrant B — Wichtig & Unbekannt**: Aussagen, die Experimente vor der Festlegung erfordern

**Schritt 5a — Experiment-Design**
Für jede der Top-5-Quadrant-B-Aussagen entwirft das Modell erste Experiment-Varianten: Hypothese, 2–3 Test-Optionen, minimal viabler Test sowie Erfolgs-/Falsifikationskriterien. Keine weitere Teilnehmer-Runde — das Modell macht dies direkt.

**Schritt 6 — Finale Synthese**
Alle Workshop-Outputs, User-Korrekturen und Zukunftsvisionen werden zum finalen qualifizierten PTW-Entwurf verdichtet.

---

## Output-Struktur

Der finale Report (`6_final/PTW-draft-final.md`) ist strukturiert als:

| Abschnitt | Zweck |
|---|---|
| **TL;DR** | 3–5 Sätze: was will diese Organisation gewinnen, wo entscheidet sie sich zu spielen, wie wird sie dort gewinnen. Für jemanden, der sonst nichts liest. |
| **Winning Aspiration** | Der Zweck / die Definition von Gewinnen. Wie sieht Erfolg aus und für wen. |
| **Where to Play** | Das gewählte Spielfeld — Geografie, Kundensegmente, Kanäle, Produktkategorien, vertikale Stufen. Die nicht getroffenen Entscheidungen zählen so viel wie die getroffenen. |
| **How to Win** | Die einzigartige Art, im gewählten Feld zu gewinnen — Wertversprechen + Wettbewerbsvorteil. Die Brücke zwischen Where to Play und Capabilities. |
| **Capabilities** | Das sich verstärkende Set an Aktivitäten, das in Kombination den How-to-Win liefert. Keine Wunschliste — ein kohärentes System. |
| **Management Systems** | Die Strukturen, Messgrößen und Normen, die die Capabilities aufbauen, erhalten und ermöglichen. |
| **Spannungen** | Legitime strategische Spannungen über die Cascade — bewusst halten, nicht wegauflösen. |
| **Mehrdeutigkeiten** | Wo Quell-Dokumente unklar, widersprüchlich oder stumm waren. |
| **Offene Fragen** | Entscheidungen, die die Organisation noch explizit treffen muss. |
| **Reverse Engineering** | Zwei explizite Quadranten: (A) Wichtig & Bekannt — im Angebot zu verankernde Behauptungen. (B) Wichtig & Unbekannt — die kritischen Wetten, die vor der Festlegung getestet werden müssen. Top 5 je Quadrant. |
| **Experimente** | Für jede Quadrant-B-Aussage: Hypothese, Test-Varianten, minimal viabler Test, Erfolgs- und Falsifikationskriterien. |
| **Facilitator-Notizen** | Qualität und Vollständigkeit des Entwurfs. Wichtigster nächster Schritt. |
| **Workshop-Befunde** | Was der Prozess spezifisch zutage brachte, das Dokumente allein nicht konnten — was sich änderte, was überraschte, was der Workshop nicht sehen konnte. |

Alle Zwischendateien landen unter `output/YYYY-MM-DD/strategy/ptw-{slug}/` in den Unterordnern `1_individual`, `2_pairs`, `3_synthesis`, `4_future`, `5_reverse`, `5a_experiments`, `6_final` (plus `0_research` bei Quelle C).

---

## Zum Framework

PTW (Play to Win), entwickelt von A.G. Lafley und Roger Martin bei Procter & Gamble, definiert Strategie als **einen integrierten Satz von Entscheidungen, der ein Unternehmen einzigartig positioniert, um nachhaltigen Vorteil und überlegenen Wert relativ zum Wettbewerb zu schaffen.** Sie wird über eine Fünf-Fragen-Choice-Cascade artikuliert:

1. **Was ist unsere Winning Aspiration?** — Der Zweck des Unternehmens, seine motivierende Definition von Gewinnen.
2. **Where will we play?** — Das Spielfeld, auf dem das Unternehmen konkurriert. Wir sind paranoid darauf, dass es eng definiert ist. Wir streben große Marktsegmente an. Das heißt nicht, dass wir die Welt beherrschen wollen. Es heißt, dass wir ein Where to Play so exakt, eng und präzise definieren können, dass wir dieses Feld tatsächlich dominieren.
3. **How will we win?** — Die gewählte Art, in diesem Feld zu gewinnen.
4. **Welche Capabilities müssen vorhanden sein?** — Das Set und die Konfiguration der Capabilities, die nötig sind, um auf die gewählte Art zu gewinnen.
5. **Welche Management Systems sind nötig?** — Die Systeme und Messgrößen, die die Capabilities ermöglichen und die Entscheidungen stützen.

Die fünf Entscheidungen verstärken sich abwärts (Aspiration formt Where, Where formt How, usw.) und validieren sich aufwärts (eine Capability ist nur real, wenn ein Management System sie trägt). Eine PTW-Strategie wird nicht danach beurteilt, ob die Entscheidungen isoliert gut klingen, sondern ob die Cascade **kohärent, sich gegenseitig verstärkend und gegen reverse-engineerte Bedingungen getestet** ist.

Eine ergänzende Disziplin — **Reverse Engineering** — fragt: Was müsste angesichts dieser Entscheidungen über die Welt (Kunden, Wettbewerber, Kanäle, Organisation, Ökonomie) wahr sein, damit sie die gewinnenden Entscheidungen sind? Das verwandelt Strategie von Advocacy („hier ist, warum wir recht haben") in testbare Hypothese („hier ist, was wir wetten, dass es wahr sein muss"). Die Bedingungen, die am unwahrscheinlichsten wahr sind, werden zu den höchst-hebelnden Testbereichen vor der Festlegung.

Der schwerste Teil jedes PTW-Workshops — live oder simuliert — ist es, der Anziehungskraft generischer Antworten zu widerstehen. Menschen formulieren von Natur aus Aspirationen, die für jedes Unternehmen gut klingen, definieren Spielfelder, die zu breit für echte Entscheidung sind, und beschreiben How-to-Win so, dass kein Wettbewerber widersprechen würde. Das Framework ist keine Doktrin, die man durchsetzt; es ist eine Disziplin, um **echte Entscheidung** zu erzwingen, bei der eine Sache zu wählen heißt, sichtbar eine andere nicht zu wählen.

Eine Entscheidung ist wahrscheinlich echt, wenn du benennen kannst, was die Organisation *nicht* zu tun wählt und was es kosten würde, falsch zu liegen. Eine strategische Behauptung ohne sichtbares „Nicht" ist es wert, hinterfragt zu werden.

---

## Unterstützende Dateien

- `SKILL.md` — vollständige Workshop-Orchestrierung und Schritt-für-Schritt-Anweisungen
- `framework.md` — vollständige PTW-Framework-Referenz (von Subagenten bei Bedarf geladen)
- `personas.md` — fünf Persona-Definitionen mit Linsen, blinden Flecken und Tendenzen
