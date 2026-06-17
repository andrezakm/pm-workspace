# Decision Brief: Neue Speichervariante

**Empfehlung:** MEHR DATEN  
**Datum:** 2026-06-16

## Das Muster

Voltaris hat mit V2 und INV-Gen3 bewährte Integrationsmuster etabliert (walking skeleton → Feldtest → SOD). Eine zweite Speichervariante wäre architektur-technisch machbar in 6–8 Monaten. Aber: Die Debatte zeigt, dass dieser Aufwand nicht auf echtem Marktbedarf oder Wettbewerbs-Intelligenz beruht. Die Entscheidung ruht auf internen Annahmen (Margendruck, Differenzierung), nicht auf Daten.

## Für wen

Keine konkreten Installateure- oder Kunden-Anfragen identifiziert. Margendruck durch asiatische Wettbewerber wird genannt, aber Wettbewerbs-Analyse fehlt: Welche konkreten Brands, welche Speicher-Optionen, welche Kosten-/Performance-Positionen? Ohne diese Benchmark ist „neue Variante bauen" reine Vorrats-Strategie, keine Reaktion auf echte Nachfrage.

## Warum jetzt

**Technisch:** Architektur-Reife und Learnings aus V2 reduzieren Risiko erheblich. Battery Adapter Layer ist bereits Multi-Batterie-ready; BMS-Integration kann über Hardware-in-the-Loop früh getestet werden (V2-Learning: +2M Verzug ohne diesen Test).

**Strategisch:** Plattform-Wachstum über modulare Hardware ist Unternehmens-Strategie. Eine zweite Variante passt this into the roadmap.

**Aber strukturelle Risiken:**
- Firmware-Team verliert 3 Personen durch neues Storage Platform-Team → Kapazität für parallel Integrations-Projekt ist marginal.
- Architektur-Team bleibt Engpass (2 Personen).
- Grid-Code-Zertifizierung pro Markt (DE, FR, IT, NL) ist nicht beschleunigbar und muss parallel laufen.
- BMS-Protokoll-Überraschungen sind klassischer Verzugs-Treiber (V2: +2M).

## Empfehlung

**MEHR DATEN (vor BUILD)**

Drei kritische externe Signale müssen vorher eingeholtsein:

1. **Markt-Pull konkretisieren:** Welche Installateure- oder Kunden-Anfragen nach einer alternativen Speichervariante liegen vor? Oder ist das eine Supply-Push-Spekulation?

2. **Wettbewerber-Analyse:** Welche Storage-Optionen bieten europäische und asiatische Konkurrenten an? Was ist der konkrete Differentiator dieser neuen Batterie (Kosten, Chemie, Thermal-Profil, Liefersicherheit)? Ohne diese Analyse ist „Differenzierung über Software" Marketing-Rhetorik.

3. **Batterielieferant & BMS-Protokoll fixieren:** Name, Hersteller, BMS-Spezifikation, Grid-Code-Auswirkungen je Markt. Das ist nicht optional — es ist die Basis der Aufwands-Schätzung.

**Wenn diese Daten verfügbar sind: dann → BUILD** (parallel zu INV-Gen3-Rollout, mit explizitem Architektur-Kapazitäts-Gate).

## Offene Fragen

- **Market-Pull vs. Supply-Push:** Auf welcher Basis wird die neue Variante priorisiert? Installateure-Anfragen? Margin-Defense? Spekulation?
- **Wettbewerbs-Kontext:** Welche konkreten Storage-Optionen bieten Konkurrenten im selben Preissegment an?
- **Architektur-Verfügbarkeit:** Kann das 2-köpfige Architektur-Team 6–8 Monate neue Integration + INV-Gen3-Wartung tragen, oder ist das Risiko, das dem Projekt später um den Hals fällt?
- **BMS-Protokoll früh testen:** Ist Hardware-in-the-Loop für die neue Batterie parallel zum walking skeleton verfügbar, oder ist das auch ein bottleneck?
- **Feldtest-Kapazität:** Die V2-Integration fand frühe Feldtests mit 5 Geräten kritisch (~80% der Bugs). Ist diese Kapazität verfügbar oder auch im Engpass?

---

**Nächste Schritte zur Daten-Sammlung:**
- Vertrieb: Installateure-Anfragen nach Speicher-Alternativen in den letzten 6 Monaten durchsuchen; 3–5 Installateure-Interviews durchführen.
- Marktforschung: Wettbewerbs-Benchmarking (Gartner, Frost & Sullivan, RegionalMarket-Reports) + Konkurrenz-Teardown starten.
- Procurement: Batterielieferanten evaluieren; Top 3 für BMS-Protokoll-Spezifikation auswählen.
- Technik: Zertifizierungs-Track für neue Batterie × 4 Märkte aufzeigen; Feldtest-Kalender reservieren.
- Architektur-Risiko: Explizites Gate für die Integration in den bestehenden Firmware-Roadmap-Plan (INV-Gen3-Rollout DE/AT + laufende Wartung) eintragen.

