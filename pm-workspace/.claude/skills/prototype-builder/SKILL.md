---
allowed-tools: Read, Write
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`- und `Write`-Tools. Keine MCP-Tools.

# Referenz: Prototyp bauen

## Was ein Prototyp ist

Eine lauffähige Streamlit-App, die alle UI-Komponenten der Spec implementiert. Startbar mit `streamlit run`. Keine Placeholder, keine TODOs.

## Input

- `output/spec-eval/spec.md` und die darin referenzierten Datendateien

## Qualitätskriterien

- Startet ohne Fehler mit `streamlit run [pfad]/app.py`
- Alle UI-Komponenten aus der Spec sind implementiert
- Daten werden aus der echten Datendatei gelesen — keine hardcodierten Inhalte
- Sonderfälle behandelt (z.B. leerer Filter → Hinweis statt leere Tabelle)
- Imports vollständig
- Kompatibel mit Python 3.8+ und streamlit >= 1.0
- Nur streamlit + pandas. Kein matplotlib, kein plotly, kein altair. Für Diagramme: `st.bar_chart`, `st.line_chart` etc.

## Output

`output/prototyping/app.py`
