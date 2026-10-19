# Direction review from xr+aigc.pptx

The original 30-slide PowerPoint stays local. `data/ppt-direction-plan.json`
contains the reviewed direction contracts, slide references, five scenario comparisons,
and factual corrections. `data/ppt-paper-updates.json` contains newly checked sources
and explicit reading-role decisions. Direction classification is interpretation, not
a replacement for a paper's original six-axis task taxonomy.

Rebuild from the repository root:

```sh
python topics/scripts/apply-ppt-direction-plan.py
python topics/scripts/render-lineage.py
python topics/scripts/validate-resources.py
```

If regenerating the historical profiles with `build-direction-analysis.py`, run it
before these commands. The PPT application script is idempotent. It updates all eight
direction articles, corresponding overviews, data memberships and paper filters.
The generated membership JSON/CSV includes both primary reading assignment and
role within each direction; historical cards and original evidence remain available.

Technical and resource annotations now also attach to direction and history cards.
The original 451-paper library, 287 technical records, and 774 resource records remain
intact. Four new PPT references carry their own checked/unknown fields inline. Two
of these are a project report and an engineering repository, not confirmed conference
papers. They are not silently included in the earlier resource-audit denominator.

The local `research-preview/problem-lineage-research.html` copy embeds annotation
data so it works with `file://`; the local sync helper is not part of the public site.
