# InsightValidator — Skill-Spezifikation

Ein mehrstufiger, interaktiver Prozess zur Validierung einer "Insight" gegen den bekannten Projektkontext. Der Anwender führt ein Gespräch mit der Skill — jede Stufe endet mit einer bewussten Entscheidung weiterzumachen oder abzubrechen.

---

## Zweck

Jemand hat eine Idee, Beobachtung oder Erkenntnis ("Insight") und möchte wissen: Ist das wirklich neu? Was fehlt? Worauf muss ich wetten? Was muss ich testen, bevor ich Ressourcen einsetze?

Der InsightValidator beantwortet diese Fragen systematisch in sechs Schritten.

---

## Vorbereitung: Run-Verzeichnis und Kontext

**Run-Verzeichnis:** Alle Outputs gehen nach `output/YYYY-MM-DD/insight-validator/` — ersetze YYYY-MM-DD durch das tatsächliche Datum. Das Verzeichnis entsteht implizit beim ersten Write-Aufruf.

**Kontext-Quellen (Priorität in dieser Reihenfolge):**

1. `context/` Ordner im aktuellen Projektverzeichnis — immer lesen:
   - `context/company.md`
   - `context/strategy.md`
   - `context/product.md` (falls vorhanden)
   - `context/metrics.md` (falls vorhanden)
   - alle weiteren `.md` Dateien im `context/` Ordner
2. Vom Anwender explizit angebotener Kontext (andere Dateien oder Ordner)
3. Falls kein `context/` Ordner existiert: den Anwender fragen, wo der Kontext liegt

Ohne Kontext kein Output — dann abbrechen und Anwender informieren.

---

## Input

Der Anwender beschreibt seine Insight auf eine von zwei Arten:

- **Direkt:** Der Anwender schreibt die Insight im Chat
- **Per Datei-Referenz:** Der Anwender nennt einen Dateipfad — die Skill liest die Datei

Die Skill fragt zu Beginn: *"Beschreibe deine Insight — entweder direkt hier oder nenne den Pfad zu einer Datei."*

---

## Schritt 1: First Impression — Insight gegen Kontext abgleichen

### Was passiert

Lies den gesamten bekannten Kontext. Vergleiche die Insight systematisch mit dem, was bereits bekannt ist.

Untersuche vier Dimensionen:

1. **Konflikte** — Widerspricht die Insight explizit vorhandenem Kontext, bestehenden Entscheidungen oder bekannten Constraints?
2. **Ergänzungen** — Was fügt die Insight hinzu, das bisher fehlte? Wo bereichert sie das Bild?
3. **Lücken** — Was müsste man wissen, um die Insight zu beurteilen — und ist dieses Wissen im Kontext nicht vorhanden?
4. **Risiken** — Welche Risiken entstehen, wenn man der Insight folgt? Was könnte schiefgehen?

Sei direkt. Keine höfliche Absicherung. Wenn etwas klar im Widerspruch steht, sag es.

### Output

Schreibe `output/YYYY-MM-DD/insight-validator/FirstImpression.md`:

```markdown
# First Impression: [Kurzname der Insight]

**Insight (Zusammenfassung):** [1-2 Sätze]

## Konflikte
[Jeder Konflikt als eigener Absatz mit Verweis auf den konkreten Kontext-Inhalt]

## Ergänzungen
[Was die Insight zum bekannten Bild hinzufügt]

## Lücken
[Was fehlt um die Insight zu beurteilen]

## Risiken
[Konkrete Risiken bei Umsetzung — nicht abstrakt]

## Erste Einschätzung
[1 Absatz: Wie stark ist die Insight? Ist sie wirklich neu oder reformuliert sie Bekanntes?]
```

### Übergabe an Anwender

Teile dem Anwender mit:
- Die Datei wurde geschrieben
- Wo sie liegt
- *"Lies die First Impression. Möchtest du weitermachen zu Schritt 2 (Upside/Downside-Analyse)?"*

**Wenn Nein: Ende.** Kein weiterer Output.

---

## Schritt 2: Upside / Downside Analyse

*Nur wenn der Anwender explizit bestätigt hat weiterzumachen.*

### Was passiert

Schätze das Verhältnis von Potential und Risiko der Insight grob ab. Das ist keine präzise Finanzmodellierung — es ist eine strukturierte Abschätzung, die dem Anwender hilft zu entscheiden ob die Insight es wert ist, tiefer zu gehen.

**Upside:** Was ist das maximale Potential dieser Insight, wenn sie sich als richtig erweist? Welche Dimensionen sind relevant (Umsatz, Reichweite, strategische Position, Kundenzufriedenheit, etc.)?

**Downside:** Was sind die realen Kosten, wenn man der Insight folgt und sie sich als falsch erweist? Direkte Kosten (Zeit, Geld, Ressourcen) + indirekte Kosten (Opportunitätskosten, verlorenes Vertrauen, strategische Fehlausrichtung).

**Research:** Starte parallele Research-Agenten für die folgenden Dimensionen:
- Marktgröße oder Relevanz des Insight-Bereichs (grob)
- Bekannte Präzedenzfälle: Hat jemand eine ähnliche Insight gehabt — was ist passiert?
- Aktuelle externe Faktoren (Markt, Technologie, Regulierung) die Upside oder Downside beeinflussen

Die Research muss hier noch nicht tief sein — Richtung und Größenordnung genügen.

Halte die Analyse im Kontext des Projekts — Upside und Downside sind relativ zum Unternehmen, nicht abstrakt.

### Output

Schreibe `output/YYYY-MM-DD/insight-validator/UpDownSide.md`:

```markdown
# Upside / Downside: [Kurzname der Insight]

## Upside — Potential wenn die Insight stimmt

**Dimensionen:** [welche Bereiche profitieren]
**Größenordnung:** [grobe Abschätzung — klein / mittel / groß / transformativ]
**Begründung:** [warum diese Einschätzung, mit Research-Ergebnissen]
**Zeitrahmen:** [wann würde das Potential realisierbar sein]

## Downside — Risiko wenn die Insight falsch ist

**Direkte Kosten:** [Zeit, Geld, Ressourcen]
**Indirekte Kosten:** [Opportunitätskosten, strategische Fehlausrichtung]
**Größenordnung:** [grobe Abschätzung]
**Schlimmster Fall:** [was ist das Worst-Case-Szenario]

## Upside/Downside-Verhältnis

**Verhältnis:** [z.B. "10:1 zugunsten Upside" oder "ausgeglichen" oder "Downside dominiert"]
**Fazit:** [1 Absatz: Lohnt es sich auf Basis dieser Abschätzung weiterzumachen?]

## Research-Quellen
[Verwendete Quellen und Fundstellen aus der parallelen Research]
```

### Übergabe an Anwender

*"Lies die Upside/Downside-Analyse. Möchtest du weitermachen zu Schritt 3 (Hypothesis Mapping)?"*

**Wenn Nein: Ende.**

---

## Schritt 3: Hypothesis Mapping — "What must be true"

*Nur wenn der Anwender explizit bestätigt hat weiterzumachen.*

### Was passiert

Identifiziere alle Annahmen, die wahr sein müssen damit die Insight funktioniert und das ermittelte Potential auch nur annähernd erreichbar ist.

Bewerte jede Annahme auf zwei unabhängigen Dimensionen:

**Dimension A — Erfolgsrelevanz:** Wie stark hängt der Erfolg der Insight vom Wahrheit dieses Statements ab?
- `1` = der Erfolg ist weitgehend unabhängig davon
- `5` = die Insight stirbt, wenn dieses Statement nicht wahr ist

**Dimension B — Evidenz:** Wie gut belegt ist dieses Statement?
- `1` = keine Daten, keine Hinweise, reine Annahme
- `5` = starke Evidenz, belastbare Daten, bestätigte Fakten

### Zwei Gruppen

Bilde zwei Gruppen aus den Statements:

**Gruppe "Zu Testen"** — Top-Statements mit hoher Erfolgsrelevanz (A ≥ 4) und niedriger Evidenz (B ≤ 2). Das sind die kritischen Unbekannten — hier entscheidet sich ob die Insight trägt.

**Gruppe "Sicherzustellen"** — Top-Statements mit hoher Erfolgsrelevanz (A ≥ 4) und hoher Evidenz (B ≥ 4). Diese Annahmen tragen den Erfolg — sie müssen aktiv geschützt und aufrechterhalten werden.

Liste je Gruppe maximal 5 Statements. Qualität vor Quantität.

### Direkt weiter zu Schritt 4

Kein Halt, keine Bestätigung nach Schritt 3. Schreibe den Output und fahre sofort mit Schritt 4 fort.

### Output

Schreibe `output/YYYY-MM-DD/insight-validator/HypothesisMapping.md`:

```markdown
# Hypothesis Mapping: [Kurzname der Insight]

## Alle Annahmen

| Statement | Erfolgsrelevanz (A, 1-5) | Evidenz (B, 1-5) | Gruppe |
|-----------|--------------------------|-------------------|--------|
| [Statement] | [A] | [B] | Zu Testen / Sicherzustellen / Nachrangig |

## Gruppe "Zu Testen" — Kritische Unbekannte

Diese Annahmen sind entscheidend für den Erfolg und aktuell nicht belegt.
Wenn sie sich als falsch erweisen, scheitert die Insight.

### [Statement 1]
[1 Absatz: Warum ist dieses Statement so erfolgskritisch? Warum fehlt uns die Evidenz?]

### [Statement 2]
...

## Gruppe "Sicherzustellen" — Fundament des Erfolgs

Diese Annahmen sind gut belegt und erfolgskritisch.
Sie müssen aktiv geschützt und aufrechterhalten werden.

### [Statement 1]
[1 Absatz: Was macht uns sicher dass dieses Statement stimmt? Wie stellen wir sicher, dass es stimmt bleibt?]

### [Statement 2]
...
```

---

## Schritt 4: Experiment-Design

*Läuft direkt im Anschluss an Schritt 3 — kein separater Bestätigungsschritt.*

### Was passiert

Zu jedem Statement in Gruppe "Zu Testen" werden drei Experimente designt — aufsteigend in Tiefe, Kosten und Präzision.

**Experiment Typ 1 — Billiger Richtungscheck:**
Sehr einfach, sehr günstig. Grobe Validierung ob wir in der richtigen Richtung sind. Kein Setup notwendig, manuell durchführbar. Ziel: Ist die Annahme grundsätzlich plausibel?
Beispiele: 5 Interviews, ein schneller Desk-Research, eine einfache Umfrage, eine Smoke-Test-Landingpage.

**Experiment Typ 2 — Strukturierte Validierung:**
Ein Niveau tiefer. Komplizierter, teurer, braucht etwas Infrastruktur oder Vorbereitung. Immer noch manuell oder nicht-skaliert. Ziel: Stimmt die Richtung wirklich, und in welcher Größenordnung?
Beispiele: Strukturierte Nutzertests, Wizard-of-Oz-Test, A/B-Test mit kleiner Gruppe, Analyse existierender Daten.

**Experiment Typ 3 — Skaliertes Präzisionsexperiment:**
Skaliert, kann mehr kosten, liefert quantitative Daten über Richtung hinaus. Ziel: Belastbare Zahlen die eine Entscheidung tragen.
Beispiele: Groß angelegter A/B-Test, quantitative Marktforschung, Beta-Rollout mit Metriken, formelle Pilotstudie.

Jedes Experiment beschreibt in 2-4 Sätzen: was gemacht wird, wie lang es dauert, was es kostet (grob), und welche konkrete Frage es beantwortet.

### Output

Ergänze `output/YYYY-MM-DD/insight-validator/HypothesisMapping.md` um den folgenden Abschnitt:

```markdown
---

## Experiment-Design: Zu Testen

### [Statement aus Gruppe "Zu Testen"]

**Experiment 1 — Billiger Richtungscheck:**
[2-4 Sätze: Was, Dauer, Kosten, welche Frage beantwortet es]

**Experiment 2 — Strukturierte Validierung:**
[2-4 Sätze: Was, Dauer, Kosten, welche Frage beantwortet es]

**Experiment 3 — Skaliertes Präzisionsexperiment:**
[2-4 Sätze: Was, Dauer, Kosten, welche Frage beantwortet es]

---

### [Nächstes Statement]
...
```

### Abschluss

Nach dem Schreiben des Experiment-Designs teile dem Anwender mit:

*"Der InsightValidator ist abgeschlossen. Alle Outputs liegen in `output/YYYY-MM-DD/insight-validator/`:"*
- `FirstImpression.md` — Konfliktanalyse gegen bekannten Kontext
- `UpDownSide.md` — Upside/Downside-Verhältnis
- `HypothesisMapping.md` — Kritische Annahmen + Experiment-Design

*"Empfohlener nächster Schritt: Starte mit den Experimenten in Gruppe 'Zu Testen', beginnend mit Typ 1."*

---

## Qualitätskriterien für den gesamten Prozess

- Jede Aussage ist entweder aus dem Kontext ableitbar oder explizit als Annahme markiert
- Konflikte werden direkt benannt — keine diplomatische Abschwächung
- Upside und Downside sind relativ zum konkreten Projektkontext, nicht abstrakt
- Hypothesen sind spezifisch genug um falsifizierbar zu sein ("Nutzer wollen X" ist keine Hypothese — "60% der Nutzer im Segment Y tauschen Feature Z gegen Eigenschaft W" schon)
- Experimente sind konkret und direkt umsetzbar — keine vagen Richtungsangaben

---

## Erlaubte Tools

```
allowed-tools: Read, Write, WebSearch, WebFetch, Agent
```

Web-Research (Schritt 2) läuft über parallele Agent-Aufrufe mit `subagent_type: general-purpose`. Jeder Agent bekommt eine klar abgegrenzte Recherche-Aufgabe und gibt ein strukturiertes Ergebnis zurück.
