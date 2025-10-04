# Testing Guide

Comprehensive testing documentation for TSDC library.

## Test Summary

**Total Tests: 97**  
**Status: ✅ All Passing**  
**Coverage: Core, Loaders, Edge Cases, Integration, Real-World Scenarios**

## Test Structure

```
tests/
├── test_core.py           # 22 tests - Core functionality
├── test_loaders.py        # 21 tests - Data loaders
├── test_edge_cases.py     # 38 tests - Edge cases & boundary conditions
└── test_integration.py    # 16 tests - Integration & real-world scenarios
```

## Running Tests

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test File

```bash
pytest tests/test_core.py -v
```

### Run Specific Test

```bash
pytest tests/test_core.py::TestSequencer::test_create_sequences_shape -v
```

### Run with Coverage

```bash
pytest tests/ --cov=tsdc --cov-report=html
```

## Test Categories

### 1. Core Functionality Tests (test_core.py)

**TestSequencer (7 tests)**
- Sequence creation and validation
- Multivariate data handling
- Stride functionality
- Target column selection

**TestPreprocessor (5 tests)**
- MinMax, Standard, and Robust scaling
- Missing value handling
- Outlier detection and removal
- 3D data inverse transformation

**TestTimeSeriesDataset (6 tests)**
- Basic dataset creation
- Train/val/test splitting
- Multivariate with target column
- Configuration management

**TestValidators (2 tests)**
- Sequence parameter validation
- Split ratio validation

**TestSplitters (2 tests)**
- Time series splitting
- Walk-forward validation

### 2. Loader Tests (test_loaders.py)

**TestBaseLoader (5 tests)**
- CSV loading and saving
- Array conversion
- DataFrame with datetime index

**TestFinancialLoader (15 tests)**
- Yahoo Finance data validation
- Technical indicators (SMA, EMA, RSI, MACD)
- OHLCV extraction
- Data resampling
- CSV loading
- Preprocessing (removing extra columns)

**TestLoaderIntegration (1 test)**
- Loader + Dataset workflow

### 3. Edge Cases & Boundary Tests (test_edge_cases.py)

**TestEdgeCases (27 tests)**
- Very small datasets
- Single feature data
- Large stride values
- Lookback equals horizon
- Horizon larger than lookback
- All zeros data
- All same values
- Extreme values (1e10, 1e-10)
- Negative values
- NaN handling (at start, middle, end, consecutive)
- Outlier detection (single, multiple)
- Very small train splits
- No validation set
- DataFrame with datetime index
- Multivariate with all-NaN column
- Target column errors
- Empty dataframes
- Scaler options
- Get data before prepare
- Inverse transform without fit
- Transform without fit

**TestBoundaryConditions (5 tests)**
- Minimum valid dataset
- Lookback one
- Horizon one
- Stride equals lookback
- Exact split sizes

**TestDataTypes (6 tests)**
- NumPy array input
- Pandas Series input
- Pandas DataFrame input
- List input to sequencer
- Integer data
- Float data

### 4. Integration & Real-World Tests (test_integration.py)

**TestEndToEndWorkflow (10 tests)**
- Complete simple workflow
- Complete multivariate workflow
- Financial loader workflow
- Preprocessing then sequencing
- Walk-forward validation workflow
- Expanding window workflow
- Sliding window workflow
- Inverse transform workflow
- Create sliding window on new data
- Get all splits

**TestRealWorldScenarios (4 tests)**
- Bitcoin price prediction (60-day lookback, 1-day horizon)
- Weather forecasting (48-hour lookback, 24-hour horizon)
- Sales forecasting (30-day lookback, 7-day horizon)
- Energy consumption (24-hour lookback, 12-hour horizon)

**TestPerformance (2 tests)**
- Large dataset performance (10,000 samples)
- High-dimensional data (50 features)

## Test Coverage Details

### Core Components
✅ TimeSeriesDataset  
✅ Sequencer  
✅ Preprocessor  
✅ BaseLoader  
✅ FinancialLoader

### Features Tested
✅ Univariate time series  
✅ Multivariate time series  
✅ Target column selection  
✅ All scaling methods (MinMax, Standard, Robust, None)  
✅ Missing value handling (drop, forward fill, backward fill, interpolate, mean)  
✅ Outlier detection  
✅ Train/val/test splitting  
✅ Walk-forward validation  
✅ Expanding window split  
✅ Sliding window split  
✅ Inverse transformation  
✅ Technical indicators (SMA, EMA, RSI, MACD)  
✅ Data resampling  
✅ CSV/Parquet/JSON loading  
✅ Financial data loading

### Edge Cases Covered
✅ Empty datasets  
✅ Very small datasets  
✅ Very large datasets  
✅ Single feature  
✅ High-dimensional (50+ features)  
✅ All zeros  
✅ All same values  
✅ Extreme values  
✅ Negative values  
✅ NaN values (various positions)  
✅ Outliers  
✅ Different data types (int, float, array, Series, DataFrame, list)  
✅ Invalid parameters  
✅ Missing columns  
✅ Out of range indices

## Example Test Cases

### Simple Test Example

```python
def test_create_sequences_shape(self):
    data = np.arange(100).reshape(-1, 1)
    sequencer = Sequencer(lookback=10, horizon=5, stride=1)
    X, y = sequencer.create_sequences(data)
    
    expected_samples = (len(data) - 10 - 5 + 1) // 1
    
    self.assertEqual(X.shape, (expected_samples, 10, 1))
    self.assertEqual(y.shape, (expected_samples, 5, 1))
```

### Integration Test Example

```python
def test_complete_workflow_simple(self):
    data = np.cumsum(np.random.randn(1000)) + 100
    
    dataset = TimeSeriesDataset(
        data=data,
        lookback=60,
        horizon=1,
        scaler_type='minmax',
        train_split=0.7,
        val_split=0.15,
        test_split=0.15
    )
    
    dataset.prepare()
    
    X_train, y_train = dataset.get_train()
    X_val, y_val = dataset.get_val()
    X_test, y_test = dataset.get_test()
    
    self.assertEqual(X_train.shape[1], 60)
    self.assertTrue(np.all(X_train >= 0))
    self.assertTrue(np.all(X_train <= 1))
```

### Edge Case Test Example

```python
def test_nan_in_middle(self):
    data = pd.Series([1, 2, 3, np.nan, 5, 6, 7, 8, 9, 10])
    preprocessor = Preprocessor(handle_missing='interpolate')
    processed = preprocessor.fit_transform(data)
    
    self.assertFalse(np.any(np.isnan(processed)))
```

## Writing New Tests

### Test Structure

```python
import unittest
from tsdc import TimeSeriesDataset

class TestNewFeature(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_feature_basic(self):
        pass
    
    def test_feature_edge_case(self):
        pass
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

### Best Practices

1. **Test One Thing**: Each test should verify one specific behavior
2. **Use Descriptive Names**: `test_create_sequences_with_nan_values`
3. **Test Edge Cases**: Empty data, very large data, invalid inputs
4. **Test Expected Failures**: Use `assertRaises` for error cases
5. **Keep Tests Fast**: Use small datasets when possible
6. **Clean Up**: Remove temporary files in tearDown

### Naming Convention

```
test_<component>_<scenario>_<expected_outcome>
```

Examples:
- `test_sequencer_large_stride_correct_samples`
- `test_preprocessor_minmax_scaler_range_zero_to_one`
- `test_dataset_invalid_splits_raises_error`

## Continuous Integration

Tests automatically run on:
- Every commit
- Pull requests
- Before releases

## Test Metrics

| Metric | Value |
|--------|-------|
| Total Tests | 97 |
| Passing | 97 |
| Failing | 0 |
| Execution Time | ~1.0s |
| Components Tested | 5 |
| Edge Cases | 38 |
| Integration Tests | 16 |

## Known Issues

None currently.

## Future Test Plans

- [ ] Add property-based testing with Hypothesis
- [ ] Add performance benchmarks
- [ ] Add memory usage tests
- [ ] Add concurrency tests
- [ ] Add GPU acceleration tests (if implemented)
- [ ] Increase coverage to 100%

---

Last Updated: 2024-10-03
