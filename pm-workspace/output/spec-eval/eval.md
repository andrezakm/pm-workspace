# Eval: Feature Backlog Prioritizer

## Anleitung
PASS = Bedingung ist erfüllt. FAIL = nicht erfüllt. UNKLAR = nicht aus Code oder Output entscheidbar.

## Kriterien

| ID | Kriterium | Wie testen | Pass-Bedingung | Ergebnis |
|----|-----------|------------|----------------|----------|
| E1 | CSV wird eingelesen | App mit `backlog.csv` starten | Alle 12 Features erscheinen in der Tabelle, kein Fehler beim Start | |
| E2 | Score-Formel korrekt implementiert | Score von Feature 3 (Meeting-Zusammenfassung) manuell berechnen: (6×0.5) + (3×0.3) + (4×0.2) = 3.0 + 0.9 + 0.8 = 4.7 | App zeigt für Feature 3 exakt 4.7 (oder gerundeten Äquivalent) | |
| E3 | Tabelle ist nach Score sortiert | App starten ohne Filter | Zeile mit höchstem Score steht oben, niedrigstem Score unten | |
| E4 | Status-Filter funktioniert | Filter auf "geplant" setzen | Nur Features 2 und 8 sichtbar, alle anderen ausgeblendet | |
| E5 | Strategischer-Fit-Filter funktioniert | Filter auf "niedrig" setzen | Nur Features 10 und 12 sichtbar | |
| E6 | Kombinierte Filter funktionieren | Status = "backlog", Fit = "hoch" setzen | Nur Features 1, 7, 8 sichtbar (backlog + hoch) — Feature 8 ist "geplant", also nur 1 und 7 | |
| E7 | Balkendiagramm zeigt alle gefilterten Features | Status-Filter auf "idee" setzen | Diagramm zeigt genau 7 Balken (Features 4, 5, 6, 9, 10, 11, 12) mit Feature-Namen auf Y-Achse | |
| E8 | Balkendiagramm ist nach Score sortiert | Diagramm ohne Filter betrachten | Balken sind absteigend nach Score geordnet, längster Balken oben | |
| E9 | CSV wird nur gelesen, nie geschrieben | Nach Nutzung der App `backlog.csv` prüfen | Dateigröße und Inhalt identisch mit Original, Timestamp unverändert | |
| E10 | App startet mit einem Befehl | `streamlit run app.py` im Terminal ausführen | App öffnet sich im Browser ohne weitere manuelle Schritte | |
| E11 | Scoring-Formel ist in der UI sichtbar | App öffnen, keine Interaktion | Formel oder Gewichtung (0.5 / 0.3 / 0.2) ist irgendwo in der UI lesbar dargestellt | |
| E12 | CSV-Pfad ist konfigurierbar | App mit alternativem Pfad starten (z.B. `backlog_test.csv`) | App liest die angegebene Datei statt Standardpfad — oder zeigt ein Eingabefeld für den Pfad | |
