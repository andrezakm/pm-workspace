# Delta-Report — Simulation „Speicher-Integration mit Bordmitteln"

**Setup:** Haiku 4.5 als Worker (je ein Agent pro Schritt), Opus als Beobachter. Bewusst dünner, approximierter interner Kontext (fiktiver OEM „Voltaris"), **kein** Web-Research. Ein einziger Durchlauf, kein Mensch im Loop.
**Ziel:** Nicht „kann das System die Aufgabe lösen", sondern **wie viel Tiefe muss man bauen, bis es trägt** — und wo liegt diese Tiefe.

---

## Kernbefund

> **Das Reasoning ist billig. Der Kontext ist der Burggraben.**
> Selbst ein günstiges Modell liefert aus dünnem-aber-sauberem internen Kontext eine glaubwürdige Engineering-Lesart, ein selbst-schließendes Strategie-Verdikt, eine *neue* adversariale Einsicht, eine ~80%-Roadmap, brauchbare Mini-Specs und ein gehärtetes Handoff. Der Qualitäts-*Boden* liegt deutlich höher als „Worst Case" befürchten ließ.

Das ist empirisch genau die These von Woche 5: der Unterschied zwischen „Skills" und „System" ist Kontext. Die Quellen, die die Teilnehmerin auflistet — Jira, Confluence, Reference Architecture, Altprojekte (+ implizit Marktdaten) — **sind** das System. Die Skills obendrauf sind dünn.

---

## Delta je Schritt

| # | Schritt | Bordmittel | Boden-Qualität (Haiku) | Delta — was das echte System braucht |
|---|---------|-----------|------------------------|----------------------------------------|
| 1 | Kür: Wettbewerb + Value-Add | `business-case-debater` (emuliert, ohne Web) | Engineering belastbar; Kür **hohl**, aber ehrlich (präzise „welche Quelle wofür"-Tabelle) | **Eine externe Quelle** (Web-Research wie im echten Skill, oder `context/competitors.md`). Kein Tiefen-, ein Quellenproblem. |
| 2 | Entscheidung | `decision-brief` | Korrekt, aber **kollabiert** zum Formatierer nach selbst-schließender Debatte | Nichts — der Schritt ist nur nötig, wenn ihn eine Scorecard (statt Debatte) füttert. Pipeline kürzbar. |
| 3 | Härtetest | `devils-advocate` | **Echter neuer Wert**: fand den zusammengesetzten Engpass (Zert. + Feldtest + Ramp-up konkurrieren) | Verdient seinen Platz. Braucht nur Grounding-Guardrail (erfand Quartale). |
| 4 | Roadmap | **kein Skill** (nackter Agent) | ~80% glaubwürdig: 3 Gates, Abhängigkeitsreihenfolge, Learnings angewandt | **Dünnes** Skill: Gate-Template + Kapazitäts-vs-Timeline-Check (scriptbar) + echte Jira-Dependency-Links. Struktur + Validierung, **nicht** Reasoning. |
| 5 | Mini-Specs + Teamabh. | `spec-writer` | Specs gut; Teamabhängigkeiten **nicht nativ** — drumherum gebaut | Kleine Erweiterung (Dependency-Tabelle / Interface-Contract). Zeigt: Spec/Build-Hälfte ist für *Software* geformt, nicht Hardware. |
| 6 | Dev-Ready | `handoff-packager` | Zuverlässig; Wert = offene Fragen → **explizite Gates** | Nichts Großes. Stärkeres Modell würde Cross-Artefakt-Widersprüche prüfen. |

---

## Drei Muster über alle Schritte

1. **Wo der Boden hält (dünnes System reicht):** strukturell-analytische Arbeit über gegebenem Kontext — Engineering-Ableitung, adversariales Quer-Denken, Sequenzierung, Bündeln. Hier braucht das echte System kaum Tiefe.
2. **Wo der Boden hohl ist — und warum:** überall, wo **externe Fakten** nötig sind (Wettbewerb, Markt). Das ist ein **Quellen**-Problem, kein Skill-Problem.
3. **Wo das billige Modell gefährlich ist:** es **konfabuliert konkrete Specifics** (Quartale, Lieferantennamen) selbst gegen explizite Anweisung. Reproduzierbar in Schritt 3, 4 und 6. → braucht ein *strukturelles* Guardrail oder ein stärkeres Modell, nicht mehr Prompt.

---

## Was das echte System WIRKLICH braucht (Tiefenbudget)

- **Wiederverwenden, as-is:** `business-case-debater` (mit Quelle), `devils-advocate`, `handoff-packager`.
- **Dünn bauen:** `/integration-roadmap` (Template + Validierung, kein Reasoning-Monster) · `spec-writer`-Erweiterung um Teamabhängigkeiten/Interface-Contract.
- **Investieren — hier liegt die Tiefe:** der **Daten-Vertrag**. Jira *mit echten Dependency-Links*, maschinenlesbare Reference Architecture, Altprojekte mit echten Aufwandsdaten, **eine Wettbewerbs-/Marktquelle**. Genau die „anzubindenden Quellen" der Aufgabe — die Simulation zeigt: sie sind nicht Beiwerk, sie sind das Produkt.
- **Quer (nicht „mehr Skills"):** (a) Grounding-Guardrails für jeden Schritt mit Datum/Zahl/Eigenname; (b) ein deterministischer Kapazitäts-/Timeline-Validator (Script).

---

## Modell-Tier-Befund (Ziel „Worst Case im billigen Modell")

- **Haiku reicht für:** Engineering-Ableitung, adversariale Kritik, Roadmap-Sequenzierung, Spec-Entwurf, Bündeln — die Arbeit *über* gegebenem Kontext.
- **Haiku ist unsicher für:** alles mit externem Faktenbezug (konfabuliert).
- **Folge — Kosten-Architektur:** Die meisten Schritte könnten auf einem günstigen Modell laufen; ein starkes Modell nur dort reservieren, wo Grounding kritisch ist (Synthese, fakten-tragende Schritte). Das senkt Kosten, ohne Qualität zu opfern.

---

## Grenzen dieser Simulation (Fairness)

- **Saubere Stubs:** echtes Jira/Confluence ist Müll-behaftet → der Engineering-Boden liegt real evtl. tiefer (Modell muss erst Struktur aus Chaos ziehen). *Testbar: Inputs absichtlich vermüllen.*
- **Kein Web:** die Kür wurde künstlich beschnitten, um den internen Boden zu zeigen. Mit Web läge sie höher.
- **Ein Durchlauf, kein Mensch im Loop:** der echte Wert entsteht oft erst im Dialog an den Checkpoints.

---

## Implikation für den Plan

Wir wissen jetzt: **das benötigte System ist überwiegend Zusammenbau** (vorhandene Skills) **+ zwei dünne Ergänzungen + ein ernsthafter Daten-Vertrag** — kein tiefer Neubau. Das Tiefenbudget gehört in die Daten und in zwei Quer-Themen (Guardrails, Validator), nicht in klügere Skills. Darauf lässt sich jetzt ein konkreter Bauplan aufsetzen.
