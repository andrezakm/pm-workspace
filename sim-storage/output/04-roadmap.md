# Integrations-Roadmap: neue Speichervariante

## Übersicht

Bewährte Meilenstein-Sequenz aus V2 und INV-Gen3 mit expliziter Berücksichtigung der operativen Engpässe (Architektur, Firmware-Team-Reife, Feldtest-Kapazität) und realistischer Parallelisierung. **Warnung:** Diese Roadmap hängt davon ab, dass INV-Gen3-Zertifizierung nicht verzögert und das neue Storage-Platform-Team in Ramp-up-Phase absorbiert wird — beide sind volatil.

---

## Meilenstein 1: Walking Skeleton  
**Ziel:** Inverter und BMS können über CAN-Handshake kommunizieren und tauschen Live-Messpunkte aus (Spannung, Strom, SoC) aus, noch ohne Lade-/Entladestrategie-Optimierung.

### Abhängige Backlog-Items (JIRA)
- **STOR-2** (8d): BMS-Protokoll neuer Batterie evaluieren — muss *vor* Handshake abgeschlossen sein
- **STOR-3** (10d): Inverter-BMS CAN-Handshake (walking skeleton) — Kern-Deliverable
- **STOR-8** (4d): OTA-Kompatibilität prüfen — parallel mit STOR-3, Input für zukünftige OTA-Rollouts

### Beteiligte Teams & Abhängigkeiten
| Team | Reihenfolge | Rolle | Blockierend für wen |
|---|---|---|---|
| **Systems/Architecture** (2) | 1 | CAN-Protokoll-Architektur finalisieren, Battery Adapter Layer v0.1 designen | Firmware, später Cloud |
| **Embedded Firmware** (3–4*) | 2 | CAN-Stack implementieren, BMS-Protokoll-Parser, Adapter-Layer-Integration | Test, Walking-Skeleton-Validierung |
| **Test & Certification** (1–2**) | 3 | Lab-Validierung: CAN-Handshake mit Sample-Hardware, Spannung/Strom-Genauigkeit | — |

*Firmware verliert 2–3 zu Storage-Platform, neu ~3–4 auf dieser Task.  
**Test blockiert durch INV-Gen3-Zertifizierung (3 Personen, 6+ Wochen laufen noch). Realistische Verfügbarkeit: 1–2 Personen.

### Learning aus Altprojekten (angewendet)
- **V2-Learning:** „BMS-Protokoll früh in Hardware-in-the-Loop testen, nicht erst im Feld" → STOR-2 + Labor-Validierung von STOR-3 sind sequenziell, nicht parallel; keine Firmware-Commits bis BMS-Protokoll validiert.
- **INV-Gen3-Learning:** „Zertifizierung parallel anstoßen" → Grid-Code-Vorbereitung (STOR-6) startet in diesem Meilenstein, nicht danach (siehe MS 2).

### Aufwands-Schätzung (qualitativ)
- **Architektur:** 2–3 Wochen (Design + Review, Engpass = 2 Personen)
- **Firmware:** 3–4 Wochen (Implementation + Debug, Engpass = eingeschränkte Kapazität durch Storage-Platform-Gründung)
- **Test (Lab):** 1–2 Wochen (parallel mit Firmware, aber BMS-Sample muss vorher da sein → +8W Lieferant-Lead-Time vor allem kann starten)
- **Kritischer Pfad:** STOR-2 (BMS-Eval) → Lieferant-Sample verfügbar → Architektur-Design → Firmware-Impl → Lab-Val  
  **Realistische Dauer bis zum Meilenstein abgeschlossen:** 6–8 Wochen nach Kickoff (nicht 3W!) — wenn Lieferant-Sample schon verfügbar. Wenn Sample noch bestellt: +8–10W.

### Risiken & Mitigationen
- **Lieferant-Sample-Delay:** BMS-Spezifikation kann unvollständig sein → frühes Eskalations-Gate mit Lieferant (Definition Done für STOR-2: „BMS hat alle Parameter dokumentiert, Sample getestet").
- **Architektur-Engpass:** 2 Personen, parallel zu INV-Gen3-Rollout + Storage-Platform-Gründung. Mitigation: Explizite 10h/Woche für diese Task blocken, nicht „ad-hoc".
- **Firmware-Ramp-up:** Neues Storage-Platform-Team ist in Wochen 1–4 nicht produktiv (Onboarding). Mitigation: Existing-Firmware-Leads auf Task, neue Team-Members shadowing.

---

## Meilenstein 2: Früher Feldtest  
**Ziel:** 5–10 Geräte mit neuer Batterie laufen im Feld (Kundenstandorten) über mindestens 6 Wochen, sammeln Telemetrie und Fehlerverhalten, ohne dass Ramp-up-Prozesse oder Installateure-Training live sind.

### Abhängige Backlog-Items (JIRA)
- **STOR-4** (12d): SoC/SoH-Schätzung für neuen Zelltyp anpassen — muss *vor* Feldtest vorliegen (wenn nicht, Test ist bedeutungslos)
- **STOR-5** (6d): Cloud-Telemetrie erweitern — neue Batterie-Metriken (Zell-Spannung, Thermik) sichtbar machen
- **STOR-6** (15d): Grid-Code-Zertifizierung DE vorbereiten — läuft *parallel*, nicht sequenziell (INV-Gen3-Learning)
- **STOR-7** (5d): App-Onboarding für neue Variante — wird benötigt, wenn Feldtests über lokale App konfiguriert werden

### Beteiligte Teams & Abhängigkeiten
| Team | Reihenfolge | Rolle | Blockierend für wen |
|---|---|---|---|
| **Embedded Firmware** (3–4) | 1 | SoC/SoH-Algorithmus für neuen Zelltyp, Lade-/Entladestrategie-Tuning (Hardware-in-the-Loop), OTA-Paket für Feldgeräte | Test & Certification, Cloud |
| **Cloud & App** (2–3) | 2 | Telemetrie-Schema erweitern, neue Metriken erfassen, Onboarding-Flow für App | Feldtest-Betrieb |
| **Test & Certification** (2–3***) | 3 | Feldtest-Planung (Kundenstandorte, Messpunkte), Hardware-Deployment, Datensammlung, Grid-Code-Tests im Parallelstrom | — |
| **Systems/Architecture** (1–2) | 4 (Support) | Code-Review für Adapter-Layer-Erweiterungen, Schema-Versionierung validieren | Keine Blockade, aber Engpass-Abhängigkeit |

***Test ist STARK limitiert: INV-Gen3-Zertifizierung läuft noch, Feldtest-Kapazität ist das andere Engpass-Nadelöhr (5 Early-Adopter verfügbar? Gleichzeitig mit INV-Gen3-Rollout DE/AT?). Realistisch: 2 Personen auf Feldtest, nicht 3.

### Parallelisierung & Abhängigkeits-Logik
```
Walking Skeleton bestanden → Architektur-Gate bestätigt
  ├─ Firmware: STOR-4 (SoC/SoH) läuft, Lade-/Entladestrategie-Tuning startet
  │  (benötigt Hardware-in-the-Loop; Test bereitgestellt)
  │
  ├─ Cloud: STOR-5 (Telemetrie) + STOR-7 (App) können parallel starten
  │  (benötigen Adapter-Layer-Signatur aus MS1, nicht Code-fertig)
  │
  ├─ Test & Certification: STOR-6 (Grid-Code-Vorbereitung)
  │  = Zertifizierungs-Unterlagen, nicht Hardware-Test
  │  (läuft unabhängig, aber benötigt später Hardware für Audit)
  │
  └─ Feldtest-Standorte absichern (Lead-Zeit 4–6 Wochen für Kundenverträge)
```

### Learning aus Altprojekten (angewendet)
- **V2-Learning:** „Frühe Feldtests fangen ~80% der Integrationsprobleme" → Feldtest läuft früh, aber **mit Hardware-in-the-Loop als Gate davor** (nicht ohne).
- **V2-Learning:** „+2M Verzug durch BMS-Protokoll-Überraschungen" → Thermisches Verhalten neuer Zelltyp ist *vor* Feldtest in simulierten HiL-Tests validiert.
- **INV-Gen3-Learning:** Zertifizierung läuft parallel, nicht danach → STOR-6 ist ein Parallelstrom, nicht eine Blockade für Feldtest-Start. Das spart ~6 Wochen später.

### Aufwands-Schätzung (qualitativ)
- **Firmware:** 3–4 Wochen (SoC/SoH + Lade-/Entladestrategie, dann HiL-Validierung)
- **Cloud & App:** 2–3 Wochen (parallel mit Firmware, benötigt nur Schema-Spezifikation von Architektur)
- **Test (Feldtest-Planung):** 2–3 Wochen (Kundenverträge, Messpunkte designen, HiL-Rig setup)
- **Test (Feldtest-Betrieb):** 6+ Wochen (läuft konstant, Firmware debuggt parallel basierend auf Daten)
- **Test (Grid-Code):** 4–6 Wochen (parallel mit Feldtest, aber Auditor braucht Real-Hardware + Test-Reports am Ende)
- **Kritischer Pfad:** Firmware STOR-4 → HiL-Tests bestanden → Feldtest-Deployment → 6W Betrieb → Daten-Auswertung  
  **Realistische Dauer Meilenstein:** 8–10 Wochen (parallel: STOR-6 läuft mit). **Abhängigkeit:** Feldtest-Standorte müssen *verfügbar* sein — das ist nicht garantiert, wenn INV-Gen3-Rollout DE/AT diese Kunden bindet.

### Risiken & Mitigationen
- **Feldtest-Kapazität-Konflikt (KRITISCH):** Test & Certification (3) sind mit INV-Gen3-Zertifizierung vollgelastet bis Q4. Feldtest für neue Batterie konkurriert um denselben Team. Mitigation: Explizites Go/No-Go Gate nach Walking Skeleton: „Sind 2 dedizierte Persons für Feldtest bis Monat X verfügbar, oder schieben wir auf Q1?". *Das ist keine theoretische Frage, das ist eine operative Gate.*
- **Zelltyp-Thermik unbekannt:** Neuer Zelltyp (LG/Huawei/BYD?) hat andere thermale Charakter als V2. HiL kann das nicht vollständig abbilden. Mitigation: Feldtest mit Temperatur-Logging, Firmware hat aggressive Thermal-Throttling (lieber sicher als schnell).
- **OTA-Migrationspfad offen:** Wenn alte V2-Geräte auf neue Batterie upzuswitchen wollen, muss OTA-Update backward-compatible sein. STOR-8 testet das nur per Bench, nicht im Feld. Entscheidung: Ist das im Scope von diesem Meilenstein, oder separate Epic?

---

## Meilenstein 3: Start of Development (SOD)  
**Ziel:** Feldtest-Learnings sind in Code/Specs eingebunden, Zertifizierung ist bestanden oder in Audit (final Stage), neuer Installer-Onboarding-Flow ist definiert, Team ist ready für scaled Produktion.

### Abhängige Backlog-Items (JIRA)
Alle bisherigen + explizite SOD-Items:
- **STOR-3, STOR-4, STOR-5, STOR-7** bereits in Production
- **STOR-6** bestanden (Grid-Code-Zertifikat da oder Audit-Phase)
- **Keine neuen Items in dieser Roadmap**, aber vorbereitete Epics (siehe unten)

### Beteiligte Teams & Abhängigkeiten
| Team | Reihenfolge | Rolle | Blockierend für wen |
|---|---|---|---|
| **Embedded Firmware** (3–4) | 1 | Feldtest-Fixes integrieren, Code-Review, Release-Kandidat bauen | Zertifizierung, Launch |
| **Cloud & App** (4) | 2 | Analytics-Dashboard für neue Batterie-Metriken, Support-Tools, Garantie-Tracking-Update | Launch, Support |
| **Test & Certification** (3) | 3 | Zertifizierungs-Abschluss (Audit-Reports), Label-Approval, Markt-Readiness-Check | Launch-Gate |
| **Systems/Architecture** (2) | 4 (Support) | Final Reference-Architecture Update (Battery Adapter Layer finalisieren), Documentation | Installer-Training |
| **Storage-Platform-Team** (neue ~3) | 5 | Installer-Onboarding-Playbook schreiben, Service-Docs, Ersatzteil-Management-Integration | Launch, Ramp-up |

### Parallelisierung & Abhängigkeits-Logik
```
Feldtest bestanden (6W Daten + keine CRITICALs) → Go-Gate
  ├─ Firmware: Feldtest-Fixes + Release-Kandidat (2–3W)
  │  → Test: Final Grid-Code-Audit (parallel, ~2W)
  │
  ├─ Cloud & App: Analytics + Support-Tools (2W, parallel)
  │  → Launch-Readiness-Check
  │
  ├─ Storage-Platform-Team: Installer-Training + Playbook (3–4W)
  │  → Abhängig von Firmware-Release + Zertifizierung, nicht davor
  │
  └─ Architecture: Final Docs + Schema-Freeze (1W)
```

### Learning aus Altprojekten (angewendet)
- **V2-Learning:** „Aufwand: 6–8 Monate bis SOD" → Diese Roadmap sitzt auf genau dieser Zeitleiste, aber **mit expliziten Gates für Engpässe**. Das heißt: 6–8 Monate *wenn* Feldtest-Kapazität verfügbar ist. Wenn nicht, +4–8 Wochen Slip.
- **INV-Gen3-Learning:** „Zertifizierung zu spät gestartet" → STOR-6 läuft ab MS2, nicht ab MS3. Das spart die +6 Wochen Launch-Verzug. 
- **Pattern:** „Das Architektur-Team ist Engpass" → Architecture sitzt in MS3 nur auf Support-Rollen. Architektur-Design war MS1, nicht hier. Das ist richtig strukturiert.

### Aufwands-Schätzung (qualitativ)
- **Firmware:** 2–3 Wochen (Feldtest-Fixes, Release-Kandidat, RC-Stabilisierung)
- **Cloud & App:** 2 Wochen (Analytics + Dashboard, Support-Features)
- **Test (Zertifizierungs-Abschluss):** 2–3 Wochen (Audit-Dokumentation, final Tests)
- **Storage-Platform:** 3–4 Wochen (Installer-Playbook, Training-Materials, Service-Docs)
- **Architecture:** 1 Woche (Dokumentation, Schema-Freeze)
- **Kritischer Pfad:** Firmware-Fixes → RC-Tests → Zertifizierungs-Audit → Launch-Gate  
  **Realistische Dauer Meilenstein:** 4–5 Wochen.

### Risiken & Mitigationen
- **Feldtest-Learnings sind CRITICAL:** Wenn Feldtest zB. thermale Probleme findet, die nicht in 2W zu fixen sind, verzögert sich SOD. Gate: „Feldtest muss MAJOR issues mit Lösung haben, nicht nur Beobachtungen."
- **Zertifizierungs-Audit kann stocken:** Auditor braucht Real-Hardware + vollständige Test-Reports + Firmware-Source. Mitigation: Audit-Dokumentation läuft parallel in MS2, nicht erst in MS3.
- **Storage-Platform-Team noch unreif:** Neues Team schreibt Installer-Playbook — das könnte bei noch eingeschränkter Reife mangelhaft sein. Mitigation: Architektur + 1 erfahrener Installer reviewen das.

---

## Engpass-Management: Architektur & Feldtest

### Der Problem-Zusammenhang (aus devils-advocate)
**Architektur (2 Personen):** Engpass über alle drei Meilensteine.  
- MS1: Battery Adapter Layer + CAN-Protokoll (5–8h/Woche)
- MS2: Code-Review + Schema-Versionierung (3–5h/Woche)
- MS3: Final Docs + Launch-Readiness (2h/Woche)
- **Parallelkonflikt:** INV-Gen3-Rollout DE/AT läuft noch in Q3–Q4. Wenn Zertifizierung verzögert, sind beide Monate des Teams weg.

**Feldtest-Kapazität:** Test & Certification (3) sind mit INV-Gen3-Zertifizierung belastet. Feldtest konkurriert um denselbe Ressource.  
- Realistische Verfügbarkeit: 2 Personen auf Feldtest (nicht 3).
- Feldtest-Standorte (Kundenverträge): knapp, weil Early-Adopter mit INV-Gen3-Rollout gebunden.
- **Entscheidung fällt hier:** Kann Feldtest in Q3 gestartet werden (braucht ~3–4 Monate parallel), oder schieben auf Q1 2027 (wenn INV-Gen3 stabil läuft)?

### Explizite Gates (Sicherung gegen Überlastung)

| Gate | Trigger | Bedingung für "Go" | "No-Go" Konsequenz |
|---|---|---|---|
| **G1: Architektur-Kapazität** | Nach MS1 Walking Skeleton bestanden | 2 Architekten haben +10h/Woche für MS2 verfügbar (INV-Gen3 verzögert nicht) | Pause bis Q1 2027 |
| **G2: Feldtest-Standorte** | Vor MS2 Feldtest-Start | Mindestens 5 Early-Adopter-Kundenverträge für 6W Feldtest + 2 dedizierte Personen aus Test & Cert | Feldtest-wegfall; Ramp-up mit reduzierten Daten (~30% Risiko-Erhöhung) |
| **G3: Firmware-Ramp-up** | Nach 4W Storage-Platform-Gründung (parallel mit MS1) | Storage-Platform-Team hat etablierte Code-Review-Prozesse + Onboarding-Docs + Lead-Shadow absolviert | Pause; Core-Firmware-Leads übernehmen Entwicklung (Kapazität-Hit) |
| **G4: Zertifizierungs-Realität** | Nach 6W Feldtest-Betrieb | Zertifizierungs-Audit kann Q4 abgeschlossen sein (STOR-6-Progress auf Track) | Verzug ins Q1; Launch-Timing ändert sich |

---

## Abhängigkeits-Matrix (Visualisierung)

```
┌─────────────────────────────────────────────────────────────────────┐
│ MS1: Walking Skeleton (6–8W gesamt, wenn Sample verfügbar)          │
├─────────────────────────────────────────────────────────────────────┤
│ Start: STOR-2 (BMS-Eval)                                            │
│   ↓                                                                  │
│ Arch: Battery Adapter Layer v0 (2–3W, Gate: 2 Arch verfügbar)       │
│   ↓                                                                  │
│ FW: CAN-Handshake (3–4W, FW-Team ramp-up, Gate: Team produktiv)     │
│   ↓                                                                  │
│ Test: Labor-Validierung (1–2W parallel mit FW)                      │
│   ↓                                                                  │
│ Gate G1: Architektur-Kapazität + Firmware-Produktivität → GO MS2    │
└─────────────────────────────────────────────────────────────────────┘
                             ⬇
┌─────────────────────────────────────────────────────────────────────┐
│ MS2: Früher Feldtest (8–10W gesamt)                                 │
├─────────────────────────────────────────────────────────────────────┤
│ Parallel-Streams:                                                   │
│                                                                     │
│ Stream A (Feldtest vorbereiten):                                    │
│   STOR-4 (SoC/SoH) 3–4W → HiL-Tests → Feldtest-Deployment          │
│   Gate G2: Feldtest-Standorte verfügbar                             │
│   ↓                                                                  │
│   Test (Feldtest-Betrieb): 6W Datensammlung                         │
│                                                                     │
│ Stream B (Zertifizierung starten):                                  │
│   STOR-6 (Grid-Code-Vorbereitung) 4–6W parallel                     │
│   = Unterlagen-Sammlung, nicht Hardware-Test (noch)                 │
│                                                                     │
│ Stream C (App & Cloud):                                             │
│   STOR-5 + STOR-7 (Telemetrie + App) 2–3W parallel                  │
│                                                                     │
│ Gate G3: Firmware-Team produktiv nach Onboarding                    │
│ Gate G4: Zertifizierungs-Audit auf Track für Q4                     │
│   ↓                                                                  │
│ → Feldtest bestanden (keine CRITICALs) → GO MS3                     │
└─────────────────────────────────────────────────────────────────────┘
                             ⬇
┌─────────────────────────────────────────────────────────────────────┐
│ MS3: Start of Development (4–5W)                                    │
├─────────────────────────────────────────────────────────────────────┤
│ Parallel-Streams:                                                   │
│                                                                     │
│ Stream A (Release-Readiness):                                       │
│   FW: Feldtest-Fixes + RC (2–3W)                                    │
│   Test: Zertifizierungs-Audit (2–3W parallel)                       │
│   Arch: Final Docs (1W)                                             │
│                                                                     │
│ Stream B (Go-to-Market):                                            │
│   Cloud + App: Analytics + Support-Tools (2W)                       │
│   Storage-Platform: Installer-Onboarding + Playbook (3–4W)          │
│                                                                     │
│   ↓                                                                  │
│ → Zertifizierungs-Gate bestanden + Installer-ready → LAUNCH-GATE    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Zusammenfassung: Reife der 3 Meilensteine

| Meilenstein | Eingang-Gate | Ausgang-Gate | Slack-Realismus |
|---|---|---|---|
| **MS1: Walking Skeleton** | Lieferant-Sample verfügbar, Architektur-Kapazität 10h/W | CAN-Handshake laborbestätigt, Firmware-Team produktiv | +8–10W wenn Sample verzögert; +2W wenn Arch überlastet |
| **MS2: Früher Feldtest** | Feldtest-Standorte vertraglich gesichert (5+ Kunden), Architektur verfügbar | 6W Feldtest-Daten ohne CRITICALs, Zertifizierungs-Audit <br>parallel fortgeschritten | +6–8W wenn Feldtest-Kapazität weg (INV-Gen3-Slip), +4W wenn Zertifizierung verzögert |
| **MS3: SOD** | Feldtest-Learnings prioritätsgeordnet, Zertifizierungs-Audit läuft | Zertifizierungs-Gate bestanden, Installer-Training live | +2–3W wenn Audit stockt, +1W wenn FW-Fixes unterschätzt |

---

## Entscheidungs-Logik: Wann kickt dieses Projekt?

**Aus devils-advocate:** Die Aufwandsschätzung (6–8 Monate bis SOD) ist abhängig von 3 volatilen Annahmen:
1. INV-Gen3-Zertifizierung verzögert nicht (Q3 stabiler Abschluss).
2. Storage-Platform-Team ramp-up läuft parallel, nicht blockierend.
3. Feldtest-Kapazität wird verfügbar (5 Kunden + 2 Personen aus Test & Cert verfügbar).

**Realistische Ausgänge:**

| Szenario | Kickoff-Timing | Realistisch? | Konsequenz |
|---|---|---|---|
| **Best Case:** Alle 3 bestätigt | Q3 Kickoff, SOD Q4/Q1 | 25 % | Walking Skeleton MS1 (6–8W) → Feldtest MS2 (8–10W) → SOD MS3 (4–5W) |
| **Likely Case:** INV-Gen3 verzögert um 3–4W, Feldtest-Kunden knapp | Q3 Kickoff, aber Gate G1 / G2 blocken → Pause / Slip → SOD Q1 2027 | 60 % | Walking Skeleton läuft, aber Feldtest shiftet (Gate G2), Ramp-up verläuft OK |
| **Worst Case:** Zertifizierungs-Audit verzögert + Feldtest-Kapazität weg | Kickoff Q3, aber beide kritischen Gates fallen → Pause bis Q1 2027 | 15 % | Walking Skeleton + Zertifizierungs-Parallelstrom ja, Feldtest nein → Ramp-up mit 30 % erhöhtem Defekt-Risiko |

**Empfehlung:** Gate G1 (nach Walking Skeleton) ist der Kontrollpunkt. Das ist 6–8 Wochen nach Kickoff. Wenn zu diesem Zeitpunkt:
- Architektur-Team nicht verfügbar (INV-Gen3 verzögert), ODER
- Feldtest-Standorte nicht vertraglich gesichert, ODER
- Firmware-Team noch in Onboarding-Turbulenz

→ Dann ist nicht die Roadmap falsch, dann war der Q3-Kickoff zu früh. Besser: Warten auf Q1 2027 mit stabilem Team-Setup.

---

## Nächste Schritte (nicht in dieser Roadmap, aber Kontext)

1. **Lieferant-Evaluation** (offenes Thema aus devils-advocate): Wer ist der Batterie-Hersteller? LG/Huawei (low-risk, aber Follower-Move)? BYD (neues Supply-Chain-Risiko, +4W Aufwand)? Startup (zu riskant für 6–8M Roadmap)?
2. **Feldtest-Kundenplan:** 5 Early-Adopter identifizieren und Verträge vor G2 absichern.
3. **Architektur-Kapazität-Planung:** INV-Gen3-Zertifizierungs-Realität (ist Q3 stabil?) klären mit Test & Cert.
4. **Storage-Platform-Team-Gründung:** Parallel mit Walking Skeleton starten (nicht danach), damit Onboarding bis MS2-Start absolviert ist.
