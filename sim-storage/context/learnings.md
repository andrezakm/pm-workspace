# Learnings — vergangene Integrationen

## Speichervariante „V2" (vor 2 Jahren)
Vorgehen: walking skeleton (Inverter↔BMS-CAN-Handshake) zuerst, dann früher Feldtest
mit 5 Geräten, dann SOD. Aufwand: ~7 Monate, davon 2 Monate Verzug durch
BMS-Protokoll-Überraschungen.
**Learning:** BMS-Protokoll früh in Hardware-in-the-Loop testen, nicht erst im Feld.

## Wechselrichter-Refresh „INV-Gen3" (letztes Jahr)
Vorgehen: Grid-Code-Zertifizierung zu spät gestartet → 6 Wochen Launch-Verzug.
**Learning:** Zertifizierung parallel zum walking skeleton anstoßen, nicht danach.

## Muster
- Frühe Feldtests fangen ~80 % der Integrationsprobleme.
- Das Architektur-Team ist in jedem Projekt der Engpass.
- Aufwand neuer Variante bisher: 6–8 Monate bis SOD.
