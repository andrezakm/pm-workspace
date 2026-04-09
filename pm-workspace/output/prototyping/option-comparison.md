# Option Vergleich: Feature Backlog Prioritizer

**Datum:** 2026-04-09

## Kern-UI-Entscheidung

Was ist das primäre Navigationselement — und welches mentale Modell bringt der Nutzer mit?

- Option A geht davon aus: Nutzer denkt in Tabellen, will vollständige Übersicht
- Option B geht davon aus: Nutzer orientiert sich am Chart, will dann ins Detail gehen
- Option C geht davon aus: Nutzer will keine Analyse — er will eine Entscheidung

## Übersicht

| Kriterium | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Interaktionsmodell | Filter → Tabelle + Chart parallel | Chart → Auswahl → Detail | Filter → Top-3-Kacheln + Rest ausklappbar |
| Informationshierarchie | Alle Features gleichwertig | Score-Ranking primär, Detail on demand | Top 3 prominent, Rest versteckt |
| Lernkurve für Nutzer | niedrig | niedrig | sehr niedrig |
| Primäre Frage die es beantwortet | "Was steht alles im Backlog?" | "Welches Feature hat welchen Score und warum?" | "Was bauen wir als nächstes?" |
| Eignet sich für | Überblick und Exploration | Analyse und Präsentation | Entscheidungs-Meetings |
| Beschreibung sichtbar | nein | ja (im Detail-Panel) | ja (in Kacheln) |
| Anzahl Klicks bis zur Entscheidung | 3–4 | 2–3 | 1 |

## Trade-offs

**Option A — Tabelle + Chart nebeneinander:**
Stärken: Vertraut, volle Datenkontrolle, alle Features auf einen Blick. Schwächen: Chart und Tabelle wiederholen dieselbe Information — der Nutzer muss selbst entscheiden wo er hinschaut. Kein Kontext zu den einzelnen Features (keine Beschreibung sichtbar).

**Option B — Chart zuerst, Drill-down:**
Stärken: Klare Hierarchie, Score ist primär, Beschreibung wird auf Anfrage angezeigt. Eignet sich gut für Präsentationen. Schwächen: Zwei Scroll-Ebenen (Chart + Tabelle unten). Nutzer muss aktiv ein Feature auswählen um Details zu sehen — das ist ein Klick der nicht intuitiv ist wenn man nur scannen will.

**Option C — Kachel-Entscheidungs-UI:**
Stärken: Radikale Fokussierung auf das Ergebnis. Top 3 sind sofort sichtbar mit allen relevanten Infos. Niedrigste kognitive Last. Rest ist ausklappbar aber nicht im Weg. Schwächen: Verliert den Überblick über das gesamte Backlog. Wer alle 12 Features vergleichen will, muss aufklappen. Ungewohnt für Nutzer die Analyse-Tools erwarten.

## Empfehlung

**Option C für Entscheidungs-Meetings mit der Geschäftsführung** — wenn die Frage "Was bauen wir als nächstes?" im Mittelpunkt steht und keine tiefe Analyse nötig ist.

**Option B für das Pattern-Team selbst** — wenn es darum geht, einzelne Features zu verstehen, zu erklären und Scores zu hinterfragen.

**Option A als Fallback** — wenn Nutzer explizit Tabellen-Kontrolle wollen oder das Tool für neue Nutzer eingeführt wird die das Scoring-Modell noch nicht kennen.
