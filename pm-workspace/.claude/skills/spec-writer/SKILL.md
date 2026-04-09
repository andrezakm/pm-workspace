---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten `Read`-, `Write`- und `Glob`-Tools. Keine MCP-Tools.

# Referenz: Spec schreiben

## Was eine Spec ist

Eine Spec beschreibt **Was** gebaut wird — nicht Wie. Sie ist Input für den Prototype Builder und Grundlage für die Eval.

## Input

- Der Pfad zum Brief wird beim Aufruf übergeben (z.B. "Führe spec-writer aus für input/mein-brief.md").
- Datendateien die im Brief referenziert werden

## Struktur einer Spec

```
# Spec: [Feature-Name]

## Zweck
Warum existiert dieses Feature? Welches Problem löst es?

## Nutzer
Wer verwendet es, welches technische Niveau?

## Daten-Input
Welche Datei(en) werden gelesen, in welchem Format?

## UI-Komponenten
1. [Komponente] — [Beschreibung]
2. ...

## Constraints
- Was wird explizit nicht gebaut
```

## Qualitätskriterien

- Beschreibt Was, nicht Wie — keine Implementierungsdetails
- Jede UI-Komponente ist konkret benannt und beschrieben
- Daten-Input benennt konkrete Felder aus den echten Datendateien
- Constraints sind explizit aufgelistet
- Kein Spekulieren über Dinge die nicht im Brief stehen

## Run-Verzeichnis

Der Run-Ordner ist `output/YYYY-MM-DD/` wobei YYYY-MM-DD das heutige Datum ist (z.B. `output/2026-04-09/`).

## Output

`output/YYYY-MM-DD/spec-eval/spec.md`
