# Brief: Feature Backlog Prioritizer

**Datum:** März 2026
**Autor:** NeoEmployee Pattern-Team

---

## Das Problem

Das Pattern-Team (2 Personen) pflegt eine wachsende Liste von Feature-Ideen für potenzielle Produkte. Stand heute: 12 Einträge in einer Excel-Tabelle, manuell sortiert nach Bauchgefühl.

Das Problem: Es gibt kein systematisches Scoring. "Strategischer Fit" ist eine Spalte die wir unterschiedlich ausfüllen. "Kundenwunsch" ist eine Zahl aber niemand weiß wie sie entstand. Aufwand ist eine grobe Schätzung ohne Kriterien.

Resultat: In jedem Team-Meeting diskutieren wir dieselben Top-3-Features ohne uns einigen zu können. Die Priorisierung ist nicht nachvollziehbar und nicht teilbar.

## Die Nutzer

Das NeoEmployee Pattern-Team (2 Personen) und gelegentlich die Geschäftsführung. Ziel: eine gemeinsame, nachvollziehbare Priorisierungsgrundlage.

## Was wir brauchen

Eine lokale App die die Backlog-CSV einliest, Features nach einem gewichteten Score berechnet und visualisiert. Filterbar nach Status und strategischem Fit. Sortierbar nach Score.

## Was wir nicht brauchen

- Keine Bearbeitung der Daten in der App — CSV wird extern gepflegt
- Kein User-Management
- Keine komplexen Scoring-Modelle — einfache Gewichtung reicht
- Läuft lokal, gestartet mit einem Befehl
