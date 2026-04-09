# Handoff: Feature Backlog Prioritizer

**Datum:** 2026-04-09
**Status:** Bereit für Entwicklung

## Zusammenfassung

Eine lokale Streamlit-App die eine Backlog-CSV einliest, Features nach gewichtetem Score berechnet und visualisiert — filterbar nach Status und Strategischem Fit, sortierbar nach Score, mit konfigurierbarem CSV-Pfad.

---

## Artefakte

| Dokument | Pfad | Status |
|----------|------|--------|
| Spec | output/2026-04-09/spec-eval/spec.md | ✅ |
| Eval (PM) | output/2026-04-09/spec-eval/eval.md | ✅ |
| Prototyp Option A | output/2026-04-09/prototyping/option-a/app.py | ✅ |
| Prototyp Option B | output/2026-04-09/prototyping/option-b/app.py | ✅ |
| Prototyp Option C | output/2026-04-09/prototyping/option-c/app.py | ✅ |
| Prototyp-Vergleich | output/2026-04-09/prototyping/option-comparison.md | ✅ |
| Eval-Ergebnisse | output/2026-04-09/prototyping/eval-results.md | ✅ |
| Decision Brief | output/2026-04-09/strategy/decision-brief.md | ✅ |

---

## Was Dev als nächstes tun soll

1. **Variante wählen:** Option B als Basis (Chart-first + Drill-down, 11/12 PASS). Optional: Top-3-Kacheln aus Option C als ersten Block einbauen — dafür Spec um E7/E8-Alternative erweitern.
2. **Encoding ist behoben:** Alle drei Apps enthalten jetzt `encoding="utf-8"` in `pd.read_csv()` — war offener Punkt aus dem vorherigen Lauf.
3. **Datenpfad vor Deployment klären:** Standardpfad `input/case/data/backlog.csv` auf Zielumgebung anpassen.
4. **E10 verifizieren:** `streamlit run app.py` ohne weitere Installation außer `pip install streamlit pandas` bestätigen.
5. **Edge Cases prüfen:** NaN in `kundenwunsche`, unbekannte Strings in `strategischer_fit` oder `aufwand`.

---

## PM-Eval vs. Dev-Eval

**PM hat geprüft (via output/2026-04-09/spec-eval/eval.md):**
Score-Formel (E2 nachgerechnet), Filter-Logik (E4–E6), Sortierung (E3, E8), Datei-Handling (E1, E9, E12), Formel-Sichtbarkeit (E11). Alle 12 Kriterien gegen alle 3 Prototypen.

**Dev soll ergänzen:**
- Laufzeitverhalten E10: Browser-Start, Ladezeit
- Encoding auf Linux/Windows (utf-8 jetzt explizit, sollte stabil sein)
- Responsiveness bei verschiedenen Fenstergrößen
- Verhalten bei fehlerhaften CSV-Werten (NaN, leere Felder, unbekannte Kategorien)

---

## Offene Fragen & Risiken

*(Aus output/2026-04-09/strategy/decision-brief.md)*

- **Option-C-Kacheln als Erweiterung:** Falls gewünscht, muss Spec vor Dev-Start erweitert werden — sonst scheitert die Eval an E7/E8.
- **Content-Ownership (strategischer Kontext):** Der Decision Brief empfiehlt BUILD für Onboarding-Automatisierung. Wer schreibt die Einweisungstexte bleibt offen — betrifft dieses Tool nicht direkt, ist aber der zentrale Blocker für das übergeordnete Strategie-Ziel.
- **Kapazitätskollision:** PharmaCare wartet auf Compliance-Angebot parallel zu Onboarding-Experiment — Priorisierung muss ans Führungsteam eskaliert werden.
