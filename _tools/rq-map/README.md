# RQ atlas maintenance

The atlas is rendered in `/literature-review/#lr-rq-atlas`. It relates the two
research routes to important questions, leaf questions, and individual papers.
It is an editorial synthesis with source evidence, not an automatically inferred
citation network or a claim of exhaustive literature coverage.

## Source and build

From the research workspace (the parent of this website checkout), run:

```powershell
python website/_tools/rq-map/build.py
node .literature-tools/build-preview.cjs
node .literature-tools/check-rq.cjs
node .literature-tools/check-preview.cjs
```

The preview and browser-check scripts are workspace tooling. The generator uses
Python's standard library and requires the local `literature-corpus/manifest.json`
and the website's existing structured reading notes. It writes the committed
`_data/literature_rq.json`; Jekyll builds need no private corpus or Python step.
The generator checks local inventory coverage, paper mappings, source anchors,
unique edges, and continuity of the displayed literature chains.

The page uses `rq-map.liquid`, `assets/js/literature-rq.js`, and
`assets/css/literature-rq.css`. Data is embedded for offline previews and also
published at `/assets/data/literature-rq.json` for download.

## Evidence conventions

- The root questions, hierarchy, and changes of conditions are our synthesis.
  `research_question.kind` distinguishes authors' explicit numbered RQs in
  Chinese paraphrase from questions rewritten from their problem statements.
- `citation` edges require a checked reference in the citing paper. `evidence`
  records a PDF page, section, or reference number; `url` opens the citing source.
  A reference may be a comparison or limitation, not an inherited algorithm.
- `synthesis` and `comparison` edges are dashed and must not be represented as
  verified citations. `lanes` selects readable chains from the evidenced edges.
- `collected` means an active local PDF exists. Reading an online abstract or
  full text does not change that state. External `Sxx` records preserve their
  discovery seed and snowball depth. Blue and amber encode collection status.
- A `core` mapping concerns the question directly; a `support` mapping provides
  a method, evaluation tool, or adjacent scenario. It does not claim that a
  generic reasoning or statistics paper implements an XR/world system.

When adding a paper, first resolve it through the manifest and historical
aliases, read cached page-numbered text, update the relevant curated branches,
and check predecessor claims against primary sources. If an external paper is
subsequently collected, merge its public record with the new canonical `Pxxx`
entry and redirect all anchors, mappings, edges, and seeds. Preserve old IDs.
Update the snapshot date when evidence changes. Archive duplicate versions only
through the established corpus workflow; do not ingest the duplicate archive.

Do not publish corpus full text, personal annotations, local chat history, or
credentials. The public data contains bibliographic metadata, summaries, and
source locations, not extracted paper bodies.

## Validation scope

The 2026-09-19 snapshot has 398 local papers, 46 external additions, 29 leaf RQs,
and 57 relations. Browser checks cover both
routes, all branches, filters, parent and paper sources, citation evidence,
canonical-ID redirects, note links, data downloads, keyboard use, and mobile
overflow. Existing library checks guard its sorting, search, notes, and exports.
After publishing, run the browser checks with the public page URL as the first
argument to verify the deployed assets and embedded data as well.

## Worldbuilding synthesis

The homepage synthesis uses `_data/literature_synthesis.json` and
`world-synthesis.liquid`. The same data is exported at
`/assets/data/literature-synthesis.json`. Paper links resolve against the atlas,
so collection colors follow the actual inventory; reading an online PDF does
not mark it collected. Evaluation protocols and candidate projects are labeled
as proposals, separately from evidence about published work.

`world-synthesis-overlay.json` preserves the reviewed root question, W1e/W3e,
paper discovery provenance, and new relations during atlas regeneration.
Keep the corresponding records in `_data/literature_annotations.json` when
extending author collections. C10 was found in Retcon's reference [17]; other
new cross-paper comparisons remain dashed. B3 remains deferred.

After a synthesis change, run these workspace checks in addition to rebuilding:

```powershell
node .literature-tools/check-synthesis.cjs
node .literature-tools/check-team-evidence.cjs
```

They check reference integrity, both directions of RQ mappings, collection
colors, filters, deep links, data downloads, keyboard use, mobile layouts and
the no-JavaScript fallback. No local PDF bodies or personal notes are exported.
