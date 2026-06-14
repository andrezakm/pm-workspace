---
allowed-tools: Read, Write, Glob, WebSearch, WebFetch, Agent
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools und Agent-Subagenten. Keine MCP-Tools (`mcp__filesystem__*`).

# Skill: InsightValidator

Validiere eine Insight systematisch gegen den Projektkontext — von First Impression bis Experiment-Design. Vier Schritte, zwei bewusste Haltepunkte.

## Schritt 0: Run-Verzeichnis bestimmen

Berechne das heutige Datum im Format YYYY-MM-DD. Alle Outputs dieses Skills gehen in `output/YYYY-MM-DD/strategy/insight-validator/` — ersetze YYYY-MM-DD durch das tatsächliche Datum. Erstelle dieses Verzeichnis implizit durch den ersten Write-Aufruf.

---

## Input

### Frage 1: Kontext bestimmen

Frage den Anwender zuerst:

*"Soll ich den bekannten Projektkontext aus `context/` verwenden, oder möchtest du anderen Kontext als Grundlage nehmen?"*

**Option A — Bekannter Kontext:** Lies die Context-Files in dieser Reihenfolge:
1. `context/company.md` — immer
2. `context/strategy.md` — immer
3. `context/product.md` — falls vorhanden
4. `context/metrics.md` — falls vorhanden
5. Alle weiteren `.md` Dateien in `context/` (verwende Glob: `context/*.md`)

Falls `context/` nicht existiert oder alle Dateien leer sind: informiere den Anwender und frage nach alternativem Kontext.

**Option B — Anderer Kontext:** Der Anwender nennt Dateipfade oder Ordner. Lies alles was genannt wird mit Read/Glob.

Ohne Kontext kein Output — abbrechen.

**Warte auf die Antwort bevor du weitermachst.**

### Frage 2: Insight erfassen

Frage den Anwender:

*"Möchtest du deine Insight direkt hier beschreiben, oder soll ich sie aus einer Datei lesen?"*

- Wenn der Anwender direkt schreibt: verwende den Text als Input
- Wenn der Anwender einen Dateipfad nennt: lies die Datei mit Read

**Warte auf die Antwort bevor du mit Schritt 1 beginnst.**

---

## Schritt 1: First Impression — Insight gegen Kontext abgleichen

Lies den gesamten bekannten Kontext. Vergleiche die Insight systematisch mit dem, was bereits bekannt ist.

Untersuche vier Dimensionen:

1. **Konflikte** — Widerspricht die Insight explizit vorhandenem Kontext, bestehenden Entscheidungen oder bekannten Constraints?
2. **Ergänzungen** — Was fügt die Insight hinzu, das bisher fehlte? Wo bereichert sie das Bild?
3. **Lücken** — Was müsste man wissen, um die Insight zu beurteilen — und ist dieses Wissen im Kontext nicht vorhanden?
4. **Risiken** — Welche Risiken entstehen, wenn man der Insight folgt? Was könnte schiefgehen?

Sei direkt. Keine höfliche Absicherung. Wenn etwas klar im Widerspruch steht, sag es.

### Output: FirstImpression.md

Schreibe `output/YYYY-MM-DD/strategy/insight-validator/FirstImpression.md`:

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

### Halt — Anwender entscheidet

Teile dem Anwender mit:
- Die Datei wurde geschrieben und wo sie liegt
- *"Lies die First Impression. Möchtest du weitermachen zu Schritt 2 (Upside/Downside-Analyse)?"*

**STOP. Warte auf die Antwort des Anwenders.**

- Wenn der Anwender bestätigt ("ja", "weiter", "next", etc.): weiter zu Schritt 2
- Wenn der Anwender ablehnt oder abbricht: Ende. Weise auf die bereits geschriebene Datei hin.

---

## Schritt 2: Upside / Downside Analyse

*Nur wenn der Anwender explizit bestätigt hat weiterzumachen.*

Schätze das Verhältnis von Potential und Risiko der Insight grob ab — im Kontext des Projekts, nicht abstrakt.

### Research — Parallele Agenten

Starte 3 Agent-Aufrufe gleichzeitig (parallel, in derselben Nachricht). Jeder Agent nutzt WebSearch und WebFetch. Gib jedem Agenten den Kontext der Insight und des Unternehmens mit. Jeder Agent macht 2-3 Suchen — Richtung genügt, keine tiefe Analyse.

**Agent 1 — Marktrelevanz:**
Recherchiere die Marktgröße und Relevanz des Bereichs, den die Insight adressiert. Liefere: Marktgröße (grob), Wachstumsrichtung, relevante Segmente. Sprache: Deutsch. Ergebnis in unter 300 Wörtern.

**Agent 2 — Präzedenzfälle:**
Recherchiere ob andere Unternehmen eine ähnliche Insight verfolgt haben — was ist passiert? Liefere: 2-3 Beispiele mit Outcome und Lessons Learned. Sprache: Deutsch. Ergebnis in unter 300 Wörtern.

**Agent 3 — Externe Faktoren:**
Recherchiere aktuelle externe Faktoren (Markttrends, Technologieentwicklung, Regulierung) die die Insight beeinflussen. Liefere: Top 3-5 Faktoren die Upside oder Downside beeinflussen. Sprache: Deutsch. Ergebnis in unter 300 Wörtern.

### Ergebnisse zusammenführen

Nachdem alle 3 Agenten abgeschlossen haben: Lies die Ergebnisse und synthetisiere sie in die Upside/Downside-Analyse. Halte die Analyse relativ zum Unternehmen und Projektkontext.

### Output: UpDownSide.md

Schreibe `output/YYYY-MM-DD/strategy/insight-validator/UpDownSide.md`:

```markdown
# Upside / Downside: [Kurzname der Insight]

## Upside — Potential wenn die Insight stimmt

**Dimensionen:** [welche Bereiche profitieren]
**Größenordnung:** [klein / mittel / groß / transformativ]
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

### Halt — Anwender entscheidet

Teile dem Anwender mit:
- Die Datei wurde geschrieben und wo sie liegt
- *"Lies die Upside/Downside-Analyse. Möchtest du weitermachen zu Schritt 3 (Hypothesis Mapping + Experiment-Design)?"*

**STOP. Warte auf die Antwort des Anwenders.**

- Wenn der Anwender bestätigt: weiter zu Schritt 3
- Wenn der Anwender ablehnt: Ende. Weise auf die bereits geschriebenen Dateien hin.

---

## Schritt 3: Hypothesis Mapping — "What must be true"

*Nur wenn der Anwender explizit bestätigt hat weiterzumachen.*

Identifiziere alle Annahmen, die wahr sein müssen damit die Insight funktioniert und das ermittelte Potential auch nur annähernd erreichbar ist.

Bewerte jede Annahme auf zwei unabhängigen Dimensionen:

**Dimension A — Erfolgsrelevanz:** Wie stark hängt der Erfolg der Insight vom Wahrheit dieses Statements ab?
- `1` = der Erfolg ist weitgehend unabhängig davon
- `5` = die Insight stirbt, wenn dieses Statement nicht wahr ist

**Dimension B — Evidenz:** Wie gut belegt ist dieses Statement?
- `1` = keine Daten, keine Hinweise, reine Annahme
- `5` = starke Evidenz, belastbare Daten, bestätigte Fakten

### Zwei Gruppen bilden

**Gruppe "Zu Testen"** — Statements mit hoher Erfolgsrelevanz (A ≥ 4) und niedriger Evidenz (B ≤ 2). Das sind die kritischen Unbekannten — hier entscheidet sich ob die Insight trägt.

**Gruppe "Sicherzustellen"** — Statements mit hoher Erfolgsrelevanz (A ≥ 4) und hoher Evidenz (B ≥ 4). Diese Annahmen tragen den Erfolg — sie müssen aktiv geschützt werden.

Je Gruppe maximal 5 Statements. Qualität vor Quantität.

### Output: HypothesisMapping.md

Schreibe `output/YYYY-MM-DD/strategy/insight-validator/HypothesisMapping.md`:

```markdown
# Hypothesis Mapping: [Kurzname der Insight]

## Alle Annahmen

| Statement | Erfolgsrelevanz (A) | Evidenz (B) | Gruppe |
|-----------|---------------------|-------------|--------|
| [Statement] | [1-5] | [1-5] | Zu Testen / Sicherzustellen / Nachrangig |

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
[1 Absatz: Was macht uns sicher dass dieses Statement stimmt? Wie stellen wir sicher, dass es so bleibt?]

### [Statement 2]
...
```

### Kein Halt — direkt weiter zu Schritt 4

Fahre SOFORT mit Schritt 4 fort. Keine Bestätigung vom Anwender.

---

## Schritt 4: Experiment-Design

Zu jedem Statement in Gruppe "Zu Testen" werden drei Experimente designt — aufsteigend in Tiefe, Kosten und Präzision.

**Experiment Typ 1 — Billiger Richtungscheck:**
Sehr einfach, sehr günstig. Kein Setup notwendig, manuell durchführbar. Ist die Annahme grundsätzlich plausibel?
Beispiele: 5 Interviews, schneller Desk-Research, einfache Umfrage, Smoke-Test-Landingpage.

**Experiment Typ 2 — Strukturierte Validierung:**
Ein Niveau tiefer. Komplizierter, braucht etwas Infrastruktur. Immer noch manuell oder nicht-skaliert. Stimmt die Richtung wirklich, und in welcher Größenordnung?
Beispiele: Strukturierte Nutzertests, Wizard-of-Oz-Test, A/B-Test mit kleiner Gruppe, Analyse existierender Daten.

**Experiment Typ 3 — Skaliertes Präzisionsexperiment:**
Skaliert, kann kosten, liefert quantitative Daten. Belastbare Zahlen die eine Entscheidung tragen.
Beispiele: Groß angelegter A/B-Test, quantitative Marktforschung, Beta-Rollout mit Metriken, Pilotstudie.

Jedes Experiment: 2-4 Sätze — was wird gemacht, wie lang dauert es, was kostet es (grob), welche konkrete Frage beantwortet es.

### Output: HypothesisMapping.md ergänzen

Lies die aktuelle `HypothesisMapping.md`, füge den folgenden Abschnitt am Ende hinzu, und schreibe die vollständige Datei neu:

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

Teile dem Anwender mit:

*"Der InsightValidator ist abgeschlossen. Alle Outputs liegen in `output/YYYY-MM-DD/strategy/insight-validator/`:"*
- `FirstImpression.md` — Konfliktanalyse gegen bekannten Kontext
- `UpDownSide.md` — Upside/Downside-Verhältnis mit Research
- `HypothesisMapping.md` — Kritische Annahmen + Experiment-Design

*"Empfohlener nächster Schritt: Starte mit den Experimenten in Gruppe 'Zu Testen', beginnend mit Typ 1 (Billiger Richtungscheck)."*

---

## Qualitätskriterien

- Jede Aussage ist entweder aus dem Kontext ableitbar oder explizit als Annahme markiert
- Konflikte werden direkt benannt — keine diplomatische Abschwächung
- Upside und Downside sind relativ zum konkreten Projektkontext, nicht abstrakt
- Hypothesen sind spezifisch genug um falsifizierbar zu sein ("Nutzer wollen X" ist keine Hypothese — "60% der Nutzer im Segment Y tauschen Feature Z gegen Eigenschaft W" schon)
- Experimente sind konkret und direkt umsetzbar — keine vagen Richtungsangaben
- Alle Outputs auf Deutsch mit korrekten Umlauten (ä, ö, ü, ß)

## Fehlerbehandlung

- Wenn ein Research-Agent keine Ergebnisse findet: notiere "Keine öffentlichen Daten verfügbar" im entsprechenden Abschnitt der UpDownSide-Analyse und arbeite mit dem vorhandenen Kontext weiter
- Wenn eine Context-Datei fehlt: überspringe sie, arbeite mit dem vorhandenen Kontext
- Wenn der Anwender nach Schritt 1 oder 2 abbricht: bestätige das Ende und weise auf die bereits geschriebenen Dateien hin
