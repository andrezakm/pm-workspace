# Eval-Ergebnis: Feature Backlog Prioritizer

**Datum:** 2026-04-09
**Eval-Datei:** output/2026-04-09/spec-eval/eval.md
**Prototypen:** output/2026-04-09/prototyping/option-{a,b,c}/app.py

## Ergebnisse

| ID | Kriterium | Option A | Option B | Option C |
|----|-----------|----------|----------|----------|
| E1 | CSV einlesen, 12 Features | PASS | PASS | PASS |
| E2 | Score-Formel korrekt (4.7) | PASS | PASS | PASS |
| E3 | Tabelle nach Score sortiert | PASS | PASS | PASS |
| E4 | Status-Filter (→ 2+8) | PASS | PASS | PASS |
| E5 | Fit-Filter (→ 10+12) | PASS | PASS | PASS |
| E6 | Kombinierte Filter (→ 1+7) | PASS | PASS | PASS |
| E7 | Balkendiagramm gefilterte Features | PASS | PASS | **FAIL** |
| E8 | Balkendiagramm nach Score | PASS | PASS | **FAIL** |
| E9 | CSV nicht geschrieben | PASS | PASS | PASS |
| E10 | Ein-Befehl-Start | UNKLAR | UNKLAR | UNKLAR |
| E11 | Formel in UI sichtbar | PASS | PASS | PASS |
| E12 | CSV-Pfad konfigurierbar | PASS | PASS | PASS |

## Begründungen

**E1–E2:** Alle drei: identische CSV-Lade- und Score-Logik. `pd.read_csv(..., encoding="utf-8")` mit `try/except`. Formel `(kundenwunsche*0.5 + fit_num*0.3 + aufwand_inv*0.2).round(2)`. Feature 3: (6×0.5)+(3×0.3)+(4×0.2)=4.7 ✓ — Encoding-Fix gegenüber Vorversion in allen drei Apps.

**E3–E6:** Alle drei: `sort_values("score", ascending=False)`, sequenzielle Filter. Korrekte AND-Verknüpfung.

**E7–E8 Option C:** Kein `st.bar_chart` — Kachel-Design. FAIL. Bewusste Abweichung von der Spec.

**E10:** UNKLAR alle drei — Browser-Start ist Laufzeitverhalten.

**E11:** A: Sidebar-Formel mit Gewichten. B: Dritte Filter-Spalte caption. C: Sidebar caption.

**E12:** A+C: `st.sidebar.text_input`. B: `st.text_input` im Hauptbereich.

## Zusammenfassung

| | Option A | Option B | Option C |
|--|----------|----------|----------|
| PASS | 11 | 11 | 9 |
| FAIL | 0 | 0 | **2** |
| UNKLAR | 1 | 1 | 1 |

**Neu gegenüber Vorversion:** Alle drei Apps enthalten jetzt `encoding="utf-8"` in `pd.read_csv()` — der Encoding-Bug aus dem letzten Handoff ist behoben. Option A und B spec-konform. Option C scheitert planmäßig an E7/E8.
