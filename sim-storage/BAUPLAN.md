# Bauplan — PM-System für Hardware-Integration
## Neue Speichervariante: Entscheidung → Dev-Ready

Basierend auf der Simulation (Delta-Report: `output/00-DELTA-REPORT.md`).

---

## Die Pipeline

```
[Kontext]            [Kür]                  [Entscheidung]         [Roadmap]           [Specs]          [Dev-Ready]
context/ + input/  → /business-case-debater → /devils-advocate  → /integration-roadmap → /spec-writer  → /handoff-packager
                                           → /decision-brief
                                             (optional, nur für
                                              Stakeholder-Aufbereitung)
```

---

## Schritt-für-Schritt: wie prompten, was hineinziehen

---

### Schritt 0 — Kontext befüllen (einmalig pro Vorhaben)

Bevor du irgendeinen Skill startest: Fülle die `context/`-Files. Das ist die Basis, auf der alle Skills aufbauen.

Prompt (in Claude Code, im Workspace-Verzeichnis):

```
Hilf mir, mein context/-Verzeichnis für das Vorhaben „neue Speichervariante" zu befüllen.
Ich habe folgende Quellen: [Dateien/PDFs auflisten oder Stubs beschreiben].
Fang mit company.md und learnings.md an und frag mich, was noch fehlt.
```

---

### Schritt 1 — Kür: Strategische Analyse (`/business-case-debater`)

**Was es tut:** 5 Rollen (Optimist, Kritiker, Techniker, Markt, Stratege) debattieren Wettbewerb und Value Add. Mit Web-Research ergibt das echte Wettbewerberanalyse. Ohne Web: Engineering-Seite belastbar, Marktseite hohl aber ehrlich (gibt Datenlücken-Tabelle aus).

**Wie prompten:**

```
/business-case-debater

Business Case: Integration einer neuen Speichervariante (Batterie + Hybrid-Wechselrichter)
in unsere bestehende Plattform. Schwerpunkt Kür: Wettbewerberanalyse und Value Add —
warum jetzt, warum wir, wo liegt der Differentiator?

Falls kein Web verfügbar: Kennzeichne Markt-Aussagen als „intern begrenzt" und gib
am Ende eine Datenlücken-Tabelle aus (Lücke → warum nötig → externe Quelle).
```

**Braucht aus context/:** `company.md`, `strategy.md`, `product.md`, `roadmap.md`

**Braucht aus input/:** wenn vorhanden — Wettbewerber-PDFs, Marktreports

---

### Schritt 2 — Entscheidung (`/decision-brief`)

**Hinweis:** Dieser Schritt ist optional. Nach einer abschließenden Debatte kollabiert er zum Formatierer (Executive-1-Pager). Nur nötig, wenn du ein Stakeholder-Dokument brauchst oder wenn Schritt 1 offen endet.

**Wie prompten:**

```
/decision-brief output/[datum]/strategy/debate-synthesis.md

Zielgruppe: [Produktleitung / Vorstand / ...]. Empfehlung BUILD/SKIP/MEHR DATEN,
Begründung, Annahmen, Risiken. Wenn MEHR DATEN: konkrete nächste Schritte
mit Verantwortlichkeit und Zeitrahmen.
```

**Braucht:** Output von Schritt 1

---

### Schritt 3 — Härtetest (`/devils-advocate`)

**Was es tut:** Greift die Annahmen an, die Debatte und Brief nicht hinterfragt haben. Hier liegt der echte Mehrwert: findet zusammengesetzte Engpässe (Zertifizierung + Feldtest + Team-Ramp-up konkurrieren gleichzeitig), nicht nur einzelne Risiken.

**Wie prompten:**

```
/devils-advocate output/[datum]/strategy/decision-brief.md

Wiederhole NICHT die Kritikpunkte aus der Debatte.
Greife die Annahmen an, die als selbstverständlich behandelt wurden:
Ist „bewährtes Vorgehen übernehmen" bei verändertem Team noch gültig?
Ist „MEHR DATEN sammeln" echte Risiko-Reduktion oder Risiko-Verschiebung?
Sind die Aufwandsschätzungen aus Altprojekten auf neuen Zelltyp übertragbar?
Erfinde keine Daten (Daten, Lieferanten, Kapazitätszahlen) die nicht im Kontext stehen.
```

**Braucht:** Output von Schritt 1 + 2, `learnings.md`, `team.md`

---

### Schritt 4 — Roadmap (`/integration-roadmap`) ← NEU ZU BAUEN

**Was es tut:** Drei Dinge:
1. Lädt ein Meilenstein-Template (walking skeleton → früher Feldtest → SOD)
2. Durchsucht `context/learnings.md` nach Integrations-Mustern: Reihenfolge, Engpässe, Aufwandsmuster aus vergangenen Projekten
3. Sequenziert die Backlog-Items aus dem Jira-Input entlang dieser Meilensteine, mit Teamabhängigkeiten und bekannten Engpässen

**Wie prompten:**

```
/integration-roadmap input/jira-backlog.csv

Meilensteine: walking skeleton → früher Feldtest → SOD.
Lies context/learnings.md für bewährte Muster (Reihenfolge, Engpässe, Aufwand).
Lies context/team.md für aktuelle und erwartete Teamstruktur.
Lies input/confluence-architecture.md für Integrationsreihenfolge.

Je Meilenstein: Ziel (1 Satz), zugehörige Backlog-Items, Teamabhängigkeiten
(wer wartet auf wen, was blockiert was), angewandtes Learning aus Altprojekten,
grober Aufwand (qualitativ, nur wenn aus Kontext ableitbar — sonst offen lassen).

Erfinde keine Kalenderdaten oder Quartale, die nicht im Kontext stehen.
Wenn Aufwand aus Altprojekten extrapolierbar ist: kennzeichne es als Schätzung.
```

**Braucht:** `learnings.md`, `team.md`, `product.md`, Jira-Backlog (CSV oder Kontext-File), Confluence-Architektur-Auszug

**Skill-Inhalt (minimal):**
- Meilenstein-Template (Gate-Struktur, Checkliste)
- Pattern-Suche-Anweisung: *„Lies learnings.md vollständig. Extrahiere: (a) welche Reihenfolge hat sich bewährt, (b) welche Engpässe haben sich wiederholt, (c) welche Aufwandsmuster sind dokumentiert."*
- Guardrail: *„Erfinde keine Daten, Lieferanten, Kapazitätszahlen oder Zeitrahmen aus deinem Trainingswissen."*

---

### Schritt 5 — Mini-Specs (`/spec-writer`) + Teamabhängigkeiten-Erweiterung

**Was es tut:** Schreibt Mini-Specs für die Kern-Items je Meilenstein: Was (nicht Wie), Akzeptanzkriterien, offene Fragen.

**Erweiterung:** Optionaler Abschnitt `## Teamabhängigkeiten` am Ende jeder Spec. Kann leer bleiben — macht das Fehlen von Abhängigkeiten genauso sichtbar wie ihr Vorhandensein.

**Wie prompten (je Meilenstein-Slice):**

```
/spec-writer [STOR-3, STOR-4] output/[datum]/roadmap/roadmap.md

Schreibe Mini-Specs für die Items des walking-skeleton-Meilensteins.
Format: Ziel/Outcome (Was, nicht Wie) — Akzeptanzkriterien — Offene Fragen —
Teamabhängigkeiten (optional: wer liefert was an wen, was ist Blocker).
Wenn keine Teamabhängigkeiten bekannt: Abschnitt leer lassen, nicht weglassen.
```

**Spec-Template (Ergänzung in `SKILL.md`):**

```markdown
## Teamabhängigkeiten
<!-- Leer lassen, wenn keine bekannt. -->
| Abhängigkeit | Lieferer | Input | Empfänger | Blockierend? |
|---|---|---|---|---|
```

---

### Schritt 6 — Dev-Ready (`/handoff-packager`)

**Was es tut:** Bündelt alle Artefakte zu einem Cover-Sheet. Wandelt offene Fragen in explizite Gates um (Blocker / Nicht-Blocker).

**Wie prompten:**

```
/handoff-packager

Bündle: Decision Brief, Devils Advocate, Roadmap, Mini-Specs.
Cover-Sheet: Vorhabens-Zusammenfassung (1 Satz), Entscheidungsstatus,
Links zu allen Artefakten, nächste 3–5 Schritte für Dev (konkret genug
um sofort loszulegen), explizite Gates (was muss geklärt sein bevor Start),
was ist explizit NICHT dev-ready.
Erfinde keine Daten.
```

---

## Querträger — kein Skill, aber systemintern

**In `CLAUDE.md` des Workspace (eine Zeile ergänzen):**

```markdown
## Guardrail
Erfinde keine Daten, die nicht im Kontext stehen:
keine Daten/Quartale, keine Lieferantennamen, keine Kapazitätszahlen.
Benenne stattdessen die Lücke explizit.
```

---

---

## Was muss ins System — Inhalt in zwei Stufen

---

### Stufe A — Statisch: alles als PDFs / Markdown-Stubs

Minimales Set, das das System zum Laufen bringt. Aus jedem Dokument wird ein File in `context/` oder `input/`.

| File | Inhalt | Woher (typisch) |
|---|---|---|
| `context/company.md` | Wer seid ihr, Geschäftsmodell, wie verdient ihr Geld | Intranet / OnePagestrategy / Onboarding-Deck |
| `context/strategy.md` | Aktuelle Constraints, Wachstumsrichtung, was jetzt Priorität hat | Jahres-/Quartalsplanung, OKR-Doc |
| `context/product.md` | Reference Architecture: Technical + Business Capabilities, bestehende Produkte, Stack | Architektur-Doc aus Confluence, Product-Wiki |
| `context/team.md` | Wer macht was, Kapazität, erwartete Veränderungen | Org-Chart, Team-Planung, Personalentscheidungen |
| `context/learnings.md` | Vorgehen + Aufwände aus vergangenen Projekten, was hat sich bewährt, was ist Warnung | Retro-Protokolle, Post-mortem-Docs, informelle Notizen — hier lohnt sich Handarbeit |
| `context/roadmap.md` | Was ist committed, was konkurriert um Ressourcen | Produkt-Roadmap, Sprint-Plan, Quartalsplanung |
| `context/metrics.md` | Aktuelle Metriken, Baselines | Tracking-Sheets, BI-Exports |
| `input/jira-backlog.csv` | Epics + Stories für das Vorhaben, mit Estimates | Jira-Export (CSV oder manuell kuratiert) |
| `input/confluence-architecture.md` | Integrationsrichtlinien, bewährte Reihenfolge, Schnittstellen-Docs | Confluence-Page-Export als Markdown oder PDF → Text |

**Für die Kür (optional, aber die Marktseite bleibt sonst hohl):**

| File | Inhalt | Woher |
|---|---|---|
| `input/competitors.md` | Wer bietet was an, Preisbänder, Differenzierer | Marktreport-PDFs, Preislisten, Vertriebsnotizen |
| `input/market-signals.md` | Kundenanfragen, Installateure-Feedback, Pipeline-Signale | CRM-Export, Vertriebsgespräche, NPS-Kommentare |

---

### Stufe B — Dynamisch: über MCPs

Richtung, keine fixe Implementierung — welche Systeme, welche Info, wie kuratieren.

**Jira** → Backlog, Stories, Estimates, **Dependencies**
- Was wir wollen: Epic-Struktur + Stories + `blocks`/`is-blocked-by`-Links (das ist der Delta gegenüber CSV-Export — Abhängigkeiten als Graph, nicht nur Liste).
- Kuratierung: nicht roher Jira-Dump. Filter auf den relevanten Epic/Sprint, Dependencies als Tabelle vorstrukturiert. Das Architektur-Team oder PM kuratiert — Jira hat zu viel Rauschen.

**Confluence** → Reference Architecture, Integration Guidelines, Entscheidungs-Log
- Was wir wollen: gezielt einzelne Pages (nicht Spaces), als Markdown exportiert.
- Kuratierung: PM oder Architektur legt eine Liste der relevanten Pages an (3–7 Pages). Kein Wildcard-Crawl — sonst landet zu viel Veraltetes im Kontext.

**Vergangene Projekte (Jira + Confluence kombiniert)**
- Was wir wollen: aus abgeschlossenen Epics — tatsächliche Zykluszeiten, Blocker-Typen, Retro-Notizen.
- Kuratierung: `context/learnings.md` bleibt das kuratierte Destillat. MCPs helfen beim *Befüllen*, nicht beim *Ersetzen*. Ein Mensch entscheidet, was als Learning zählt.

**Web / Marktdaten** (`/business-case-debater` macht das bereits)
- Was wir wollen: Wettbewerber-Produkte, Preisbänder, Marktbewegungen.
- Kuratierung: der Skill macht parallele Searches. Ergebnis immer als „extern, nicht verifiziert" kennzeichnen — davon lebt die Datenlücken-Tabelle.

**CRM / Vertrieb** (Salesforce, HubSpot o.ä.) → Markt-Pull-Signale
- Was wir wollen: Kundenanfragen nach bestimmten Produktvarianten, Pipeline-Signale, Lost-Deals mit Begründung.
- Kuratierung: dieser Feed ist hochwertig und fragil. Kein Rohdaten-Dump — PM oder Sales destilliert quartalsweise in `input/market-signals.md`. MCP könnte suchen und vorstrukturieren, Mensch bestätigt.

---

---

## Skill-Entwurf: `/integration-roadmap`

Dieser Entwurf kann direkt als `.claude/skills/integration-roadmap/SKILL.md` abgelegt werden.

```markdown
---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.
> Erfinde keine Daten (Kalendertermine, Quartale, Lieferantennamen, Kapazitätszahlen),
> die nicht im Kontext stehen. Benenne fehlende Daten statt sie zu erfinden.

# Integration Roadmap

## Was dieser Skill tut

Erstellt eine Integrations-Roadmap entlang der bewährten drei Meilensteine:
**walking skeleton → früher Feldtest → SOD (Start of Delivery)**.

Zwei Quellen steuern das Ergebnis:
1. **Kontext-Muster** (`context/learnings.md`) — wie laufen Integrationen hier,
   welche Reihenfolge hat sich bewährt, welche Engpässe wiederholen sich.
2. **Backlog** (`input/jira-backlog.csv` oder übergebener Pfad) —
   welche Items gehören zu welchem Meilenstein, wer hängt von wem ab.

## Aufruf

```
/integration-roadmap [Pfad zum Backlog]
```

Beispiel: `/integration-roadmap input/jira-backlog.csv`

---

## Ausführung

### Phase 1 — Muster aus Altprojekten extrahieren

Lies `context/learnings.md` vollständig. Extrahiere daraus:

- **Bewährte Reihenfolge:** In welcher Sequenz wurden Integrations-Schritte
  bisher durchgeführt? (z.B. Handshake vor Kalibrierung vor Feldtest)
- **Wiederkehrende Engpässe:** Welche Teams, Ressourcen oder externe
  Abhängigkeiten wurden in mehreren Projekten zum Blocker?
- **Aufwandsmuster:** Wo lagen tatsächliche Aufwände — und wo gab es
  systematische Unterschätzungen?
- **Bewährte Gates:** Welche Zwischenstände haben sich als
  sinnvolle Entscheidungspunkte erwiesen?

Schreibe diese Muster intern als Arbeitsgrundlage auf — sie steuern
die Zuordnung in Phase 2.

### Phase 2 — Backlog-Items den Meilensteinen zuordnen

Lies den Backlog (übergebener Pfad). Lies außerdem:
- `context/product.md` — Architektur und Integrationsschnittstellen
- `context/team.md` — aktuelle und erwartete Teamstruktur
- `input/confluence-*.md` — falls vorhanden: Integrationsrichtlinien

Ordne jeden Backlog-Item einem Meilenstein zu. Kriterium:
- **Walking Skeleton:** alles, was die grundlegende Kommunikation herstellt
  (Hardware-zu-Hardware, Protokoll, erste Daten)
- **Früher Feldtest:** alles, was für einen stabilen, messbaren Betrieb
  mit echten Geräten nötig ist (Kalibrierung, Monitoring, erste Zertifizierung)
- **SOD:** alles, was für den Launch-Gate nötig ist
  (vollständige Zertifizierung, Onboarding, OTA-Readiness)

Wenn ein Item nicht eindeutig zugeordnet werden kann: in den
späteren Meilenstein einordnen und als „Reihenfolge offen" markieren.

### Phase 3 — Roadmap schreiben

Schreibe nach `output/YYYY-MM-DD/roadmap/roadmap.md`.

Verwende dieses Template:

---

# Integrations-Roadmap: [Vorhaben]

## Muster aus Altprojekten (angewandt)
<!-- Was aus context/learnings.md direkt in diese Roadmap eingeflossen ist -->
- [Muster 1]
- [Muster 2]
- [Engpass X wiederholt sich → Gate eingeplant]

---

## Meilenstein 1 — Walking Skeleton

**Ziel:** [1 Satz: was kommuniziert mit was, was ist der erste nachweisbare Stand]

**Backlog-Items:**
| Item | Komponente | Team | Depends on |
|------|-----------|------|-----------|
| STOR-x | ... | ... | — |
| STOR-y | ... | ... | STOR-x |

**Teamabhängigkeiten:**
| Wer liefert | Was | An wen | Blockiert MS1? |
|------------|-----|--------|---------------|
| ... | ... | ... | ja / nein |

**Angewandtes Learning:** [Verweis auf Muster aus Altprojekten]

**Gate-Kriterien (bevor MS2 startet):**
- [ ] [Konkretes, prüfbares Kriterium]
- [ ] [Konkretes, prüfbares Kriterium]

**Offener Aufwand:** [aus Backlog-Estimates; wenn nicht ableitbar: „nicht im Kontext"]

---

## Meilenstein 2 — Früher Feldtest

**Ziel:** [1 Satz]

**Backlog-Items:**
| Item | Komponente | Team | Depends on |
|------|-----------|------|-----------|

**Teamabhängigkeiten:**
| Wer liefert | Was | An wen | Blockiert MS2? |
|------------|-----|--------|---------------|

**Angewandtes Learning:** [Verweis]

**Gate-Kriterien:**
- [ ] Zertifizierungs-Track gestartet (parallel, nicht danach)
- [ ] Feldtest-Standorte und Early-Adopter bestätigt
- [ ] [Weitere aus Kontext ableitbare Kriterien]

**Offener Aufwand:** [oder „nicht im Kontext"]

---

## Meilenstein 3 — SOD (Start of Delivery)

**Ziel:** [1 Satz]

**Backlog-Items:**
| Item | Komponente | Team | Depends on |
|------|-----------|------|-----------|

**Teamabhängigkeiten:**
| Wer liefert | Was | An wen | Blockiert SOD? |
|------------|-----|--------|---------------|

**Angewandtes Learning:** [Verweis]

**Gate-Kriterien:**
- [ ] Zertifizierung abgeschlossen
- [ ] Feldtest-Learnings integriert
- [ ] Installer-Onboarding ready
- [ ] [Weitere aus Kontext ableitbare Kriterien]

**Offener Aufwand:** [oder „nicht im Kontext"]

---

## Bekannte Risiken & offene Fragen

| Risiko / Frage | Meilenstein | Quelle | Verantwortlich |
|----------------|------------|--------|---------------|
| ... | MS1 | learnings.md | ... |

## Was dieser Roadmap fehlt (Datenlücken)

<!-- Benenne explizit, was du NICHT aus dem Kontext ableiten konntest -->
- [ ] [Fehlende Information X] → nötig für [Meilenstein Y]
- [ ] [Fehlende Information Z] → nötig für [Gate-Kriterium]
```

---

## Checkliste: bereit für den ersten Lauf?

```
context/
  ✅ company.md          ausgefüllt (nicht nur Template)
  ✅ strategy.md         ausgefüllt
  ✅ product.md          Reference Architecture drin
  ✅ team.md             aktuelle + erwartete Struktur
  ✅ learnings.md        mind. 2 vergangene Projekte mit Muster
  ⚠️ roadmap.md         was ist committed? was konkurriert?
  ○  metrics.md          nice to have

input/
  ✅ jira-backlog.csv    Epic + relevante Stories + Estimates
  ✅ confluence-*.md     mind. Integration-Guidelines-Page
  ○  competitors.md      für Kür nötig, sonst Marktseite hohl
  ○  market-signals.md   für Kür nötig

CLAUDE.md
  ✅ Guardrail-Zeile     keine erfundenen Daten
```
