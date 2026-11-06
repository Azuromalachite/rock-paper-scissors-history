# Review process

How a wrong claim gets found, fixed and kept fixed. This is the cycle used in
espmap (seven rounds), and later in PINDR and ambl-ont-fungal-wgs, adapted for
historical claims instead of code.

## Why review adversarially here

A claim that overstates its source looks exactly like one that doesn't. Both
are fluent, both cite something. Reading the notes again does not find this
kind of error. Going back to the source does. So the reviewer's job is to
**try to break claims**, not to read for flow.

## Roles

- **Author:** writes or edits notes and registry entries.
- **Reviewer:** checks a pinned commit against the sources, reproduces each
  finding, and in the next round checks the fixes. The reviewer did not write
  the notes under review. An agent reviewing is given the repository and this
  file, not the conversation that produced the notes, because reading the
  author's reasoning first imports their blind spots.
- **Owner** (the repository maintainer): decides anything a finding leaves
  open, such as whether a claim is worth keeping.

## A round

Round N reviews one commit, named by its full SHA. A review of an
unidentified version cannot be re-run.

File: `reviews/review-r<N>.md`, in this order:

1. **Title with SHA and scope.**
2. **Retractions:** any earlier claim, by anyone, that turned out wrong. They
   come first, because a buried retraction is not one.
3. **Baseline:** what passes as reviewed (`check_evidence.py`, tests).
4. **Disposition of round N−1** (from round 2).
5. **Lead finding:** exactly one, the most consequential, not the first found.
6. **Findings.**
7. **What it got right:** the hardest correct calls, not the easy ones.
8. **Verdict:** what blocks reuse of the notes, and what can wait.
9. **Sources consulted**, with URLs and access dates.

### Each finding has

- an ID `R<N>-<n>` (round 1: `R1-1`, `R1-2`, …). Outside its own round, refer
  to it with its round: `r1/R1-3`;
- a severity: `[BLOCKER]` (a reader would be told something false),
  `[HIGH]` (a claim outruns its source), `[MEDIUM]` (it can't be re-checked as
  written), `[LOW]`;
- **how it was established**:
  - `CONFIRMED AGAINST SOURCE`: the reviewer read the source passage;
  - `CONFIRMED BY CATALOGUE`: bibliographic facts only;
  - `SOURCE NOT LOCATED`: the reviewer could not find what is cited;
  - `INTERNAL INCONSISTENCY`: the repository contradicts itself;
  - `METHODOLOGICAL CONCERN`: an inference problem, not a factual error;
- a **correction**: the concrete edit (prose, registry, or both);
- a **validation**: what would show it fixed. For example, the anchor that
  must change, the status the registry must hold, or the passage a re-check
  must find.

## Fixing

One small commit or pull request per group of related findings, citing their
IDs. A status change or an anchor change goes in its own commit, saying why.
If a finding needs a decision, the owner makes it first.

## Disposition: what "fixed" means

Round N opens by auditing every finding of round N−1:

| ID | finding | verdict | guarded? | evidence and residue |
| --- | --- | --- | --- | --- |

- **Verdict:** `FIXED`, `PARTIAL` (it then says *blocks* or *does not block*),
  `OPEN`, `DECIDED` (the owner chose not to change it, and why), or
  `REJECTED` (the finding was wrong).
- **Guarded:** the checker would now catch a regression. For example, the
  finding's claim has a registry entry whose anchor would break if the
  overstated wording came back. Not every fix can be guarded. Say which.
- **Residue:** whatever a fix left unestablished. It becomes a new finding,
  cross-referenced, so the rounds are cumulative rather than just numbered.

## Open findings

A finding about committed content that is not fixed in its round goes into
[`open-findings.md`](open-findings.md) in the same commit. A lesson that
recurs becomes an invariant in [`AGENTS.md`](../AGENTS.md), citing the
finding that taught it.

## When to review

Review is triggered by an event, never by the calendar:

- before the notes are cited, taught from or published elsewhere;
- after a batch of new sources or a change in any `status`;
- before a tagged release.
