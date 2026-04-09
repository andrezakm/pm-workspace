# Eval-Ergebnis: Feature Backlog Prioritizer

**Datum:** 2026-04-09
**Eval-Datei:** output/spec-eval/eval.md
**Prototypen:** option-a/app.py, option-b/app.py, option-c/app.py

---

## Ergebnisse

| ID | Kriterium | Option A | Option B | Option C |
|----|-----------|----------|----------|----------|
| E1 | CSV einlesen, 12 Features | PASS | PASS | PASS |
| E2 | Score-Formel korrekt (Feature 3 = 4.7) | PASS | PASS | PASS |
| E3 | Tabelle nach Score sortiert | PASS | PASS | PASS |
| E4 | Status-Filter (geplant → Features 2+8) | PASS | PASS | PASS |
| E5 | Fit-Filter (niedrig → Features 10+12) | PASS | PASS | PASS |
| E6 | Kombinierte Filter korrekt | PASS | PASS | PASS |
| E7 | Balkendiagramm zeigt gefilterte Features | PASS | PASS | **FAIL** |
| E8 | Balkendiagramm nach Score sortiert | PASS | PASS | **FAIL** |
| E9 | CSV nicht geschrieben | PASS | PASS | PASS |
| E10 | Ein-Befehl-Start | UNKLAR | UNKLAR | UNKLAR |
| E11 | Scoring-Formel in UI sichtbar | PASS | PASS | PASS |
| E12 | CSV-Pfad konfigurierbar | PASS | PASS | PASS |

---

## Begründungen

**E1** — Alle drei: `pd.read_csv(csv_path)` mit `try/except FileNotFoundError`. CSV wird geladen, Fehler abgefangen. (Alle: Z. 12–15)

**E2** — Alle drei: identische Formel `(kundenwunsche * 0.5 + fit_num * 0.3 + aufwand_inv * 0.2).round(2)` mit `fit_map = {"hoch": 3, ...}` und `aufwand_map = {"S": 4, ...}`. Feature 3: (6×0.5)+(3×0.3)+(4×0.2) = 4.7 ✓ (Alle: Z. 18–23)

**E3** — Alle drei: `gefiltert.sort_values("score", ascending=False)` vor Darstellung. (A: Z. 42, B: Z. 48, C: Z. 46)

**E4** — Alle drei: `gefiltert[gefiltert["status"] == status_filter]` — filtert korrekt auf exakten String-Match. (A: Z. 38, B: Z. 43, C: Z. 42)

**E5** — Alle drei: `gefiltert[gefiltert["strategischer_fit"] == fit_filter]` — gleiche Logik. (A: Z. 40, B: Z. 45, C: Z. 44)

**E6** — Alle drei: beide Filter werden sequenziell auf denselben DataFrame angewendet — korrekte AND-Verknüpfung. (A: Z. 36–40, B: Z. 41–46, C: Z. 40–44)

**E7** — A+B: `st.bar_chart(chart_data)` auf gefiltertem DataFrame. (A: Z. 68, B: Z. 57) — **Option C: kein Balkendiagramm** — die App nutzt Kacheln als Hauptdarstellung, kein `st.bar_chart` vorhanden. FAIL.

**E8** — A+B: `sort_values("score", ascending=False)` vor `set_index("feature")` → Chart zeigt absteigende Reihenfolge. (A: Z. 42+67, B: Z. 48+56) — **Option C: kein Chart.** FAIL.

**E9** — Alle drei: ausschließlich `pd.read_csv()`, kein `to_csv()`, kein File-Write anywhere im Code. PASS.

**E10** — UNKLAR für alle drei: Der Code ist syntaktisch valider Streamlit-Code mit Standard-Imports (`streamlit`, `pandas`). Ein-Befehl-Start mit `streamlit run app.py` ist aus dem Code-Aufbau ableitbar. Ob der Browser tatsächlich öffnet, ist Laufzeitverhalten — nicht aus dem Code entscheidbar.

**E11** — A: Sidebar zeigt `### Scoring-Formel` mit Formel und Gewichten. (Z. 45–49) B: Dritte Spalte der Filter-Row zeigt Formel als caption. (Z. 37–39) C: Sidebar zeigt `### Scoring-Formel` mit caption. (Z. 35–37) Alle PASS.

**E12** — A+C: `st.sidebar.text_input("CSV-Pfad", value="input/case/data/backlog.csv")` — konfigurierbarer Pfad. B: `st.text_input(...)` im Hauptbereich. Alle drei PASS.

---

## Zusammenfassung

| | Option A | Option B | Option C |
|--|----------|----------|----------|
| PASS | 11 | 11 | 9 |
| FAIL | 0 | 0 | **2** |
| UNKLAR | 1 | 1 | 1 |

**Option A und B** erfüllen alle testbaren Kriterien vollständig. Beide sind spec-konform.

**Option C** scheitert an E7 und E8 — kein Balkendiagramm. Das ist eine bewusste Design-Entscheidung (Kachel-UI statt Chart), aber sie verletzt die Spec. Wer Option C wählt, müsste die Spec an diesem Punkt anpassen oder das Diagramm als ausklappbaren Zusatz nachrüsten.

Das einzige offene UNKLAR (E10) betrifft Laufzeitverhalten und ist bei allen drei Varianten identisch — kein Differenzierungsfaktor.
