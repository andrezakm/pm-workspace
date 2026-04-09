---
allowed-tools: Read, Write, Glob
---

# Orchestrator: Spec, Eval & Prototyp bauen

Führe die folgenden drei Schritte sequenziell aus. Schreibe alle drei Dateien wirklich — kein Code nur als Text.

## Vorbereitung

Der Pfad zum Brief wird beim Aufruf übergeben.
Prüfe mit Glob welche Datendateien im Brief referenziert werden. Lies den Brief und identifiziere die Datendateien. Wenn keine Datendateien gefunden: stoppe und melde den Fehler.

## Schritt 1: Spec → `output/spec-eval/spec.md`

Prüfe mit Glob ob `output/spec-eval/spec.md` bereits existiert.
- **Existiert:** Lies die Datei und melde "spec.md gefunden — wird verwendet." Kein Neuschreiben.
- **Existiert nicht:** Lies Brief und alle Datendateien. Schreibe `output/spec-eval/spec.md` mit: **Zweck**, **Nutzer**, **Daten-Input**, **UI-Komponenten** (nummeriert), **Constraints**. Was, nicht Wie. Keine Implementierungsdetails.

Verifiziere mit Glob, bevor du weitermachst.

## Schritt 2: Eval → `output/spec-eval/eval.md`

Prüfe mit Glob ob `output/spec-eval/eval.md` bereits existiert.
- **Existiert:** Lies die Datei und melde "eval.md gefunden — wird verwendet." Kein Neuschreiben.
- **Existiert nicht:** Lies `output/spec-eval/spec.md`. Schreibe `output/spec-eval/eval.md` als Tabelle mit 8–12 Kriterien:

| ID | Kriterium | Wie testen | Pass-Bedingung | Ergebnis |
|----|-----------|------------|----------------|----------|

Jedes Kriterium eindeutig pass/fail entscheidbar. Ergebnis-Spalte wird mit FAIL vorbelegt.

Verifiziere mit Glob, bevor du weitermachst.

## Schritt 3: Prototyp → `output/prototyping/app.py`

Lies `output/spec-eval/spec.md`. Schreibe vollständige, lauffähige Streamlit-App:
- Echte Daten aus Datendatei, kein Hardcoding
- Alle UI-Komponenten der Spec implementiert
- Sonderfälle behandelt
- Startbar mit `streamlit run`
- Nur streamlit + pandas. Kein matplotlib, kein plotly, kein altair. Für Diagramme: `st.bar_chart`, `st.line_chart` etc.
- Kein `@st.cache_data` — CSV direkt mit `pd.read_csv()` laden.

Verifiziere mit Glob.

## Abschluss

Alle drei Dateien vorhanden? Dann:
- Pfade ausgeben: `output/spec-eval/spec.md`, `output/spec-eval/eval.md`, `output/prototyping/app.py`
- `streamlit run output/prototyping/app.py`
- "Jetzt bist du dran — öffne die eval.md und gehe jeden Punkt manuell durch, bevor du den eval-runner startest."
