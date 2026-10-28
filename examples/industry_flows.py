"""All-category mutual fund flow snapshot for a given month: net flows,
AUM, folio growth, market share, and derived flow signals per category.
"""
from _client import get


def industry_flows(period: str | None = None) -> list[dict]:
    """period: 'YYYY-MM', omit for the latest available month."""
    params = {"period": period} if period else None
    return get("/industry/flows", params)


if __name__ == "__main__":
    for row in industry_flows():
        print(row)
