# Review round 1: commit 7292a2be0cb99734184547b59732b2a1e42ab140

**Scope.** `README.md` and `01-global-chronology.md` … `06-open-questions.md`
as committed at `7292a2be0cb99734184547b59732b2a1e42ab140` (read with
`git show 7292a2b:<file>`). The working-tree files `evidence/`, `tests/` and
everything else uncommitted were not reviewed. Process: `docs/review-process.md`
(working tree). Reviewer: independent agent, did not write the notes and was
not given the conversation that produced them. Date of all source access:
**2026-11-06**.

**Coverage.** Checked against sources: Culin 1895; Xie Zhaozhe, *Wuzazu*; the
Children's Bureau handbook and the teachinghistory.org answer; the NDL
Collaborative Reference Database (CRD); Hervey 1903 (all of pp. 284–304); the
ASEAN 2009 compilation; *BiblioAsia* 9(4); the suten article; Ogawa (catalogue);
the Phuket dialect dictionary (catalogue). Searched for and **not located**:
the DBP 2018 enquiry, Kamaruddin Abdullah 2013, the Thai Junior Encyclopedia
vol. 13 online text, the Dek-D 2008 article and comments, Traditional Games
Returns. **Not checked at all** (no time spent, no finding either way):
Thailand Cultural Encyclopedia entries, the ฉู่ฉี้ / Thung Song account and
thesis, *108 ซองคำถาม*, Wilkinson 1925 / eHRAF, the New Zealand Ministry of
Education pages, Elsdon Best 1925, the *Times of India* 2015 article, the
Silpakorn bibliography. The Facebook post and comments (owner's private
screenshots) are **not checkable** and were not looked for.

## Retractions

None. This is the first round.

## Baseline

At `7292a2b` the repository holds prose only: no source registry, no
`check_evidence.py`, no tests. Nothing passes as reviewed; there is no checker
that could guard a fix. Every "guarded?" verdict in round 2 will therefore
depend on infrastructure that does not exist at this commit.

## Lead finding

**R1-1** (below). The headline answer to the repository's first question is
framed against a 1939 cutoff, but the earliest *dated* Thai record the notes
actually cite is a 1989 catalogue date (itself not verified). A reader is
steered towards "records exist from the 1940s on, consistent with a wartime
introduction" when the evidence found is silent until 1989.

## Findings

### R1-1 [HIGH] "No securely dated pre-1939 Siamese record" implies post-1939 records that the notes do not have

- **How established:** `INTERNAL INCONSISTENCY`.
- **Where:** `README.md` (Short answers, first bullet); `02-thailand.md` (bold
  opening sentence).
- **What:** Both files bound the negative result at 1939. The "Thai
  documentary anchors" table in `02-thailand.md` lists three items: the Thai
  Junior Encyclopedia vol. 13 ("catalogued as 2532 BE / 1989"), the Thailand
  Cultural Encyclopedia entry (no date given), and Dek-D, 26 June 2008. No
  record dated between 1939 and 1989 is cited anywhere in the six files. The
  1939 qualifier therefore does not describe the evidence; it narrows the gap
  to "before 1939" when the gap actually runs to 1989. Combined with the
  README's next sentence about the Japanese/WWII hypothesis, a reader will
  infer that the game is documented from about the war onward. It is not, in
  these notes. (The 1989 date itself is unverified: see R1-12.)
- **Correction:** In both places, replace the 1939 framing with the actual
  earliest anchor, for example: "The earliest dated Thai description found is
  the Thai Junior Encyclopedia vol. 13, catalogued as 2532 BE / 1989 (not yet
  verified against the printed volume). No earlier dated Thai or Siamese
  record was found." If 1939 is kept as a meaningful boundary (the
  Siam→Thailand name change), say why, and state separately that 1939–1989 is
  also undocumented.
- **Validation:** No sentence in `README.md` or `02-thailand.md` uses "pre-1939"
  as the bound of the search result unless the same paragraph states the
  earliest dated record found and its year.

### R1-2 [HIGH] The Hat Yai chant "วัน ทู ส้ม", the keystone of the "shared peninsular tradition" answer, rests on one uncited forum comment that could not be located

- **How established:** `SOURCE NOT LOCATED`, plus `METHODOLOGICAL CONCERN`.
- **Where:** `README.md` (third short answer: "Hat Yai's chant วัน ทู ส้ม
  matches Malaysian *one two som/osom*, and the symbols match too");
  `03-southern-thailand.md` (Dek-D table, "Inference" paragraph);
  `06-open-questions.md` ("Current defensible answers", third bullet).
- **What:** The *Thai* half of the chant match is a single commenter in the
  Dek-D thread of 26–29 June 2008. No URL, thread ID or comment number is
  given. Web searches for the article and for the chant with the Hat Yai
  bird–stone–water version (Thai and English) found nothing. The Facebook
  comments table in `03-southern-thailand.md` lists Hat Yai/Songkhla as
  bird–stone–water but does not attribute the chant to Hat Yai, so it does not
  corroborate the chant. The *Malaysian* half is now verified (ASEAN 2009,
  R1-7). The inference "persuasive … a stronger explanation" therefore stands
  on one checkable leg and one uncheckable one. The README presents it as the
  strongest explanation with no hint of this.
- **Correction:** Give the Dek-D thread URL and the comment number (or an
  archived copy) in the notes or registry. Until then, the README and
  `06-open-questions.md` should say that the Hat Yai chant is attested by a
  single 2008 online comment and has not been re-located, and the symbol
  match (bird–stone–water in Songkhla/Hat Yai, also reported in the Facebook
  comments) should be separated from the chant match.
- **Validation:** Either a registry entry for the Dek-D comment with a working
  or archived URL, or README wording that names "one 2008 online comment" as
  the source of the Hat Yai chant.

### R1-3 [HIGH] "Rock–paper–scissors becomes securely identifiable" is attached to an estimate that its own source calls undated; the source is also misdescribed

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `01-global-chronology.md`, Chronology, "Nineteenth-century Japan".
- **What:** The CRD entry that gives 1804–1843 is a reference answer
  registered by **Yokohama Central Library** (管理番号 横浜市中央2750, case
  created 2025-01-09, registered 2025-02-06). It is not an NDL research guide
  and the estimate is not the library's. It relays 加古里子, 『伝承遊び考 4』
  (Kobunsha, 2008), pp. 11, 40–45, which derives 石拳 from 虫拳, says the
  "年代や詳細な経緯は不明だが" (date and details unknown), and *estimates*
  Bunka–Tenpō. A second CRD answer on the same question (Takasaki City Central
  Library, R1001861) gives no period at all. So the cited source supports "an
  estimate of 1804–1843 for the emergence of 石拳, explicitly uncertain", not
  "securely identifiable". The only secure 19th-century document in the notes
  is Culin 1895, in the next row. The notes' "with acknowledged uncertainty"
  clause contradicts the row's own first sentence.
- **Correction:** Rewrite the row: "Kako Satoshi (2008) estimates that 石拳
  (stone-ken) developed from 虫拳 between Bunka and Tenpō (1804–1843), while
  stating that the date and process are unknown (relayed in a Yokohama Central
  Library answer in the NDL Collaborative Reference Database)." Move "securely
  identifiable" to the 1895 row or delete it. Registry: cite Kako 2008 as the
  source and the CRD entry as the locator.
- **Validation:** The phrase "securely identifiable" no longer qualifies the
  1804–1843 estimate; the row names Kako 2008 and the CRD entry ID.

### R1-4 [HIGH] "The same cycle is recorded in Singaporean schoolyard folklore": no source is given, and the only Singapore source cited records a different game

- **How established:** `SOURCE NOT LOCATED` (for the claim);
  `CONFIRMED AGAINST SOURCE` (for what the cited Singapore source does say).
- **Where:** `03-southern-thailand.md` ("The Malaysian parallel …", third
  bullet); `README.md` ("shared peninsular tradition with Malaysia and
  Singapore").
- **What:** The bullet cites nothing. The one Singapore source in the
  repository, Nor Afidah Abd Rahman's *BiblioAsia* piece (`04-malay-peninsula.md`),
  was read: its "OH BEY SOM!" entry is a palm-up/palm-down selection for teams
  or a catcher, and the article does not mention bird, stone and water at all.
  The notes say this themselves in 04 ("similar 'som' names refer to different
  hand procedures"). So the Singapore leg of the README's answer is
  unsupported as written.
- **Correction:** Cite a source that records bird–stone–water in Singapore, or
  delete the bullet and drop "and Singapore" from the README answer (or say
  "Singapore: a palm-up/palm-down *oh bey som* is documented; the
  bird–stone–water cycle was not found in a Singapore source").
- **Validation:** Either a registry entry whose passage shows bird–stone–water
  in Singapore, or no claim of a Singapore bird–stone–water attestation.

### R1-5 [MEDIUM] "The Malaysian parallel is independently documented": two of the three supports cannot be checked as cited

- **How established:** `SOURCE NOT LOCATED`.
- **Where:** `03-southern-thailand.md`, first two bullets of "The Malaysian
  parallel is independently documented".
- **What:** (a) The DBP enquiry of 7 September 2018 on *ohsom / osom / wan tu
  som*: the PRPM portal (`prpm.dbp.gov.my/Cari1`) was searched for "osom",
  "ohsom", "oh som", "wan tu som" and "batu air burung"; no advisory-archive
  (khidmat nasihat) result was returned. The archive may not be fully
  searchable, so this is "not located", not "does not exist". (b) "A Malaysian
  artist's statement … Malaysian reporting documents this": neither the artist,
  the statement, the outlet nor a date is named, so it cannot be searched for.
  The one Malaysian document that *is* verifiable, the ASEAN 2009 compilation,
  sits in a different file (04) and is not mentioned here.
- **Correction:** Give the DBP item's URL or reference number (or a screenshot
  archived in `evidence/`), name the artist, outlet and date, and add the ASEAN
  2009 compilation (R1-7) to this list as the dated documentary support.
- **Validation:** Each bullet under "independently documented" has a registry
  entry with a locator; the ASEAN 2009 Malaysia-section passage is cited here.

### R1-6 [MEDIUM] Kamaruddin Abdullah, "The Games We Played" (20 May 2013) not located

- **How established:** `SOURCE NOT LOCATED`.
- **Where:** `04-malay-peninsula.md`, "A childhood account from the 1950s".
- **What:** This is the only source that places *osom* in a remembered period
  (1954–1961), so it carries the notes' only mid-century claim for the
  Malaysian game. No URL or publication venue is given. Searches combining the
  author, title, *osom* and *opek* returned nothing matching. A Penang library
  record lists a different book by a Kamaruddin Abdullah; it was not opened
  and is not claimed to be the source.
- **Correction:** Add the URL (or venue) and an archived copy. Until then, mark
  the 1954–1961 framing as unverified in `04-malay-peninsula.md`.
- **Validation:** Registry entry with URL and the passage giving the
  1954–1961 frame and the water > stone > bird > water cycle.

### R1-7 [MEDIUM] The ASEAN 2009 compilation can be checked after all; the notes understate it and omit one of its rules

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `04-malay-peninsula.md`, "Formal regional documentation of 'One
  Two Som'".
- **What:** The notes say the hosted PDF returns an error and the summary
  rests on indexed text. The live Indonesian government URL now returns a
  "page not found" page, but the Internet Archive holds a copy captured
  2025-05-20 (279 pp.; PDF creation date December 2009). In the **Malaysia**
  section, the list of games (printed p. 85) glosses One Two Som as "One Two
  Three", and the "Ten popular balloting games" (printed pp. 86–87) describe it
  as a two-player method for who begins, chanted "One Two Som" or "One Two
  Juz", with bird (fingers closed together), water (open palm) and stone
  (fist). The notes list only two of the three rules. The source gives all
  three, including "Water and Stone -- Water wins because stone sinks", plus a
  replay on a tie. The same list includes numbered ballots and short sticks,
  as the notes say. Also: the ASEAN Resource Centre catalogue URL for this book
  (`resourcecentre.asean.org/Book_Detail/?ID=1145`) currently serves unrelated
  gambling-spam content and should not be linked.
- **Correction:** Replace "The hosted PDF currently returns an error; this
  rests on its indexed text" with the archived locator and printed page
  numbers. Add the third rule. Do not link the ASEAN Resource Centre record.
- **Validation:** Registry entry with the Wayback URL, "Malaysia section,
  pp. 86–87", and status confirmed against source; the third rule appears.

### R1-8 [MEDIUM] The 1935 "Rochambeau" handbook: author attribution unconfirmed, imprint year 1936, and the game described is a team variant

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `01-global-chronology.md`, Chronology, "Twentieth century".
- **What:** (a) The teachinghistory.org "Ask a Historian" answer on rock paper
  scissors (node 23932) matches the notes' account: Ella Gardner's *Handbook
  for Recreation Leaders* (Children's Bureau) as the earliest American mention
  found, Culin 1895 as the likely ultimate source, *Stars and Stripes* and
  returning G.I.s after WWII, the Lafayette Square statue theory of the name.
  But the page as served carries **no author name**, and no source opened
  during this review attributes it to John B. Buescher. (b) The copy of the
  handbook digitised by FRASER (Federal Reserve Bank of St. Louis) is Bureau
  Publication No. 231, **GPO 1936**, with a letter of transmittal dated
  4 December 1935. The teachinghistory answer says it was first published in
  1935; no 1935 imprint was seen. (c) The handbook's "Rochambeau" (p. 50) is a
  game for two lines of players whose captains signal behind their backs,
  "choosing rock, scissors, or paper", explicitly likened to the handbook's
  Hunter, Fox, and Gun line game. It is a team version, not the two-player
  hand game.
- **Correction:** Cite the handbook directly (Gardner, *Handbook for
  Recreation Leaders*, Children's Bureau Publication 231, GPO; "1935 per
  teachinghistory.org; the digitised copy is dated 1936", p. 50) and describe
  it as a team variant. Cite the teachinghistory answer by URL and as
  unsigned, unless an attribution to Buescher is found and cited.
- **Validation:** Registry has two entries (handbook with FRASER URL and page;
  teachinghistory URL); "Buescher" appears only with a source for the
  attribution.

### R1-9 [MEDIUM] Hervey 1903 has now been read: it contains no *osom*-type game

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `04-malay-peninsula.md` (Hervey row: "Not yet checked");
  `06-open-questions.md` ("Read Hervey (1903) … in full").
- **What:** Wellcome Collection's digitised offprint (Wellcome b30208993) was
  read page by page, pp. 284–304. It describes some sixty games, mostly from
  Malacca (from notes by Munshi Muhammad Jaafar, per the first footnote), a few
  from Perak and Penang. There is no three-way hand game and no bird, stone or
  water hand signs. Turn-deciding is done by guessing which hand holds a seed
  (*tawak buta*, p. 288), drawing lots with palm-leaf ribs of unequal length
  (p. 298), tossing shells (p. 292) or coins. Absence in one 1903 Malacca
  collection is weak evidence; it does not show the game was unknown.
- **Correction:** Update the Hervey row to "Read in full (pp. 284–304): no
  *osom*-type game; turn-deciding by hidden-seed guessing, lots and shell
  tosses". Remove Hervey from the to-do item in `06-open-questions.md` and keep
  Wilkinson. State that the absence is not evidence of absence.
- **Validation:** Registry entry for Hervey with the Wellcome locator and
  status "checked: not present"; 06 no longer lists Hervey as unread.

### R1-10 [MEDIUM] Ogawa's *Jan Ken Po* is dated by a later listing (1982) rather than its publication (c1973; 2nd ed. 1978)

- **How established:** `CONFIRMED BY CATALOGUE`.
- **Where:** `05-regional-comparisons.md`, Hawaiʻi.
- **What:** CiNii (NCID BA10433802) records *Jan ken po: the world of Hawaii's
  Japanese Americans*, 2nd ed., Honolulu: University Press of Hawaii, **1978,
  c1973**, xii + 183 pp., ISBN 0824803981. The University of Hawaiʻi Press
  listing (via UBC Press) gives 1 December 1982 for the same ISBN
  (9780824803988), so "1982" is a listing or reprint date. The notes do say
  "listed", but the year a reader takes away is 1982, about ten years late for
  dating when the localised chant was in print. The publisher's description
  was checked only as the distributor's summary of the book, not against the
  book's text.
- **Correction:** "Dennis M. Ogawa, *Jan Ken Po* (1973; 2nd ed., University
  Press of Hawaii, 1978)". Cite the chant from the book with a page number if
  it is used as evidence.
- **Validation:** Registry entry with the CiNii NCID and date "c1973"; the 1982
  date no longer stands alone.

### R1-11 [MEDIUM] Claims that rest only on uncheckable screenshots appear in the headline answers without a flag

- **How established:** `METHODOLOGICAL CONCERN`.
- **Where:** `README.md` (second short answer: "glass–stone–water (Phuket,
  Krabi)", "bird–gun–water (… Phatthalung)"); `06-open-questions.md` (last
  "defensible answer": Phuket "supported by specific local accounts").
- **What:** Phuket glass–stone–water, the Krabi cup/glass version and the
  Phatthalung report come only from the owner's Facebook screenshots (one post
  plus comments; Phatthalung from "one grouped regional comment"). These are
  not reproduced, not archived, and not checkable by a reviewer. The body text
  (03) labels them as informal reports, but the README and 06 state them in
  the same register as the Dek-D-dated and documented items. "Specific local
  accounts" in 06 is the post plus one commenter.
- **Correction:** In the README and 06, mark these as "reported in one Facebook
  post and its comments (screenshots held privately; not independently
  checkable)". Consider archiving redacted screenshots in `evidence/` so a
  reviewer can at least see what was read.
- **Validation:** Every README/06 mention of Phuket, Krabi or Phatthalung
  variants carries the screenshot-only qualifier, or points to an archived
  copy.

### R1-12 [MEDIUM] None of the three Thai documentary anchors could be located as cited

- **How established:** `SOURCE NOT LOCATED`.
- **Where:** `02-thailand.md`, "Thai documentary anchors" table.
- **What:** (a) Thai Junior Encyclopedia vol. 13, "การละเล่นของเด็ก": the
  foundation's site (saranukromthai.or.th) has been restructured; old
  `sub/book/book.php?book=13…` URLs return 404 and the new index exposes
  volumes only by internal IDs. The online text, the spelling เป้ายิงฉุบ and
  the 2532/1989 catalogue date could not be confirmed. (b) Thailand Cultural
  Encyclopedia, "การเล่นพื้นบ้านในภาคกลาง": not checked (no locator given).
  (c) Dek-D, 26 June 2008: not located (see R1-2). Since (a) is the only dated
  Thai anchor (R1-1), the whole answer to question 1 currently has no
  re-checkable document.
- **Correction:** For each, give a URL or archived copy, the catalogue record
  for the volume (library, record ID, year) and, for vol. 13, a page number
  from the print volume.
- **Validation:** Registry entries for all three with locators; the vol. 13
  entry cites a catalogue record showing 2532.

### R1-13 [LOW] The *Wuzazu* passage is datable, and the notes undersell it

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `01-global-chronology.md`, Chronology row 1 and "Caution on the
  Chinese evidence".
- **What:** The passage (卷六 人部二, Wikisource text) is as the notes describe:
  手勢令 at a banquet of 後漢 generals and ministers, a list of names for palm,
  joints and each finger, and the author's admission "但不知其用法云何" (he does
  not know how it was played). It goes on to say Shi Hongzhao, not
  understanding it, drew his sword, which led to the extermination of his
  clan. Shi Hongzhao was a general of the Five Dynasties Later Han, killed
  with his relatives in 950. So the passage itself places 手勢令 at a
  mid-10th-century Later Han court. The notes call the Han identification
  "problematic"; the source makes it clear. The passage also likens it to a
  children's game of catching the middle finger, which the notes omit.
- **Correction:** Row 1: "Xie Zhaozhe's *Wuzazu* (Ming, c. 1600), juan 6,
  describes 手勢令 at a banquet of Five Dynasties Later Han (947–950)
  officials …". In the caution, replace "problematic" with "the reference to
  Shi Hongzhao (d. 950) places it in the Five Dynasties Later Han, not the Han
  dynasty".
- **Validation:** The row gives the juan and the 10th-century date; the
  caution no longer hedges what the passage states.

### R1-14 [LOW] Relevant evidence missed: the ASEAN Malaysia section also has a palm white/black balloting rhyme "Lai Lai Li Tham Plom"

- **How established:** `CONFIRMED AGAINST SOURCE`.
- **Where:** `03-southern-thailand.md` (assessment row "โอน้อยออก developed from
  Lai Lai Li Tam Plong"); `04-malay-peninsula.md` (Singapore palm-up/palm-down
  section).
- **What:** The same Malaysia section (printed p. 86) gives "Lai Lai Li Tham
  Plom" (variants "Lat Ta Li Lat Tham Plom", "La Da Li La Tham Pom"): players
  chant and show palm (white) or back of hand (black); the odd one out is
  chosen. This is a dated (2009) Malaysian attestation of the name the Facebook
  post links to โอน้อยออก, and a Malaysian counterpart to Singapore's *oh bey
  som*. It does not prove a derivation, but the notes say this claim "needs
  separate … evidence" without citing what exists.
- **Correction:** Cite it in both places as a dated attestation of the name
  and practice in Malaysia, with the same caution about derivation.
- **Validation:** The ASEAN p. 86 passage is cited in 03 and 04.

### R1-15 [LOW] Citation details: *BiblioAsia* title and the suten article

- **How established:** `CONFIRMED BY CATALOGUE` (both); the *BiblioAsia*
  content `CONFIRMED AGAINST SOURCE`.
- **Where:** `04-malay-peninsula.md`; `05-regional-comparisons.md`.
- **What:** (a) The article is titled **"Kampung Living: A–Z"** (not
  "Kampong"), *BiblioAsia* vol. 9 issue 4, Jan–Mar 2014, page dated
  1 January 2014. The *oh bey som* description in the notes matches it.
  (b) doi:10.21831/ej.v4i1.59575 resolves (Crossref) to Dewi Oktaviani and Dewi
  Kinasih, "Suten Games: Exploration of Empirical and Theoretical Probability
  for Junior High School Mathematics Learning", *Ethnomathematics Journal*
  **4(1): 19–35, 2023**. Content matches the notes (thumb elephant, index finger
  man, little finger ant; framed as fair determination; probability analysis;
  no historical claim). The notes give neither year, volume nor pages.
- **Correction:** Fix the title spelling; add year, volume, issue and pages
  for the suten article.
- **Validation:** Registry entries carry these fields.

### R1-16 [LOW] "Traditional Games Returns" not located

- **How established:** `SOURCE NOT LOCATED`.
- **Where:** `05-regional-comparisons.md`, Indonesia.
- **What:** No organisation or page of that name was found. The distinction
  between *suit* (elephant–human–ant) and *suit Jepang* /
  *batu–gunting–kertas* does appear in Indonesian sources seen in search
  results (not opened), so the claim is plausible; the citation is not
  re-checkable.
- **Correction:** Give the URL, or replace with a locatable source.
- **Validation:** Registry entry with a working URL.

### R1-17 [LOW] Small wording drift between README and body

- **How established:** `INTERNAL INCONSISTENCY`.
- **Where:** `README.md`, `03-southern-thailand.md`, `05-regional-comparisons.md`.
- **What:** The README lists "glass–stone–water (Phuket, Krabi)"; 03 reports
  Krabi as "cup/glass (จอก/แก้ว)–stone–water". The Phuket chant is spelled
  วันตูโส้ม (03 heading) and วันตูส้ม (03 last paragraph, 05) without saying
  whether these are variants or one form.
- **Correction:** README: "glass–stone–water (Phuket), cup/glass–stone–water
  (Krabi)". Pick one spelling or state that both occur and where.
- **Validation:** README and 03 agree; one spelling or an explicit note.

## What it got right

- **Culin 1895 is a real, firm anchor and is described correctly.** In
  *Korean Games* (1895), under XXXVII Syou-pyek-tchi-ki (hand-clapping),
  pp. 44–45, Culin describes Japanese Ishi Ken, usually called Janken, with
  stone (fist), paper (open hand) and scissors, and the rules: "Stone beats
  scissors, as scissors will not cut stone." He also describes Mushi Ken
  (snake, frog, slug), matching the notes' symbol list.
- **The *Wuzazu* reading is correct and resists the popular overclaim.** The
  passage does list hand and finger names and does say the author did not know
  how it was played; the notes refused to turn it into "Han-dynasty RPS"
  (only too cautious about the date: R1-13).
- **The Phuket dictionary date discrepancy is real and correctly stated.** NDL
  Search (R100000002-I028323271) gives the title with "พุทธศักราช ๒๕๖๐" and
  "(พ.ศ. ๒๔๕๒-๒๕๖๐)" for the 108th anniversary, but "issued 2559 [2016]",
  486 pp., publisher โรงเรียนสตรีภูเก็ต, creator ʻAnan ʻĀrīphong, ISBN
  9786163956347, LC control no. 2017341583. The notes also correctly say the
  วันตูโส้ม entry itself was not located.
- **The ASEAN summary is accurate where it speaks** (names, simultaneous
  reveal, three symbols, the two rules given, the other lot-drawing methods),
  despite having been written without the PDF.
- **The *oh bey som* reading is accurate**, and the notes drew the right
  conclusion from it: "som" names cover different procedures, so names alone
  cannot reconstruct the history.
- **The 1935 handbook and the WWII servicemen story match the teachinghistory
  answer**, including the Lafayette Square theory being flagged as
  speculative there (attribution and date aside: R1-8).
- **The WWII-introduction story is correctly treated as a hypothesis**, and the
  notes repeatedly separate "attested in X by year Y" from "arrived in X in
  year Y", and the four transmission directions in 03 are left open rather
  than picked.

## Verdict

**Blocks reuse (citing, teaching or publishing the short answers):**

- R1-1: the question-1 answer's 1939 framing; fix the wording now, it needs no
  new source.
- R1-2 and R1-4: the question-2 answer's evidence base. Until the Dek-D comment
  is re-located and the Singapore claim is sourced or dropped, the README
  should not present the chant match and the Singapore leg as established.
- R1-3: the 19th-century row overstates its source.
- R1-12: the Thai documentary anchors need locators before anything dated is
  quoted from them.

**Can wait (before the source registry is called complete):** R1-5, R1-6,
R1-7, R1-8, R1-9, R1-10, R1-11 (wording can be fixed now; archiving
screenshots can wait), R1-13 to R1-17.

**Count:** BLOCKER 0, HIGH 4, MEDIUM 8, LOW 5 (17 findings).

## Sources consulted

All accessed 2026-11-06.

| source | URL opened | result |
| --- | --- | --- |
| Culin, *Korean Games* (1895), Internet Archive full text (item `koreangameswith01culigoog`) | https://archive.org/download/koreangameswith01culigoog/koreangameswith01culigoog_djvu.txt | read pp. 44–45 |
| Xie Zhaozhe, *Wuzazu* 卷06, Wikisource (raw wikitext) | https://zh.wikisource.org/w/index.php?title=%E4%BA%94%E9%9B%9C%E4%BF%8E/%E5%8D%B706&action=raw | passage read |
| Chinese Text Project search for 手勢令 | https://ctext.org/wiki.pl?if=gb&res=834213&searchu=手勢令 | blocked automated access; not used |
| Wikipedia, "Shi Hongzhao" | https://en.wikipedia.org/wiki/Shi_Hongzhao | death 950, Later Han |
| Wikipedia, "Rock paper scissors" | https://en.wikipedia.org/wiki/Rock_paper_scissors | used only to find the teachinghistory URL |
| teachinghistory.org, Ask a Historian: Rock Paper Scissors | https://teachinghistory.org/history-content/ask-a-historian/23932 | read; no author named on page |
| Gardner, *Handbook for Recreation Leaders* (Children's Bureau Pub. 231), FRASER full text | https://fraser.stlouisfed.org/title/handbook-recreation-leaders-8506/fulltext | Rochambeau p. 50; imprint 1936; transmittal 4 Dec 1935 |
| Mental Floss, "Why Do People Call Rock-Paper-Scissors 'Roshambo?'" | https://www.mentalfloss.com/article/80201/why-do-people-call-rock-paper-scissors-roshambo | does not mention Buescher |
| NDL CRD, Yokohama Central Library answer (横浜市中央2750) | https://crd.ndl.go.jp/reference/entry/index.php?id=1000362787&page=ref_view | 1804–1843 estimate, from Kako 2008 |
| NDL CRD, Takasaki City Central Library answer (R1001861) | https://crd.ndl.go.jp/reference/entry/reference/show?page=ref_view&id=1000360742 | no period given |
| Hervey, "Malay Games" (1903), Wellcome offprint PDF | https://iiif.wellcomecollection.org/pdf/b30208993 | pp. 284–304 read (page images) |
| Internet Archive search, title "malay games" | https://archive.org/advancedsearch.php?q=title%3A%28malay+games%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=creator&fl%5B%5D=date&rows=20&output=json | no Hervey copy |
| ASEAN 2009 compilation, live hosted URL | https://dispar.ciamiskab.go.id/wp-content/uploads/2023/08/Compilation-od-Tradional-Asean-Childrens-Songs-Dances-Games-and-Story-Telling.pdf | returns "page not found" HTML |
| ASEAN 2009 compilation, Internet Archive capture | http://web.archive.org/web/20250520185553/https://dispar.ciamiskab.go.id/wp-content/uploads/2023/08/Compilation-od-Tradional-Asean-Childrens-Songs-Dances-Games-and-Story-Telling.pdf | read Malaysia section pp. 85–87 |
| ASEAN Resource Centre record ID 1145 | https://resourcecentre.asean.org/Book_Detail/?ID=1145 | serves gambling spam; do not link |
| PBRU library record for the ASEAN compilation | https://book.pbru.ac.th/bib/61309 | connection refused |
| *BiblioAsia* vol. 9 issue 4 contents | https://biblioasia.nlb.gov.sg/vol-9/issue-4/jan-mar-2014/ | article listed |
| Nor Afidah Abd Rahman, "Kampung Living: A–Z" | https://biblioasia.nlb.gov.sg/all-sections/vol-9-issue-4-jan-march-2014-kampung-living-singapore/ | *oh bey som* read |
| DBP PRPM search | https://prpm.dbp.gov.my/Cari1?keyword=osom (also `ohsom`, `oh%20som`, `wan%20tu%20som`, `batu%20air%20burung`) | no advisory result |
| Suten DOI / Crossref / article | https://doi.org/10.21831/ej.v4i1.59575 ; https://api.crossref.org/works/10.21831/ej.v4i1.59575 ; https://journal.uny.ac.id/index.php/ethnomath/article/download/59575/19437 | metadata and text read |
| Ogawa, CiNii record | https://ci.nii.ac.jp/ncid/BA10433802 | 1978, c1973 |
| Ogawa, UBC Press (UH Press distributor) listing | https://www.ubcpress.ca/jan-ken-po | 1 Dec 1982 listing |
| Phuket dialect dictionary, NDL Search OpenSearch API | https://ndlsearch.ndl.go.jp/api/opensearch?title=%E0%B8%9E%E0%B8%88%E0%B8%99%E0%B8%B2%E0%B8%99%E0%B8%B8%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B8%96%E0%B8%B4%E0%B9%88%E0%B8%99%E0%B8%A0%E0%B8%B9%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95 | record R100000002-I028323271 |
| Thai Junior Encyclopedia site | https://www.saranukromthai.or.th/index ; https://www.saranukromthai.or.th/sub/book/book.php?book=13&chap=6&page=t13-6-infodetail01.html (and two sibling URLs) | old URLs 404; vol. 13 not found |
| "Colour of Time" blog (checked as a possible Kamaruddin source) | https://landbelowwind098.blogspot.com/search?q=osom | no match; not the source |

Web searches without an opened result (Dek-D article; Hat Yai chant;
Kamaruddin Abdullah; Traditional Games Returns; Buescher attribution) are
recorded in the findings as `SOURCE NOT LOCATED` and support no claim here.

## Source locators found

For the owner's source registry. Only sources actually opened are listed.

| source | locator |
| --- | --- |
| Culin, Stewart. *Korean Games, with Notes on the Corresponding Games of China and Japan*. Philadelphia: University of Pennsylvania, 1895. Ishi Ken / Janken and Mushi Ken: pp. 44–45 (§ XXXVII, hand-clapping) | Internet Archive item `koreangameswith01culigoog`: https://archive.org/details/koreangameswith01culigoog (full text: https://archive.org/download/koreangameswith01culigoog/koreangameswith01culigoog_djvu.txt) |
| Xie Zhaozhe 謝肇淛, *Wuzazu* 五雜俎, 卷六 人部二, 手勢令 passage | https://zh.wikisource.org/wiki/五雜俎/卷06 |
| Kako Satoshi 加古里子, 『伝承遊び考 4』, Kobunsha, 2008.7, pp. 11, 40–45 (1804–1843 estimate), as relayed in NDL CRD answer by Yokohama Central Library, 管理番号 横浜市中央2750 | https://crd.ndl.go.jp/reference/entry/index.php?id=1000362787&page=ref_view |
| NDL CRD answer, Takasaki City Central Library, R1001861 (no date estimate) | https://crd.ndl.go.jp/reference/entry/reference/show?page=ref_view&id=1000360742 |
| Gardner, Ella. *Handbook for Recreation Leaders*. U.S. Children's Bureau Publication No. 231. Washington: GPO, 1936 (transmittal dated 4 Dec 1935). "Rochambeau", p. 50 | FRASER: https://fraser.stlouisfed.org/title/handbook-recreation-leaders-8506 (full text: …/fulltext) |
| "Rock Paper Scissors", Ask a Historian, teachinghistory.org (RRCHNM, George Mason University), unsigned on page | https://teachinghistory.org/history-content/ask-a-historian/23932 |
| Hervey, D. F. A. "Malay Games." *Journal of the Anthropological Institute of Great Britain and Ireland* 33 (1903): 284–304 (offprint) | Wellcome Collection b30208993: https://iiif.wellcomecollection.org/pdf/b30208993 ; persistent URL printed in the PDF: https://wellcomecollection.org/works/weqtqs57 |
| ASEAN Committee on Culture and Information. *Compilation of Traditional ASEAN Children's Songs, Dances, Games, and Story-Telling*. 2009. Malaysia section: One Two Som pp. 86–87; Lai Lai Li Tham Plom p. 86; games list p. 85 | Wayback capture 2025-05-20: http://web.archive.org/web/20250520185553/https://dispar.ciamiskab.go.id/wp-content/uploads/2023/08/Compilation-od-Tradional-Asean-Childrens-Songs-Dances-Games-and-Story-Telling.pdf |
| Nor Afidah Abd Rahman. "Kampung Living: A–Z." *BiblioAsia* 9(4), Jan–Mar 2014 (page dated 1 Jan 2014). "OH BEY SOM!" entry | https://biblioasia.nlb.gov.sg/all-sections/vol-9-issue-4-jan-march-2014-kampung-living-singapore/ |
| Oktaviani, Dewi, and Dewi Kinasih. "Suten Games: Exploration of Empirical and Theoretical Probability for Junior High School Mathematics Learning." *Ethnomathematics Journal* 4(1): 19–35, 2023 | doi:10.21831/ej.v4i1.59575 → https://journal.uny.ac.id/index.php/ethnomath/article/view/59575 |
| Ogawa, Dennis M. *Jan Ken Po: The World of Hawaii's Japanese Americans*. 2nd ed. Honolulu: University Press of Hawaii, 1978, c1973. ISBN 0824803981 | CiNii NCID BA10433802: https://ci.nii.ac.jp/ncid/BA10433802 ; LCCN 78009513 |
| อนันต์ อารีย์พงศ์ (ed.). *พจนานุกรมภาษาถิ่นภูเก็ต พุทธศักราช ๒๕๖๐ : ที่ระลึกครบ ๙ รอบ ๑๐๘ ปี สตรีภูเก็ต (พ.ศ. ๒๔๕๒-๒๕๖๐)*. Phuket: โรงเรียนสตรีภูเก็ต, 2559 [2016]. 486 pp. ISBN 9786163956347 | NDL Search R100000002-I028323271: https://ndlsearch.ndl.go.jp/books/R100000002-I028323271 ; NDLBibID 028323271; LC control no. 2017341583 |
| Shi Hongzhao (d. 950), for dating the *Wuzazu* passage | https://en.wikipedia.org/wiki/Shi_Hongzhao |

**Not located** (no locator to record): DBP 7 Sept 2018 *osom* enquiry;
Kamaruddin Abdullah, "The Games We Played" (2013); Thai Junior Encyclopedia
vol. 13 online text and its 2532 catalogue record; Dek-D article and comments
of 26–29 June 2008; Traditional Games Returns; an attribution of the
teachinghistory answer to John B. Buescher.
