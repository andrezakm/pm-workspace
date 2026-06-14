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

## Schritt 0: Run-Verzeichnis bestimmen

Berechne das heutige Datum im Format YYYY-MM-DD. Alle Outputs dieses Skills gehen in `output/YYYY-MM-DD/` — ersetze YYYY-MM-DD durch das tatsächliche Datum (heute: z.B. `output/2026-04-09/`). Erstelle dieses Verzeichnis implizit durch den ersten Write-Aufruf.

## Output

`output/YYYY-MM-DD/spec-eval/spec.md`
