# Set up or update topic-based progress journals

Journals are optional. Agree on their name, location, contents, and Git policy before creating them. In a multi-topic workspace, keep a small central LEARNING-JOURNAL.md as an index plus genuinely cross-topic notes. Put detailed reflections and problem history in a LEARNING-JOURNAL.md beside each relevant topic's materials.

## Set up journals if you want them

First agree on the central index and any topic paths. Then say:

> Read skills/progress-journal/SKILL.md and follow it. I want an optional topic-based journal in [chosen workspace]. Propose a small central LEARNING-JOURNAL.md index and a journal beside [topic] materials at [exact path]. Use the supplied templates if useful. Include only the topics and files I agree to. These records will be [tracked in Git / kept private and ignored]. Show me the proposed files and paths before creating them.

Use templates/learner-journal-template.md for the central index and templates/topic-journal-template.md for a topic journal. Do not create a journal, topic folder, or personal workspace without the learner's agreement.

## Update after a session or solved problem

Point to the agreed topic journal and ask for a reviewable proposal:

> Read the central index and only [current topic]/README.md and [current topic]/LEARNING-JOURNAL.md. Propose an update from today's session. For each problem, record the approach I proposed, what hints or guidance I needed, whether I report the solution was accepted (or mark that as not reported), and what I want to derive or revisit independently. Keep my report distinct from evidence you observed. Do not infer mastery from a commit, submission, or accepted answer. Show the exact changes before saving.

Record an explanation in the learner's own words, an independently derived solution, transfer to a new problem, or an assessment as evidence when observed. Record activities separately; do not claim mastery because a topic was covered.

## Convert an existing monolithic journal

Before moving entries, ask for an inventory and proposed mapping:

> Read skills/progress-journal/SKILL.md and follow its migration workflow. Inventory every session entry and problem-history row in [journal path]. Propose which topic journal each belongs in, list any ambiguous entries, and report source counts. Do not edit or move anything until I review the map.

After agreement, preserve every entry and row, fix relative links, and compare source and destination counts. Keep the central file as an index and cross-topic notes only. Review the final map and links before retiring the original. See [the existing-repository conversion guide](12-convert-existing-learning-repo.md) for repo-wide migrations.

Before tracking or sharing journal files, check the agreed Git policy. Keep private details out by default. A journal update does not itself authorize staging, committing, or pushing.
