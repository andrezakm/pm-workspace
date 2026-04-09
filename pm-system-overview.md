PM SYSTEM — BUILD SPEC FÜR CLAUDE CODE CLI
══════════════════════════════════════════════════

Dieses Dokument ist die Arbeitsanweisung für Claude Code CLI.
Ziel: Ein Starter-Kit Repo bauen das Kursteilnehmer klonen und
mit eigenem Kontext befüllen.


══════════════════════════════════════════════════
PHASE 1: ORDNERSTRUKTUR ANLEGEN
══════════════════════════════════════════════════

Lege folgende Struktur an. Noch keine Inhalte, nur Ordner und leere Dateien.

```
pm-workspace/
├── CLAUDE.md
├── context/
│   ├── company.md
│   ├── strategy.md
│   ├── product.md
│   ├── team.md
│   ├── metrics.md
│   ├── learnings.md
│   └── roadmap.md
├── skills/
│   ├── README.md                          ← Folder-Index: alle Skills, 1 Zeile je Skill
│   ├── discovery/
│   │   ├── README.md                      ← Folder-Index: Discovery-Skills
│   │   ├── feedback-synthesizer/SKILL.md
│   │   ├── interview-analyzer/SKILL.md
│   │   └── slack-importer/SKILL.md
│   ├── strategy/
│   │   ├── README.md                      ← Folder-Index: Strategy-Skills
│   │   ├── opportunity-scorer/SKILL.md
│   │   ├── decision-brief/SKILL.md
│   │   ├── devils-advocate/SKILL.md
│   │   └── business-case-debater/SKILL.md
│   ├── roadmap/
│   │   └── README.md                      ← Folder-Index: Roadmap-Skills (+ Plugin-Hinweis)
│   ├── spec-eval/
│   │   ├── README.md                      ← Folder-Index: Spec/Eval-Skills + Handoff-Erklärung
│   │   ├── spec-writer/SKILL.md
│   │   ├── eval-writer/SKILL.md
│   │   └── build-eval/SKILL.md
│   ├── prototyping/
│   │   ├── README.md                      ← Folder-Index: Prototyping-Skills
│   │   ├── prototype-builder/SKILL.md
│   │   ├── eval-runner/SKILL.md
│   │   └── option-stormer/SKILL.md
│   ├── handoff/
│   │   ├── README.md                      ← Folder-Index: Handoff-Skills
│   │   └── handoff-packager/SKILL.md
│   └── meta/
│       ├── README.md                      ← Folder-Index: Meta-Skills
│       └── system-auditor/SKILL.md
├── output/
│   ├── discovery/.gitkeep
│   ├── strategy/.gitkeep
│   ├── roadmap/.gitkeep
│   ├── spec-eval/.gitkeep
│   ├── prototyping/.gitkeep
│   ├── handoff/.gitkeep
│   └── meta/.gitkeep
└── README.md
```


══════════════════════════════════════════════════
PHASE 2: CONTEXT-TEMPLATES SCHREIBEN
══════════════════════════════════════════════════

Jedes File in context/ bekommt exakt diese Struktur:
1. Titel + 2-3 Sätze was hier reingehört
2. Beispiel aus NeoEmployee (damit es konkret ist)
3. Platzhalter-Abschnitt "## Dein Kontext" (leer, hier füllt der Teilnehmer aus)

Hier die Inhalte:

--- context/company.md ---

# Company

Wer bist du, was macht dein Unternehmen, wie verdient ihr Geld.
Claude liest dieses File als erstes um zu verstehen in welchem
Kontext alle anderen Artefakte stehen.

## Beispiel: NeoEmployee

NeoEmployee baut custom AI Agents die Mitarbeiterfähigkeiten in
Unternehmen ersetzen. Wir arbeiten als Beratung auf
Time-&-Material-Basis. Jeder Agent wird individuell für den
Kunden gebaut — keine Produkte von der Stange.

## Dein Kontext

<!-- Ersetze das Beispiel mit deinem eigenen Unternehmen -->


--- context/strategy.md ---

# Strategy

Wo steht ihr gerade, welche Constraints gelten, was ist das Ziel.
Dieses File steuert wie Skills Empfehlungen gewichten — ein
bootstrapped Startup bekommt andere Prioritäten als ein
Series-B-Unternehmen.

## Beispiel: NeoEmployee

Bootstrapped. Kein Investor, keine Bankkredite. Revenue ist Runway.
Alles was Geld bringt und zur Vision passt, machen wir.
Langfristig: produktisierbare Agenten. Kurzfristig: Custom-Projekte
die den Cashflow sichern. 2 von 14 Leuten suchen nach Mustern
über Kundenprojekte hinweg — das sind die Samen für Produkte.

## Dein Kontext

<!-- Ersetze das Beispiel mit deiner eigenen Strategie -->


--- context/product.md ---

# Product

Was existiert schon. Features, Tech Stack, Architektur-Überblick.
Dieses File verhindert dass Skills Dinge vorschlagen die es
schon gibt oder die mit dem bestehenden Stack kollidieren.

## Beispiel: NeoEmployee

Kein eigenes Produkt bisher. Portfolio aus Custom-Agents:
Onboarding-Bots (4x gebaut), Meeting-Summarizer (4x gebaut),
Tier-1-Support-Agents (2x angefragt). Stack: Python, LangChain,
verschiedene LLMs je nach Kunde. Deployment: kundenspezifisch.

## Dein Kontext

<!-- Ersetze das Beispiel mit deinem eigenen Produkt -->


--- context/team.md ---

# Team

Wer macht was, wie viele Leute, welche Kapazität ist verfügbar.
Dieses File steuert ob Skills Empfehlungen als "baubar" oder
"zu ambitioniert für die aktuelle Teamgröße" einordnen.

## Beispiel: NeoEmployee

14 Leute. 10 Engineers auf Kundenprojekten. 2 im Pattern-Team
(Lisa, Tom). 1 PM. 1 Gründer/CEO. Keine Designer.
Kapazität für Produktarbeit: nur was Lisa und Tom neben den
Kundenprojekten schaffen.

## Dein Kontext

<!-- Ersetze das Beispiel mit deinem eigenen Team -->


--- context/metrics.md ---

# Metrics

Was messt ihr, was sind die aktuellen Werte, wo ist die Baseline.
Dieses File gibt Skills einen Anker für "besser" oder "schlechter" —
ohne Baseline ist jede Verbesserung Behauptung.

## Beispiel: NeoEmployee

Revenue: X€/Monat (reicht für Y Monate Runway).
Kundenprojekte: 6 aktiv, 3 in Pipeline.
Wiederkehrende Muster: Onboarding (4x), Meeting-Summary (4x).
Noch keine Produktmetriken — es gibt kein Produkt.

## Dein Kontext

<!-- Ersetze das Beispiel mit deinen eigenen Metriken -->


--- context/learnings.md ---

# Learnings

Was hat funktioniert, was nicht, welche Muster wiederholen sich.
Dieses File ist das Gedächtnis des Systems. Hier landen Dinge
die man nicht noch einmal falsch machen will.

## Beispiel: NeoEmployee

Onboarding-Agents haben niedrigen Integrationsaufwand — meistens
nur Intranet + HR-System. Meeting-Summarizer variieren stark
wegen Transkriptions-Qualität. Tier-1-Support ist komplex:
Multi-Channel (Telefon + Chat + Mail) ist zu viel für ein
erstes Produkt.

## Dein Kontext

<!-- Ersetze das Beispiel mit deinen eigenen Learnings -->


--- context/roadmap.md ---

# Roadmap

Was ist committed, was geplant, was konkurriert um Ressourcen.
Dieses File verhindert dass neue Ideen im luftleeren Raum
bewertet werden — sie müssen gegen das antreten was schon
versprochen ist.

## Beispiel: NeoEmployee

Committed: 3 laufende Kundenprojekte (Q2).
Geplant: Pattern-Team evaluiert Onboarding als erstes Produkt.
Offen: Meeting-Summarizer als zweiter Kandidat.
Constraint: Kein dediziertes Produktteam, Pattern-Team arbeitet
neben Kundenprojekten.

## Dein Kontext

<!-- Ersetze das Beispiel mit deiner eigenen Roadmap -->


══════════════════════════════════════════════════
PHASE 3: EXISTIERENDE SKILLS KOPIEREN
══════════════════════════════════════════════════

Quelle: GitHub Repos. Die SKILL.md Files 1:1 kopieren, aber
Pfade generalisieren (kein input/case1/ mehr, sondern
variable Pfade).

DISCOVERY:

  skills/discovery/feedback-synthesizer/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche3
    Pfad:   .claude/skills/feedback-synthesizer/SKILL.md
    Änderung: Input/Output-Pfade auf output/discovery/ umbiegen

  skills/discovery/slack-importer/SKILL.md
    Quelle: Week 3 Übung (falls Teilnehmer es gebaut haben,
    sonst Platzhalter-SKILL.md mit Beschreibung was er tun soll)

STRATEGY:

  skills/strategy/opportunity-scorer/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche3
    Pfad:   .claude/skills/opportunity-scorer/SKILL.md
    Änderung: Liest jetzt context/company.md + context/strategy.md
    statt input/company.md + input/strategy.md

  skills/strategy/decision-brief/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche3
    Pfad:   .claude/skills/decision-brief/SKILL.md
    Änderung: Output nach output/strategy/decision-brief.md

  skills/strategy/devils-advocate/SKILL.md
    Quelle: Week 3 Übung (Variante 2)
    Änderung: Input ist jetzt output/strategy/decision-brief.md

SPEC-EVAL:

  skills/spec-eval/spec-writer/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche4
    Pfad:   .claude/skills/spec-writer/SKILL.md
    Änderung: Generische Pfade. Input: ein brief.md (Pfad wird
    beim Aufruf übergeben). Output: output/spec-eval/spec.md

  skills/spec-eval/eval-writer/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche4
    Pfad:   .claude/skills/eval-writer/SKILL.md
    Änderung: Input: output/spec-eval/spec.md.
    Output: output/spec-eval/eval.md

  skills/spec-eval/build-eval/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche4
    Pfad:   .claude/skills/build-eval/SKILL.md
    Änderung: Orchestrator-Pfade auf neue Struktur.
    Liest brief aus übergebenem Pfad, schreibt nach
    output/spec-eval/ und output/prototyping/

PROTOTYPING:

  skills/prototyping/prototype-builder/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche4
    Pfad:   .claude/skills/prototype-builder/SKILL.md
    Änderung: Output nach output/prototyping/app.py

  skills/prototyping/eval-runner/SKILL.md
    Quelle: github.com/andrezakm/AIAugmentedPM-Woche4
    Pfad:   .claude/skills/eval-runner/SKILL.md
    Änderung: Output nach output/prototyping/eval-results.md


══════════════════════════════════════════════════
PHASE 4: KONVERTIEREN (Week 1 + 2 → Skill-Format)
══════════════════════════════════════════════════

INTERVIEW-ANALYZER:

  skills/discovery/interview-analyzer/SKILL.md

  Quelle: github.com/andrezakm/AIAugmented_Woche1
  Pfad:   scripts/interview-analysis.md

  Was er tut: Nimmt Interview-Transkripte, extrahiert Insights,
  gruppiert nach Themen.

  Konvertierung:
  - Skill-Header mit allowed-tools: Read, Write, Glob
  - Input: Pfad zu einem Ordner mit Interview-Files (.md)
  - Output: output/discovery/interview-synthesis.md
  - Qualitätskriterien aus dem Original übernehmen
  - Format angleichen an feedback-synthesizer (gleiche Cluster-Logik)

BUSINESS-CASE-DEBATER:

  skills/strategy/business-case-debater/SKILL.md

  Quelle: github.com/andrezakm/AIAugmentedPM-Woche2
  Pfad:   prompts/p4_debate_optimist.md, p4_debate_critic.md,
          p4_debate_technician.md, p4_debate_market.md,
          p4_debate_strategist.md + p5_synthesis.md

  Was er tut: Nimmt eine Hypothese/Opportunity und lässt 5 Rollen
  darüber debattieren (Optimist, Kritiker, Techniker, Markt, Stratege).
  Dann Synthese.

  Konvertierung:
  - Ein einzelner Skill der alle 5 Perspektiven sequenziell durchläuft
  - Input: output/strategy/decision-brief.md oder eine Hypothese
  - Output: output/strategy/debate-synthesis.md
  - Jede Rolle bekommt eine Sektion im Output
  - Synthese am Ende: wo sind sich alle einig, wo nicht, was folgt daraus


══════════════════════════════════════════════════
PHASE 5: NEUE SKILLS BAUEN
══════════════════════════════════════════════════

OPTION-STORMER (Priorität 1 — Kern-Skill):

  skills/prototyping/option-stormer/SKILL.md

  Was er tut: Nimmt eine Spec und baut 3 verschiedene Prototypen.
  Nicht 1 und dann iterieren — 3 parallel, dann vergleichen.

  Input:
  - output/spec-eval/spec.md
  - Datendateien (wenn vorhanden)

  Output:
  - output/prototyping/option-a/app.py
  - output/prototyping/option-b/app.py
  - output/prototyping/option-c/app.py
  - output/prototyping/option-comparison.md

  Vorgehen:
  1. Lies die Spec vollständig
  2. Identifiziere die Kern-UI-Entscheidung (Layout, Interaktionsmodell,
     Informationshierarchie)
  3. Baue 3 Varianten die sich in dieser Kern-Entscheidung unterscheiden
     - Variante A: die naheliegendste Lösung
     - Variante B: eine Alternative die ein anderes Interaktionsmuster nutzt
     - Variante C: die unerwartete Variante — was wäre wenn man das
       Problem ganz anders angeht?
  4. Schreibe eine Vergleichstabelle: Was unterscheidet die drei?
     Welche Trade-offs?

  Qualitätskriterien:
  - Alle 3 sind lauffähig mit streamlit run
  - Alle 3 erfüllen die Spec (gleiche Funktionalität, andere UX)
  - Die Unterschiede sind nicht kosmetisch sondern strukturell
  - comparison.md benennt die Trade-offs explizit

  Kontext (für die Kurs-Story):
  Das ist der Willison-Move. "Ich prototype drei verschiedene Wege
  wie ein Feature funktionieren könnte, weil es fast nichts kostet."
  Der PM baut nicht eine Lösung und hofft. Er baut drei, schaut sie
  an, und urteilt welche lebt.


HANDOFF-PACKAGER (Priorität 2):

  skills/handoff/handoff-packager/SKILL.md

  Was er tut: Bündelt alles was Dev braucht um zu starten.
  Kein neues Artefakt — sammelt bestehende und schreibt ein
  Cover-Sheet.

  Input:
  - output/spec-eval/spec.md
  - output/spec-eval/eval.md
  - output/prototyping/option-comparison.md (falls vorhanden)
  - output/strategy/decision-brief.md (falls vorhanden)
  - context/product.md
  - context/team.md

  Output:
  - output/handoff/handoff.md (Cover-Sheet + Links zu allen Dateien)

  Cover-Sheet enthält:
  - Feature-Name + 1-Satz-Zusammenfassung
  - Links zu Spec, Eval, Prototyp, Decision Brief
  - Was der Dev als nächstes tun soll (konkret, 3-5 Punkte)
  - Was die PM-Eval prüft vs. was der Dev in seiner Eval ergänzen soll
  - Bekannte Risiken/Offene Fragen aus dem Decision Brief

  Qualitätskriterien:
  - Kein Copy-Paste aus den Quellen — nur Verweise
  - "Nächste Schritte" sind konkret genug um sofort loszulegen
  - Die Trennung PM-Eval vs. Dev-Eval ist explizit benannt


SYSTEM-AUDITOR (Priorität 3):

  skills/meta/system-auditor/SKILL.md

  Was er tut: Prüft den aktuellen Zustand des Systems.
  Welche Context-Files sind ausgefüllt, welche leer?
  Welche Skills existieren, welche fehlen?
  Welche Output-Ordner haben Artefakte, welche sind leer?

  Input: Der gesamte pm-workspace/ Ordner

  Output: output/meta/system-audit.md

  Prüft:
  - context/: Welche Files haben echten Inhalt vs. nur das Template?
  - skills/: Welche SKILL.md Files existieren und sind vollständig?
  - output/: Welche Bereiche haben Artefakte, welche sind leer?
  - CLAUDE.md: Ist sie aktuell? Kennt sie alle existierenden Skills?

  Output-Format:
  - Ampelsystem: ✅ ausgefüllt / ⚠️ Template / ❌ fehlt
  - Empfehlung: "Als nächstes solltest du X ausfüllen/bauen"


══════════════════════════════════════════════════
PHASE 6: CLAUDE.md SCHREIBEN
══════════════════════════════════════════════════

Die CLAUDE.md ist der Agent-Kern. Sie wird zuletzt geschrieben
weil sie alles kennen muss was vorher gebaut wurde.

WICHTIG — ARCHITEKTUR-PRINZIP:
Die Root-CLAUDE.md bleibt unter 500 Tokens. Keine langen
Skill-Listen, keine detaillierten Beschreibungen, keine
Qualitätskriterien. Die leben in den Folder-Indexes (README.md
in jedem skills/-Unterordner) und in den SKILL.md Files selbst.

Claude lädt die Root-CLAUDE.md bei jeder Session automatisch.
Folder-Indexes lädt Claude nur wenn er in den Bereich navigiert.
Das hält den Kontext effizient — auch wenn das System auf
50+ Skills wächst.

Warum das so gebaut ist (für den Kurs-Hinweis):
Claude neigt dazu, alles in eine zentrale Datei zu packen —
weil das einfacher ist als eine saubere Hierarchie zu denken.
Das rächt sich sobald das System wächst: zu große CLAUDE.md
frisst Kontext bei jeder Session. Wir haben dem vorgebeugt
durch Nested Indexes. Die Root kennt die Struktur.
Die Folders kennen den Inhalt.

WAS IN DIE ROOT-CLAUDE.md GEHÖRT:

1. SYSTEM-BESCHREIBUNG (3 Sätze)
   Was ist das hier? Ein PM-Workspace mit 7 Bereichen.
   Für wen? Product Manager die mit Claude Code arbeiten.

2. KONTEXT-REGEL (1 Absatz)
   Bevor du irgendeinen Skill ausführst, lies die relevanten
   Context-Files. Immer. Ohne Kontext kein Output.
   - company.md + strategy.md: immer
   - product.md: bei Spec, Prototyping, Handoff
   - team.md + roadmap.md: bei Priorisierung
   - metrics.md: bei Scoring, Tracking

3. ORDNERSTRUKTUR (nur die 4 Top-Level-Ordner)
   context/ — permanenter Kontext
   skills/  — Skill-Bibliothek, Details in skills/README.md
   output/  — Artefakte, gespiegelt nach Bereichen
   (input/  — Live-Quellen via MCP, kein fester Ordner)

4. HANDOFF-GRENZE (1 Satz)
   skills/spec-eval/ ist die Grenze zwischen PM und Dev.

5. NAVIGATION (1 Satz)
   Für Skills: lies zuerst skills/README.md

WAS NICHT IN DIE ROOT-CLAUDE.md GEHÖRT:
   ✗ Vollständige Skill-Listen → skills/README.md
   ✗ Skill-Beschreibungen → SKILL.md Files
   ✗ Qualitätskriterien → SKILL.md Files
   ✗ Flow-Details → skills/[bereich]/README.md
   ✗ Plugin-Listen → skills/README.md

WAS IN DIE FOLDER-INDEXES (skills/[bereich]/README.md):
   Jede README.md enthält:
   - Zweck des Bereichs (1 Satz)
   - Liste der Skills mit je 1 Zeile Beschreibung
   - Relevante Plugins für diesen Bereich
   - Typischer Input/Output-Flow für den Bereich


══════════════════════════════════════════════════
PHASE 7: README.md
══════════════════════════════════════════════════

Kurz. Erklärt:
- Was ist das (PM System für Claude Code)
- Wie starten (klonen, context/ ausfüllen, Claude Code öffnen)
- Die 7 Bereiche in je 1 Satz
- "Starte mit: Führe /system-auditor aus"

HINWEIS DER INS README GEHÖRT:

Abschnitt "Architektur-Entscheidung" einfügen:

  Diese CLAUDE.md ist bewusst kurz gehalten — unter 500 Tokens.
  Details zu einzelnen Skills leben in den README.md Files
  der jeweiligen skills/-Unterordner. Das ist keine Faulheit,
  das ist Architektur.

  Claude lädt die Root-CLAUDE.md bei jeder Session.
  Je größer sie ist, desto weniger Kontext bleibt für die
  eigentliche Arbeit. Die Folder-Indexes werden nur geladen
  wenn Claude in den Bereich navigiert.

  Wenn du das System erweiterst: neue Skills in den richtigen
  Unterordner, den Folder-Index updaten, fertig. Die Root
  bleibt unberührt.

  (Claude wird versuchen, alles zentral reinzupacken.
  Lass es nicht.)


══════════════════════════════════════════════════
REIHENFOLGE FÜR CLAUDE CODE CLI
══════════════════════════════════════════════════

1. Repo anlegen, Ordnerstruktur (Phase 1)
2. Context-Templates schreiben (Phase 2)
3. Skills aus Week 3 + 4 Repos klonen und umziehen (Phase 3)
4. interview-analyzer + business-case-debater konvertieren (Phase 4)
5. option-stormer bauen (Phase 5)
6. handoff-packager bauen (Phase 5)
7. system-auditor bauen (Phase 5)
8. CLAUDE.md schreiben — kennt jetzt alles (Phase 6)
9. README.md (Phase 7)
10. Einmal system-auditor laufen lassen als Selbsttest
