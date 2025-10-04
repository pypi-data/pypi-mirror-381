import numpy as np
import pandas as pd
from tsdc import TimeSeriesDataset, Sequencer, Preprocessor


def example_simple_array():
    print("=" * 50)
    print("Example 1: Simple Array")
    print("=" * 50)
    
    data = np.sin(np.linspace(0, 20, 1000)) + np.random.normal(0, 0.1, 1000)
    
    dataset = TimeSeriesDataset(
        data=data,
        lookback=50,
        horizon=10,
        stride=1,
        scaler_type="minmax"
    )
    
    dataset.prepare()
    
    X_train, y_train = dataset.get_train()
    X_val, y_val = dataset.get_val()
    X_test, y_test = dataset.get_test()
    
    print(f"Training set: X={X_train.shape}, y={y_train.shape}")
    print(f"Validation set: X={X_val.shape}, y={y_val.shape}")
    print(f"Test set: X={X_test.shape}, y={y_test.shape}")
    print()


def example_multivariate():
    print("=" * 50)
    print("Example 2: Multivariate Time Series")
    print("=" * 50)
    
    dates = pd.date_range("2020-01-01", periods=1000, freq="h")
    data = pd.DataFrame({
        "temperature": np.sin(np.linspace(0, 20, 1000)) * 10 + 20 + np.random.normal(0, 1, 1000),
        "humidity": np.cos(np.linspace(0, 20, 1000)) * 20 + 60 + np.random.normal(0, 2, 1000),
        "pressure": np.sin(np.linspace(0, 10, 1000)) * 5 + 1013 + np.random.normal(0, 1, 1000)
    }, index=dates)
    
    dataset = TimeSeriesDataset(
        data=data,
        lookback=24,
        horizon=6,
        target_column="temperature",
        scaler_type="standard"
    )
    
    dataset.prepare()
    
    X_train, y_train = dataset.get_train()
    
    print(f"Input shape: {X_train.shape}")
    print(f"Output shape: {y_train.shape}")
    print(f"Features: {data.columns.tolist()}")
    print(f"Target: temperature")
    print()


def example_sequencer():
    print("=" * 50)
    print("Example 3: Direct Sequencer Usage")
    print("=" * 50)
    
    data = np.arange(100).reshape(-1, 1)
    
    sequencer = Sequencer(lookback=5, horizon=3, stride=2)
    
    X, y = sequencer.create_sequences(data)
    
    print(f"Original data shape: {data.shape}")
    print(f"Sequences shape: X={X.shape}, y={y.shape}")
    print(f"First sequence (X): {X[0].flatten()}")
    print(f"First target (y): {y[0].flatten()}")
    print()


def example_preprocessor():
    print("=" * 50)
    print("Example 4: Preprocessing Pipeline")
    print("=" * 50)
    
    data = pd.DataFrame({
        "value": [1, 2, np.nan, 4, 5, 100, 7, 8, 9, 10]
    })
    
    preprocessor = Preprocessor(
        scaler_type="robust",
        handle_missing="interpolate",
        remove_outliers=True,
        outlier_threshold=2.0
    )
    
    print("Original data:")
    print(data.values.flatten())
    
    processed = preprocessor.fit_transform(data)
    
    print("\nProcessed data:")
    print(processed.flatten())
    
    restored = preprocessor.inverse_transform(processed)
    print("\nInverse transformed:")
    print(restored.flatten())
    print()


def example_custom_split():
    print("=" * 50)
    print("Example 5: Custom Train/Val/Test Split")
    print("=" * 50)
    
    data = np.random.randn(1000, 3)
    
    dataset = TimeSeriesDataset(
        data=data,
        lookback=20,
        horizon=5,
        train_split=0.6,
        val_split=0.2,
        test_split=0.2
    )
    
    dataset.prepare(preprocess=False)
    
    info = dataset.get_info()
    
    print("Dataset Info:")
    for key, value in info.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            print(f"{key}: {value}")
    print()


def example_walk_forward():
    print("=" * 50)
    print("Example 6: Walk-Forward Validation")
    print("=" * 50)
    
    from tsdc.utils.splitters import walk_forward_validation
    
    data = np.random.randn(500, 2)
    
    sequencer = Sequencer(lookback=10, horizon=1)
    X, y = sequencer.create_sequences(data)
    
    print(f"Total sequences: {len(X)}")
    
    fold = 0
    for X_train, y_train, X_test, y_test in walk_forward_validation(X, y, n_splits=3):
        fold += 1
        print(f"Fold {fold}: Train={X_train.shape}, Test={X_test.shape}")
    print()


if __name__ == "__main__":
    example_simple_array()
    example_multivariate()
    example_sequencer()
    example_preprocessor()
    example_custom_split()
    example_walk_forward()
