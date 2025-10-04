# API Reference

Complete API documentation for TSDC library.

## Core Classes

### TimeSeriesDataset

Main class for creating time series datasets.

#### Constructor

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

**Parameters:**
- `data`: Input time series data (numpy array, pandas DataFrame/Series, or path to CSV/parquet/JSON file)
- `lookback`: Number of past timesteps to use as input
- `horizon`: Number of future timesteps to predict
- `stride`: Step size for sliding window (default: 1)
- `target_column`: Column name or index for target variable in multivariate case
- `scaler_type`: Type of scaling ('minmax', 'standard', 'robust', 'none')
- `train_split`: Proportion of data for training
- `val_split`: Proportion of data for validation
- `test_split`: Proportion of data for testing

#### Methods

##### prepare()

```python
prepare(preprocess: bool = True) -> TimeSeriesDataset
```

Prepares the dataset by creating sequences and splitting into train/val/test sets.

**Parameters:**
- `preprocess`: Whether to apply preprocessing (scaling, etc.)

**Returns:** Self for method chaining

**Example:**
```python
dataset = TimeSeriesDataset(data=prices, lookback=60)
dataset.prepare()
```

##### get_train()

```python
get_train() -> Tuple[np.ndarray, np.ndarray]
```

Returns training data.

**Returns:** Tuple of (X_train, y_train)

##### get_val()

```python
get_val() -> Tuple[np.ndarray, np.ndarray]
```

Returns validation data.

**Returns:** Tuple of (X_val, y_val)

##### get_test()

```python
get_test() -> Tuple[np.ndarray, np.ndarray]
```

Returns test data.

**Returns:** Tuple of (X_test, y_test)

##### get_all()

```python
get_all() -> Dict[str, Tuple[np.ndarray, np.ndarray]]
```

Returns all splits in a dictionary.

**Returns:** Dictionary with keys 'train', 'val', 'test'

##### get_info()

```python
get_info() -> Dict[str, Any]
```

Returns dataset information.

**Returns:** Dictionary with dataset configuration and shapes

##### inverse_transform_predictions()

```python
inverse_transform_predictions(predictions: np.ndarray) -> np.ndarray
```

Converts scaled predictions back to original scale.

**Parameters:**
- `predictions`: Scaled predictions

**Returns:** Predictions in original scale

##### create_sliding_window()

```python
create_sliding_window(
    data: Optional[Union[np.ndarray, pd.DataFrame, pd.Series]] = None
) -> Tuple[np.ndarray, np.ndarray]
```

Creates sequences from new data using existing configuration.

**Parameters:**
- `data`: New data (uses original data if None)

**Returns:** Tuple of (X, y)

---

### Sequencer

Low-level class for creating sequences from time series data.

#### Constructor

```python
Sequencer(lookback: int, horizon: int = 1, stride: int = 1)
```

**Parameters:**
- `lookback`: Number of past timesteps
- `horizon`: Number of future timesteps to predict
- `stride`: Step size for sliding window

#### Methods

##### create_sequences()

```python
create_sequences(
    data: Union[np.ndarray, pd.DataFrame, pd.Series, list],
    target_column: Optional[Union[int, str]] = None
) -> Tuple[np.ndarray, np.ndarray]
```

Creates sequences from data.

**Parameters:**
- `data`: Input time series data
- `target_column`: Column to use as target (if multivariate)

**Returns:** Tuple of (X, y) where X has shape (n_samples, lookback, n_features)

**Example:**
```python
sequencer = Sequencer(lookback=10, horizon=5)
X, y = sequencer.create_sequences(data)
```

##### create_sequences_with_indices()

```python
create_sequences_with_indices(
    data: Union[np.ndarray, pd.DataFrame, pd.Series, list],
    target_column: Optional[Union[int, str]] = None
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]
```

Creates sequences along with their indices.

**Returns:** Tuple of (X, y, indices)

##### inverse_sequences()

```python
inverse_sequences(
    sequences: np.ndarray,
    original_shape: Optional[Tuple[int, ...]] = None
) -> np.ndarray
```

Reconstructs original data from sequences (approximate).

---

### Preprocessor

Class for data preprocessing and scaling.

#### Constructor

```python
Preprocessor(
    scaler_type: Literal["standard", "minmax", "robust", "none"] = "minmax",
    feature_range: Tuple[float, float] = (0, 1),
    handle_missing: Literal["drop", "forward_fill", "backward_fill", "interpolate", "mean"] = "forward_fill",
    remove_outliers: bool = False,
    outlier_threshold: float = 3.0
)
```

**Parameters:**
- `scaler_type`: Type of scaling
- `feature_range`: Range for MinMax scaling
- `handle_missing`: Method for handling missing values
- `remove_outliers`: Whether to remove outliers
- `outlier_threshold`: Z-score threshold for outlier detection

#### Methods

##### fit()

```python
fit(data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> Preprocessor
```

Fits the preprocessor to data.

##### transform()

```python
transform(data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> np.ndarray
```

Transforms data using fitted parameters.

##### fit_transform()

```python
fit_transform(data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> np.ndarray
```

Fits and transforms data in one step.

##### inverse_transform()

```python
inverse_transform(data: Union[np.ndarray, pd.DataFrame]) -> Union[np.ndarray, pd.DataFrame]
```

Converts scaled data back to original scale.

##### get_params()

```python
get_params() -> Dict[str, Any]
```

Returns preprocessor parameters.

**Example:**
```python
preprocessor = Preprocessor(
    scaler_type='robust',
    handle_missing='interpolate',
    remove_outliers=True
)
scaled = preprocessor.fit_transform(data)
original = preprocessor.inverse_transform(scaled)
```

---

## Loaders

### BaseLoader

Abstract base class for data loaders.

#### Methods

##### load()

```python
@abstractmethod
load(*args, **kwargs) -> pd.DataFrame
```

Loads data from source. Must be implemented by subclasses.

##### validate()

```python
@abstractmethod
validate(data: pd.DataFrame) -> bool
```

Validates loaded data. Must be implemented by subclasses.

##### save()

```python
save(path: str, format: str = "csv") -> None
```

Saves data to file.

**Parameters:**
- `path`: Output file path
- `format`: File format ('csv', 'parquet', 'json')

---

### FinancialLoader

Loader for financial data from Yahoo Finance.

#### Methods

##### load()

```python
load(
    symbol: str = None,
    start_date: Union[str, datetime] = None,
    end_date: Union[str, datetime] = None,
    source: str = "yahoo"
) -> pd.DataFrame
```

Loads financial data.

**Parameters:**
- `symbol`: Ticker symbol (e.g., 'BTC-USD', 'AAPL')
- `start_date`: Start date
- `end_date`: End date
- `source`: Data source ('yahoo' or 'csv')

**Returns:** DataFrame with OHLCV data

##### add_technical_indicators()

```python
add_technical_indicators(
    sma_periods: List[int] = [20, 50],
    ema_periods: List[int] = [12, 26],
    rsi_period: int = 14,
    macd: bool = True
) -> pd.DataFrame
```

Adds technical indicators to data.

**Parameters:**
- `sma_periods`: List of periods for Simple Moving Averages
- `ema_periods`: List of periods for Exponential Moving Averages
- `rsi_period`: Period for RSI calculation
- `macd`: Whether to add MACD indicators

**Returns:** DataFrame with added indicators

##### get_ohlcv()

```python
get_ohlcv() -> pd.DataFrame
```

Returns only OHLCV columns.

##### resample()

```python
resample(freq: str) -> pd.DataFrame
```

Resamples data to different frequency.

**Parameters:**
- `freq`: Frequency string (e.g., '1h', '1D', '1W')

**Example:**
```python
loader = FinancialLoader()
data = loader.load(symbol="BTC-USD", start_date="2023-01-01")
data = loader.add_technical_indicators()
daily = loader.resample('1D')
```

---

## Utility Functions

### Validators

Located in `tsdc.utils.validators`

#### validate_sequence_params()

```python
validate_sequence_params(
    data_length: int,
    lookback: int,
    horizon: int,
    stride: int = 1
) -> bool
```

Validates sequence parameters.

#### validate_data_shape()

```python
validate_data_shape(
    data: Union[np.ndarray, pd.DataFrame, pd.Series],
    expected_dims: int = None
) -> Tuple[int, int]
```

Validates and returns data shape.

#### validate_splits()

```python
validate_splits(
    train_split: float,
    val_split: float,
    test_split: float
) -> bool
```

Validates split ratios.

---

### Splitters

Located in `tsdc.utils.splitters`

#### time_series_split()

```python
time_series_split(
    X: np.ndarray,
    y: np.ndarray,
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15
) -> Tuple[Tuple[np.ndarray, np.ndarray], ...]
```

Splits data temporally into train/val/test sets.

#### walk_forward_validation()

```python
walk_forward_validation(
    X: np.ndarray,
    y: np.ndarray,
    n_splits: int = 5,
    test_size: int = None,
    train_size: int = None,
    gap: int = 0
) -> Generator
```

Creates walk-forward validation splits.

**Parameters:**
- `n_splits`: Number of splits
- `test_size`: Size of test set
- `train_size`: Size of training set
- `gap`: Gap between train and test

**Yields:** (X_train, y_train, X_test, y_test) tuples

**Example:**
```python
for X_train, y_train, X_test, y_test in walk_forward_validation(X, y, n_splits=5):
    model.fit(X_train, y_train)
    score = model.evaluate(X_test, y_test)
```

#### expanding_window_split()

```python
expanding_window_split(
    X: np.ndarray,
    y: np.ndarray,
    initial_train_size: int,
    test_size: int,
    step: int = 1
) -> Generator
```

Creates expanding window splits.

#### sliding_window_split()

```python
sliding_window_split(
    X: np.ndarray,
    y: np.ndarray,
    window_size: int,
    test_size: int,
    step: int = 1
) -> Generator
```

Creates sliding window splits.

---

## Data Shapes

Understanding output shapes is crucial for using TSDC effectively.

### Univariate Time Series

```python
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
dataset.prepare()
X, y = dataset.get_train()
```

- `X.shape`: `(n_samples, 3, 1)` - (samples, lookback, features)
- `y.shape`: `(n_samples,)` - one value per sample

### Multivariate Time Series (All Features as Output)

```python
data = pd.DataFrame({
    'feature1': [...],
    'feature2': [...],
    'feature3': [...]
})
dataset = TimeSeriesDataset(data, lookback=5, horizon=2)
dataset.prepare()
X, y = dataset.get_train()
```

- `X.shape`: `(n_samples, 5, 3)` - (samples, lookback, features)
- `y.shape`: `(n_samples, 2, 3)` - predict 2 steps ahead for all features

### Multivariate Input, Single Target

```python
data = pd.DataFrame({
    'temperature': [...],
    'humidity': [...],
    'pressure': [...]
})
dataset = TimeSeriesDataset(
    data, 
    lookback=10, 
    horizon=3, 
    target_column='temperature'
)
dataset.prepare()
X, y = dataset.get_train()
```

- `X.shape`: `(n_samples, 10, 3)` - all features as input
- `y.shape`: `(n_samples, 3)` - only temperature as output

---

## Common Patterns

### Pattern 1: Basic LSTM Setup

```python
from tsdc import TimeSeriesDataset
dataset = TimeSeriesDataset(data, lookback=60, horizon=1)
dataset.prepare()
X_train, y_train = dataset.get_train()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(50, input_shape=(60, X_train.shape[2])),
    Dense(1)
])
```

### Pattern 2: Multi-step Forecasting

```python
dataset = TimeSeriesDataset(data, lookback=24, horizon=12)
dataset.prepare()
X_train, y_train = dataset.get_train()

model = Sequential([
    LSTM(50, input_shape=(24, X_train.shape[2])),
    Dense(12)
])
```

### Pattern 3: Custom Preprocessing

```python
from tsdc import Preprocessor, Sequencer

preprocessor = Preprocessor(scaler_type='robust')
scaled_data = preprocessor.fit_transform(data)

sequencer = Sequencer(lookback=30, horizon=7)
X, y = sequencer.create_sequences(scaled_data)
```

---

For more examples, see the `examples/` directory in the repository.
