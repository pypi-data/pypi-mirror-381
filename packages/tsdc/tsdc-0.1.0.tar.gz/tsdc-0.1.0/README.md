# TSDC - Time Series Dataset Creator

[![PyPI version](https://badge.fury.io/py/tsdc.svg)](https://badge.fury.io/py/tsdc)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/DeepPythonist/tsdc/actions/workflows/tests.yml/badge.svg)](https://github.com/DeepPythonist/tsdc/actions/workflows/tests.yml)

A powerful and intuitive Python library for creating time series datasets ready for machine learning models like LSTM, GRU, and Transformers. No more manual data preprocessing - just load your data and start training!

## Why TSDC?

When working with time series models (especially LSTM), you always need to:
- Convert raw data into sliding window sequences
- Split data temporally (not randomly!)
- Normalize/scale features properly
- Handle multivariate inputs with single target outputs
- Create proper shapes for neural networks

**TSDC automates all of this in just a few lines of code.**

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Advanced Usage](#advanced-usage)
- [Development](#development)
- [Contributing](#contributing)

## Installation

### From source (recommended for development)

```bash
git clone https://github.com/DeepPythonist/tsdc.git
cd tsdc
pip install -e .
```

### For additional features

```bash
pip install -e ".[examples]"
```

This includes `yfinance` for financial data loading and `matplotlib` for visualization.

## Quick Start

### Basic Example: Single Variable

```python
import numpy as np
from tsdc import TimeSeriesDataset

bitcoin_prices = np.random.randn(1000) * 1000 + 40000

dataset = TimeSeriesDataset(
    data=bitcoin_prices,
    lookback=60,
    horizon=1
)
dataset.prepare()

X_train, y_train = dataset.get_train()
X_val, y_val = dataset.get_val()
X_test, y_test = dataset.get_test()

print(f"X_train shape: {X_train.shape}")  # (samples, 60, 1)
print(f"y_train shape: {y_train.shape}")  # (samples, 1)
```

### Multivariate Example with Target Column

```python
import pandas as pd
from tsdc import TimeSeriesDataset

data = pd.DataFrame({
    'temperature': [...],
    'humidity': [...],
    'pressure': [...]
})

dataset = TimeSeriesDataset(
    data=data,
    lookback=24,
    horizon=6,
    target_column='temperature',
    scaler_type='minmax'
)
dataset.prepare()

X_train, y_train = dataset.get_train()
```

## Core Concepts

### 1. Lookback and Horizon

- **lookback**: Number of past timesteps to use as input
- **horizon**: Number of future timesteps to predict

```python
lookback=60, horizon=1   # Use 60 past points to predict next 1 point
lookback=24, horizon=12  # Use 24 hours to predict next 12 hours
```

### 2. Stride

Control how windows overlap:

```python
stride=1   # Maximum overlap, windows shift by 1 timestep
stride=5   # Less overlap, windows shift by 5 timesteps
```

### 3. Train/Val/Test Splits

**IMPORTANT:** TSDC uses **temporal (sequential) splitting**, NOT random splitting!

Time series splitting preserves temporal order to prevent data leakage:

```python
TimeSeriesDataset(
    data=data,
    train_split=0.7,   # First 70% for training (oldest data)
    val_split=0.15,    # Next 15% for validation (middle data)
    test_split=0.15    # Last 15% for testing (newest data)
)

# Train ← Val ← Test (sequential, no shuffling)
# This prevents training on future data and testing on past data!
```

### 4. Scaling Options

```python
scaler_type='minmax'    # Scale to [0, 1]
scaler_type='standard'  # Zero mean, unit variance
scaler_type='robust'    # Robust to outliers
scaler_type='none'      # No scaling
```

## API Reference

### TimeSeriesDataset

Main class for dataset creation.

```python
TimeSeriesDataset(
    data: Union[np.ndarray, pd.DataFrame, pd.Series, str],
    lookback: int = 10,
    horizon: int = 1,
    stride: int = 1,
    target_column: Optional[Union[int, str]] = None,
    scaler_type: str = "minmax",
    train_split: float = 0.7,
    val_split: float = 0.15,
    test_split: float = 0.15
)
```

**Methods:**
- `prepare(preprocess=True)`: Prepare the dataset
- `get_train()`: Returns (X_train, y_train)
- `get_val()`: Returns (X_val, y_val)
- `get_test()`: Returns (X_test, y_test)
- `get_all()`: Returns dictionary with all splits
- `get_info()`: Get dataset information
- `inverse_transform_predictions(predictions)`: Convert scaled predictions back

### Sequencer

Low-level API for creating sequences.

```python
from tsdc import Sequencer

sequencer = Sequencer(lookback=10, horizon=5, stride=1)
X, y = sequencer.create_sequences(data)
```

### Preprocessor

Standalone preprocessing utilities.

```python
from tsdc import Preprocessor

preprocessor = Preprocessor(
    scaler_type='minmax',
    handle_missing='forward_fill',
    remove_outliers=True,
    outlier_threshold=3.0
)
scaled_data = preprocessor.fit_transform(data)
original_data = preprocessor.inverse_transform(scaled_data)
```

### FinancialLoader

Load financial data from Yahoo Finance.

```python
from tsdc.loaders import FinancialLoader

loader = FinancialLoader()
btc_data = loader.load(
    symbol="BTC-USD",
    start_date="2023-01-01",
    end_date="2024-01-01",
    source="yahoo"
)

btc_data = loader.add_technical_indicators(
    sma_periods=[20, 50],
    ema_periods=[12, 26],
    rsi_period=14,
    macd=True
)
```

## Examples

### Example 1: Bitcoin Price Prediction with LSTM

```python
import numpy as np
from tsdc import TimeSeriesDataset
from tsdc.loaders import FinancialLoader

loader = FinancialLoader()
btc_data = loader.load(symbol="BTC-USD", start_date="2022-01-01")

dataset = TimeSeriesDataset(
    data=btc_data[['Close', 'Volume']],
    lookback=60,
    horizon=1,
    target_column='Close',
    scaler_type='minmax'
)
dataset.prepare()

X_train, y_train = dataset.get_train()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(100, return_sequences=True, input_shape=(60, 2)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32)
```

### Example 2: Walk-Forward Validation

```python
from tsdc import TimeSeriesDataset, Sequencer
from tsdc.utils.splitters import walk_forward_validation

data = np.random.randn(1000, 3)
sequencer = Sequencer(lookback=20, horizon=1)
X, y = sequencer.create_sequences(data)

for X_train, y_train, X_test, y_test in walk_forward_validation(X, y, n_splits=5):
    model.fit(X_train, y_train)
    score = model.evaluate(X_test, y_test)
    print(f"Test Score: {score}")
```

### Example 3: Loading from CSV

```python
from tsdc import TimeSeriesDataset

dataset = TimeSeriesDataset(
    data="path/to/data.csv",
    lookback=30,
    horizon=7,
    target_column="sales"
)
dataset.prepare()
```

### Example 4: Custom Preprocessing

```python
from tsdc import Preprocessor

preprocessor = Preprocessor(
    scaler_type='robust',
    handle_missing='interpolate',
    remove_outliers=True,
    outlier_threshold=2.5
)

cleaned_data = preprocessor.fit_transform(raw_data)
```

## Advanced Usage

### Multi-step Forecasting

Predict multiple timesteps ahead:

```python
dataset = TimeSeriesDataset(
    data=data,
    lookback=48,
    horizon=24,
    target_column='price'
)
dataset.prepare()
X_train, y_train = dataset.get_train()
```

### Custom Splits with Indices

```python
from tsdc.utils.splitters import expanding_window_split

for X_train, y_train, X_test, y_test in expanding_window_split(
    X, y, 
    initial_train_size=100,
    test_size=20,
    step=10
):
    pass
```

### Inverse Transform Predictions

```python
predictions = model.predict(X_test)
original_scale = dataset.inverse_transform_predictions(predictions)
```

## Project Structure

```
tsdc/
├── tsdc/
│   ├── __init__.py
│   ├── core/
│   │   ├── dataset.py       # Main TimeSeriesDataset class
│   │   ├── sequencer.py     # Sliding window operations
│   │   └── preprocessor.py  # Data preprocessing
│   ├── loaders/
│   │   ├── base.py         # Base loader class
│   │   └── financial.py    # Financial data loaders
│   └── utils/
│       ├── validators.py   # Input validation
│       └── splitters.py    # Time series splitting
├── examples/
│   ├── basic_usage.py      # Basic examples
│   ├── lstm_bitcoin.py     # Bitcoin prediction
│   └── quick_start.py      # Quick start guide
├── tests/
│   └── test_core.py        # Unit tests
├── setup.py
├── requirements.txt
└── README.md
```

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Running Examples

```bash
python examples/basic_usage.py
python examples/lstm_bitcoin.py
```

### Code Style

This project follows PEP 8 guidelines. Format your code with:

```bash
black tsdc/
flake8 tsdc/
```

## Features

- ✅ Easy sequence creation for LSTM/GRU/Transformer models
- ✅ Built-in preprocessing and normalization
- ✅ Proper train/validation/test splitting for time series
- ✅ Support for univariate and multivariate data
- ✅ Target column selection for multivariate inputs
- ✅ Financial data loaders with technical indicators
- ✅ Walk-forward and expanding window validation
- ✅ Flexible sliding window operations
- ✅ Missing value handling
- ✅ Outlier detection and removal
- ✅ Inverse transform for predictions
- ✅ Multiple scaling methods

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use TSDC in your research, please cite:

```bibtex
@software{tsdc2024,
  title={TSDC: Time Series Dataset Creator},
  author={DeepPythonist},
  year={2024},
  url={https://github.com/DeepPythonist/tsdc}
}
```

## Support

For issues and questions:
- Open an issue on [GitHub Issues](https://github.com/DeepPythonist/tsdc/issues)
- Check the `examples/` directory for usage examples

## Roadmap

- [ ] Add more data loaders (crypto, weather, etc.)
- [ ] Add data augmentation techniques
- [ ] Support for irregular time series
- [ ] Integration with PyTorch DataLoader
- [ ] Built-in visualization tools
- [ ] Automated hyperparameter tuning for lookback/horizon

---

Made with ❤️ for the ML community
