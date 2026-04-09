# Eval: Feature Backlog Prioritizer

## Anleitung
PASS = Bedingung erfüllt. FAIL = nicht erfüllt. UNKLAR = nicht aus Code entscheidbar.

## Kriterien

| ID | Kriterium | Wie testen | Pass-Bedingung | Ergebnis |
|----|-----------|------------|----------------|----------|
| E1 | CSV einlesen | App mit backlog.csv starten | Alle 12 Features in Tabelle, kein Fehler | |
| E2 | Score-Formel korrekt | Feature 3 manuell: (6×0.5)+(3×0.3)+(4×0.2)=4.7 | App zeigt 4.7 für Feature 3 | |
| E3 | Tabelle nach Score sortiert | App ohne Filter öffnen | Höchster Score steht oben | |
| E4 | Status-Filter | Filter auf "geplant" | Nur Features 2 und 8 sichtbar | |
| E5 | Fit-Filter | Filter auf "niedrig" | Nur Features 10 und 12 sichtbar | |
| E6 | Kombinierte Filter | Status=backlog + Fit=hoch | Nur Features 1 und 7 sichtbar | |
| E7 | Balkendiagramm zeigt gefilterte Features | Status auf "idee" | Genau 7 Balken (Features 4,5,6,9,10,11,12) | |
| E8 | Balkendiagramm nach Score sortiert | Diagramm ohne Filter | Balken absteigend, längster oben | |
| E9 | CSV nicht geschrieben | backlog.csv nach Nutzung prüfen | Inhalt und Timestamp unverändert | |
| E10 | Ein-Befehl-Start | streamlit run app.py | App öffnet im Browser ohne weitere Schritte | |
| E11 | Formel in UI sichtbar | App öffnen, keine Interaktion | Gewichte 0.5/0.3/0.2 irgendwo lesbar | |
| E12 | CSV-Pfad konfigurierbar | Alternativen Pfad eingeben | App liest angegebene Datei | |
