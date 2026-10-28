# Indian Mutual Fund & Stock Market Data API - Python Examples (Punji)

Python examples for the [Punji Data API](https://punji.ai/developers) - programmatic access
to Indian mutual fund and stock market data: fund/stock lookup, returns, risk metrics,
holdings, category leaderboards, AMC/fund-manager info, industry fund-flow data, and
fund/stock comparison.

Full endpoint reference: [punji.ai/llms-api.md](https://punji.ai/llms-api.md) (also readable
by LLM agents directly) or the human docs at [punji.ai/developers](https://punji.ai/developers).

## Quickstart

```bash
curl -s "https://api.punji.ai/v1/schemes/parag-parikh-flexi-cap-fund-direct-plan-growth-48b786/returns/rolling" \
  -H "X-API-Key: $PUNJI_API_KEY"
```

```python
import requests

resp = requests.get(
    "https://api.punji.ai/v1/schemes/parag-parikh-flexi-cap-fund-direct-plan-growth-48b786/returns/rolling",
    headers={"X-API-Key": "pk_live_..."},
)
print(resp.json())
```

Real response, Parag Parikh Flexi Cap Fund (Direct Plan - Growth) as of `calc_as_of` 2026-09-14.
Run the curl command above to get a current one - this snapshot ages as the fund's data refreshes.

```json
[
  { "duration_years": 1, "min_cagr_pct": -21.2652, "max_cagr_pct": 100.0569, "median_cagr_pct": 17.3433, "calc_as_of": "2026-09-14" },
  { "duration_years": 3, "min_cagr_pct": 0.742,   "max_cagr_pct": 37.6443,  "median_cagr_pct": 19.2866, "calc_as_of": "2026-09-14" },
  { "duration_years": 5, "min_cagr_pct": 4.1806,  "max_cagr_pct": 33.6188,  "median_cagr_pct": 19.09,   "calc_as_of": "2026-09-14" },
  { "duration_years": 7, "min_cagr_pct": 14.1952, "max_cagr_pct": 22.3035,  "median_cagr_pct": 19.2757, "calc_as_of": "2026-09-14" },
  { "duration_years": 10, "min_cagr_pct": 16.8544, "max_cagr_pct": 21.5043, "median_cagr_pct": 18.9819, "calc_as_of": "2026-09-14" }
]
```

## Data coverage

| Source | Covers | Refresh |
|---|---|---|
| AMFI | Every AMFI-registered mutual fund scheme - metadata, NAV, returns | Nightly |
| NSE | Stock and index data for the liquid, AMFI-relevant universe (not every micro-cap name on the exchange); key benchmarks (Nifty 50, 100, 200, 500, Midcap 50/100, Next 50, Smallcap 100, and TRI variants) | Nightly |
| BSE | Index data (Sensex, 100, 200, 500, and TRI variants) | Nightly |

See [punji.ai/data-sources](https://punji.ai/data-sources) for the full methodology.

## Getting an API key

1. Sign in at [chat.punji.ai](https://chat.punji.ai).
2. Go to Settings → API Keys.
3. Click "Get free API access" - this auto-activates the free evaluation plan.
4. Create a key. The plaintext key is shown **once** - store it immediately (e.g. in a
   local `.env` file, never committed).

The free tier: 10 calls/minute, 7 calls/hour, 50 calls/day, across up to 20 distinct
funds or stocks per calendar month. See [punji.ai/developers](https://punji.ai/developers)
for paid tiers.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then fill in PUNJI_API_KEY
```

## Examples

| File | What it does |
|---|---|
| `examples/resolve_fund.py` | Resolve a fund name (e.g. "parag parikh flexi cap") to its stable `slug`. |
| `examples/fund_risk_and_returns.py` | Pull a fund's risk metrics and rolling-window returns by slug. |
| `examples/sip_returns.py` | SIP (systematic investment plan) returns for a fund over several lookback windows. |
| `examples/compare_funds.py` | Compare 2-3 funds in one call: returns, risk, portfolio overlap. |
| `examples/stock_lookup_and_deals.py` | Resolve a stock name to its slug, then pull recent bulk/block deals. |
| `examples/industry_flows.py` | Category-level mutual fund flow snapshot for a given month. |

Each script is self-contained - run directly, e.g.:

```bash
python examples/resolve_fund.py
```

All requests use the `requests` library and the `X-API-Key` header documented in the
[API reference](https://punji.ai/llms-api.md). Responses are JSON.

## Error codes

| Status | Meaning |
|---|---|
| `401` | Missing, invalid, or revoked API key. |
| `402` | Subscription not active. |
| `403` | `free_scheme_cap_reached` - Free plan's 20 distinct funds/stocks per month used up. |
| `404` | Resource not found. |
| `422` | Bad request - missing/invalid param. |
| `429` | Rate limit exceeded. |

## Not investment advice

This repo is a developer reference for the Punji Data API. Data returned by the API is
for informational and research purposes only and does not constitute investment advice.
