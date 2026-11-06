# Contributing

Corrections, dated sources and oral histories are the most useful
contributions. Open an issue or a pull request. The binding rules are in
[`AGENTS.md`](AGENTS.md); this file explains how to meet them.

## Adding or correcting a source

Add an entry to [`evidence/sources.yml`](evidence/sources.yml). For a source to
be re-findable by someone else, record:

| field | what to put |
| --- | --- |
| `title`, `author`, `date` | as printed, in the original script; a translation in `notes` |
| `url` or `catalogue` | the page you read, or a library catalogue ID / DOI |
| `archived` | for web pages, a Wayback Machine (`web.archive.org`) snapshot URL taken when you read it. Web references rot, and a snapshot is the copy a reviewer can still open. |
| `accessed` | the date you read it (YYYY-MM-DD) |
| `locator` | page, section, paragraph or comment date: where the passage is |
| `access` | how far you got: `primary_inspected`, `indexed_text`, `catalogue_record`, `secondary_report`, `user_screenshot`, `not_located` |
| `relocated` | `true` only when a second person found the source again from what is recorded. A claim can be `supported` only on such a source. |

Cite the original page and add the archive snapshot next to it. Don't cite the
snapshot alone.

## Adding or changing a claim

Add an entry to [`evidence/claims.yml`](evidence/claims.yml). It has two
independent axes:

- **`layer`**: what kind of statement it is: `documented` (a dated document
  says it), `recollection` (someone remembering an earlier time), `testimony`
  (an informal report of current practice), `interpretation` (our inference),
  `hypothesis` (a proposed history), `absence` (we looked and did not find).
- **`status`**: what the evidence currently says: `supported`,
  `partly_supported`, `unverified`, `unsupported`, `open`.

The checker enforces the rules that can be mechanised:

- a `hypothesis` is never `supported`. If one becomes established, re-layer it
  and say why;
- an `absence` claim records what was `searched`;
- `supported` needs at least one source at `catalogue_record` or deeper;
- every page anchor is still on its page.

The rest is a human check:

- **Claim strength does not exceed design strength.** Five online comments are
  not a survey. A 2013 memoir of the 1950s is a recollection, not a 1950s
  document.
- **Scope before status.** Two reports conflict only if they describe the
  same place, period and game. Different towns playing different versions is
  variation, not contradiction.
- **A trailing qualifier applies to every item in its list.** Check this, and
  split the sentence where it does not hold.

## Oral histories

Record: birth year (or decade), childhood locality, the symbols, gestures,
chant and winning rules, who taught the game, and the date of the interview.
Get consent before publishing, and publish no names unless the person asks to
be named. An oral history goes in as `layer: recollection`.

## Before you open a pull request

```bash
python evidence/check_evidence.py
python -m unittest discover -s tests     # if you touched the checker
```

**Read the exit status directly.** A loop that formats its own output can
print success over a failure. To prove the harness propagates failure, run
`python -c "import sys; sys.exit(3)"` through it first and confirm it reports
3.

## Reviews

See [`docs/review-process.md`](docs/review-process.md).
