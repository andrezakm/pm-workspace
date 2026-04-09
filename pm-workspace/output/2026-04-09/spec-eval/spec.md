# Spec: Feature Backlog Prioritizer

## Zweck

Das Pattern-Team pflegt 12 Feature-Ideen in einer CSV-Datei, sortiert nach Bauchgefühl. Die App berechnet einen gewichteten Score aus den vorhandenen Feldern und visualisiert das Ergebnis so, dass Priorisierungsentscheidungen nachvollziehbar und im Team teilbar werden — auch gegenüber der Geschäftsführung.

## Nutzer

Pattern-Team (2 Personen) und Geschäftsführung. Kein technisches Onboarding nötig. App startet mit einem Befehl.

## Daten-Input

**Datei:** `input/case/data/backlog.csv`

**Felder:**
- `id` — numerische ID
- `feature` — Name des Features
- `beschreibung` — Kurzbeschreibung
- `kundenwunsche` — Zahl (1–10)
- `strategischer_fit` — `hoch`, `mittel`, `niedrig`
- `aufwand` — `S`, `M`, `L`, `XL`
- `status` — `backlog`, `geplant`, `idee`

## UI-Komponenten

1. **Score-Tabelle** — Alle Features, sortierbar. Spalten: Feature, Kundenwünsche, Strategischer Fit, Aufwand, Score. Standard: absteigend nach Score.

2. **Score-Berechnung** — Gewichteter Score:
   - `strategischer_fit` → hoch=3, mittel=2, niedrig=1
   - `aufwand` → S=4, M=3, L=2, XL=1 (invertiert)
   - Formel: `(kundenwunsche × 0.5) + (fit_num × 0.3) + (aufwand_inv × 0.2)`

3. **Filter: Status** — Dropdown: backlog / geplant / idee / alle.

4. **Filter: Strategischer Fit** — Dropdown: hoch / mittel / niedrig / alle.

5. **Balkendiagramm** — Horizontales Balkendiagramm aller sichtbaren Features, sortiert nach Score.

6. **CSV-Pfad-Eingabe** — Textfeld mit Standardwert `input/case/data/backlog.csv`.

## Constraints

- CSV wird nur gelesen, nie geschrieben
- Kein User-Management
- Formel fix, in der UI sichtbar
- Läuft lokal: `streamlit run app.py`
- Keine Datenbankanbindung, keine Export-Funktion
