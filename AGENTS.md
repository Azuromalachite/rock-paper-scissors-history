# AGENTS.md — rules for anyone changing this repository, human or AI

This repository is a set of **research notes on cultural history**, not
software. What can go wrong is a sentence that says more than its source.
That error looks exactly like a correct sentence. Read this file before
editing anything. `CLAUDE.md` imports it, so every agent reads the same rules.

## Run it

```bash
python -m pip install pyyaml          # the only dependency
python evidence/check_evidence.py     # must exit 0 before a commit
python -m unittest discover -s tests  # after changing the checker
```

The checker verifies **structure only**: claim IDs, vocabulary, source keys,
and that each claim's anchor phrase still appears on its page. It cannot tell
whether a sentence is faithful to its source. Humans and reviewers do that part
(see `docs/review-process.md`).

## Where facts live

| what | where |
| --- | --- |
| each load-bearing claim, its kind (`layer`), its evidence state (`status`) | `evidence/claims.yml` |
| each source, how it was accessed, where it is | `evidence/sources.yml` |
| prose for readers | `README.md`, `notes/*.md` |
| known defects not yet fixed | `docs/open-findings.md` |
| review rounds | `reviews/` |

The prose is **downstream** of the registry. When a page states a claim more
strongly than its registry entry allows, the page is wrong.

## Never

- **Upgrade a claim's status without new evidence.** That includes rewording
  prose so it reads as more certain. If a claim moves from `unverified` to
  `supported`, the same commit records which source was inspected, how
  (`access`), and the locator.
- **Write a lower bound as an origin.** "Attested by 2008" is not "began in
  2008". "Remembered for 1954–1961" is not "documented in 1954".
- **Write an absence of evidence as evidence of absence.** "Not found" claims
  are `layer: absence` and record what was searched (languages, terms,
  collections). An absence claim without a `searched:` field fails the check.
- **Fuse separately evidenced observations into one historical sequence.**
  Matching chants in Hat Yai and Malaysia are evidence of a connection. They
  are not a route and they do not give a direction. Describe the present
  configuration unless the order is actually documented.
- **Treat a name or sound-alike as lineage.** Etymologies need a dated sound
  change, not a resemblance.
- **Cite a source you have not located.** Use `access: not_located` and keep
  the claim `unverified`.
- **Reproduce copyrighted text.** At most one short quotation (under 15 words)
  per source, in quotation marks, with attribution. Summarise everything else.
- **Publish private people.** No names, handles or images of social-media
  commenters. Report the locality and version they gave, and nothing that
  identifies them. Screenshots stay out of the repository.
- **Change an expectation to make the checker pass.** That covers a claim's
  status, a test's expected outcome, or an anchor phrase. Argue for the change
  in its own commit.
- **Fix your own review finding unreviewed.** Whoever fixes a finding is not
  the one who confirms it fixed (see `docs/review-process.md`).

## Invariants

Each cites what taught it. "Open:" marks one the repository violates today.

1. **Every source is findable again.** A source carries enough to re-locate the
   exact passage: a URL or catalogue ID, an access date, an archived snapshot
   for web pages, and a locator (page, section, comment date). *Open: OF-1.*
2. **Verification says who and how.** `access` records the deepest level
   anyone reached (`primary_inspected` > `indexed_text` > `catalogue_record` >
   `secondary_report` > `user_screenshot` > `not_located`). The notes were
   compiled by one AI-assisted search pass and have not been independently
   re-checked. *Open: OF-2.*
3. **A check must be able to fail.** Every rule in `check_evidence.py` has a
   case in `tests/` that plants the defect and asserts exit 1, plus one healthy
   copy that must pass. A rule with no failing case is not known to work.
4. **Anchors bind prose to claims.** Each claim names a phrase on its page. If
   the prose is edited away, the check fails, and the editor must decide
   whether the claim moved, changed or died. Matching ignores whitespace and
   case and nothing else.
5. **Thai, Malay and other non-English text stays in its own script**, with a
   translation beside it. A transliteration is never the only record of a
   word.

## Working style

- Respect human edits. Never rewrite text you were not asked to change.
- Commit subjects are imperative and say what changed; the body says why.
  AI-assisted commits carry a `Co-Authored-By` line.
- A new finding about committed content goes into `docs/open-findings.md` in
  the same commit that discovers it.
