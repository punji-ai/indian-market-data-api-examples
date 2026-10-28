"""Resolve a stock name to its slug, then pull recent bulk/block deals.
Mirrors the stock example in https://punji.ai/llms-api.md.
"""
from _client import get


def resolve_stock(query: str) -> str | None:
    result = get("/stocks/resolve", {"q": query})
    if result["status"] == "resolved":
        return result["candidates"][0]["slug"]
    if result["status"] == "ambiguous":
        print(f"Ambiguous match for {query!r}:", result["candidates"])
        return None
    return None


def recent_deals(slug: str, limit: int = 10) -> list[dict]:
    return get(f"/stocks/{slug}/deals", {"limit": limit})


if __name__ == "__main__":
    slug = resolve_stock("reliance industries")
    if slug:
        print(f"Resolved slug: {slug}")
        for deal in recent_deals(slug, limit=10):
            print(deal)
