# Quick Start Guide

Get started with TSDC in 5 minutes!

## Installation

```bash
pip install -e .
```

## Your First Dataset

### Step 1: Import and Create Data

```python
import numpy as np
from tsdc import TimeSeriesDataset

prices = np.random.randn(1000) * 100 + 5000
```

### Step 2: Create Dataset

```python
dataset = TimeSeriesDataset(
    data=prices,
    lookback=60,
    horizon=1
)
```

### Step 3: Prepare

```python
dataset.prepare()
```

### Step 4: Get Data

```python
X_train, y_train = dataset.get_train()
X_val, y_val = dataset.get_val()
X_test, y_test = dataset.get_test()
```

### Step 5: Train Your Model

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(50, input_shape=(60, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)
```

That's it! You're ready to go.

---

## Common Use Cases

### Use Case 1: Stock Price Prediction

```python
from tsdc import TimeSeriesDataset
from tsdc.loaders import FinancialLoader

loader = FinancialLoader()
stock_data = loader.load(symbol="AAPL", start_date="2023-01-01")

dataset = TimeSeriesDataset(
    data=stock_data['Close'],
    lookback=60,
    horizon=1,
    scaler_type='minmax'
)
dataset.prepare()
```

### Use Case 2: Weather Prediction

```python
import pandas as pd
from tsdc import TimeSeriesDataset

weather_data = pd.DataFrame({
    'temperature': [...],
    'humidity': [...],
    'pressure': [...]
})

dataset = TimeSeriesDataset(
    data=weather_data,
    lookback=24,
    horizon=6,
    target_column='temperature'
)
dataset.prepare()
```

### Use Case 3: Sales Forecasting

```python
dataset = TimeSeriesDataset(
    data="sales_data.csv",
    lookback=30,
    horizon=7,
    target_column='sales'
)
dataset.prepare()
```

---

## Configuration Options

### Lookback and Horizon

```python
lookback=60   # Use 60 past points
horizon=1     # Predict next 1 point
```

### Scaling

```python
scaler_type='minmax'     # Scale to [0, 1]
scaler_type='standard'   # Zero mean, unit variance
scaler_type='robust'     # Robust to outliers
scaler_type='none'       # No scaling
```

### Train/Val/Test Split

```python
train_split=0.7   # 70% for training
val_split=0.15    # 15% for validation
test_split=0.15   # 15% for testing
```

---

## Tips and Tricks

### Tip 1: Choose the Right Lookback

```python
lookback=24   # For hourly data predicting daily patterns
lookback=60   # For daily data predicting monthly patterns
lookback=252  # For daily data predicting yearly patterns
```

### Tip 2: Multi-step Forecasting

```python
horizon=7   # Predict next 7 days
horizon=24  # Predict next 24 hours
```

### Tip 3: Handle Missing Data

```python
from tsdc import Preprocessor

preprocessor = Preprocessor(
    handle_missing='interpolate',
    remove_outliers=True
)
clean_data = preprocessor.fit_transform(raw_data)
```

### Tip 4: Walk-Forward Validation

```python
from tsdc.utils.splitters import walk_forward_validation

for X_train, y_train, X_test, y_test in walk_forward_validation(X, y):
    model.fit(X_train, y_train)
    score = model.evaluate(X_test, y_test)
```

---

## Common Mistakes

### Mistake 1: Random Splitting

Don't use random train/test split for time series!

```python
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(X, y)  # ❌ WRONG
```

TSDC automatically does temporal splitting:
```python
dataset.prepare()  # ✅ CORRECT
```

### Mistake 2: Not Scaling Data

Always scale your data for neural networks:

```python
dataset = TimeSeriesDataset(
    data=prices,
    scaler_type='minmax'  # ✅ Good
)
```

### Mistake 3: Wrong Shape

Make sure you understand the output shapes:

```python
X_train.shape  # (samples, lookback, features)
y_train.shape  # (samples,) or (samples, horizon)
```

---

## Next Steps

1. Check out [API Reference](API_REFERENCE.md) for detailed documentation
2. See `examples/` directory for more examples
3. Read [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

Happy forecasting! 🚀
