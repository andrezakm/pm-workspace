# Handoff: Neue Speichervariante für Voltaris

**Datum:** 2026-06-16  
**Status:** Bedingt bereit für Entwicklung (siehe „Blocker & offene Gating")

## Zusammenfassung

Entwicklung einer zweiten Speichervariante für Voltaris Invertersystem, basierend auf bewährtem Integrationsmuster (Walking Skeleton → Feldtest → SOD), aber mit kritischer Abhängigkeit von Feldtest-Kapazität und Architektur-Verfügbarkeit in Q3.

---

## Artefakte & Navigation

| Dokument | Pfad | Status | Verwendung |
|----------|------|--------|-----------|
| **Decision Brief** | `output/02-decision-brief.md` | ✅ PM-Entscheidung | Strategie & Empfehlung: „MEHR DATEN vor BUILD" |
| **Devils Advocate** | `output/03-devils-advocate.md` | ✅ Kritische Analyse | 7 Annahmen hinterfragt; empfiehlt PAUSE statt Q3-Kickoff |
| **Integrations-Roadmap** | `output/04-roadmap.md` | ✅ Operative Planung | 3 Meilensteine mit Gates, Team-Zuordnungen, Engpass-Analyse |
| **Mini-Specs (Walking Skeleton)** | `output/05-mini-specs.md` | ✅ Entwicklungs-Spezifikation | STOR-3 (CAN-Handshake) + STOR-4 (SoC/SoH) mit Akzeptanzkriterien |
| **Team-Kontext** | `context/team.md` | ✅ Kapazitäts-Baseline | Heutige Teamgröße + erwartete Veränderungen (Storage-Platform-Team) |

---

## Was Dev als nächstes tun soll

1. **Lieferant-Evaluation absichern (Gate vor Kickoff)**
   - Welcher Batterie-Hersteller? (LG/Huawei = low-risk, BYD = neues Supply-Chain-Risiko, Startup = zu riskant)
   - BMS-Spezifikation + CAN-ICD vollständig vorliegen?
   - Liefersample-Lead-Time bekannt? (typisch: +8–10 Wochen nach Bestellung)
   - **Blockiert:** Walking Skeleton kann nicht starten ohne STOR-2 BMS-Protokoll-Definition

2. **Feldtest-Kundenplan konkretisieren (Gate G2 in Roadmap)**
   - Sind 5–10 Early-Adopter-Kunden bereit für 6-wöchigen Feldtest parallel zum INV-Gen3-Rollout DE/AT?
   - Verträge + Messpunkt-Definition vor Walking Skeleton abgeschlossen?
   - **Kritisch:** Wenn diese Kapazität nicht verfügbar ist, verzögert sich MS2 um mindestens 6 Wochen

3. **INV-Gen3-Zertifizierungs-Realität klären (Gate G1 & G4)**
   - Ist Grid-Code-Zertifizierung Q3 stabil abgeschlossen, oder droht Slip?
   - Wenn Slip > 3–4 Wochen: Architektur-Team nicht verfügbar für neue Battery-Integration → Kickoff verschieben auf Q1 2027
   - **Abhängigkeit:** Walking Skeleton braucht 10h/Woche Architektur-Kapazität

4. **Storage-Platform-Team-Gründung vorbereiten (parallel mit MS1)**
   - Team-Zusammensetzung: 2 aus Firmware + 1 aus Cloud?
   - Onboarding-Playbook für neue Team-Members (4–6W bis produktiv)?
   - **Risiko:** Neue Teams unter Zeitdruck arbeiten schlecht; besser: realistische Velocity einplanen

5. **Hardware-in-the-Loop-Rig verfügbar machen**
   - Ist die Test-Rig nach INV-Gen3-Zertifizierung verfügbar (aktuell überlastet)?
   - STOR-4 (SoC/SoH-Validierung) braucht HiL-Rig für 2–3 Wochen in MS1
   - **Gate:** Rig-Verfügbarkeit ist Teil von G1 (Walking Skeleton abgeschlossen)

---

## PM-Eval vs. Dev-Eval

### PM hat geprüft (via Decision Brief + Devils Advocate)

✅ **Markt-Readiness:** Daten-Sammlung erforderlich (Installateure-Anfragen, Wettbewerbs-Analyse), aber Basis-Strategie OK  
✅ **Technische Feasibility:** Architektur stabil genug für 6–8M Roadmap (Learning aus V2 & INV-Gen3 anwendbar)  
✅ **Operative Engpässe erkannt:** Architektur-Team (2 Personen), Feldtest-Kapazität, neues Storage-Platform-Team-Reife  
⚠️ **Kritisches Risiko:** Parallelisierungsannahmen sind volatil (INV-Gen3-Slip, Feldtest-Kunden knapp) → realistischer Kickoff Q1 2027, nicht Q3

### Dev soll ergänzen

✅ **Hardware-Integration Reality-Check:** BMS-Sample verfügbar? Spezifikation wirklich vollständig?  
✅ **Code-Review der Mini-Specs:** Sind Akzeptanzkriterien praktikabel? Fehlen Edge Cases?  
✅ **Lieferanten-Risikovotum:** Wer ist der BMS-Hersteller? Liefersicherheit OK?  
✅ **Feldtest-Daten-Qualität:** Sind 6 Wochen + 5–10 Geräte ausreichend, um 80% der Bugs zu fangen (V2-Learning)?  
✅ **Performance-Risiken:** CAN-Handshake bei 100ms Zykluszeit realistische? Thermische Lastprofile des neuen Zelltyps bekannt?

---

## Offene Fragen & Risiken

Aus dem Decision Brief und Roadmap-Analyse:

### Kritische Gates (Entscheidung fällt hier)

1. **Gate G1: Architektur-Kapazität nach Walking Skeleton**
   - Bedingung: Architektur-Team hat +10h/Woche für MS2 verfügbar (INV-Gen3 nicht verzögert)
   - Nein → Pausieren bis Q1 2027
   - Warum: 2-köpfiges Team ist Engpass über alle 3 Meilensteine

2. **Gate G2: Feldtest-Standorte vertraglich gesichert**
   - Bedingung: Mindestens 5 Early-Adopter + 2 dedizierte Test-Personen verfügbar für 6W parallel zu INV-Gen3
   - Nein → MS2 verschieben oder ohne early Feldtest starten (riskant: ~30% höhere Fehlerquote)
   - Warum: Test & Cert sind zu 100% auf INV-Gen3-Zertifizierung fokussiert

3. **Gate G3: Storage-Platform-Team produktiv nach 4 Wochen Onboarding**
   - Bedingung: Team etabliert Coding-Standards, Escalation-Routes; neue Members shadowing absolviert
   - Nein → Core-Firmware-Leads übernehmen (Kapazitäts-Hit, Verzug wahrscheinlich)

4. **Gate G4: Zertifizierungs-Audit auf Track für Q4**
   - Bedingung: STOR-6 (Grid-Code-Vorbereitung) läuft parallel zu MS2; Auditor confirmiert Audit-Ende Q4 möglich
   - Nein → Launch verzögert sich in Q1 2027

### Annahmen die Dev prüfen muss

- **BMS-Sample-Lead-Time:** Hersteller kann Sample in 8–10 Wochen liefern? (Otherwise: +8–10W Gesamtverzug)
- **Lieferant-Vertrauenswürdigkeit:** Support-Level für BMS-Protokoll-Dokumentation? (BYD hat Spezifikations-Lücken)
- **OTA-Kompatibilität:** Sollte alte V2-Geräte auf neue Batterie wechseln können? (separate Epic oder Teil von STOR-8?)
- **Feldtest-Daten-Verarbeitung:** Wer analyzed die 6W Telemetrie und priorisiert Bugs? (Cloud-Team oder dediziert?)

---

## Blocker & nicht Dev-Ready

### Nicht freigegeben für Kickoff

🔴 **Lieferant ist nicht entschieden**  
→ STOR-2 (BMS-Protokoll-Evaluation) kann nicht starten ohne konkreten Hersteller  
→ **Dev braucht von PM:** Hersteller-Shortlist + Evaluierungs-Kriterien

🔴 **Feldtest-Kapazität ist ungesichert**  
→ Gate G2 ist blocker für MS2-Start  
→ **Dev braucht von PM:** Verträge mit 5–10 Kundenstandorten VOR Walking Skeleton abgeschlossen

🔴 **Architektur-Kapazität ist volatil**  
→ INV-Gen3-Zertifizierung könnte Q3 verzögern  
→ **Dev braucht von PM:** Realistisches Szenario-Planung: Wenn INV-Gen3 +4W verspätet, ist Q3-Kickoff nicht möglich

🔴 **Storage-Platform-Team-Ramp-up ist nicht in 6–8M eingepreist**  
→ Mini-Specs unterstellen „Storage-Platform-Team 3–4 Personen" ab Woche 1  
→ **Realität:** Weeks 1–4 sind Onboarding; echte Velocity startet Woche 5  
→ **Dev braucht von PM:** Entscheidung: 10–12M Timeline akzeptieren, oder Experienced Leads on full-time, neue Members shadowing?

---

## Status in 1 Zeile

**🟡 GELB — Bedingt dev-ready:** Artefakte sind complete (Roadmap, Specs, Risikovotum), aber 4 kritische Gates (Lieferant, Feldtest-Kunden, Architektur-Verfügbarkeit, Team-Reife) müssen vor echtem Kickoff geklärt sein. Realistische Wahrscheinlichkeit Q3-Start: ~25% (Likely Case: Q1 2027 mit stabilerem Setup).

---

## Ehrliche Bewertung: Wert des Handoff auf billigem Modell

**Funktioniert reines Bündeln zuverlässig?** Teilweise ja — das Modell konnte alle Artefakte lesen, die Abhängigkeits-Ketten rekonstruieren und Gates identifizieren. Das war möglich, weil die Input-Artefakte bereits strukturiert waren (Decision Brief, Devils Advocate, Roadmap mit expliziten Gates).

**Liefert dieser Schritt echten Wert?** Ja, aber mit Einschränkung: Der Wert liegt nicht im „Inhaltsverzeichnis schreiben", sondern im **De-Risking durch Gate-Verschärfung**. Das handoff doc hat die 4 kritischen Gates (G1–G4) aus der Roadmap extrahiert und zu Blockers erklärt, die PM *vor* Kickoff lösen muss. Das ist ein Mehrwert gegenüber „verlinke alle Dateien". Das „Nicht Dev-Ready"-Kapitel nennt konkret, was PM noch liefern muss. Ein echtes Inhaltsverzeichnis würde das nicht tun.

**Aber:** Ein besseres Modell (Opus, Claude 3.5) würde wahrscheinlich noch eine Schicht tiefergehen — z.B. Cross-Checking zwischen Decision Brief und Roadmap (Wiedersprüche finden), oder spezifische Code-Fragestellungen aus den Mini-Specs herausheben, die Lieferanten-abhängig sind. Haiku hat das nicht geleistet; es hat primär sammel-und-strukturiert (was OK ist, aber nicht brilliant).

