"""SIP (Systematic Investment Plan) returns for a fund over several lookback
windows - distinct from CAGR, since a SIP has many cash flows on different
dates rather than a single start/end value.
"""
from _client import get

SLUG = "ppfas-flexi-cap-fund"


def sip_returns(slug: str, years: str = "3,5,7,10") -> list[dict]:
    return get(f"/schemes/{slug}/returns/sip", {"years": years})


if __name__ == "__main__":
    # Printed raw: the exact response field names for this endpoint aren't
    # spelled out in https://punji.ai/llms-api.md, so inspect the real
    # response here rather than guessing field names.
    for row in sip_returns(SLUG):
        print(row)
