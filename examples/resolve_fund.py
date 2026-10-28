"""Resolve a fund name typed by a user into a stable `slug` - the key every
other Punji API endpoint expects. See the Conventions section in
https://punji.ai/llms-api.md for why resolve-first is the right pattern
whenever you have free-text input rather than a known slug.
"""
from _client import get


def resolve_fund(query: str) -> str | None:
    result = get("/schemes/resolve", {"q": query})
    if result["status"] == "resolved":
        return result["candidates"][0]["slug"]
    if result["status"] == "ambiguous":
        print(f"Ambiguous match for {query!r}, candidates:")
        for c in result["candidates"]:
            print(f"  - {c['slug']}: {c.get('scheme_name', c['slug'])}")
        return None
    print(f"No match for {query!r}")
    return None


if __name__ == "__main__":
    slug = resolve_fund("parag parikh flexi cap")
    if slug:
        print(f"Resolved slug: {slug}")
