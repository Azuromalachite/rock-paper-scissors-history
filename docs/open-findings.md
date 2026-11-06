# Open findings

Known, specific, unfixed defects in the committed notes, and what would fix
them. Updated in the same commit that adds or closes one. One block per
finding. Review-round findings are referenced as `r<N>/R<N>-<n>`.

---

## Open

### Review round 1: fixes made, awaiting round 2

**Location:** [`reviews/review-r1.md`](../reviews/review-r1.md), against
`7292a2b`

17 findings: 4 high, 8 medium, 5 low. Each has its correction and validation
in the review. All 17 have been addressed by the author. None counts as fixed
until round 2 audits it: the fixer is not the one who confirms the fix.

Five could only be addressed in the wording, because the missing source has
still not been found. The prose now says so and the claims were downgraded.
Each stays open until its source is re-located:

| ID | what is still missing |
| --- | --- |
| r1/R1-2 | the 2008 Dek-D thread with the Hat Yai chant วัน ทู ส้ม |
| r1/R1-5 | the DBP 2018 enquiry; the Malaysian artist and outlet |
| r1/R1-6 | Kamaruddin Abdullah, "The Games We Played" (2013) |
| r1/R1-12 | the Thai Junior Encyclopedia vol. 13 text and catalogue record; the Thailand Cultural Encyclopedia entry; the 2008 Dek-D article |
| r1/R1-16 | "Traditional Games Returns" |

New guard from round 1: `check_evidence.py` now refuses `supported` unless a
source has `relocated: true`, meaning a second person found it again. A claim
can no longer rest on a source read once and never found again.

### OF-1: sources cannot be re-found

**Severity:** medium · **Location:** `evidence/sources.yml`

Almost every source has `url`, `archived`, `accessed` and `locator` set to
`null`. The notes cite sources by name, and several only by description
("a Malaysian artist's statement", "a university thesis", "one recent
article"). Nobody can re-run the research from the repository as it stands.
`check_evidence.py` reports the count on every run instead of failing, so the
gap stays visible without blocking.

**Correction:** for each source, record a URL or catalogue ID, a Wayback
Machine snapshot for web pages, an access date, and a locator. Sources that
cannot be identified stay `not_located` and their claims stay `unverified`.

### OF-2: one compilation pass, no independent check

**Severity:** medium · **Location:** all notes

Every `access` level was reached by a single AI-assisted search pass, before
2026-11-06. No second person or agent has re-read a source, so a
`primary_inspected` source is only as good as that pass.

**Correction:** review rounds (`docs/review-process.md`). Each source a
reviewer re-checks gets its `by` / `when` updated in the fixing commit.

### OF-4: the Phuket variant rests on evidence outside the repository

**Severity:** low · **Location:** `notes/03-southern-thailand.md`,
`claim.phuket.glass_stone_water`

The glass–stone–water rules and the Phuket/Krabi locality reports come from
private screenshots of one Facebook post. They are deliberately not
published, to protect the commenters. So no reader can check them.

**Correction:** the Phuket dictionary entry (`claim.phuket.dictionary_entry`)
or dated oral histories would give a checkable source. Until then the claim
stays `partly_supported`.

---

## Closed

### OF-3: the prose called Culin 1895 "firm" but it had not been read

Closed 2026-11-06. Review r1 read Culin pp. 44–45 (Internet Archive), and the
author confirmed the index entry. "Firm" now carries the locator, and the claim
is `supported`.
