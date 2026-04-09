# Option Vergleich: Feature Backlog Prioritizer

**Datum:** 2026-04-09

## Kern-UI-Entscheidung

Was ist das primäre Navigationselement — und welches mentale Modell bringt der Nutzer mit?

## Übersicht

| Kriterium | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Interaktionsmodell | Filter → Tabelle + Chart parallel | Chart → Auswahl → Detail | Filter → Top-3-Kacheln + Rest ausklappbar |
| Informationshierarchie | Alle Features gleichwertig | Score primär, Detail on demand | Top 3 prominent, Rest versteckt |
| Lernkurve | niedrig | niedrig | sehr niedrig |
| Primäre Frage | "Was steht im Backlog?" | "Welcher Score und warum?" | "Was bauen wir jetzt?" |
| Beschreibung sichtbar | nein | ja (Detail-Panel) | ja (Kacheln) |
| Spec-konform | ja | ja | nein (kein Chart → E7/E8 FAIL) |

## Trade-offs

**Option A:** Vertraut, vollständige Datenkontrolle. Chart und Tabelle wiederholen dieselbe Information.

**Option B:** Klare Hierarchie, Score primär, Beschreibung on demand. Gut für Präsentationen und Analyse.

**Option C:** Radikale Fokussierung auf Entscheidung. Beschreibungstext sichtbar. Verletzt E7/E8 (kein Balkendiagramm). Wertvoll als Inspiration für hybride Lösung.

## Empfehlung

**Option B für Analyse und Präsentation.** Option C als Inspiration: Top-3-Block in B einbauen, Spec um diese Anforderung erweitern.
