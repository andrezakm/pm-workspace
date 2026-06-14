TEAMWORK IN CLAUDE CODE — Wie ein PM-Team mit dem System arbeitet
══════════════════════════════════════════════════════════════════

Dieses File beschreibt wie mehrere Menschen mit demselben
PM-System in Claude Code zusammenarbeiten. Es ist Teil des
Starter-Kits und wird von Claude gelesen wenn Teilnehmer
Fragen zu Teamarbeit stellen.


══════════════════════════════════════════════════
DAS PRINZIP: ZIMMER VS. WOHNZIMMER
══════════════════════════════════════════════════

Dein Workspace hat zwei Bereiche. Dein Zimmer und das Wohnzimmer.

DEIN ZIMMER (Persönlicher Workspace):
Sandbox. Hier probierst du aus. Hier denkst du nach.
Hier liegen deine drei Prototyp-Varianten, dein erster
Entwurf vom Decision Brief, dein halbfertiger Skill.
Niemand sieht das. Niemand muss das sehen.
Das ist der Raum fürs Denken.

DAS WOHNZIMMER (Geteilte Infrastruktur):
Truth. Hier gelten die Familienregeln. Was hier liegt,
gilt für alle. Skills die alle nutzen. Context-Files die
den Stand der Wahrheit abbilden. Learnings die das Team
gesammelt hat. Entscheidungen die getroffen wurden.

DER ÜBERGANG WIRD BEWACHT:
Aus dem Zimmer ins Wohnzimmer kommt etwas nur durch
Interaktion. Synchron (Meeting, Review) oder asynchron
(Slack, PR). Das ist dasselbe Prinzip wie ein Pull Request:
aus meinem Branch geht etwas in den Trunk, aber nur
nach Review. Nicht automatisch. Nicht heimlich.


══════════════════════════════════════════════════
DIE DREI SCHICHTEN
══════════════════════════════════════════════════


SCHICHT 1: GETEILTE INFRASTRUKTUR (Git)
────────────────────────────────────────

Das ist das Wohnzimmer. Lebt im gemeinsamen Repo.

Was hier liegt:

  CLAUDE.md
    Der Agent-Kern. Konventionen, Skill-Register, Flow.
    Gilt für alle. Änderungen nur per PR.

  context/
    company.md, strategy.md, product.md, team.md,
    metrics.md, learnings.md, roadmap.md
    Das ist der Stand der Wahrheit über euer Unternehmen.
    Wenn sich die Strategie ändert, ändert sich strategy.md.
    Eine Quelle, alle lesen dasselbe.

  skills/
    Alle SKILL.md Files. Das sind die Werkzeuge des Teams.
    Wenn jemand den eval-writer verbessert, profitieren alle —
    aber nur nach Review.

Was NICHT hier liegt:

  output/ — das ist persönlich, Zimmer, nicht Wohnzimmer.
  Drafts, Prototypen, halbfertige Analysen — privat bis zum
  bewussten Teilen.

Wie es funktioniert:

  Jeder klont das Repo. Jeder hat lokal eine Kopie.
  Änderungen an Skills, Context oder CLAUDE.md laufen
  über Branches und Pull Requests. Kein PR ohne Review.
  Skills sind jetzt quasi Code. Selber Prozess, selbes Tool.

  Wie genau Review läuft — synchron im Weekly, asynchron
  als PR-Kommentar, zu zweit am Bildschirm — das entscheidet
  jedes Team selbst. Aber: der Übergang ins Wohnzimmer
  passiert nicht unbemerkt.


SCHICHT 2: GETEILTE QUELLEN (APIs / MCPs)
──────────────────────────────────────────

Slack, Granola, Gong, Jira, Linear, Analytics.

Die Quellen sind geteilt — alle sehen denselben Slack-Kanal,
dieselben Meetings, dieselben Tickets.

Aber die Verarbeitung ist individuell. Ein PM und ein
Designer lesen denselben Slack-Thread und extrahieren
verschiedene Dinge. Der PM sieht ein Feature-Signal.
Der Designer sieht ein UX-Problem. Das ist gewollt.

Geteilte Quelle. Persönliche Verarbeitung. Dann teilen
was relevant ist — über Schicht 1 (ins Repo) oder über
Schicht 2 selbst (Slack-Nachricht, Meeting).

Konfiguration: MCP-Verbindungen werden pro Person
eingerichtet. Wer Slack-Zugang hat, verbindet Slack.
Wer Granola nutzt, verbindet Granola. Kein Zwang,
jeder verbindet was für seinen Workflow relevant ist.


SCHICHT 3: PERSÖNLICHER WORKSPACE (Lokal)
──────────────────────────────────────────

Dein Zimmer. Hier passiert die eigentliche Arbeit.

  output/ — alle Artefakte die du produzierst
  Prototypen, Decision Briefs, Eval-Ergebnisse,
  Synthesen, Drafts. Alles privat bis du es teilst.

Was hier passiert:
  - Du probierst drei Prototyp-Varianten aus (option-stormer)
  - Du schreibst einen Decision Brief und lässt den
    Devil's Advocate drüber laufen
  - Du synthetisierst Feedback und sortierst Cluster
  - Du schreibst eine Spec und testest sie gegen die Eval

Nichts davon muss sofort im Team sichtbar sein.
Das schützt den Denkraum. Nicht alles was du produzierst
muss sofort im Teamkontext stehen. Das ist wichtig —
auch wegen der Exhaustion-Problematik. Dein Zimmer
ist dein Zimmer.

Wann etwas rausgeht:
  - Du bist zufrieden mit dem Decision Brief → teilen
    (Slack, Meeting, oder ins Repo)
  - Du hast einen Skill verbessert → PR ins Repo
  - Du hast ein Learning → in context/learnings.md
    eintragen, per PR
  - Du hast ein Handoff-Package → dem Dev übergeben


══════════════════════════════════════════════════
WAS GETEILT WIRD UND WIE
══════════════════════════════════════════════════

SKILLS (Werkzeuge):
  Wo:      Git Repo, skills/
  Wie:     Branch → PR → Review → Merge
  Wer:     Jeder kann vorschlagen, Team reviewed
  Beispiel: Du verbesserst den decision-brief Skill um
            eine Risk-Sektion. Branch, PR, Kollege schaut
            drüber, Merge. Ab jetzt hat jeder die Risk-Sektion.

CONTEXT (Stand der Wahrheit):
  Wo:      Git Repo, context/
  Wie:     Branch → PR → Review → Merge
  Wer:     Wer die Info hat, trägt sie ein
  Beispiel: Strategie-Meeting ergibt neuen Fokus.
            PM updated strategy.md, PR, kurzer Review,
            Merge. Ab jetzt arbeiten alle Skills mit
            dem neuen Kontext.

CLAUDE.md (Konventionen):
  Wo:      Git Repo, Root
  Wie:     Branch → PR → Review → Merge
  Wer:     Wer eine Konvention ändern will
  Beispiel: Team beschließt neue Naming-Konvention für
            Output-Files. Jemand updated CLAUDE.md, PR,
            Merge.

ARTEFAKTE (Ergebnisse):
  Wo:      Persönlich (output/) → geteilt über Slack,
           Meeting, oder einen shared Ordner
  Wie:     Bewusste Entscheidung: "das teile ich jetzt"
  Wer:     Der Ersteller entscheidet wann
  Beispiel: Dein Decision Brief ist fertig. Du postest
            ihn in Slack oder präsentierst ihn im Weekly.

LEARNINGS (Gedächtnis):
  Wo:      Git Repo, context/learnings.md
  Wie:     Branch → PR → Merge (leichtgewichtiger Review)
  Wer:     Jeder der etwas gelernt hat
  Beispiel: Prototyp hat gezeigt dass Streamlit für
            komplexe Dashboards nicht reicht. Learning
            eintragen. Ab jetzt weiß das System das.


══════════════════════════════════════════════════
BEISPIEL: ONBOARDING-AGENT VON RESEARCH BIS HANDOFF
══════════════════════════════════════════════════

Setting: PM-Team bei NeoEmployee, 2 PMs (Anna, Ben).
Anna macht Discovery, Ben übernimmt ab Spec/Eval.
Geteiltes Repo mit dem PM-System. Beide haben Slack
und Granola verbunden.

──── WOCHE 1: DISCOVERY (Anna, in ihrem Zimmer) ────

Anna verbindet Slack MCP, zieht Nachrichten aus
#kundenfeedback und #retros.

  > "Führe /feedback-synthesizer aus auf die letzten
  >  3 Monate aus #kundenfeedback und #retros"

Ergebnis: output/discovery/clusters.md
4 Cluster, Onboarding dominiert mit 8 Erwähnungen.

Anna lässt auch den research-synthesizer über die
letzten 3 Granola-Meeting-Transkripte laufen.

  > "Führe /synthesize-research aus auf die Sales Calls
  >  der letzten 4 Wochen aus Granola"

Ergebnis: output/discovery/research-synthesis.md
Bestätigt: Onboarding ist das stärkste Signal.

Alles noch in Annas Zimmer. Niemand sieht es.

──── WOCHE 1: STRATEGIE (Anna, noch im Zimmer) ─────

Anna lässt den Opportunity Scorer laufen.

  > "Führe /opportunity-scorer aus.
  >  Input: output/discovery/clusters.md"

Ergebnis: output/strategy/scored.md
Onboarding: 14/15. Meeting-Summarizer: 11/15.

Dann den Decision Brief.

  > "Führe /decision-brief aus für den Top-Kandidaten"

Ergebnis: output/strategy/decision-brief.md
Empfehlung: BUILD.

Anna ist nicht sicher. Lässt den Devil's Advocate laufen.

  > "Führe /devils-advocate aus auf
  >  output/strategy/decision-brief.md"

Ergebnis: output/strategy/devils-advocate.md
Stärkstes Gegenargument: "Onboarding-Agents gibt es
von der Stange. Warum custom bauen?"
Annas Antwort: Weil wir die Brücke zum Produkt suchen,
nicht die schnellste Lösung für einen Kunden.

──── WOCHE 1: ANNA TEILT (Zimmer → Wohnzimmer) ─────

Anna ist zufrieden. Jetzt wird geteilt.

Variante A — Synchron:
  Anna zeigt Decision Brief + Devil's Advocate im
  Team-Weekly. Diskussion. Team sagt: "Go."

Variante B — Asynchron:
  Anna postet Decision Brief in Slack #produktteam.
  Ben liest, kommentiert, sagt: "Nehme ich für Spec."

In beiden Fällen: die Entscheidung ist jetzt im Team.
Der Decision Brief kann optional ins Repo (als Referenz),
muss aber nicht.

Was ins Repo MUSS: wenn Anna den decision-brief Skill
dabei verbessert hat (z.B. Risk-Sektion ergänzt) →
Branch, PR, Review, Merge. Ab jetzt hat Ben den
verbesserten Skill auch.

──── WOCHE 2: SPEC & EVAL (Ben, in seinem Zimmer) ──

Ben nimmt Annas Decision Brief und schreibt einen
Feature-Brief für den Onboarding-Agent.

  > "Führe /spec-writer aus für input/onboarding-brief.md"

Ergebnis: output/spec-eval/spec.md
Was der Agent können muss, welche Fragen er beantworten
muss, welche Datenquellen er braucht.

Ben reviewt die Spec. Passt zwei Punkte an.
Dann die Eval:

  > "Führe /eval-writer aus für output/spec-eval/spec.md"

Ergebnis: output/spec-eval/eval.md
10 Kriterien, alle pass/fail. Das ist Bens Abnahme-Liste.

──── WOCHE 2: PROTOTYPING (Ben, noch im Zimmer) ────

Ben will drei Varianten sehen.

  > "Führe /option-stormer aus für output/spec-eval/spec.md"

Ergebnis:
  output/prototyping/option-a/app.py  — Chat-Interface
  output/prototyping/option-b/app.py  — FAQ mit Suchfeld
  output/prototyping/option-c/app.py  — Guided Onboarding Flow
  output/prototyping/option-comparison.md

Ben startet alle drei, klickt durch, zeigt Variante B
einem Kollegen auf Zoom (echter Mensch, kein simulierter
User). Variante B gewinnt.

Ben lässt den eval-runner über Variante B laufen:

  > "Führe /eval-runner aus für
  >  output/spec-eval/eval.md und
  >  output/prototyping/option-b/app.py"

Ergebnis: 8 PASS, 1 FAIL, 1 UNKLAR.
FAIL: "Agent antwortet auf Fragen außerhalb des
Onboarding-Kontexts" — muss in der Spec nachgeschärft werden.

Ben passt die Spec an, baut Variante B neu, Eval läuft
nochmal. 9 PASS, 1 UNKLAR. Gut genug.

──── WOCHE 2: HANDOFF (Ben → Dev, Zimmer → draußen) ──

  > "Führe /handoff-packager aus"

Ergebnis: output/handoff/handoff.md

Enthält:
  - Feature: Onboarding-Agent
  - Links zu: Spec, Eval (PM-Schicht), Prototyp, Decision Brief
  - Nächste Schritte für Dev (5 konkrete Punkte)
  - PM-Eval prüft: "Agent beantwortet Onboarding-Fragen korrekt"
  - Dev ergänzt in seiner Eval: Latenz, Halluzinations-Rate,
    Security-Review, Integration mit HR-System

Ben übergibt das Handoff-Package an die Entwicklerin.
Sie nimmt Spec + Eval, ergänzt ihre technische Schicht
(spec-technical.md, eval-technical.md), und baut.

Die PM-Eval bleibt bestehen. Wenn der Production-Code
fertig ist, muss er beide Evals bestehen — Bens PM-Eval
UND die technische Eval der Entwicklerin.

──── DANACH: LERNEN (beide → Wohnzimmer) ───────────

Was ins Repo zurückfließt:

  context/learnings.md (per PR):
    "Onboarding-Agent: FAQ-Pattern (Variante B) war
    klar besser als Chat-Interface. User wollen suchen,
    nicht chatten. Guided Flow zu einschränkend."

  Skills (per PR, falls verbessert):
    Ben hat den eval-writer angepasst — ein neues Kriterium
    für "Agent-Scope-Begrenzung" eingebaut. PR, Review, Merge.
    Ab jetzt prüft jede Eval automatisch ob der Agent
    seinen Scope einhält.


══════════════════════════════════════════════════
ZUSAMMENFASSUNG: WAS IST WAS
══════════════════════════════════════════════════

  WOHNZIMMER (Repo)         ZIMMER (Lokal)
  ─────────────────         ──────────────
  CLAUDE.md                 output/
  context/                  Drafts
  skills/                   Prototypen
                            Experimente

  Übergang: PR (async)      Übergang: Teilen (bewusst)
  oder Meeting (sync)       wenn du bereit bist

  Familienregeln:           Deine Regeln:
  Kein PR ohne Review       Mach was du willst
  Skills sind Code          Probier drei Varianten
  Context ist Truth         Scheitere leise
  Änderungen sind sichtbar  Teile wenn's gut ist


══════════════════════════════════════════════════
ANWEISUNG FÜR CLAUDE
══════════════════════════════════════════════════

Wenn Teilnehmer Fragen stellen zu Teamarbeit, Teilen,
Zusammenarbeit oder "wie arbeiten mehrere PMs mit
diesem System", dann lies dieses File und erkläre
anhand der drei Schichten und der Zimmer/Wohnzimmer-
Metapher.

Zentrale Punkte die Claude vermitteln soll:

1. Das System hat zwei Bereiche: privat (Zimmer) und
   geteilt (Wohnzimmer). Die Grenze ist bewusst.

2. Geteilte Infrastruktur lebt in Git. Skills sind Code.
   Context ist Truth. Änderungen laufen über PRs.

3. Persönliche Arbeit ist Sandbox. Nicht alles muss
   sofort sichtbar sein. Das schützt den Denkraum.

4. Der Übergang vom Zimmer ins Wohnzimmer wird bewacht.
   Synchron (Meeting) oder asynchron (Slack, PR).
   Nie automatisch, immer bewusst.

5. Quellen (Slack, Granola etc.) sind geteilt, die
   Verarbeitung ist individuell. Jeder sieht dasselbe,
   aber jeder extrahiert was er braucht.

6. Learnings fließen zurück ins Repo. Das System wird
   besser durch Benutzung — aber nur wenn Learnings
   auch eingetragen werden.

Wenn jemand fragt "aber wie genau läuft der Review ab":
Das entscheidet jedes Team selbst. Das System gibt die
Struktur vor (PR, Review, Merge). Die Kultur bestimmt
das Team (async, sync, wie detailliert, wer reviewed).
