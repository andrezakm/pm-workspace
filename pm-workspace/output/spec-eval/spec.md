# Spec: Feature Backlog Prioritizer

## Zweck

Das Pattern-Team hat 12 Feature-Ideen in einer CSV-Datei, die bisher nach Bauchgefühl sortiert werden. Die App berechnet für jedes Feature einen gewichteten Score aus den vorhandenen Feldern und visualisiert das Ergebnis so, dass Priorisierungsentscheidungen nachvollziehbar und teilbar werden — auch für die Geschäftsführung.

## Nutzer

Pattern-Team (2 Personen) und Geschäftsführung. Kein technisches Onboarding nötig — App startet mit einem Befehl, keine Installation außer einmaligem Setup.

## Daten-Input

**Datei:** `input/case/data/backlog.csv`

**Felder:**
- `id` — numerische ID
- `feature` — Name des Features
- `beschreibung` — Kurzbeschreibung
- `kundenwunsche` — Zahl (Skala implizit 1–10)
- `strategischer_fit` — Kategorie: `hoch`, `mittel`, `niedrig`
- `aufwand` — T-Shirt-Größe: `S`, `M`, `L`, `XL`
- `status` — Kategorie: `backlog`, `geplant`, `idee`

## UI-Komponenten

1. **Score-Tabelle** — Alle Features als sortierbare Tabelle. Spalten: Feature-Name, Kundenwünsche, Strategischer Fit, Aufwand, berechneter Gesamt-Score. Standardmäßig absteigend nach Score sortiert.

2. **Score-Berechnung** — Gewichteter Score aus drei Eingaben:
   - `kundenwunsche` (Zahl, direkt)
   - `strategischer_fit` → numerisch umgerechnet: hoch = 3, mittel = 2, niedrig = 1
   - `aufwand` → invertiert (weniger Aufwand = höherer Score): S = 4, M = 3, L = 2, XL = 1
   - Formel: `(kundenwunsche × 0.5) + (strategischer_fit_num × 0.3) + (aufwand_inv × 0.2)`

3. **Filter: Status** — Dropdown oder Checkbox-Gruppe zum Filtern nach `status`-Wert (backlog / geplant / idee / alle). Beeinflusst welche Zeilen in der Tabelle und im Chart erscheinen.

4. **Filter: Strategischer Fit** — Dropdown zum Filtern nach `strategischer_fit` (hoch / mittel / niedrig / alle).

5. **Balkendiagramm** — Horizontales Balkendiagramm aller sichtbaren Features, sortiert nach Score. X-Achse: Score-Wert. Y-Achse: Feature-Name. Gibt auf einen Blick einen Überblick ohne in die Tabelle schauen zu müssen.

6. **CSV-Pfad-Eingabe** — Einfaches Textfeld oder Parameter beim Start um den Pfad zur CSV-Datei anzugeben. Standardwert: `backlog.csv` im selben Verzeichnis.

## Constraints

- Keine Bearbeitung der Daten innerhalb der App — CSV wird ausschließlich gelesen, nie geschrieben
- Kein User-Management, keine Authentifizierung
- Keine komplexen Scoring-Modelle — die Gewichtungsformel ist fix und transparent sichtbar
- Läuft lokal, gestartet mit einem einzigen Befehl (z.B. `streamlit run app.py`)
- Keine Datenbankanbindung
- Keine Export-Funktion (nicht im Brief erwähnt)
