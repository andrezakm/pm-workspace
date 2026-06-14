# PM Workspace

Ein modulares System für Product Manager die mit Claude Code arbeiten.
Von rohem Feedback bis zum Dev-Handoff — in einem Repo, mit einem gemeinsamen Kontext.

## Wie starten

1. Repo klonen
2. Python-Umgebung einrichten (einmalig):
   ```bash
   python -m venv .venv && source .venv/bin/activate && pip install streamlit pandas
   ```
3. Claude Code öffnen im `pm-workspace/` Ordner
4. `context/` befüllen — dein Unternehmen, deine Strategie, dein Team
5. Starte mit: `/system-auditor`

> Prototypen starten: `.venv` aktivieren, dann `streamlit run output/YYYY-MM-DD/prototyping/app.py`

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

## Prototyping-Prinzip

Drei Varianten, dann entscheiden — nicht eine Lösung und hoffen. Fällt eine Variante durch die Eval, heißt das nicht verwerfen: welche Prinzipien funktionieren? Rekombination aus mehreren Optionen führt oft zu besseren Ergebnissen als Iteration auf einer.

---

## Architektur

- Skills: `.claude/skills/[name]/SKILL.md` — aufgerufen mit `/name`
- Kontext: `context/` — wird von jedem Skill gelesen
- Input: `input/` — Rohdaten, Briefs, Datendateien
- Output: `output/YYYY-MM-DD/` — ein Verzeichnis pro Run
- Scripts: `scripts/` — persönliche Sandbox für neue Skills in Entwicklung

**Skill-Entwicklungs-Flow:** `scripts/` → `SKILL.md` → Branch → PR → Review → Merge

CLAUDE.md ist bewusst kurz. Details zu jedem Skill: `.claude/skills/[name]/README.md`.

---

## Kurse und Präsentationen

| Kurs | Präsentation | Thema |
|------|-------------|-------|
| `/kurs` | `doc/PM-System-Übersicht.html` | Das System verstehen: Struktur, Flows, Anpassung |
| `/zeig_mir_teamwork` | `doc/PM-Teamwork-Übersicht.html` | Teamwork: Zimmer/Wohnzimmer, Übergabe-Flow |
| `/mini_git_kurs` | `doc/Git-Grundlagen.html` | Git: Versionierung, Branches, PRs — das Werkzeug hinter dem Flow |

**Empfohlener Kurs-Flow:**

```
Schritt 1 — Alleine starten
  /kurs                       System verstehen, Notizen machen
  → doc/PM-System-Übersicht.html als Referenz
  → context/ befüllen, /system-auditor, ersten Flow manuell durchlaufen

Schritt 2 — Mit dem Team
  /zeig_mir_teamwork          Teamwork-Prinzipien, Notizen machen
  → doc/PM-Teamwork-Übersicht.html für Team-Gespräch nutzen
  /mini_git_kurs              Git-Grundlagen — jetzt macht es Sinn
  → doc/Git-Grundlagen.html als Referenz

Schritt 3 — Plan machen
  Claude: "Hier sind meine Notizen aus beiden Kursen.
           Hilf mir einen konkreten Plan zu erstellen."
```
