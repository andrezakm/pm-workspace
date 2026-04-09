# Decision Brief: Onboarding-Automatisierung

**Empfehlung:** BUILD
**Datum:** 2026-04-09

## Das Muster

In 4 von 5 analysierten Projekten und Kundengesprächen (KW 8–12/2025) taucht derselbe Schmerz auf: Der manuelle Onboarding-Prozess beim Go-Live eines Agents kostet 2–8 Stunden pro Nutzer, wird von Kunden als Investitionshürde erlebt und verursacht intern nicht budgetierte Aufwände. NeoEmployee baut denselben Onboarding-Ablauf projekt für Projekt von Hand neu — Felix Braun intern: "Wir haben das jetzt zum dritten Mal fast identisch gebaut."

Das ist das einzige Muster im Datensatz das branchenübergreifend und ohne Anpassung wiederkehrt (Score: 5/5 Wiederholbarkeit).

## Für wen

- **Peter Hartmann, LogiTrans GmbH** — Musste 4 Kollegen manuell einweisen (je 45–60 Min.), war selbst zwei Wochen lang "Support für sein Team". Bereit extra zu zahlen für selbstständig onboardbare Agents.
- **Dr. Sabine Roth, PharmaCare AG** — "Wenn das Ding sich selbst erklären kann, ist das für mich ein Kaufargument." Vier Stunden Schulung beim ersten Projekt, danach wochenlang Nachfragen.
- **Thomas Berg, FinancePlus** — Onboarding eines einzelnen Kollegen kostete ihn als CFO einen halben Tag. Explizit: weitere Investitionen hängen davon ab, ob das Onboarding-Problem gelöst wird.
- **Sandra Pfeiffer, BauLogik AG** (Prospect) — Zwei vorherige Automatisierungsprojekte sind gescheitert weil das Onboarding zu komplex war. Kaufentscheidung explizit an 15-Minuten-Hürde geknüpft.
- **Intern:** Sarah Klein, Marc Hoffmann, Felix Braun sehen denselben Schmerz auf der Delivery-Seite — kein Template, kein Playbook, jedes Mal neu.

## Warum jetzt

**Strategischer Fit:** `context/strategy.md` beschreibt das Ziel als "branchenübergreifend ausrollbare Agents" (Horizon 2). Onboarding-Automatisierung ist die einzige Opportunity im Datensatz die dieses Kriterium erfüllt — sie ist unabhängig von Branche, Regularien oder Datenstruktur des Kunden.

**Multiplikatoreffekt:** Ein wiederverwendbares Onboarding-Modul senkt die Delivery-Kosten aller zukünftigen Projekte. Julia Meyer (Pattern-Team): "Das würde alle unsere zukünftigen Projekte günstiger machen." Das ist kein Feature — das ist ein struktureller Kostenvorteil.

**Konkurrenz-Kontext:** BauLogik hat bereits zwei Produkte verworfen weil das Onboarding gescheitert ist. Das bedeutet: wer das löst, hat einen seltenen Differenziator im Markt.

**Kapazität:** Kai Schmidt schätzt 2 Engineering-Wochen für ein MVP. `context/roadmap.md`: Pattern-Team (Lisa + Tom) evaluiert Onboarding bereits als erstes skalierbares Produkt — die Entscheidung ist damit nicht neu, sie braucht nur eine Bestätigung.

## Empfehlung

**BUILD** — als internes Modul zuerst, dann als wiederverwendbare Komponente in Kundenprojekten.

Kein eigenständiges Produkt im ersten Schritt. Kein Sales-Pitch nach außen. Stattdessen: In den nächsten 2 Engineering-Wochen (Lisa + Tom) ein Onboarding-Flow bauen der in das nächste Kundenprojekt eingebettet wird — LogiTrans oder FinancePlus bieten sich als erste Referenz an, da beide den Schmerz explizit geäußert haben und bestehende Kundenbeziehungen existieren.

Erfolgsmaßstab: Onboarding-Zeit pro Nutzer von heute 2–8 Stunden auf unter 30 Minuten ohne menschliche Einweisung.

## Offene Fragen

- **Content-Ownership:** Wer schreibt die Einweisungstexte? (Marc Hoffmann hat diesen Engpass explizit benannt — es ist kein Tech-Problem.) Ohne Antwort auf diese Frage scheitert das Modul unabhängig von der technischen Qualität.
- **Zahlungsmodell:** Kunden reagieren unterschiedlich — Peter Hartmann würde extra zahlen, Dr. Roth behandelt es als Hygiene-Faktor. Ist das ein Preisaufschlag, ein kostenloses Modul zur Kundenbindung, oder eine eigene SKU?
- **Abgrenzung zu Compliance-Checking:** PharmaCare zahlt jetzt für Compliance (konkretes Budget-Gespräch). Wenn Lisa + Tom mit Onboarding beschäftigt sind, verschiebt sich das PharmaCare-Projekt. Muss explizit priorisiert werden.
