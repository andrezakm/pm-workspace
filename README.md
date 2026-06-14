# AI-Augmented PM · Woche 5 — The System

Das fünfte Modul des Kurses **AI-Augmented PM**. Die ersten vier Wochen bauen einzelne Skills — Interviews analysieren, Opportunities scoren, Specs schreiben, Prototypen bauen. Diese Woche fügt sich alles zu **einem System** zusammen: dem `pm-workspace`.

Ein System ist kein Stapel Skills. Der Unterschied ist **Kontext** — ein gemeinsames Fundament, das jeder Skill liest, bevor er arbeitet. Von rohem Feedback bis zum Dev-Handoff, in einem Repo.

---

## Schnellstart

```bash
cd pm-workspace
# einmalig: Python-Umgebung für Prototypen
python -m venv .venv && source .venv/bin/activate && pip install streamlit pandas
# dann Claude Code im pm-workspace/ öffnen
```

1. `context/` befüllen — dein Unternehmen, deine Strategie, dein Team
2. `/system-auditor` — zeigt, was fehlt und was als Nächstes kommt
3. Einen Flow einmal manuell durchlaufen

Details: **[pm-workspace/README.md](pm-workspace/README.md)**.

---

## Dokumentation — wo finde ich was?

### Kurse & Präsentationen (im Browser öffnen)

Die vier HTML-Präsentationen in **[`pm-workspace/doc/`](pm-workspace/doc/)** sind das Herz der Teilnehmer-Doku. Jede wird auch über einen Skill aufgerufen:

| Aufruf | Präsentation | Thema |
|---|---|---|
| `/kurs` | [PM-System-Übersicht.html](pm-workspace/doc/PM-System-Übersicht.html) | Das System verstehen — Struktur, Flows, Anpassung |
| `/zeig_mir_teamwork` | [PM-Teamwork-Übersicht.html](pm-workspace/doc/PM-Teamwork-Übersicht.html) | Teamwork — Zimmer / Wohnzimmer, Übergabe-Flow |
| `/mini_git_kurs` | [Git-Grundlagen.html](pm-workspace/doc/Git-Grundlagen.html) | Git — Versionierung, Branches, PRs |
| `/PTW-workshop` | [PTW-Workshop-Anleitung.html](pm-workspace/doc/PTW-Workshop-Anleitung.html) | Strategie-Skill **Play to Win** + vollständige Fallstudie LEGO 2004 |

> Die drei erstgenannten sind Slide-Decks (reveal.js), die PTW-Anleitung ein blätterbares Deck im überproduct-Design (← / → blättern, **F** Vollbild).

### System-Referenz

- **[pm-workspace/README.md](pm-workspace/README.md)** — Skill-Übersicht (7 Bereiche), typischer Flow, Architektur, der empfohlene Kurs-Flow
- **[pm-workspace/CLAUDE.md](pm-workspace/CLAUDE.md)** — die Kontext-Regel, die jeder Skill befolgt
- **Skill-Details** — pro Skill ein `README.md` unter `pm-workspace/.claude/skills/[name]/`

### Der PTW-Demo-Lauf (Beispiel-Output)

Ein vollständiger, dokumentierter Workshop-Lauf am LEGO-Turnaround liegt als Beispiel bei:

- **Falldokumente:** [`pm-workspace/input/ptw-workshop/`](pm-workspace/input/ptw-workshop/) — rekonstruiertes Lehrbeispiel, neutralisiert
- **Ergebnis-Run:** [`pm-workspace/output/2026-06-14/strategy/ptw-lego/`](pm-workspace/output/2026-06-14/strategy/ptw-lego/) — alle sechs Schritte, vom Einzel-Befund bis zum finalen Strategieentwurf

### Hintergrund — wie das System entstand

Spezifikations- und Methodik-Dokumente (für Neugierige, nicht für den Einstieg nötig):

| Datei | Inhalt |
|---|---|
| [pm-system-overview.md](pm-system-overview.md) | Build-Spec — die Arbeitsanweisung, mit der der `pm-workspace` gebaut wurde |
| [pm-system-teststrategie.md](pm-system-teststrategie.md) | Teststrategie in drei Ebenen |
| [TeamworkinClaude.md](TeamworkinClaude.md) | Wie ein PM-Team mit demselben System arbeitet |
| [InsightValidator.md](InsightValidator.md) | Skill-Spezifikation: mehrstufige Insight-Validierung |
| [call-highlights-woche5.md](call-highlights-woche5.md) | Sprechzettel für den Woche-5-Call |

---

## Verzeichnisstruktur

```
Woche5TheSystem/
├── README.md                  ← dieses Dokument
├── pm-workspace/              ← das System (hier wird gearbeitet)
│   ├── README.md              Skill-Übersicht, Flows, Architektur
│   ├── CLAUDE.md              Kontext-Regel
│   ├── context/               das Fundament — company, strategy, product, …
│   ├── input/                 Rohdaten (inkl. ptw-workshop/ Fallbeispiel)
│   ├── output/                Ergebnisse, ein Ordner pro Run
│   ├── doc/                   die vier HTML-Präsentationen
│   ├── scripts/               persönliche Sandbox für neue Skills
│   └── .claude/skills/        die Skills (je mit eigenem README)
└── *.md                       Begleit-Specs & Call-Material (s. o.)
```

---

## Empfohlener Kurs-Flow

```
Schritt 1 — Alleine starten
  /kurs            System verstehen · context/ befüllen · /system-auditor · ersten Flow durchlaufen

Schritt 2 — Mit dem Team
  /zeig_mir_teamwork   Teamwork-Prinzipien
  /mini_git_kurs       Git-Grundlagen — jetzt ergibt es Sinn

Schritt 3 — Strategie vertiefen
  /PTW-workshop        Play-to-Win-Workshop fahren — oder die LEGO-Fallstudie nachlesen

Schritt 4 — Plan machen
  Notizen aus den Kursen zusammenführen und einen konkreten Plan bauen
```
