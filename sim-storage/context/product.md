# Product — Reference Architecture

## Technical Capabilities (bestehend)
- **Power Electronics**: Wechselrichter-Plattform (3–10 kW), MPPT, Netz-Synchronisation
- **Battery Management**: BMS-Schnittstelle (CAN), SoC/SoH-Schätzung, Lade-/Entladestrategie
- **Embedded Firmware**: Echtzeit-Regelung, „Battery Adapter Layer" (abstrahiert Zellchemie), OTA-Update
- **Connectivity**: Gateway → Cloud (MQTT), lokale App (BLE)
- **Cloud Platform**: Telemetrie, Monitoring, Remote-Konfiguration, Garantie-Tracking

## Business Capabilities
- Produktzertifizierung (Grid-Codes je Markt)
- Garantieabwicklung, Installateur-Onboarding
- After-Sales-Monitoring, Ersatzteil- und Service-Logistik

## Hinweis zur neuen Variante
Neue Speichervariante = neue Batterie (anderer Zelltyp/Hersteller, anderes BMS-Protokoll)
+ passender Hybrid-Wechselrichter. Muss in obige Capabilities integrieren — primär über
den Battery Adapter Layer und das Telemetrie-Schema.
