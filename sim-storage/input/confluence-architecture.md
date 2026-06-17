# Confluence (Auszug): Storage Integration Guidelines

## Integrationsschnittstellen
- Jede neue Batterie muss das BMS-CAN-Profil implementieren (siehe BMS-ICD v3).
- Wechselrichter-Firmware abstrahiert Zellchemie über den „Battery Adapter Layer".
- Cloud erwartet Telemetrie im Standard-Schema; neue Felder nur via Schema-Version.

## Bewährte Reihenfolge (aus V2)
1. Adapter-Layer + CAN-Handshake (walking skeleton)
2. Lade-/Entladestrategie kalibrieren (Hardware-in-the-Loop)
3. Früher Feldtest (5–10 Geräte)
4. Zertifizierung + SOD

## Offene Punkte
- Neuer Zelltyp: thermisches Verhalten unklar → früh testen.
- OTA-Migrationspfad von V2-Geräten noch offen.
