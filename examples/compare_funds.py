"""Compare 2-3 funds in one call: returns, risk, and pairwise portfolio
overlap. Mirrors the compare example in https://punji.ai/llms-api.md.
"""
from _client import post

SLUGS = ["ppfas-flexi-cap-fund", "quant-flexi-cap-fund"]


def compare(slugs: list[str], include: list[str]) -> dict:
    return post("/compare", {"slugs": slugs, "include": include})


if __name__ == "__main__":
    result = compare(SLUGS, include=["returns", "risk", "overlap"])
    print(result)
