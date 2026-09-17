"""Build the durable, page-numbered local text corpus before any paper Q&A."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


def write_json(file, value):
    temporary = file.with_suffix(file.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    out = root / "literature-corpus"
    text_dir = out / "text"
    notes_dir = out / "notes"
    text_dir.mkdir(parents=True, exist_ok=True)
    notes_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for source in (root / "website/_data/literature_review").glob("papers_*.json"):
        records.extend(json.loads(source.read_text(encoding="utf-8")))
    by_hash = {paper["sha256"]: paper for paper in records}
    files = []
    excluded = {"website", "literature-review", "literature-corpus", "duplicate-paper-archive"}
    for folder in sorted(root.iterdir()):
        if folder.is_dir() and not folder.name.startswith(".") and folder.name not in excluded:
            files.extend(sorted(folder.rglob("*.pdf")))
    grouped = {}
    print(f"Hashing {len(files)} PDFs...", flush=True)
    for file in files:
        if not file.resolve().is_relative_to(root):
            continue
        with file.open("rb") as source:
            digest = hashlib.file_digest(source, "sha256").hexdigest()
        grouped.setdefault(digest, []).append(str(file.relative_to(root)))
    documents = []
    now = datetime.now(timezone.utc).isoformat()
    for position, (digest, paths) in enumerate(grouped.items(), 1):
        record = by_hash.get(digest)
        label = record["id"] if record else "UNINDEXED"
        print(f"[{position}/{len(grouped)}] {label} {paths[0]}", flush=True)
        json_file = text_dir / (digest + ".json")
        document = {"sha256": digest, "paper_id": record["id"] if record else None, "title": record["title"] if record else "", "sources": paths, "extracted_at": now, "status": "pending"}
        try:
            saved = json.loads(json_file.read_text(encoding="utf-8")) if json_file.exists() and not args.refresh else None
            if saved and saved.get("sha256") == digest:
                pages = saved["pages"]
            else:
                reader = PdfReader(root / paths[0])
                pages = [{"page": index + 1, "text": (page.extract_text() or "").encode("utf-16-le", "surrogatepass").decode("utf-16-le", "replace")} for index, page in enumerate(reader.pages)]
            empty_pages = [page["page"] for page in pages if len(page["text"].strip()) < 40]
            document.update(status="extracted", pages=len(pages), characters=sum(len(page["text"]) for page in pages), sparse_pages=empty_pages, replacement_characters=sum(page["text"].count("\ufffd") for page in pages), text_file=f"text/{digest}.txt", json_file=f"text/{digest}.json")
            write_json(json_file, {"schema_version": 1, "sha256": digest, "extracted_at": now, "pages": pages, "sparse_pages": empty_pages, "scope": "PDF text layer; figures and scanned images are not OCR'd"})
            (text_dir / (digest + ".txt")).write_text("\n\n".join(f"=== PDF PAGE {page['page']} ===\n{page['text']}" for page in pages), encoding="utf-8")
            first = "\n".join(page["text"] for page in pages[:2])
            document["first_page_excerpt"] = first[:1600]
            document["arxiv_candidates"] = sorted(set(re.findall(r"arXiv\s*:\s*(\d{4}\.\d{4,5})(?:v\d+)?", first, re.I)))
            if record:
                lines = [f"# {record['id']} · {record['title']}", "", f"全文提取：{len(pages)} 页；SHA-256：`{digest}`。", f"完整提取文本：`../text/{digest}.txt`。", "", f"摘要来源：已有结构化阅读笔记（原核查日期：{record.get('verified', '未记录')}）。全文缓存重建不等于人工重新核验全部摘要。", ""]
                labels = {"authors": "作者", "date": "时间与版本", "venue": "发表信息", "abstract_zh": "中文摘要", "contribution": "贡献", "boundary": "问题边界", "method": "方法", "results": "结果", "limitations": "局限", "evidence": "依据", "paper_links": "论文链接", "project_links": "项目链接", "abstract_en": "原文摘要"}
                for field, title in labels.items():
                    if record.get(field):
                        lines.extend([f"## {title}", "", str(record[field]), ""])
                (notes_dir / (record["id"] + ".md")).write_text("\n".join(lines), encoding="utf-8")
                document["summary_file"] = "notes/" + record["id"] + ".md"
                document["summary_status"] = "existing_review"
            else:
                document["summary_status"] = "needs_review"
        except Exception as error:
            document.update(status="failed", error=f"{type(error).__name__}: {str(error)[:300]}")
        documents.append(document)
        write_json(out / "manifest.json", {"schema_version": 1, "updated_at": now, "complete": position == len(grouped), "source_files": len(files), "unique_documents": len(grouped), "documents": documents})
    by_title = {}
    for record in records:
        key = re.sub(r"[^a-z0-9]", "", record["title"].lower())
        by_title.setdefault(key, []).append({"id": record["id"], "title": record["title"], "sha256": record["sha256"], "date": record.get("date"), "version": record.get("version"), "links": record.get("paper_links")})
    report = {"exact_duplicates": [doc for doc in documents if len(doc["sources"]) > 1], "same_title_candidates": [group for group in by_title.values() if len(group) > 1], "unindexed": [doc for doc in documents if not doc["paper_id"]], "failed": [doc for doc in documents if doc["status"] != "extracted"], "missing_local_pdf": [paper["id"] for paper in records if paper["sha256"] not in grouped]}
    write_json(out / "audit.json", report)
    print(json.dumps({"files": len(files), "unique_documents": len(grouped), "pages": sum(doc.get("pages", 0) for doc in documents), "exact_duplicate_groups": len(report["exact_duplicates"]), "same_title_groups": len(report["same_title_candidates"]), "unindexed": len(report["unindexed"]), "failed": len(report["failed"]), "missing_local_pdf": report["missing_local_pdf"]}), flush=True)


if __name__ == "__main__":
    main()
