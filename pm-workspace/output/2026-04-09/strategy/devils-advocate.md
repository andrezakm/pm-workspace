# Devils Advocate: Onboarding-Automatisierung

**Datum:** 2026-04-09

## Annahmen im Decision Brief

### Annahme 1: Onboarding-Schmerz ist ein Produkt-Problem, nicht ein Delivery-Problem

**Was der Brief annimmt:** Ein technisches Onboarding-Modul löst das Problem weil Kunden über schlechtes Onboarding klagen.

**Gegenargument:** Möglicherweise sind die Agents selbst zu komplex. Ein besseres Produkt braucht weniger Onboarding — nicht mehr davon.

**Evidenz dagegen:** Peter Hartmann: "Die Dokumentation war okay, aber zu allgemein. Wir haben Logistik-spezifische Felder, Abkürzungen, interne Prozesse." Das beschreibt einen zu wenig kontextualisierten Agent — nicht ein fehlendes Einweisungs-Framework. Sandra Pfeiffer hat die 15-Minuten-Hürde als Kaufbedingung genannt — das könnte ebenso für Vereinfachung der Bedienung sprechen.

---

### Annahme 2: Branchenübergreifend bedeutet einheitlich lösbar

**Was der Brief annimmt:** Weil der Schmerz bei Logistik, Pharma, Finance und Bau auftaucht, kann eine einheitliche Lösung gebaut werden.

**Gegenargument:** Die Inhalte des Onboardings sind pro Branche und Agent komplett verschieden. Was skaliert ist bestenfalls ein leeres Framework.

**Evidenz dagegen:** Marc Hoffmann: "Der Engpass ist nicht die Technik sondern der Content — wer schreibt die Einweisungstexte?" Der Brief listet das als offene Frage — es ist der Blocker. Ein Framework ohne Content ist kein Produkt.

---

### Annahme 3: 2 Engineering-Wochen sind eine belastbare Schätzung

**Was der Brief annimmt:** Kais informelle Schätzung aus einem E-Mail-Thread ist Planungsgrundlage.

**Gegenargument:** Lisa und Tom arbeiten neben Kundenprojekten. Julia Meyer: "Wir zwei reichen nicht." 2 Wochen ist unter diesen Bedingungen eher 6–8 Wochen real.

**Evidenz dagegen:** `context/strategy.md`: "Revenue ist Runway." Ein 6–8-wöchiges internes Experiment ohne direkten Cashflow steht im Widerspruch zu diesem Constraint — besonders wenn PharmaCare gleichzeitig auf ein bezahltes Angebot wartet.

---

### Annahme 4: Strategischer Langzeitwert schlägt kurzfristigen Cashflow

**Was der Brief annimmt:** Der Multiplier-Effekt rechtfertigt BUILD gegenüber Compliance.

**Gegenargument:** "Günstiger in Zukunft" ist hypothetisch. "PharmaCare zahlt jetzt" ist konkret. In einem bootstrapped Unternehmen ist das keine akademische Abwägung.

**Evidenz dagegen:** `context/strategy.md`: "Horizon 1: Custom AI Agent Beratung auf T&M-Basis — Umsatz generieren." Onboarding generiert in Horizon 1 keinen Umsatz. Der Brief priorisiert Horizon-2-Wert über Horizon-1-Cashflow ohne diesen Trade-off explizit zu benennen.

---

### Annahme 5: Kunden würden ein automatisches Onboarding-Modul akzeptieren

**Was der Brief annimmt:** Weil Kunden über manuelles Onboarding klagen, adoptieren sie ein automatisches Modul.

**Gegenargument:** Bei regulierten Kunden (PharmaCare, FinancePlus) könnte ein externes Modul das Mitarbeiter einweist auf IT-Governance- oder Compliance-Bedenken stoßen.

**Evidenz dagegen:** Keine direkte Evidenz im Datensatz. Die Klagen bezogen sich auf manuellen Aufwand — nicht auf die Frage wer oder was das Onboarding übernehmen soll.

---

## Verdikt

**PAUSE**

Onboarding ist das stärkste branchenübergreifende Muster. Aber BUILD ist verfrüht: Das Content-Problem ist ungelöst und macht ein technisches Modul allein wertlos. Die Kapazitätsschätzung ist nicht belastbar. Und PharmaCare zahlt jetzt für Compliance, während Onboarding keinen direkten Cashflow generiert. Vor einem Commitment müssen beantwortet sein: Wer schreibt den Content? Und kann das Pattern-Team beides parallel liefern?

---

## Offene Fragen die zuerst beantwortet werden müssen

- **Content-Ownership:** Wer schreibt die branchenspezifischen Einweisungstexte — NeoEmployee, Kunde, oder LLM-Draft?
- **Kapazitätskollision:** Onboarding-MVP vs. PharmaCare-Compliance — muss explizit priorisiert werden.
- **Ursachenklärung:** Ist das Problem Content, UX, oder zu komplexes Produkt? Bestimmt die richtige Lösung.
- **Zahlungsbereitschaft validieren:** Peter Hartmanns Aussage ist Feedback, kein Angebot. Hat NeoEmployee je versucht es zu bepreisen?
