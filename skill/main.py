import os
import re
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
import requests


load_dotenv()


def normalize_tokens(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    tokens = text.split()
    return [t for t in tokens if len(t) > 2]


def find_in_obsidian(vault_path: str, prompt: str) -> List[Dict[str, Any]]:
    if not vault_path or not Path(vault_path).exists():
        return []

    prompt_tokens = normalize_tokens(prompt)
    hits: List[Dict[str, Any]] = []

    for p in Path(vault_path).rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        content = text.lower()
        title = p.stem.lower()
        score = 0

        for token in prompt_tokens:
            if token in title:
                score += 4
            if token in content:
                score += 2

        if score > 0:
            hits.append({
                "title": p.stem,
                "path": str(p),
                "score": score,
                "preview": text[:220].replace("\n", " ")
            })

    return sorted(hits, key=lambda x: x["score"], reverse=True)[:5]


def notion_search(query: str, api_key: str, database_id: str) -> List[Dict[str, Any]]:
    if not api_key or not database_id:
        return []

    url = "https://api.notion.com/v1/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    payload = {
        "query": query,
        "filter": {"property": "object", "value": "page"},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return []

    results = []
    for item in data.get("results", []):
        page_id = item.get("id")
        props = item.get("properties", {})
        title = ""
        for key, value in props.items():
            if value.get("type") == "title":
                title = "".join([t.get("plain_text", "") for t in value.get("title", [])])
                break

        if not title:
            title = item.get("object", "page")

        url_value = item.get("url", "")
        results.append({
            "title": title,
            "url": url_value,
            "id": page_id,
        })

    return results[:5]


def build_response(prompt: str, obsidian_hits: List[Dict[str, Any]], notion_hits: List[Dict[str, Any]]) -> str:
    literal = []
    if obsidian_hits:
        for hit in obsidian_hits[:3]:
            literal.append(f"- {hit['title']} :: {hit['path']}")
    if notion_hits:
        for hit in notion_hits[:3]:
            literal.append(f"- {hit['title']} :: {hit['url']}")

    if not literal:
        literal.append("- Nothing cleanly matched. That is not a failure. It means the hidden thread is still underneath the obvious surface.")

    metaphors = [
        "- The feeling is probably a signal, not a fact.",
        "- Look for the pattern beneath the emotional noise.",
        "- The connection may not be literal; it may be structural.",
    ]

    wild = [
        "- The weirdest link is often the one that keeps the system open.",
        "- If this seems random, test whether it is actually the missing bridge.",
        "- Do not treat the strange part as noise; treat it as a clue.",
    ]

    return (
        f"Prompt: {prompt}\n\n"
        "The Literal:\n" + "\n".join(literal) + "\n\n"
        "The Metaphorical:\n" + "\n".join(metaphors) + "\n\n"
        "The Wild:\n" + "\n".join(wild) + "\n\n"
        "Anchor:\n"
        "- The missing piece is probably not the obvious fact. It is the hidden connection that keeps the story coherent."
    )


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Mycelium Connector")
    parser.add_argument("--prompt", required=True, help="The feeling, word, or concept to search for.")
    args = parser.parse_args()

    prompt = args.prompt.strip()
    vault_path = os.getenv("OBSIDIAN_VAULT_PATH", "")
    api_key = os.getenv("NOTION_API_KEY", "")
    database_id = os.getenv("NOTION_DATABASE_ID", "")

    obsidian_hits = find_in_obsidian(vault_path, prompt)
    notion_hits = notion_search(prompt, api_key, database_id)

    print(build_response(prompt, obsidian_hits, notion_hits))


if __name__ == "__main__":
    main()
