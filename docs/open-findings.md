# Open findings

Known, specific, unfixed defects in the committed notes, and what would fix
them. Updated in the same commit that adds or closes one. One block per
finding. Review-round findings are referenced as `r<N>/R<N>-<n>`.

---

## Open

### Review round 1: R1-1 … R1-17, all open

**Location:** [`reviews/review-r1.md`](../reviews/review-r1.md), against
`7292a2b`

17 findings: 4 high, 8 medium, 5 low. Each has its correction and validation
in the review, which is not repeated here. These block reuse of the short
answers:

- **r1/R1-1:** the "pre-1939" bound. The earliest dated Thai record actually
  cited is 1989.
- **r1/R1-2:** the Hat Yai chant วัน ทู ส้ม rests on one 2008 comment that
  could not be re-located.
- **r1/R1-3:** the 1804–1843 estimate is Kako Satoshi (2008), relayed by
  Yokohama Central Library in the NDL database. It is not an NDL guide, and
  it does not make the game "securely identifiable".
- **r1/R1-4:** the Singapore bird–water–stone record has no source.
- **r1/R1-12:** none of the three Thai documentary anchors could be located as
  cited.

The review also located sources that close parts of OF-1 and OF-3 (Culin pp.
44–45, verified independently on 2026-11-06). Its "Source locators found"
table is the input for filling `evidence/sources.yml`.

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

### OF-3: the prose calls Culin 1895 "firm" but it has not been read

**Severity:** medium · **Location:** `01-global-chronology.md`, 1895 row;
`claim.japan.culin_1895`

The chronology calls Culin (1895) "a firm documentary anchor", but the notes
only saw his description as reproduced in Japanese scholarship
(`access: secondary_report`). The registry holds it at `partly_supported`.
The prose is stronger than its registry entry. Found while building the
registry.

**Correction:** read the 1895 book (public domain, digitised), record the page,
then either keep "firm" with the locator, or soften the prose.

### OF-4: the Phuket variant rests on evidence outside the repository

**Severity:** low · **Location:** `03-southern-thailand.md`,
`claim.phuket.glass_stone_water`

The glass–stone–water rules and the Phuket/Krabi locality reports come from
private screenshots of one Facebook post. They are deliberately not
published, to protect the commenters. So no reader can check them.

**Correction:** the Phuket dictionary entry (`claim.phuket.dictionary_entry`)
or dated oral histories would give a checkable source. Until then the claim
stays `partly_supported`.
