[![pipeline status](https://gitlab.com/elmotec/finquotes/badges/main/pipeline.svg)](https://gitlab.com/elmotec/finquotes/-/commits/main)
[![coverage report](https://gitlab.com/elmotec/finquotes/badges/main/coverage.svg)](https://gitlab.com/elmotec/finquotes/-/commits/main)

# FinQuotes

FinQuotes is a small Python library to be used as a facade to fetch financial data from public sources through a single, consistent interface.  It adapts various interface to a consistent one described below allowing one to quickly switch between service.

It supports close snapshots, historical OHLCV, distributions (dividends), splits, and security metadata across multiple providers (Yahoo Finance, yfinance, yahooquery, Stooq, Morningstar, Quandl).

- Python: 3.11–3.13
- License: GPL-3.0

## Features

- Unified API and CLI for multiple data sources
- Normalized data models: Price, Distribution, Split, Security
- Deterministic CSV output for easy piping and testing
- Robust network options: retry, timeout, max retries
- Pluggable sources via lightweight “feed” builders

## Install

```powershell
python -m pip install --upgrade pip
python -m pip install finquotes
```

Optional extras:

- Types only: `python -m pip install 'finquotes[types]'`
- Dev/test: `python -m pip install -e '.[develop,test,types]'`

## Quick start (Python)

Use typed builder helpers for clarity, or `build_feed` with a `FeedType`.

```python
import finquotes as fq

# Historical OHLCV (yfinance)
hfeed = fq.build_historical_feed("finquotes.yfinance", auto_adjust=True)
for p in hfeed.fetch_hist_prices("MSFT", begin_date=fq.today(), end_date=fq.today()):
	assert p.open is not None and p.high is not None and p.low is not None

# Distributions & splits (yahooquery)
qhist = fq.build_historical_feed("finquotes.yahooquery")
for d in qhist.fetch_hist_dists("BIL", begin_date=fq.today(), end_date=fq.today()):
	print(d)
for s in qhist.fetch_hist_splits("AAPL", begin_date=fq.today(), end_date=fq.today()):
	print(s)
```

Network parameters (`timeout`, `max_retries`, `retry_delay`, and provider-specific args) can be passed to feed builders as keyword arguments.

## API keys

Some providers require an API key (e.g., Quandl). FinQuotes looks for keys in:

1) Environment variable: `FINQUOTES_<PROVIDER>_API_KEY` (e.g. `FINQUOTES_QUANDL_API_KEY`)
2) File: `~/.finquotes/api_keys.txt` with lines like:

```text
finquotes.quandl=<YOUR_KEY>
```

On Windows the file path expands to `%USERPROFILE%\.finquotes\api_keys.txt`.

You can also pass `--api-key` on the CLI or `api_key="..."` to feed builders where applicable.

## Data model at a glance

- `Price(symbol, date|datetime, close[, open, high, low, volume, source])`
- `Distribution(symbol, ex_date, amount[, pay_date])`
- `Split(symbol, ex_date, new_quantity, old_quantity)` and `Split.from_ratio(...)`
- `Security(symbol, name[, type, currency, exchange, country, sector, industry, source, source_id])`

Instances print to CSV for easy piping; attributes are typed (Decimal for prices) and validated by a helper (`PriceValidator`).

## Tips & caveats

- Some providers adjust historical series (e.g., Stooq distributions are adjusted); check source notes before using for cash-flow analysis.
- Yahoo-derived OHLC fields may be dividend-adjusted; see in-code comments where noted.
- Timezone defaults to America/New_York for timestamp parsing.

## Development

Set up a local environment once:

```powershell
python -m venv venv
. .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e '.[develop,test,types]'
```

Run tests:

```powershell
pytest -q
```

Pre-commit hooks:

```powershell
pre-commit install
pre-commit run --all-files
```

### Publishing (maintainers)

```powershell
cz bump -ch    # bump version, update files, create tag
git push --tags
# build & upload using your preferred toolchain
python -m build          # or: python -m setup sdist
python -m twine upload dist/*       # or target a custom repository URL
```
