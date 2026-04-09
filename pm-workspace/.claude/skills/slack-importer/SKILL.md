---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: Slack Importer

Importiert und strukturiert Slack-Exporte für die Feedback-Analyse.

## Input

Der Pfad zum Slack-Export-Ordner wird beim Aufruf übergeben. Verwende Glob um alle Dateien im Ordner zu finden.

> **Hinweis:** Dieser Skill ist ein Platzhalter. Slack-Exportformate variieren je nach Plan und Konfiguration. Passe den Input-Abschnitt an dein spezifisches Exportformat an (JSON-Export, CSV-Export, oder kopierter Text).

## Vorgehen

1. **Dateien finden** — Verwende Glob um alle Dateien im übergebenen Ordner zu finden. Identifiziere das Format (JSON, CSV, Markdown/Text).

2. **Dateien lesen** — Lies jede gefundene Datei vollständig.

3. **Einträge strukturieren** — Extrahiere aus dem rohen Slack-Export einzelne Feedback-Einträge. Jeder Eintrag enthält:
   - **Datum:** Zeitstempel der Nachricht (Format: YYYY-MM-DD)
   - **Kanal:** Name des Slack-Kanals
   - **Autor:** Benutzername oder Anzeigename des Absenders
   - **Nachricht:** Vollständiger Nachrichtentext

4. **Filtern** — Überspringe System-Nachrichten, Bot-Nachrichten und Einträge ohne erkennbares Datum.

5. **Schreiben** — Schreibe alle strukturierten Einträge in das Output-Format.

## Schritt 0: Run-Verzeichnis bestimmen

Berechne das heutige Datum im Format YYYY-MM-DD. Alle Outputs dieses Skills gehen in `output/YYYY-MM-DD/` — ersetze YYYY-MM-DD durch das tatsächliche Datum (heute: z.B. `output/2026-04-09/`). Erstelle dieses Verzeichnis implizit durch den ersten Write-Aufruf.

## Output-Format

Schreibe `output/YYYY-MM-DD/discovery/slack-feedback.md` im cluster-ready Format:

```
# Slack Feedback

**Quelle:** Slack-Export
**Importiert:** [Datum des Imports]
**Anzahl Einträge:** [N]

---

## Eintrag 1
**Datum:** YYYY-MM-DD
**Kanal:** #[kanalname]
**Autor:** [benutzername]
**Nachricht:**
[vollständiger Nachrichtentext]

---

## Eintrag 2
...
```

## Output

Schreibe die strukturierten Einträge nach `output/YYYY-MM-DD/discovery/slack-feedback.md`.

## Qualitätskriterien

- Jeder Eintrag hat eine Quelle (Kanal + Autor)
- Keine Einträge ohne Datum
- Systembenachrichtigungen und automatische Bot-Nachrichten werden nicht als Feedback-Einträge aufgenommen
- Doppelte Einträge (z.B. durch mehrfache Exporte) werden nicht aufgenommen
