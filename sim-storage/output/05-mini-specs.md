# Mini-Specs: Walking Skeleton Meilenstein

## Spec 1: Inverter↔BMS CAN-Handshake (STOR-3)

### Zweck
Inverter und BMS können über CAN-Bus kommunizieren und tauschen Live-Messpunkte aus (Spannung, Strom, SoC). Dies ist die Grundlage für alle weiteren Battery-Integration. Noch ohne Lade-/Entladestrategie-Optimierung.

### Nutzer
- **Firmware-Entwickler:** Implementiert CAN-Stack und BMS-Parser  
- **Labortest-Team:** Validiert Handshake mit Sample-Hardware  
- **Systeme/Architektur:** Überwacht Protokoll-Compliance, gibt Code-Reviews

### Daten-Input
- BMS-Profil (aus STOR-2 "BMS-Protokoll neuer Batterie evaluieren") — konkret:
  - CAN-ICD v3: Nachrichtenformat (ID, Länge, Byteordnung, Cycle-Time)
  - BMS-spezifische Register: Zellenspannung, Temperatur, Fehler-Flags
  - Sample-Hardware: Batterie-Management-System mit CAN-Schnittstelle
- Bestehender Inverter-Firmware-Code: Battery Adapter Layer v0 (Design aus Systems/Arch)

### Deliverables / Akzeptanzkriterien
1. **CAN-Stack implementiert:** Handshake-Nachricht sendet Inverter → BMS und parst BMS-Response (Zykluszeit ≤ 100ms)
2. **3 Standard-Messpunkte transmittiert:** 
   - Batterie-Spannung (V), Auflösung ±0,1V, Genauigkeit Lab-validiert gegen Multimeter
   - Strom (A, positiv=Laden), Auflösung ±0,5A
   - State of Charge (SoC, %), aus BMS-Register gelesen, nicht berechnet
3. **Lab-Validierung bestanden:**
   - CAN-Bus läuft fehlerfrei über 10 Min mit Sample-Hardware
   - Keine Lost-Frames oder CRC-Fehler
   - Spannungs-/Stromwerte = Referenzmessung ±5%
4. **Code-Review durch Systems/Architecture:** Adapter-Layer-Integration ist D.R.Y., keine Duplizierung mit bestehenden BMS-Treibern
5. **Dokumentation:** 1-seitige Integration Guide für nächsten Zelltyp (kein umfassendes Manual, aber Ramp-up-Pfad klar)

### Teamabhängigkeiten (explizit)

| Abhängigkeit | Lieferndes Team | Lieferndes Item | Empfangendes Team | Blockierend? | Kritisch? |
|---|---|---|---|---|---|
| BMS-Protokoll-Definition | Systems/Architecture | STOR-2 Design Output (CAN-ICD) | Firmware | JA | JA |
| Battery Adapter Layer v0 Design | Systems/Architecture | Architektur-Design (kein Code) | Firmware | JA | JA |
| Sample-Hardware Test-Setup | Test & Certification | Bench-Rig (Batterie + Wiring) | Firmware | MITTEL | JA |
| Lab-Validierung mit Messpunkten | Test & Certification | 1–2W Bench-Zeit | Firmware | JA (für Abnahme) | MITTEL |
| Code-Review Adapter-Layer | Systems/Architecture | Review-Stunden (~8h) | Firmware | MITTEL | NEIN |

**Blockierungs-Szenario:** Wenn Systems/Architecture BMS-Protokoll-Definition verzögert (STOR-2 Design), startet Firmware erst 5–7 Tage später. Sample-Hardware-Verzug = +8–10W Gesamtslip.

### Offene Fragen
1. Ist die BMS-Spezifikation vom Lieferant komplett? (Prüfpunkt: STOR-2 Definition Done)
2. Thermisches Verhalten des neuen Zelltyps — brauchen wir spezielle CAN-Register für Temperatur-Alarm?
3. Sollte OTA-Update-Fähigkeit für CAN-Stack in dieser Spec enthalten sein? → Nein, das ist STOR-8 (Spike).

---

## Spec 2: SoC/SoH-Schätzung für neuen Zelltyp anpassen (STOR-4)

### Zweck
Inverter-Firmware kann SoC (State of Charge) und SoH (State of Health) für den neuen Zelltyp präzise schätzen. Dies ist Voraussetzung für:
- Lade-/Entladestrategie-Tuning (richtige Lebensdauer-Balance)
- Feldtest-Datenqualität (falsche SoC → missinterpretierte Fehler)
- Garantie-Tracking (SoH-Degradation über 6W Feldtest messen)

Noch ohne Ramp-up-Optimierung oder Kundentraining — nur Algorithmus + Hardware-in-the-Loop-Validierung.

### Nutzer
- **Firmware-Entwickler:** Kalibiert SoC/SoH-Algorithmus für neue Zellchemie  
- **Hardware-in-the-Loop Test-Rig:** Simuliert Lade-/Entlade-Zyklen, verifiziert Algorithmus-Genauigkeit  
- **Cloud/App-Team:** Erhält SoC/SoH-Werte über MQTT/BLE, zeigt sie im Dashboard

### Daten-Input
- Zelltyp-Datenblatt (von STOR-2):
  - Nennkapazität (Ah), Nominal-Spannung (V), Chemie (LFP/NCA/etc.)
  - Spannungs-Kurven über SoC-Bereich (Lade- + Entladekurven)
  - Temperatur-Abhängigkeit, Alterungskurve (Kapazitäts-Degradation über 5000 Zyklen)
- Bestehendes SoC/SoH-Modell aus V2 (Code-Basis, Kalman-Filter o.ä.)
- Hardware-in-the-Loop Rig: Batterie-Simulator + Wechselrichter-Prototyp + Spannungs-/Temperatur-Logger

### Deliverables / Akzeptanzkriterien
1. **SoC-Algorithmus kalibriert:**
   - Konvertiert BMS-Spannung (V) + Strom (A) → SoC (%), Model-Typ: Kalman-Filter oder OCV-Lookup
   - Genauigkeit: ±3% SoC nach 100 simulierte Lade-/Entlade-Zyklen in HiL (tolerant für Feldtest, nicht für Bilanz-Optimierung)
2. **SoH-Algorithmus implementiert:**
   - Schätzt Kapazitäts-Degradation basierend auf Zellalterung (Cycle-Count + Temperatur-History)
   - Startwert: 100%, degradiert nach Datenblatt-Kurve
   - Feldtest-Gate: Nach 6W Betrieb sollte SoH-Trend ≤ 2% Degradation zeigen (oder Alarm)
3. **Hardware-in-the-Loop Validierung:**
   - 10 simulierte Lade-/Entlade-Zyklen (0%→100% und zurück), je mit 3 Temperatur-Profile (10°C, 25°C, 40°C)
   - SoC-Fehler gemessen gegen referenzierten Coulomb-Counter: max. ±2% nach Zyklus
   - SoH-Trend-Korrektheit: Degradation-Kurve entspricht Datenblatt ±10%
4. **OTA-ready:** Algorithmus-Parameter sind in Over-The-Air-Update-Paket versioniert, nicht fest im Code (Vorbereitung für schnelle Feld-Tuning)
5. **Cloud-Integration:** SoC/SoH-Werte werden über Standard-Telemetrie-Schema an Cloud gesendet (siehe STOR-5)

### Teamabhängigkeiten (explizit)

| Abhängigkeit | Lieferndes Team | Lieferndes Item | Empfangendes Team | Blockierend? | Kritisch? |
|---|---|---|---|---|---|
| Zelltyp-Datenblatt + Spannungskurven | Systems/Architecture (via Lieferant) | STOR-2 Output: Zelltyp-Charakterisierung | Firmware | JA | JA |
| Walking-Skeleton-Gate bestanden | Test & Certification | STOR-3 Lab-Validierung abgeschlossen | Firmware | MITTEL | JA |
| Hardware-in-the-Loop Rig verfügbar | Test & Certification | HiL-Simulator (Batterie-Emulator + Rig-Setup) | Firmware | JA | JA |
| Cloud-Telemetrie-Schema Spezifikation | Cloud & App | STOR-5 Input (SoC/SoH-Felder definiert) | Firmware | MITTEL | MITTEL |
| Code-Review Kalman-Filter / Algorithmus | Systems/Architecture | Review-Stunden (~12h) | Firmware | MITTEL | NEIN |

**Blockierungs-Szenario:** Wenn HiL-Rig nicht rechtzeitig verfügbar (Test & Cert überlastet), verzögert sich Firmware-Validierung um ~2–3W. Walking-Skeleton-Gate blockiert nicht, aber verzögert MS2 Start (Feldtest braucht STOR-4 abgeschlossen).

### Offene Fragen
1. Welche SoC/SoH-Modellierung ist gewünscht? Einfacher OCV-Lookup (schnell, aber weniger präzise) oder Kalman-Filter (präziser, höherer Aufwand)? → Entscheidung mit Systems/Architecture in kickoff.
2. Ist 3% SoC-Genauigkeit ausreichend für Feldtest, oder brauchen wir ±2% für Lade-Strategie-Tuning? → Abhängig von MS2-Lernzielen.
3. Sollte temperaturabhängige Kalibration (20°C vs. 40°C) in diese Spec gehören, oder gehört das zu „Lade-/Entladestrategie-Tuning"? → Gehört zu STOR-4, nicht zu späteren Tasks.
4. Ist Cloud-Telemetrie-Schema (STOR-5) rechtzeitig verfügbar? → Must-have nach Walking Skeleton, idealerweise parallel.

---

## Teamabhängigkeits-Matrix (beide Specs zusammen)

```
STOR-2 (BMS-Protokoll evaluieren)
├─ liefert: Zelltyp-Datenblatt, CAN-ICD, BMS-Sample
├─ blockiert: STOR-3 (Handshake Design) + STOR-4 (Algorithmus-Kalibrierung)
└─ lieferndes Team: Systems/Architecture (mit Lieferant-Evaluation)

         ↓ (Gate: BMS-Protokoll bestätigt)

STOR-3 (CAN-Handshake, Firmware)
├─ abhängig von: STOR-2 + Systems/Architecture Design + Test Setup
├─ liefert: Walking-Skeleton-Validierung, Adapter-Layer-Integrationspfad
├─ blockiert: Test & Certification (Lab-Validierung), indirekt STOR-4 (HiL braucht funktionierende BMS-Integration)
└─ lieferndes Team: Firmware (3–4 Personen, mit Storage-Platform-Ramp-up)

         ↓ (Gate: CAN-Handshake laborbestätigt)

STOR-4 (SoC/SoH-Schätzung, Firmware)
├─ abhängig von: STOR-2 (Datenblatt) + STOR-3 (Handshake funktioniert) + Test (HiL-Rig)
├─ liefert: SoC/SoH-Werte → Cloud-Telemetrie (STOR-5)
├─ blockiert: Feldtest (MS2 kann nicht starten ohne SoC/SoH)
└─ lieferndes Team: Firmware (2–3 Personen, parallel mit Cloud/App auf STOR-5/7)

         ↓ (Gate: SoC/SoH HiL-validiert)

STOR-5 + STOR-7 (Cloud-Telemetrie + App Onboarding, parallel)
├─ abhängig von: Adapter-Layer-Design (aus STOR-3) + SoC/SoH-Werte (STOR-4)
├─ liefert: Cloud-Schema, App-UI
└─ lieferndes Team: Cloud & App (2–3 Personen)

         ↓ (alle drei parallel)

Feldtest (MS2) startet wenn: STOR-3 + STOR-4 + STOR-5/7 + Test-Standorte verfügbar
├─ Firmware liefert: OTA-Paket mit CAN-Handshake + SoC/SoH
├─ Cloud liefert: Telemetrie-Erfassung + Dashboard
└─ Test liefert: Feldtest-Planung + Datensammlung (6W Betrieb)
```

---

## Kritische Engpässe (aus Roadmap, konkretisiert auf Mini-Specs)

### Engpass 1: Systems/Architecture (2 Personen)
- **STOR-2 Input:** BMS-Protokoll-Evaluation + Lieferant-Spezifikation (3–5W)
- **STOR-3 Input:** CAN-Protokoll-Design + Adapter-Layer v0 (2–3W, Code-Review parallel)
- **STOR-4 Input:** Datenblatt-Interpretation (1W, Code-Review parallel)
- **Parallel-Konflikt:** INV-Gen3-Rollout läuft noch, Architektur-Team ist zu 40% gebunden
- **Mitigation:** 10h/Woche explicitly blocken für diese Task, nicht ad-hoc.

### Engpass 2: Test & Certification (effektiv 1–2 Personen auf Walking Skeleton)
- **STOR-2 Input:** BMS-Sample-Lieferung (externe Lead-Zeit ~8–10W)
- **STOR-3 Gate:** Labor-Validierung (1–2W, parallel mit Firmware)
- **STOR-4 Input:** HiL-Rig-Verfügbarkeit und Betrieb (2–3W)
- **Parallel-Konflikt:** INV-Gen3-Zertifizierung bindet 2–3 Personen bis Q4
- **Mitigation:** Expliziter Slot nach G1 (Walking Skeleton Gate): Sind 2 Personen für Feldtest verfügbar, oder nicht?

### Engpass 3: Firmware (eingeschränkt durch Storage-Platform-Gründung)
- **STOR-3:** Braucht BMS-Design (STOR-2) + Adapter-Layer-Design (Systems/Arch), dann 3–4W Implementation
- **STOR-4:** Braucht SoC/SoH-Kalibrierung + HiL-Tests, dann 3–4W (parallel mit STOR-3, nicht sequenziell)
- **Parallel-Konflikt:** Neues Storage-Platform-Team (zieht 2 Firmware-Personen ab), Onboarding bis Woche 4 nicht produktiv
- **Mitigation:** Experienced Firmware-Leads auf STOR-3/STOR-4, neue Team-Members shadowing.

---

## Fazit: Nachverfolgung nach Fertigstellung

Nach STOR-3 und STOR-4 abgeschlossen (Gate am Ende MS1):
1. **Code-Quality:** Adapter-Layer-Review bestanden? Duplikation mit V2-Code?
2. **Feldtest-Readiness:** Sind HiL-Test-Results credible genug für Feldtest-Start, oder brauchen wir zusätzliche Bench-Validierung?
3. **Team-Produktivität:** Ist Storage-Platform-Team produktiv? Firmware-Kapazität für STOR-5/7 verfügbar?
4. **Supplier-Realität:** BMS-Sample da? Zelltyp-Datenblatt vollständig?

Wenn alle Antworten "Ja", kann MS2 (Feldtest) kicken. Wenn nicht, verzögert sich Roadmap (besser: ehrlich akzeptieren, nicht hoffen).
