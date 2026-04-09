---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: Interview Analyzer

Du analysierst qualitative Interview-Dateien und erzeugst zwei Outputs: eine Einzel-Analyse pro Interview und eine Synthese über alle Interviews.

## Input

Der Pfad zum Ordner mit Interview-.md-Dateien wird beim Aufruf übergeben. Verwende Glob um alle .md-Dateien im Ordner zu finden.

## Vorgehen

### Schritt 1 — Einzel-Analysen

Lies jede Interview-Datei einzeln und erstelle eine Einzel-Analyse pro Interview. Gehe die Dateien nacheinander durch — eine nach der anderen.

Jede Einzel-Analyse muss alle 6 Dimensionen abdecken:

**1. Interviewee Profile**
- Name, Rolle, Datum des Interviews
- Ein Absatz, der beschreibt, wer diese Person in der Organisation ist und durch welche Linse sie die Welt sieht

**2. Sentiment**
- Dominanter emotionaler Ton (spezifisch — nicht nur "frustriert", sondern welche Art und warum)
- Energielevel: ausgebrannt, aufgeladen, resigniert, defensiv?
- Vertrauenslevel: vertraut die Person ihren Tools, Kollegen, der Führung?
- Ein Direktzitat, das den emotionalen Zustand am besten einfängt

**3. Problems They Described**
- Jedes genannte Problem, direkt oder impliziert
- Pro Problem: was ist es, wie wurde es beschrieben, wie viel Schmerz wurde ausgedrückt?

**4. Urgency Signals**
- Welche Probleme wurden als dringend, drängend oder aktuell kostenverursachend markiert?
- Achte auf Sprache wie "right now", "every day", "I can't", "it's killing us", Zahlen und Metriken, emotionale Intensitätsspitzen

**5. Underlying Needs**
- Was braucht diese Person wirklich, um ihren Job gut zu machen?
- Formuliere jedes Bedürfnis als: "Diese Person braucht X, damit Y"
- Unterscheide zwischen dem, was sie sagt zu wollen, und dem, was sie wirklich braucht

**6. Notable Quotes**
- 3–5 Direktzitate, die lebendig, spezifisch oder besonders aufschlussreich sind

Speichere jede Einzel-Analyse nach: `output/discovery/interview-individual-[nachname].md`

### Schritt 2 — Synthese über alle Interviews

Nachdem alle Einzel-Analysen abgeschlossen sind, lies alle erzeugten Output-Dateien und erstelle ein einzelnes Synthese-Dokument.

Die Synthese muss folgende 4 Abschnitte enthalten:

**1. Sentiment Across the Group**
- Tabelle: Interviewee | Rolle | Dominantes Sentiment
- Gesamtabsatz: Was ist das emotionale Klima dieser Organisation? Gibt es Muster über Hierarchieebenen hinweg (Führung vs. operative Ebene)? Wer ist ein Ausreißer und warum?

**2. Main Problems (cross-interview)**
- Probleme gruppieren und konsolidieren, die in mehreren Interviews auftauchen
- Pro konsolidiertem Problem: benennen, beschreiben, auflisten welche Interviewees es erwähnt haben und wie
- Ranken nach Häufigkeit (wie viele Personen haben es erwähnt) und Tiefe (wie viel Schmerz hat es verursacht)

**3. Urgent Problems**
- Aus der konsolidierten Liste nur diejenigen identifizieren, die direkte, messbare Auswirkungen heute haben
- Erklären, was heute dadurch verloren geht oder sich verschlechtert
- Konkrete Belege aus konkreten Interviews referenzieren

**4. High-Level Summary**
- Maximal 2–3 Absätze
- Frage beantworten: Was ist die einzige Grundursache? Was wäre die Intervention mit dem höchsten Hebel?
- Direkt und ohne Absicherungen. Aus den Belegen sprechen.

Speichere die Synthese nach: `output/discovery/interview-synthesis.md`

## Qualitätskriterien

- Mindestens 2 Belege pro Cluster in der Synthese (Direktzitat oder konkrete Paraphrase mit Quellenangabe)
- Kein konsolidiertes Problem ohne mindestens 2 unabhängige Nennungen
- Keine Interpretation die nicht direkt aus dem Datenmaterial ableitbar ist
- Widersprüche explizit dokumentieren, nicht glätten

## Output

- Eine Datei pro Interviewee: `output/discovery/interview-individual-[nachname].md`
- Eine Synthese-Datei: `output/discovery/interview-synthesis.md`
- Diese Skill-Anweisungen nicht in Output-Dateien aufnehmen
