# PM Workspace — AI-Augmented PM, Woche 5

Ein modulares System für Product Manager, die mit Claude Code arbeiten. Von rohem Feedback bis zum Dev-Handoff — in einem Repo, mit einem gemeinsamen Kontext.

Dies ist das fünfte Modul des Kurses **AI-Augmented PM**: Die ersten vier Wochen bauen einzelne Skills. Diese Woche fügt sich alles zu **einem System** zusammen. Der Unterschied zwischen „14 Skills" und „einem System" ist **Kontext** — ein gemeinsames Fundament, das jeder Skill liest, bevor er arbeitet.

---

## Schnellstart

```bash
git clone https://github.com/andrezakm/pm-workspace.git
cd pm-workspace
claude            # Claude Code in genau diesem Ordner starten
```

Dann im Chat:

```
/kurs
```

`/kurs` ist der geführte Einstieg — er erklärt das System Schritt für Schritt. **Wichtig:** Claude Code muss in *diesem* Ordner laufen (hier liegt `.claude/skills/`), sonst sind die Kurse und Skills nicht verfügbar.

> Prototypen starten (optional): `python -m venv .venv && source .venv/bin/activate && pip install streamlit pandas`, dann `streamlit run output/YYYY-MM-DD/prototyping/app.py`.

---

## Die Kurse

Drei aufeinander aufbauende Kurse führen durch das System — jeder mit kleinen Aufgaben zum Mitdenken und Anpassen:

| Aufruf | Präsentation | Thema |
|---|---|---|
| `/kurs` | [doc/PM-System-Übersicht.html](doc/PM-System-Übersicht.html) | Das System verstehen — Struktur, Flows, Anpassung |
| `/zeig_mir_teamwork` | [doc/PM-Teamwork-Übersicht.html](doc/PM-Teamwork-Übersicht.html) | Teamwork — Zimmer / Wohnzimmer, Übergabe-Flow |
| `/mini_git_kurs` | [doc/Git-Grundlagen.html](doc/Git-Grundlagen.html) | Git — Versionierung, Branches, PRs |

**Optionaler Zusatz:** `/PTW-workshop` ([doc/PTW-Workshop-Anleitung.html](doc/PTW-Workshop-Anleitung.html)) — ein Play-to-Win-Strategie-Workshop mit vollständiger Fallstudie (LEGO 2004).

---

## Dokumentation — wo finde ich was?

- **Kurse & Präsentationen:** die vier HTML-Dateien in [`doc/`](doc/) (im Browser öffnen)
- **Skill-Details:** pro Skill ein `README.md` unter `.claude/skills/[name]/`
- **Kontext-Regel:** [CLAUDE.md](CLAUDE.md) — was jeder Skill liest, bevor er arbeitet
- **PTW-Demo-Lauf** (Beispiel-Output): Falldokumente in [`input/ptw-workshop/`](input/ptw-workshop/), vollständiger Lauf in [`output/2026-06-14/strategy/ptw-lego/`](output/2026-06-14/strategy/ptw-lego/)
- **Hintergrund — wie das System entstand:** [pm-system-overview.md](pm-system-overview.md) (Build-Spec), [pm-system-teststrategie.md](pm-system-teststrategie.md), [TeamworkinClaude.md](TeamworkinClaude.md), [InsightValidator.md](InsightValidator.md)

---

## Skill-Übersicht

Die Skills liegen technisch flach in `.claude/skills/` — konzeptuell sind sie in 7 Bereiche gegliedert:

```
Discovery
├── /feedback-synthesizer   Rohes Feedback → thematische Cluster
├── /interview-analyzer     Interviews → Einzel-Analysen + Synthese
└── /slack-importer         Slack-Export → strukturiertes Feedback (Platzhalter)

Strategy
├── /opportunity-scorer     Cluster → Scorecard (Vision / Wiederholbarkeit / Baubarkeit)
├── /decision-brief         Scorecard → 1-Pager (BUILD / SKIP / MEHR DATEN)
├── /devils-advocate        Brief → Annahmen-Kritik + Verdikt
├── /insight-validator      Insight → Validierung gegen Kontext + Experiment-Design
├── /business-case-debater  Vollständige Analyse: Research → Debatte → Synthese
└── /PTW-workshop           Play-to-Win Strategie-Workshop: 5 Perspektiven → Choice Cascade + Reverse Engineering

Roadmap
└── (Erweiterungspunkt — Plugin-Kandidaten: Linear, Jira, Notion)

Spec & Eval
├── /spec-writer            Brief → Spec (Was, nicht Wie)
├── /eval-writer            Spec → 8–12 pass/fail Kriterien
└── /build-eval             Orchestrator: Brief → Spec + Eval + Prototyp

Prototyping
├── /prototype-builder      Spec → eine Streamlit-App
├── /option-stormer         Spec → 3 strukturell verschiedene Apps + Vergleich
└── /eval-runner            Eval + App → PASS/FAIL/UNKLAR pro Kriterium

Handoff
└── /handoff-packager       Alle Artefakte → Cover-Sheet für Dev

Meta
└── /system-auditor         Workspace-Audit: was fehlt, was als nächstes tun
```

---

## Typischer Flow

```
input/raw_feedback/         input/interviews/
        ↓                           ↓
/feedback-synthesizer       /interview-analyzer
        ↓
/opportunity-scorer
        ↓
/decision-brief
        ↓
/devils-advocate
        ↓
/spec-writer [brief]
        ↓
/option-stormer             (oder /build-eval für alles auf einmal)
        ↓
/eval-runner
        ↓
/handoff-packager
```

Alle Outputs landen in `output/YYYY-MM-DD/` — ein Run, ein Verzeichnis.

---

## Architektur

- **Skills:** `.claude/skills/[name]/SKILL.md` — aufgerufen mit `/name`
- **Kontext:** `context/` — wird von jedem Skill gelesen (Regel in `CLAUDE.md`)
- **Input:** `input/` — Rohdaten, Briefs, Datendateien
- **Output:** `output/YYYY-MM-DD/` — ein Verzeichnis pro Run
- **Scripts:** `scripts/` — persönliche Sandbox für neue Skills in Entwicklung

**Skill-Entwicklungs-Flow:** `scripts/` → `SKILL.md` → Branch → PR → Review → Merge.
`CLAUDE.md` ist bewusst kurz. Details zu jedem Skill: `.claude/skills/[name]/README.md`.

---

## Empfohlener Kurs-Flow

```
Schritt 1 — Alleine starten
  /kurs                System verstehen, Notizen machen · context/ befüllen
                       /system-auditor · ersten Flow manuell durchlaufen

Schritt 2 — Mit dem Team
  /zeig_mir_teamwork   Teamwork-Prinzipien (Zimmer / Wohnzimmer)
  /mini_git_kurs       Git-Grundlagen — jetzt ergibt es Sinn

Schritt 3 — Plan machen
  „Hier sind meine Notizen aus den Kursen. Hilf mir, einen konkreten Plan zu
   erstellen: was passe ich an, welchen Flow starte ich, was baue ich neu?"
```

---

## Verzeichnisstruktur

```
.
├── README.md            ← dieses Dokument
├── CLAUDE.md            Kontext-Regel — was jeder Skill liest
├── context/             das Fundament: company, strategy, product, team, …
├── input/               Rohdaten (inkl. ptw-workshop/ Fallbeispiel)
├── output/              Ergebnisse, ein Ordner pro Run
├── doc/                 die vier HTML-Präsentationen
├── scripts/             persönliche Sandbox für neue Skills
├── .claude/skills/      die Skills (je mit eigenem README)
└── *.md                 Hintergrund-Specs (Build-Spec, Teststrategie, Teamwork …)
```
