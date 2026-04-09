# Devils Advocate: Onboarding-Automatisierung

**Datum:** 2026-04-09

## Annahmen im Decision Brief

### Annahme 1: Onboarding-Schmerz ist ein Produkt-Problem, nicht ein Delivery-Problem

**Was der Brief annimmt:** Weil Kunden über schlechtes Onboarding klagen, ist ein technisches Onboarding-Modul die richtige Antwort.

**Gegenargument:** Onboarding ist möglicherweise schlecht weil die Agents selbst zu komplex sind, nicht weil ein Einweisungs-Flow fehlt. Ein besseres Produkt braucht weniger Onboarding — nicht mehr davon. Das Symptom (Kunden fragen nach) und die Ursache (zu komplexe Bedienung) werden im Brief gleichgesetzt ohne das zu prüfen.

**Evidenz dagegen:** Peter Hartmann: "Die Dokumentation war okay, aber zu allgemein. Wir haben Logistik-spezifische Felder, Abkürzungen, interne Prozesse." Das klingt nach einem zu wenig kontextualisierten Agent, nicht nach fehlendem Onboarding-Flow. Sandra Pfeiffer: "Wenn es nicht in 15 Minuten klar ist wie es geht, nutzen sie es nicht." — Das könnte ebenso für Vereinfachung des Agents sprechen wie für ein Onboarding-Modul.

---

### Annahme 2: "Branchenübergreifend" bedeutet "einheitlich lösbar"

**Was der Brief annimmt:** Weil Onboarding-Schmerz bei Logistik, Pharma, Finance und Bau auftaucht, kann eine einheitliche Lösung gebaut werden.

**Gegenargument:** Die Inhalte des Onboardings sind pro Branche und pro Agent komplett verschieden. Was LogiTrans einweisen muss (Logistik-Abkürzungen, CO2-Felder) hat nichts mit PharmaCare (FDA/EMA-Terminologie) oder FinancePlus (MiFID II) gemeinsam. Was skaliert ist bestenfalls ein Framework — aber das Framework schreibt noch keine einzige Einweisungszeile.

**Evidenz dagegen:** Marc Hoffmann intern: "Der Engpass ist nicht die Technik sondern der Content — wer schreibt die Einweisungstexte?" Der Brief listet das als offene Frage, behandelt es aber nicht als Blocker. Es ist der Blocker.

---

### Annahme 3: 2 Engineering-Wochen reichen für ein MVP das echten Wert liefert

**Was der Brief annimmt:** Kai Schmidts Schätzung von 2 Wochen ist eine belastbare Grundlage für die Entscheidung.

**Gegenargument:** 2 Wochen ist eine informelle Einschätzung aus einem E-Mail-Thread, kein durchdachtes Scoping. Lisa und Tom arbeiten neben Kundenprojekten — `context/team.md` ist explizit: "Kapazität für Produktarbeit: nur was Lisa und Tom neben Kundenprojekten schaffen." Das Pattern-Team ist laut Julia Meyer bereits unterbesetzt: "Wir zwei reichen nicht. Wir bräuchten mindestens eine dritte Person." Ein 2-Wochen-MVP unter diesen Bedingungen ist eher 6-8 Wochen in der Realität.

**Evidenz dagegen:** `context/strategy.md`: "Revenue ist Runway — jedes Engagement muss positiven Cashflow generieren." Ein internes Experiment das die Kapazität des Pattern-Teams für 6-8 Wochen bindet, ohne direkten Umsatz zu generieren, steht im direkten Widerspruch zu diesem Constraint.

---

### Annahme 4: Onboarding ist wichtiger als Compliance weil es skalierbarer ist

**Was der Brief annimmt:** Der Multiplikator-Effekt (alle zukünftigen Projekte werden günstiger) rechtfertigt BUILD gegenüber Compliance-Checking, für das PharmaCare jetzt zahlen würde.

**Gegenargument:** "Günstiger in der Zukunft" ist hypothetisch. "PharmaCare zahlt jetzt" ist konkret. `context/strategy.md`: "Bootstrapped. Kein Investor, keine Bankkredite. Revenue ist Runway." Der Brief priorisiert strategischen Langzeitwert über akuten Cashflow — das ist eine Entscheidung, die in einem bootstrapped Unternehmen existenzielle Konsequenzen haben kann, wenn die Kundenprojekte nicht ausreichend Puffer bieten.

**Evidenz dagegen:** `context/strategy.md`: "Horizon 1 (jetzt): Custom AI Agent Beratung auf T&M-Basis — Umsatz generieren." Onboarding-Automatisierung generiert in Horizon 1 keinen direkten Umsatz. PharmaCare tut es.

---

### Annahme 5: Kunden würden ein eingebautes Onboarding-Modul tatsächlich nutzen

**Was der Brief annimmt:** Weil Kunden über manuelles Onboarding klagen, würden sie ein automatisches Modul akzeptieren und adoptieren.

**Gegenargument:** Kunden haben unterschiedliche Lernkulturen und IT-Governance. Ein interaktiver Onboarding-Flow könnte bei PharmaCare (reguliertes Unternehmen, IT-Abteilung involviert) auf Compliance-Bedenken stoßen — darf ein externer Agent Mitarbeiter einweisen? Bei FinancePlus (MiFID II) könnten ähnliche Fragen entstehen.

**Evidenz dagegen:** Keine direkte Evidenz im Datensatz — aber auch keine Bestätigung dass Kunden ein automatisches Modul akzeptieren würden. Die Klage bezog sich auf den manuellen Aufwand, nicht auf die Frage wer oder was das Onboarding übernehmen soll.

---

## Verdikt

**PAUSE**

Der Decision Brief hat recht, dass Onboarding das stärkste branchenübergreifende Muster ist. Aber er übersieht den zentralen Widerspruch: Das Content-Problem (wer schreibt die Einweisungstexte?) ist nicht gelöst und macht ein technisches Modul allein wertlos. Gleichzeitig bindet BUILD die einzige verfügbare Produktkapazität (Lisa + Tom) in einem Unternehmen das von Cashflow lebt — während PharmaCare konkret für Compliance zahlen würde. Vor einem BUILD-Commitment müssen zwei Fragen beantwortet sein: Wie wird der Content skaliert? Und: Kann das Pattern-Team beides parallel leisten ohne den PharmaCare-Deal zu gefährden?

---

## Offene Fragen die zuerst beantwortet werden müssen

- **Content-Ownership:** Wer schreibt die branchenspezifischen Einweisungstexte — NeoEmployee, der Kunde, oder ein LLM-generierter Draft? Ohne konkrete Antwort ist das Modul ein leeres Framework.
- **Kapazitätskollision:** Kann das Pattern-Team (Lisa + Tom) Onboarding-MVP und PharmaCare-Compliance-Projekt parallel liefern — oder muss explizit priorisiert werden?
- **Ursachenklärung:** Ist das Onboarding-Problem ein Content-Problem (zu komplex erklärt), ein UX-Problem (zu unintuitiv gebaut), oder ein Produkt-Problem (zu viele Konfigurationsoptionen)? Die Antwort bestimmt die Lösung.
- **Zahlungsbereitschaft validieren:** Peter Hartmann sagt er zahlt extra — hat NeoEmployee das je versucht zu bepreisen? Bis dieser Satz in einem signierten Angebot steht, ist er Feedback, kein Umsatz.
