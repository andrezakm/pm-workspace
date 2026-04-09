---
allowed-tools: Read, Write, Glob
---

> **Hinweis:** Verwende ausschließlich die eingebauten Tools. Keine MCP-Tools.

# Skill: Handoff Packager

Du bündelst alles was Dev braucht um zu starten. Kein neues Artefakt — du sammelst bestehende und schreibst ein Cover-Sheet.

## Input

Verwende Glob um zu prüfen welche der folgenden Dateien existieren:
- `output/spec-eval/spec.md` (Pflicht)
- `output/spec-eval/eval.md` (Pflicht)
- `output/prototyping/option-comparison.md` (optional)
- `output/prototyping/option-a/app.py`, `option-b/app.py`, `option-c/app.py` (optional)
- `output/prototyping/app.py` (optional, falls kein option-stormer gelaufen)
- `output/strategy/decision-brief.md` (optional)
- `context/product.md`
- `context/team.md`

Wenn spec.md oder eval.md fehlen: stoppe und melde welche Pflicht-Datei fehlt.

## Vorgehen

1. Prüfe mit Glob welche Dateien existieren.
2. Lies alle vorhandenen Dateien.
3. Schreibe das Cover-Sheet nach `output/handoff/handoff.md`.

## Qualitätskriterien

- Kein Copy-Paste aus den Quell-Dateien — nur Verweise (relative Pfade)
- "Nächste Schritte" sind konkret genug um sofort loszulegen
- Die Trennung PM-Eval vs. Dev-Eval ist explizit benannt
- Offene Fragen kommen aus dem Decision Brief, nicht erfunden

## Output: output/handoff/handoff.md

```
# Handoff: [Feature-Name aus Spec]

**Datum:** [Heute]
**Status:** Bereit für Entwicklung

## Zusammenfassung
[1 Satz was gebaut werden soll]

## Artefakte

| Dokument | Pfad | Status |
|----------|------|--------|
| Spec | output/spec-eval/spec.md | ✅ |
| Eval (PM) | output/spec-eval/eval.md | ✅ |
| Prototyp-Optionen | output/prototyping/option-comparison.md | ✅ / ⚠️ nicht vorhanden |
| Decision Brief | output/strategy/decision-brief.md | ✅ / ⚠️ nicht vorhanden |

## Was Dev als nächstes tun soll

1. [Konkreter Schritt 1]
2. [Konkreter Schritt 2]
3. [Konkreter Schritt 3]
4. [Optional: Schritt 4]
5. [Optional: Schritt 5]

## PM-Eval vs. Dev-Eval

**PM hat geprüft (via eval.md):** [Was wurde aus PM-Sicht evaluiert]
**Dev soll ergänzen:** [Was Dev in seiner eigenen Eval prüfen soll — Implementierungsdetails, Performance, Edge Cases]

## Offene Fragen & Risiken
[Aus dem Decision Brief, falls vorhanden. Sonst: leer lassen.]
- [Frage/Risiko 1]
- [Frage/Risiko 2]
```
