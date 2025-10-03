# OilPriceAPI Python SDK

[![PyPI version](https://badge.fury.io/py/oilpriceapi.svg)](https://badge.fury.io/py/oilpriceapi)
[![Python](https://img.shields.io/pypi/pyversions/oilpriceapi.svg)](https://pypi.org/project/oilpriceapi/)
[![Tests](https://github.com/oilpriceapi/python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/oilpriceapi/python-sdk/actions/workflows/test.yml)
[![Coverage](https://codecov.io/gh/oilpriceapi/python-sdk/branch/main/graph/badge.svg)](https://codecov.io/gh/oilpriceapi/python-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The official Python SDK for [OilPriceAPI](https://oilpriceapi.com) - Real-time and historical oil prices for Brent Crude, WTI, Natural Gas, and more.

## 🚀 Quick Start

### Installation

```bash
pip install oilpriceapi
```

### Basic Usage

```python
from oilpriceapi import OilPriceAPI

# Initialize client (uses OILPRICEAPI_KEY env var by default)
client = OilPriceAPI()

# Get latest Brent Crude price
brent = client.prices.get("BRENT_CRUDE_USD")
print(f"Brent Crude: ${brent.value:.2f}")
# Output: Brent Crude: $71.45

# Get multiple prices
prices = client.prices.get_multiple(["BRENT_CRUDE_USD", "WTI_USD", "NATURAL_GAS_USD"])
for price in prices:
    print(f"{price.commodity}: ${price.value:.2f}")
```

### Historical Data with Pandas

```python
# Get historical data as DataFrame
df = client.prices.to_dataframe(
    commodity="BRENT_CRUDE_USD",
    start="2024-01-01",
    end="2024-12-31",
    interval="daily"
)

# Add technical indicators
df = client.analysis.with_indicators(
    df,
    indicators=["sma_20", "sma_50", "rsi", "bollinger_bands"]
)

# Calculate spread between Brent and WTI
spread = client.analysis.spread("BRENT_CRUDE_USD", "WTI_USD", start="2024-01-01")
```

## 📊 Features

- ✅ **Simple API** - Intuitive methods for all endpoints
- ✅ **Type Safe** - Full type hints for IDE autocomplete
- ✅ **Pandas Integration** - First-class DataFrame support
- ✅ **Async Support** - High-performance async client
- ✅ **Smart Caching** - Reduce API calls automatically
- ✅ **Rate Limit Handling** - Automatic retries with backoff
- ✅ **Technical Indicators** - Built-in SMA, RSI, MACD, etc.
- ✅ **CLI Tool** - Command-line interface included

## 📚 Documentation

### Authentication

```python
# Method 1: Environment variable (recommended)
export OILPRICEAPI_KEY="your_api_key"
client = OilPriceAPI()

# Method 2: Direct initialization
client = OilPriceAPI(api_key="your_api_key")

# Method 3: With configuration
client = OilPriceAPI(
    api_key="your_api_key",
    timeout=30,
    max_retries=3,
    cache="memory",
    cache_ttl=300
)
```

### Available Commodities

- `BRENT_CRUDE_USD` - Brent Crude Oil
- `WTI_USD` - West Texas Intermediate
- `NATURAL_GAS_USD` - Natural Gas
- `DIESEL_USD` - Diesel
- `GASOLINE_USD` - Gasoline
- `HEATING_OIL_USD` - Heating Oil
- [View all commodities](https://docs.oilpriceapi.com/commodities)

### Error Handling

```python
from oilpriceapi.exceptions import OilPriceAPIError, RateLimitError, DataNotFoundError

try:
    price = client.prices.get("INVALID_CODE")
except DataNotFoundError as e:
    print(f"Commodity not found: {e}")
except RateLimitError as e:
    print(f"Rate limited. Resets in {e.seconds_until_reset}s")
except OilPriceAPIError as e:
    print(f"API error: {e}")
```

## ⚡ Async Support

```python
import asyncio
from oilpriceapi import AsyncOilPriceAPI

async def get_prices():
    async with AsyncOilPriceAPI() as client:
        prices = await asyncio.gather(
            client.prices.get("BRENT_CRUDE_USD"),
            client.prices.get("WTI_USD"),
            client.prices.get("NATURAL_GAS_USD")
        )
        return prices

# Run async function
prices = asyncio.run(get_prices())
```

## 🛠️ CLI Tool

```bash
# Get current price
oilprice get BRENT_CRUDE_USD

# Export historical data
oilprice export WTI_USD --start 2024-01-01 --format csv -o wti_2024.csv

# Watch prices in real-time
oilprice watch BRENT_CRUDE_USD --interval 60
```

## 🧪 Testing

The SDK includes utilities for testing your applications:

```python
from oilpriceapi.testing import MockClient

def test_my_strategy():
    client = MockClient()
    client.set_price("BRENT_CRUDE_USD", 75.50)

    result = my_trading_strategy(client)
    assert result.action == "BUY"
```

## 📈 Examples

Check out the [examples/](examples/) directory for:
- [Quickstart Notebook](examples/quickstart.ipynb)
- [Data Analysis](examples/data_analysis.ipynb)
- [Trading Signals](examples/trading_signals.ipynb)
- [Async Operations](examples/async_example.py)

## 🔧 Development

```bash
# Clone repository
git clone https://github.com/oilpriceapi/python-sdk
cd python-sdk

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Type checking
mypy oilpriceapi
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 💬 Support

- 📧 Email: support@oilpriceapi.com
- 🐛 Issues: [GitHub Issues](https://github.com/oilpriceapi/python-sdk/issues)
- 📖 Docs: [Documentation](https://docs.oilpriceapi.com/sdk/python)

## 🔗 Links

- [OilPriceAPI Website](https://oilpriceapi.com)
- [API Documentation](https://docs.oilpriceapi.com)
- [Pricing](https://oilpriceapi.com/pricing)
- [Status Page](https://status.oilpriceapi.com)

---

Made with ❤️ by the OilPriceAPI Team