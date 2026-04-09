PM SYSTEM — TESTSTRATEGIE
══════════════════════════════════════════════════

Drei Ebenen. Von innen nach außen. Jede Ebene muss
bestanden sein bevor die nächste Sinn ergibt.


══════════════════════════════════════════════════
EBENE 1: EINZELNE SKILLS FUNKTIONIEREN
══════════════════════════════════════════════════

Ziel: Jeder Skill nimmt Input, produziert Output,
erfüllt seine eigenen Qualitätskriterien.

KOPIERTE SKILLS (aus Week 3 + 4, neue Pfade):

  □ feedback-synthesizer
    Input:  Testdaten aus NeoEmployee (raw_feedback.md)
    Prüfen: Output landet in output/discovery/clusters.md
    Prüfen: Cluster-Format stimmt, Belege vorhanden

  □ opportunity-scorer
    Input:  output/discovery/clusters.md + context/company.md + context/strategy.md
    Prüfen: Liest er context/ statt input/? (Pfad-Änderung!)
    Prüfen: Output in output/strategy/scored.md

  □ decision-brief
    Input:  output/strategy/scored.md + context/strategy.md
    Prüfen: Output in output/strategy/decision-brief.md
    Prüfen: Format: Muster, Für wen, Warum jetzt, Empfehlung, Offene Fragen

  □ devils-advocate
    Input:  output/strategy/decision-brief.md
    Prüfen: Output in output/strategy/devils-advocate.md
    Prüfen: 3 echte Gegenargumente, nicht höflich

  □ spec-writer
    Input:  Ein brief.md (NeoEmployee Onboarding-Brief als Testcase)
    Prüfen: Output in output/spec-eval/spec.md
    Prüfen: Was, nicht Wie. Keine Implementierungsdetails.

  □ eval-writer
    Input:  output/spec-eval/spec.md
    Prüfen: Output in output/spec-eval/eval.md
    Prüfen: 8-12 Kriterien, alle pass/fail, Ergebnis-Spalte leer

  □ build-eval (Orchestrator)
    Input:  Ein brief.md
    Prüfen: Erzeugt er spec.md, eval.md UND app.py?
    Prüfen: Respektiert er existierende Files (kein Überschreiben)?

  □ prototype-builder
    Input:  output/spec-eval/spec.md
    Prüfen: Output in output/prototyping/app.py
    Prüfen: streamlit run läuft ohne Fehler

  □ eval-runner
    Input:  output/spec-eval/eval.md + output/prototyping/app.py
    Prüfen: Output in output/prototyping/eval-results.md
    Prüfen: Jeder Punkt hat Status + Begründung

KONVERTIERTE SKILLS (aus Week 1 + 2):

  □ interview-analyzer
    Input:  3-4 Test-Interviews aus Week 1 Repo
    Prüfen: Output in output/discovery/interview-synthesis.md
    Prüfen: Cluster-Format konsistent mit feedback-synthesizer

  □ business-case-debater
    Input:  output/strategy/decision-brief.md
    Prüfen: Output in output/strategy/debate-synthesis.md
    Prüfen: Alle 5 Rollen haben eine Sektion, Synthese am Ende

NEUE SKILLS:

  □ option-stormer
    Input:  output/spec-eval/spec.md
    Prüfen: 3 Varianten in output/prototyping/option-a/, -b/, -c/
    Prüfen: Alle 3 starten mit streamlit run
    Prüfen: option-comparison.md existiert, Trade-offs benannt
    Prüfen: Unterschiede sind strukturell, nicht kosmetisch

  □ handoff-packager
    Input:  output/spec-eval/ + output/prototyping/ + context/
    Prüfen: Output in output/handoff/handoff.md
    Prüfen: Cover-Sheet mit Links, nächste Schritte, PM-Eval vs. Dev-Eval
    Prüfen: Kein Copy-Paste, nur Verweise

  □ system-auditor
    Input:  Gesamter pm-workspace/
    Prüfen: Output in output/meta/system-audit.md
    Prüfen: Ampelsystem für alle Files
    Prüfen: Erkennt ausgefüllte vs. leere Templates korrekt


══════════════════════════════════════════════════
EBENE 2: DIE KETTE FUNKTIONIERT
══════════════════════════════════════════════════

Ziel: Ein Case komplett durchspielen, Ende zu Ende.
Jeder Skill liest was der vorherige geschrieben hat.

TESTCASE: NeoEmployee Onboarding-Agent

Vorbereitung:
  □ context/ mit NeoEmployee-Daten befüllt
    (company.md, strategy.md aus Week 3 Repo übernehmen)
  □ NeoEmployee raw_feedback.md als Testdaten bereit
  □ Alle output/ Ordner leer

Durchlauf:

  Schritt 1: Discovery
  □ "Führe /feedback-synthesizer aus auf [raw_feedback]"
  □ Prüfen: output/discovery/clusters.md existiert

  Schritt 2: Strategy
  □ "Führe /opportunity-scorer aus"
  □ Prüfen: Liest er clusters.md UND context/company.md + context/strategy.md?
  □ Prüfen: output/strategy/scored.md existiert

  □ "Führe /decision-brief aus"
  □ Prüfen: output/strategy/decision-brief.md existiert
  □ Prüfen: Empfehlung ist BUILD (wir wissen dass Onboarding gewinnt)

  □ "Führe /devils-advocate aus"
  □ Prüfen: Bezieht sich auf den richtigen Decision Brief

  Schritt 3: Spec & Eval
  □ Brief für Onboarding-Agent schreiben (manuell, 1 Seite)
  □ "Führe /spec-writer aus für [brief]"
  □ Prüfen: output/spec-eval/spec.md

  □ "Führe /eval-writer aus"
  □ Prüfen: output/spec-eval/eval.md
  □ Prüfen: Kriterien passen zur Spec

  Schritt 4: Prototyping
  □ "Führe /option-stormer aus"
  □ Prüfen: 3 Varianten, alle lauffähig
  □ Prüfen: comparison.md zeigt echte Unterschiede

  □ Beste Variante wählen
  □ "Führe /eval-runner aus"
  □ Prüfen: Ergebnis referenziert die richtige app.py

  Schritt 5: Handoff
  □ "Führe /handoff-packager aus"
  □ Prüfen: Links in handoff.md zeigen auf echte Files
  □ Prüfen: Nächste Schritte sind konkret

  Schritt 6: Meta
  □ "Führe /system-auditor aus"
  □ Prüfen: Erkennt alle erzeugten Artefakte
  □ Prüfen: Markiert nicht-befüllte Context-Files korrekt

KETTEN-SPEZIFISCHE FEHLERQUELLEN:

  □ Pfad-Konsistenz: Schreibt Skill A in denselben Pfad
    den Skill B als Input erwartet?
  □ Context-Loading: Liest jeder Skill die context/ Files
    oder arbeitet er im Vakuum?
  □ Überschreiben: Was passiert wenn output/ schon
    Artefakte enthält? Überschrieben, ignoriert, Fehler?
  □ CLAUDE.md Routing: Wenn du sagst "analysiere das
    Feedback" — findet Claude den richtigen Skill?


══════════════════════════════════════════════════
EBENE 3: DER TEILNEHMER KOMMT KLAR
══════════════════════════════════════════════════

Ziel: Jemand ohne Vorwissen klont das Repo und
findet sich zurecht.

COLD START TEST:

  □ Repo klonen, Claude Code öffnen
  □ Ohne Anleitung: versteht der Teilnehmer was das ist?
  □ README.md reicht als Einstieg?
  □ "Führe /system-auditor aus" als erster Befehl —
    sagt ihm das Ergebnis was er als nächstes tun soll?

CONTEXT-AUSFÜLL-TEST:

  □ Teilnehmer öffnet context/company.md
  □ Ist klar was reingehört?
  □ Ist das NeoEmployee-Beispiel hilfreich oder verwirrend?
  □ Wie lange dauert es alle 7 Files auszufüllen?
    (Ziel: unter 30 Minuten)

ERSTER SKILL-TEST:

  □ Teilnehmer führt einen Skill aus (z.B. decision-brief)
  □ Findet er den Skill? Weiß er wie er ihn aufruft?
  □ Liest Claude automatisch den Context? Oder muss
    der Teilnehmer es explizit sagen?
  □ Ist der Output wo er ihn erwartet?

ORIENTIERUNGS-TEST:

  □ Nach 30 Minuten: weiß der Teilnehmer welche Skills
    existieren und was sie tun?
  □ Weiß er wo seine Artefakte liegen?
  □ Versteht er den Unterschied context/ vs. output/?
  □ Kann er erklären was die CLAUDE.md tut?

FEHLER-TEST:

  □ Was passiert wenn context/ leer ist und er einen
    Skill ausführt? Sinnvolle Fehlermeldung oder Müll-Output?
  □ Was passiert wenn er einen Skill aufruft der nicht
    existiert? Hilft Claude weiter?
  □ Was passiert wenn output/ schon voll ist von einem
    vorherigen Durchlauf?


══════════════════════════════════════════════════
REIHENFOLGE
══════════════════════════════════════════════════

1. Ebene 1 komplett durchlaufen.
   Jeden Skill einzeln. Abhaken. Kaputte fixen.
   Zeitschätzung: 2-3 Stunden.

2. Ebene 2 einmal durchspielen.
   NeoEmployee End-to-End. Kette prüfen.
   Zeitschätzung: 1-2 Stunden.

3. Ebene 2 Fehler fixen.
   Erfahrungsgemäß: Pfade, Context-Loading,
   Überschreib-Verhalten.
   Zeitschätzung: 1-2 Stunden.

4. Ebene 3 mit frischen Augen.
   Selbst als Neuling durchgehen oder jemanden bitten.
   Zeitschätzung: 1 Stunde.

5. Fixes aus Ebene 3 einarbeiten.
   Meistens: README anpassen, CLAUDE.md nachschärfen,
   Fehlermeldungen verbessern.
   Zeitschätzung: 1 Stunde.

Gesamt: ~1 Tag realistisch.


══════════════════════════════════════════════════
ANWEISUNG FÜR CLAUDE CODE CLI
══════════════════════════════════════════════════

Wenn du dieses File liest um das System zu testen:

1. Arbeite Ebene 1 Skill für Skill ab.
   Markiere jeden mit ✅ oder ❌.
   Bei ❌: beschreibe was kaputt ist, fix es, teste nochmal.

2. Für Ebene 2: lösche output/ komplett, starte frisch.
   Dann den Durchlauf Schritt für Schritt.
   Jeder Schritt einzeln — nicht alles auf einmal.

3. Für Ebene 3: du kannst das nur begrenzt simulieren.
   Aber: teste den Cold Start. Klone das Repo in einen
   neuen Ordner, öffne Claude Code, tu so als wüsstest
   du nichts. Fang mit README an. Schau was passiert.
