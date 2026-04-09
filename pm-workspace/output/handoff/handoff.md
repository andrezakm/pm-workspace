# Handoff: Feature Backlog Prioritizer

**Datum:** 2026-04-09
**Status:** Bereit für Entwicklung

## Zusammenfassung

Eine lokale Streamlit-App die eine Backlog-CSV einliest, Features nach gewichtetem Score berechnet und visualisiert — filterbar nach Status und Strategischem Fit, sortierbar nach Score.

---

## Artefakte

| Dokument | Pfad | Status |
|----------|------|--------|
| Spec | output/spec-eval/spec.md | ✅ |
| Eval (PM) | output/spec-eval/eval.md | ✅ |
| Prototyp Option A | output/prototyping/option-a/app.py | ✅ |
| Prototyp Option B | output/prototyping/option-b/app.py | ✅ |
| Prototyp Option C | output/prototyping/option-c/app.py | ✅ |
| Prototyp-Vergleich | output/prototyping/option-comparison.md | ✅ |
| Eval-Ergebnisse | output/prototyping/eval-results.md | ✅ |
| Decision Brief | output/strategy/decision-brief.md | ✅ |

---

## Was Dev als nächstes tun soll

1. **Prototyp-Variante wählen:** Option A und B sind spec-konform (je 11/12 PASS). Empfehlung aus dem Vergleich: **Option B** als Basis (Chart-first + Drill-down), mit Top-3-Kacheln aus Option C als erstem Block einbauen — siehe `output/prototyping/option-comparison.md`.

2. **Datenpfad klären:** Die Apps verwenden als Standardpfad `input/case/data/backlog.csv`. Vor Deployment klären wo die CSV in der Zielumgebung liegt und ob der Standardpfad angepasst werden muss.

3. **Beschreibungsfeld einbauen:** Option B zeigt `beschreibung` bereits im Detail-Panel — sicherstellen dass das Feld aus der CSV korrekt eingelesen und vollständig angezeigt wird.

4. **E10 verifizieren (Laufzeit):** `streamlit run app.py` muss ohne weitere Installationsschritte außer `pip install streamlit pandas` funktionieren. Vom PM nicht testbar, von Dev zu bestätigen.

5. **Edge Cases absichern:** Leerer Filter zeigt bereits eine Warning — prüfen ob weitere Edge Cases aus der CSV entstehen können (fehlende Werte in `strategischer_fit` oder `aufwand`, unbekannte Strings die nicht in den Maps stehen).

---

## PM-Eval vs. Dev-Eval

**PM hat geprüft (via `output/spec-eval/eval.md`):**
Funktionale Korrektheit aus dem Code: Score-Formel (E2 nachgerechnet), Filter-Logik (E4–E6), Sortierung (E3, E8), Datei-Handling (E1, E9, E12), Formel-Sichtbarkeit (E11). Alle 12 Kriterien wurden gegen alle drei Prototypen geprüft.

**Dev soll ergänzen:**
- Laufzeitverhalten (E10): startet der Browser, gibt es Timing-Probleme beim CSV-Laden?
- Performance bei größeren CSVs (>100 Einträge) — kein `@st.cache_data` per Spec, bewusste Entscheidung aber Auswirkung prüfen
- Encoding der CSV (UTF-8 mit Umlauten in Feature-Namen und Beschreibungen)
- Responsiveness im Browser bei unterschiedlichen Fenstergrößen
- Verhalten wenn CSV-Felder leer oder fehlerhaft sind (NaN in `kundenwunsche`)

---

## Offene Fragen & Risiken

*(Aus `output/strategy/decision-brief.md` und `output/prototyping/eval-results.md`)*

- **Datenpfad in Produktionsumgebung:** Wer pflegt die CSV, wo liegt sie, und wie wird der Pfad beim Start konfiguriert — Sidebar-Input reicht das, oder braucht es ein CLI-Argument?
- **Option-C-Inspiration:** Falls die Top-3-Kacheln aus Option C eingebaut werden sollen, muss die Spec entsprechend erweitert werden — aktuell ist das kein definiertes Kriterium in der Eval.
- **Encoding:** `backlog.csv` enthält deutsche Umlaute in Beschreibungen — `pd.read_csv()` ohne explizites `encoding`-Argument kann auf manchen Systemen fehlschlagen. Dev soll `encoding="utf-8"` explizit setzen.
