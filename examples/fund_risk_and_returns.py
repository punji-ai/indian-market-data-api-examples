"""Pull a fund's risk metrics and rolling-window returns by slug.

Mirrors the example in https://punji.ai/llms-api.md#example-requests, using
the real slug for Parag Parikh Flexi Cap Fund's Direct-Growth plan.
"""
from _client import get

SLUG = "ppfas-flexi-cap-fund"


def fund_risk(slug: str, years: int = 3) -> dict:
    return get(f"/schemes/{slug}/risk", {"years": years})


def fund_rolling_returns(slug: str) -> list[dict]:
    return get(f"/schemes/{slug}/returns/rolling")


if __name__ == "__main__":
    risk = fund_risk(SLUG, years=3)
    print(f"{SLUG} - 3Y risk metrics:")
    print(risk)

    returns = fund_rolling_returns(SLUG)
    print(f"\n{SLUG} - rolling returns, all windows:")
    for r in returns:
        print(f"  {r['duration_years']}Y: median CAGR {r['median_cagr_pct']}%")
