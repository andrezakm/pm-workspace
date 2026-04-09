# Opportunity Scorecard

**Basis:** `output/discovery/feedback-clusters.md`
**Kontext:** `context/company.md`, `context/strategy.md`, `context/team.md`, `context/roadmap.md`
**Datum:** 2026-04-09

*Bewertet werden die 3 Cluster mit Produktpotenzial. Cluster 4 (Team-Kapazität) ist ein internes Betriebsproblem, kein Opportunity — wird nicht gescort.*

---

## Cluster 1: Onboarding-Schmerz

| Dimension | Score | Begründung |
|-----------|-------|------------|
| Fit mit Vision | 3/5 | Ein Onboarding-Modul automatisiert eine interne Aufgabe (Einweisen), ersetzt aber keine Mitarbeiterfähigkeit beim Kunden direkt. Die Vision laut `context/company.md` ist "AI Agents die Mitarbeiterfähigkeiten in Unternehmen ersetzen" — Onboarding-Automatisierung ist eher ein Enabler der eigenen Produkte als ein eigenständiger Agenten-Anwendungsfall. Passt zur Horizon-2-Logik (skalierbare Produkte), aber ist kein Kern-Use-Case. |
| Wiederholbarkeit | 5/5 | Stärkstes branchenübergreifendes Muster im gesamten Datensatz: alle 4 befragten Kunden (Logistik, Pharma, Finance, Bau), 3 interne Quellen, Pattern-Team-Analyse bestätigt "4 von 5 Projekten". Kai schätzt es als "branchenunabhängig" — laut `context/strategy.md` genau das was für Horizon 2 gesucht wird: "Agent-Typen die branchenübergreifend wiederkehren, werden zu skalierbaren Produkten." |
| Baubarkeit | 3/5 | Kai schätzt 2 Engineering-Wochen — realistisch für ein MVP. Aber Marc benennt den eigentlichen Engpass: "Der Engpass ist nicht die Technik sondern der Content — wer schreibt die Einweisungstexte?" Das ist ein ungelöstes Problem das außerhalb des Tech-Stacks liegt. `context/team.md`: Kapazität nur durch Lisa + Tom neben Kundenprojekten. Machbar, aber mit offenem Risiko. |
| **Gesamt** | **11/15** | |

**Fazit:** Stärkstes Wiederholbarkeitsmuster, strategisch wertvoll für die Skalierung aller zukünftigen Produkte — aber kein direkter Umsatztreiber und mit ungeklärtem Content-Problem. Gutes internes Experiment, solange es kein vollständiges Produktteam erfordert.

---

## Cluster 2: Compliance-Checking

| Dimension | Score | Begründung |
|-----------|-------|------------|
| Fit mit Vision | 4/5 | Hochgradig visionsnah: Compliance-Checking ersetzt direkt spezialisierte Mitarbeiterfähigkeiten (Regulatory Affairs, 30% Arbeitszeit bei PharmaCare; Lieferketten-Compliance bei LogiTrans). `context/company.md`: "Tiefes Verständnis wo Automatisierung in der Praxis scheitert" — das ist genau dieser Fall. Einschränkung: jede Compliance-Domäne (FDA/EMA vs. MiFID II vs. CO2) ist separat — schwerer zu produktisieren als zu customizen. |
| Wiederholbarkeit | 3/5 | 3 Kunden, aber aus grundlegend verschiedenen Regulierungsdomänen. `context/strategy.md` sucht "branchenübergreifende Muster" — Compliance als Kategorie ist breit, aber die konkrete Implementierung ist jedes Mal domänenspezifisch. Felix Braun (intern): "nur bei regulierten Kunden". Das ist eine Teilmenge, kein universelles Muster. |
| Baubarkeit | 3/5 | PharmaCare wartet auf ein Angebot — ein konkretes bezahltes Projekt ist sofort baubar. `context/company.md`: bestehende Claude API + OpenAI API Kompetenz trägt. Aber `context/strategy.md` warnt explizit: "GDPR-Friction ist bekannter Blocker" — Compliance-Daten sind oft hochsensibel. Als wiederverwendbares Produkt: deutlich schwerer. Als Custom-Projekt: sofort. |
| **Gesamt** | **10/15** | |

**Fazit:** Höchste kurzfristige Zahlungsbereitschaft und direktester Umsatztreiber (PharmaCare bereit für "ernsthaftes Budget-Gespräch"), aber schwer zu skalieren — jede Branche braucht eigene Domain-Expertise. Stärker als Custom-Projekt im Horizon-1-Modell als als Horizon-2-Produkt.

---

## Cluster 3: Status-Reporting-Automatisierung

| Dimension | Score | Begründung |
|-----------|-------|------------|
| Fit mit Vision | 2/5 | NeoEmployee baut bereits Reporting-Agents — das ist ihr existierendes Custom-Geschäft. Ein Status-Reporting-Tool wäre keine neue Produktkategorie, sondern eine Erweiterung dessen was schon gemacht wird. `context/strategy.md`: "Vision-Filter — nur Arbeit innerhalb von 'AI Agents die Mitarbeiterfähigkeiten ersetzen'" ist formal erfüllt, aber der strategische Mehrwert für die Horizon-2-Transition ist gering. Differenzierung fehlt. |
| Wiederholbarkeit | 3/5 | 5 Nennungen insgesamt, aber Felix Braun (intern, Pattern-Team) ordnet es explizit als "nice to have" ein — Kunden würden es "nur nehmen wenns günstig ist". Intern ist der Schmerz echter als extern. Taucht auf, aber ohne die Dringlichkeit von Cluster 1 oder die Zahlungsbereitschaft von Cluster 2. |
| Baubarkeit | 4/5 | Höchste Baubarkeit der drei Cluster: NeoEmployee hat hier bereits Kernkompetenz und Referenzprojekte. `context/company.md`: "Portfolio aus Custom-Agents: Reporting-Bots mehrfach gebaut." Ein internes Tool oder ein weiteres Kundenmodul ist technisch trivial. Sarah und Tom könnten das ohne externe Unterstützung bauen. |
| **Gesamt** | **9/15** | |

**Fazit:** Einfach zu bauen, aber strategisch am schwächsten — weil NeoEmployee das im Kern schon macht. Sinnvoll als internes Effizienz-Tool (Team-Problem lösen), aber kein Produktkandidat für Horizon 2.

---

## Gesamtübersicht

| Cluster | Fit mit Vision | Wiederholbarkeit | Baubarkeit | Gesamt |
|---------|---------------|-----------------|------------|--------|
| Onboarding-Schmerz | 3/5 | 5/5 | 3/5 | **11/15** |
| Compliance-Checking | 4/5 | 3/5 | 3/5 | **10/15** |
| Status-Reporting | 2/5 | 3/5 | 4/5 | **9/15** |

## Strategische Lesart

Die Scorecard bestätigt die Spannung die im Feedback bereits sichtbar war:

**Onboarding** gewinnt durch Universalität — es ist das einzige Muster das wirklich skalierbar ist, weil es branchenunabhängig in jeden zukünftigen Agenten eingebettet werden kann. Aber es zahlt sich nicht direkt aus.

**Compliance** gewinnt durch Zahlungsbereitschaft — es ist der klarste kurzfristige Umsatztreiber, aber es hat strukturell niedrigere Skalierbarkeit weil jede Domäne eigene Expertise erfordert.

**Status-Reporting** ist das einfachste, aber das am wenigsten differenzierende — NeoEmployee macht das schon.

Die intern diskutierte Dual-Track-Strategie (Marc: "Compliance als nächstes bezahltes Projekt, Onboarding als internes Experiment") ist mit diesen Scores konsistent und bleibt die logische Empfehlung.
