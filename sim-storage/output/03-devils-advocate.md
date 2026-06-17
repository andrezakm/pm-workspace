# Devils Advocate: Neue Speichervariante

## Annahmen im Decision Brief

### Annahme 1: Bewährte Aufwandsschätzung ist direkt übertragbar
**Was der Brief annimmt:** V2 brauchte 7 Monate, INV-Gen3 brauchte parallel Zertifizierung → 6–8 Monate für neue Batterie ist kalkulierbar, weil die Architektur stabil ist.

**Gegenargument:** V2 war eine Firmware-Neuimplementierung einer BMS-Integration mit *bekanntem* Protokoll (LG Chem oder Huawei). INV-Gen3 war Hardware-Refresh ohne neue BMS. Diese neue Batterie ist noch nicht definiert — Name, Hersteller, BMS-Spezifikation liegen nicht vor. Du vergleichst eine Aufwandsschätzung für „Bekanntes neu integrieren" mit „Unbekanntes zum ersten Mal integrieren". Das sind zwei verschiedene Risiko-Kurven. V2 hatte +2M Verzug wegen BMS-Überraschungen *nach* Go. Wenn dich BMS-Tests blockieren, bevor du Start drückst, ist die 6–8-Monats-Schätzung ein Wunsch, kein Plan.

**Was das für die Entscheidung bedeutet:** Die Aufwandsschätzung ist nicht „konservativ mit Gates", sondern spekulativ. Ein explizites Gate („Hardware-in-the-Loop muss bestanden sein vor Kickoff") bedeutet: Dein echtes Startdatum ist unbekannt. Das könnte Q4 sein, nicht Q3. Der Brief sagt „MEHR DATEN vor BUILD", sagt aber nicht „und der Aufwand ändert sich vielleicht noch".

---

### Annahme 2: „MEHR DATEN" ist der richtige nächste Schritt, nicht eine Ausrede für „Nein"
**Was der Brief annimmt:** Wenn Markt-Pull, Wettbewerber-Analyse und Batterie-Lieferant fixiert sind, dann → BUILD. Das ist eindeutig.

**Gegenargument:** Was wenn „MEHR DATEN" das Projekt in eine Zwickmühle führt? Z.B.:
- Daten zeigen: Konkurrenten haben die gleiche Batterie schon im Portfolio (Huawei, Sungrow). Dann ist „neue Variante" kein Differentiator, sondern Follower-Move. BUILD ist jetzt soziopolitisch schwächer.
- Installateure-Anfragen zeigen: Der Druck ist nicht „alternative Speichervariante", sondern „günstiger Preis". Eine neue Batterie löst das nicht.
- Lieferant-Eval zeigt: Nur ein Hersteller ist Grid-Code-ready in den nächsten 6 Monaten, aber die Chemie ist marginal anders. Aufwand bleibt gleich, Differentiator ist marginal.

In allen drei Fällen hat „MEHR DATEN" nicht die Entscheidung geklärt, sondern neue Unklarheiten aufgelöst. Das ist nicht „klügere Entscheidung", das ist „Entscheidung verschoben, bis die nächste Blockade auftaucht".

**Was das für die Entscheidung bedeutet:** Der Brief formuliert die Daten-Sammlung als *Bedingungen* für GO, nicht als *Szenarios für KILL*. Wenn die Aufgabe „sammle Daten, bevor du Ja sagst" ist, dann ist das implizit „lass mich nicht Nein sagen, solange noch Hoffnung existiert". Das ist eine Risiko-Verschiebung in die operative Phase.

---

### Annahme 3: Architektur-Team bleibt tragbar parallel zu INV-Gen3-Rollout
**Was der Brief annimmt:** 2-köpfiges Architektur-Team ist der Engpass. Das ist bekannt. Ein explizites „Gate" (z.B. "Architektur-Kapazität für neue Integration + INV-Gen3-Wartung muss aktualisiert werden") schützt das Projekt vor parallelem Kollaps.

**Gegenargument:** Ein Gate ist ein Check-In, nicht ein Shield. Die Realität ist: INV-Gen3-Rollout DE/AT läuft *jetzt* (Zertifizierung kann noch verzögern). Grid-Code-Zertifizierung ist nicht beschleunigbar. Wenn diese jetzt +3 Wochen verzögert (nicht unwahrscheinlich), dann haben die 2 Architekten in Q3 KEINE Kapazität für neue Batterie-Integration. Dann musst du entweder:
- Neues Projekt schieben (OK, aber dann war die DATEN-Sammlung verschwendet).
- Hiring für Architekten (6 Wochen Ramp-up, nicht mitgerechnet in 6–8 Monaten).
- Architektur-Arbeit auf Dev-Teams verteilen (Handschrift-Verlust, BMS-Integration wird Wildwuchs).

Das Gate sagt nicht „dieser Fall wird nicht eintreten", es sagt „wir prüfen das später". Das ist Hoffnung, nicht Plan.

**Was das für die Entscheidung bedeutet:** Du hängst dieses Projekt an die *Annahme* auf, dass INV-Gen3-Zertifizierung nicht verzögert und Firmware-Team während Storage-Platform-Gründung stabil bleibt. Beides ist volatil. Die richtige Frage ist nicht „Explizites Gate einbauen?", sondern „Wollen wir diesen Volatilitäts-Batch jetzt nehmen, oder warten wir bis INV-Gen3 DE/AT stabil läuft (= Q4)?"

---

### Annahme 4: BMS-Protokoll-Tests verringern Risiko, wenn sie früh laufen
**Was der Brief annimmt:** V2 hatte +2M Verzug durch BMS-Überraschungen. Learning: Hardware-in-the-Loop früher (parallel zu walking skeleton). Das wird diese Integration sicherer machen.

**Gegenargument:** Das Learning ist, dass Tests früher laufen *müssen*. Das ist nicht ein „wir haben das jetzt im Griff", das ist „diese Test-Phase blockiert Kickoff, bis der Lieferant die Hardware gibt". Das heißt:
- Lieferant-Sample muss verfügbar sein (+ 8 Wochen nach Bestellung typisch).
- Hardware-in-the-Loop braucht eine Test-Rig (bereits überlastet per Debatte: "Feldtest-Kapazität ist ein bottleneck").
- Wenn Test-Rig Probleme findet: +4–6 Wochen Design-Iteration mit Lieferant.

Die V2-Learning ist nicht „diesen Fehler bauen wir jetzt früher", die Learning ist „dieser Fehler ist unvermeidbar, weil BMS-Hersteller ihre Spezifikation oft erst in Hardware-Tests klären". Du verschiebst das Risiko-Fenster nach vorne, aber das Risiko bleibt gleich oder wird größer (weil du am meisten Zeit brauchst).

**Was das für die Entscheidung bedeutet:** Die 6–8-Monats-Schätzung setzt voraus, dass BMS-Hardware schnell verfügbar ist und Tests bestanden werden. Beides ist Spekulation. Realistisch: +10–12 Wochen für Lieferant-Sample + Test, bevor echte Firmware-Integration beginnt. Das ist ein anderes Projekt.

---

### Annahme 5: Feldtest-Kapazität wird verfügbar, weil „sie ist unverzichtbar"
**Was der Brief annimmt:** V2-Learning: Frühe Feldtests mit 5 Geräten fangen ~80% der Bugs. Diese Kapazität ist kritisch. Der Brief flaggt das als offene Frage: „Ist diese verfügbar oder auch im Engpass?"

**Gegenargument:** Das ist keine „offene Frage", das ist ein bekanntes Nein. Heute:
- Test & Certification (3) sind überlastet mit INV-Gen3-Grid-Code-Zertifizierung (parallel laufend, 6W+ noch zu gehen).
- Feldtest-Standorte (Kunden mit 5–10 Geräten, bereit Experimente zu tolerieren) sind knapp.
- OTA-Updates sind neu (Vorteil der Brief nennt), aber das bedeutet auch: Die Test-Last ist *höher*, nicht niedriger, weil du ohne Vor-Ort-Service debuggen musst.

Wenn du Q3 kickoffst, dann brauchst du im Oktober (Monat 4–5 der Integration) Feldtest-Standorte. Die sind jetzt nicht verfügbar, weil sie INV-Gen3-Rollout DE/AT supporten. Das heißt: Feldtest startet fünf Monate später oder gar nicht.

Wenn Feldtest wegfällt oder verzögert: +80% mehr Fehler, die erst bei Markt-Rollout auftauchen. Das ist nicht ein „hübsches Risiko-Profil mit Gates", das ist katastrophal.

**Was das für die Entscheidung bedeutet:** Der Brief nennt Feldtest-Kapazität als kritisch, schreibt dann aber „ist auch im Engpass?" das ist keine offene Frage, das ist eine verdrängte Antwort. Die realistische Entscheidung ist: Ohne Feldtest-Kapazität in Q3–Q4 ist dieses Projekt KILL, weil der Qualitäts-Hit zu groß ist.

---

### Annahme 6: Neues Storage Platform-Team bringt echte Kapazität, nicht ramp-up-Risiko
**Was der Brief annimmt:** Firmware-Team verliert 2–3 Personen zur Gründung eines neuen Storage-Platform-Teams. Dieses Team wird die neue Batterie-Integration bauen. Das ist effizient.

**Gegenargument:** Ein neues Team (Gründung läuft *jetzt*) braucht 2–4 Wochen, um gemeinsame Patterns, Konventionen, Escalation-Routen zu etablieren. Die 2–3 Personen sind nicht sofort produktiv auf neuer Task — sie bauen erst das Team. Das ist in der 6–8-Monats-Schätzung nicht mitgerechnet (oder verdrängt).

Realistisch:
- Wochen 1–4: Team Onboarding, codebase Exploration, Design Sprints.
- Wochen 5–8: Erste Integrations-Versuche, viele Fragen zurück an Architektur.
- Wochen 9+: Produktive Velocity.

Das ist nicht 6–8 Monate Entwicklung, das ist 6–8 Monate mit 4 Wochen Lost Productivity am Start. Unter Druck wird das schlimmer (junge Teams machen mehr Fehler unter Zeitdruck).

**Was das für die Entscheidung bedeutet:** Die Kapazität-Freigabe durch neues Team ist theoretisch, nicht praktisch. Praktisch brauchst du entweder 10–12 Monate für die neue Batterie *oder* du akzeptierst schlechtere Code-Qualität, weil ein unreifes Team unter Zeitdruck arbeitet.

---

### Annahme 7: Batterielieferant-Kontext ist „zu sammeln", aber nicht strategisch entscheidend
**Was der Brief annimmt:** Batterielieferant, BMS-Protokoll, Grid-Code-Auswirkungen sind nicht bekannt → müssen vor BUILD geklärt sein. Das ist Bedingung. Wenn bekannt → BUILD.

**Gegenargument:** Der Lieferant *ist* die Entscheidung. Es gibt in Europa ~3–5 Batterie-Hersteller, die Grid-Code-Ready sind in diesem Preissegment:
- LG Chem / Huawei (beide etabliert, bereits bei V2-Konkurrenten).
- BYD (aggressiv, aber Supply-Chain neu).
- Localstorage (startup, Grid-Code unklar, support-Risiko).

Wenn die Analyse zeigt: „LG oder Huawei", dann baue ich Batterie-Integration Nr. 3–4 (sie haben es schon gemacht, wenn auch bei Konkurrenten). Das ist low-risk, aber auch low-differentiation. Dann ist „neue Speichervariante" ein Follower-Move, und der Brief-Verdikt sollte „PASS" sein, nicht „BUILD".

Wenn die Analyse zeigt: „Nur BYD ist verfügbar", dann habe ich neues Supply-Chain-Risiko (Verfügbarkeit, Support, Zertifizierung) und die Aufwandsschätzung steigt um 4–6 Wochen (weil BYD-BMS-Protokoll nicht dokumentiert ist).

Das ist keine „Daten-Sammlung als Hygiene vor Entscheidung", das ist „Lieferant-Wahl fällt die Entscheidung". Der Brief sagt nicht, was du dann mit diesem Resultat machst.

**Was das für die Entscheidung bedeutet:** „MEHR DATEN" ist ein Euphemismus für „Lieferant-Evaluierung". Das ist nicht neutral, das ist eine Go/No-Go Entscheidung, die du nur verschiebst. Wenn du jetzt MEHR DATEN sagst, musst du auch sagen: „Und wenn Lieferant X ist, dann sagen wir Kill." Das steht nicht im Brief.

---

## Verdikt

**PAUSE (nicht BUILD, nicht KILL, nicht MEHR DATEN)**

Die Debatte und der Brief haben recht, dass die Entscheidung auf zu vielen Annahmen ruht. Aber die Lösung ist nicht „mehr Daten sammeln vor BUILD", sondern **„stabilisiere zuerst die operativen Engpässe, dann neu bewerten"**.

Grund: Sechs der sieben Annahmen sind volatile — sie hängen von Faktoren ab, die sich in den nächsten 8 Wochen ändern (INV-Gen3-Zertifizierungsverzug, Storage-Platform-Team-Reife, Feldtest-Kapazität). Wenn du jetzt MEHR DATEN sammelst und in Q3 mit voller Kraft kickoffst, dann bist du im Oktober in einer operativen Krise: Zertifizierung verzögert, neues Team unreif, Feldtest-Kapazität weg, BMS-Tests blockieren.

**Besser:** 
1. Lass INV-Gen3 DE/AT stabil laufen (= Architektur-Team free, Grid-Code gelernt, Zertifizierung solved, Q4).
2. Lass Storage-Platform-Team 4 Wochen ramp-up haben (parallel dazu).
3. *Dann* sammle MEHR DATEN (Lieferant-Eval, Markt-Interviews, Wettbewerbs-Analyse).
4. *Dann* kick off neue Batterie mit Q1-Zielstellung (nicht Q3, nicht Q4).

Das ist kein Verzug, das ist Risiko-Verschiebung auf Monate, in denen die Engpässe gelöst sind.

---

## Offene Fragen die zuerst beantwortet werden müssen

- **INV-Gen3 Zertifizierungs-Realität:** Wie hoch ist die Wahrscheinlichkeit, dass Grid-Code-Zertifizierung in Q3 bestanden ist (nicht verzögert)?
- **Storage-Platform-Team Ramp-up:** Ist eine 4-Wochen-Onboarding-Phase in der 6–8-Monats-Schätzung enthalten, oder wird das optimistisch weggedacht?
- **Feldtest-Standorte:** Sind 5 Early-Adopter-Kunden bereit, im Oktober/November Feldtests zu fahren, oder sind die mit INV-Gen3-Rollout gebunden?
- **Lieferant-Konsequenz:** Wenn Batterie-Eval zeigt, dass nur BYD oder nur Startup verfügbar ist — ist das ein KILL-Kriterium, oder akzeptiert die Strat das Supply-Chain-Risiko?
- **Wettbewerbs-Kontext-Realität:** Wenn Markt-Interviews zeigen, dass Konkurrenten *dieselbe* Batterie schon anbieten — ist das eine Disqualifikation für dieses Projekt, oder akzeptiert die Strat einen Follower-Move?

---

## Abschließende Einschätzung

Dieser Schritt hat den Debatten-Kritiker teilweise recycelt, aber mit einer wichtigen neuen Einsicht: Die Annahme über **Kapazitäts-Parallelität** ist nicht nur riskant, sie ist faktisch illusorisch, wenn man die Engpässe (INV-Gen3, Feldtest, neues Team) Ernst nimmt. Der Brief sagt „Gate einbauen", was richtig ist, aber **sagt nicht, dass dieses Gate Q3-Kickoff sehr wahrscheinlich abblockt**. Das ist die scharfe neue Einsicht: MEHR DATEN ist richtig, aber der realistisch beste Startpunkt ist nicht Q3, das ist Q1 2027 — nicht wegen Daten-Mangel, sondern wegen operativer Unreife *jetzt*.
