"""Read the extracted corpus first. Q&A never opens or reparses a PDF."""
import argparse
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(input())
    text_dir = args.root.resolve() / "literature-corpus/text"
    output = []
    terms = set(re.findall(r"[a-z0-9]{3,}", request.get("question", "").lower()))
    for paper in request["papers"]:
        digest = paper["sha256"]
        item = {"id": paper["id"], "pages": [], "source": "summary", "total_pages": paper.get("pages", 0)}
        try:
            if not re.fullmatch(r"[a-f0-9]{64}", digest):
                raise ValueError("Invalid paper fingerprint")
            saved = json.loads((text_dir / (digest + ".json")).read_text(encoding="utf-8"))
            if saved.get("sha256") != digest or not isinstance(saved.get("pages"), list):
                raise ValueError("Invalid extracted text")
            pages = saved["pages"]
            requested = {int(n) for n in re.findall(r"(?:page|p\.?|页)\s*(\d+)", request.get("question", ""), re.I)}
            requested.update(int(n) for n in re.findall(r"第?\s*(\d+)\s*页", request.get("question", "")))
            ranked = sorted(pages, key=lambda page: (page["page"] in requested, page["page"] <= 2, sum(page["text"].lower().count(t) for t in terms), -page["page"]), reverse=True)
            remaining = 60000
            chosen = []
            for page in ranked:
                text = page["text"].strip()
                if not text or remaining <= 0:
                    continue
                selected = text[:remaining]
                chosen.append({"page": page["page"], "text": selected, "truncated": len(selected) < len(text)})
                remaining -= len(selected)
            item.update(source="pdf" if chosen else "summary", read_from="extracted_text", pages=sorted(chosen, key=lambda p: p["page"]), total_pages=len(pages))
        except (OSError, ValueError, KeyError, TypeError):
            item["warning"] = "Extracted text missing or invalid. Rebuild the local corpus; this answer only has the library summary."
        output.append(item)
    print(json.dumps(output, ensure_ascii=True))


if __name__ == "__main__":
    main()
