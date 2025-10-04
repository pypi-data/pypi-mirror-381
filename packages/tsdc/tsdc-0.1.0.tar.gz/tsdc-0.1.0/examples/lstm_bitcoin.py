import numpy as np
import pandas as pd
from tsdc import TimeSeriesDataset
from tsdc.loaders import FinancialLoader


def create_bitcoin_dataset():
    print("=" * 50)
    print("Bitcoin Dataset for LSTM")
    print("=" * 50)
    
    loader = FinancialLoader()
    
    try:
        btc_data = loader.load(
            symbol="BTC-USD",
            start_date="2022-01-01",
            end_date="2023-12-31",
            source="yahoo"
        )
        
        btc_data = loader.add_technical_indicators(
            sma_periods=[20, 50],
            ema_periods=[12, 26],
            rsi_period=14,
            macd=True
        )
        
    except Exception as e:
        print(f"Could not load real data: {e}")
        print("Creating synthetic data instead...")
        
        dates = pd.date_range("2022-01-01", "2023-12-31", freq="D")
        btc_data = pd.DataFrame({
            "Close": 40000 + np.cumsum(np.random.randn(len(dates)) * 500),
            "Volume": np.random.uniform(1e9, 3e9, len(dates)),
            "High": 41000 + np.cumsum(np.random.randn(len(dates)) * 500),
            "Low": 39000 + np.cumsum(np.random.randn(len(dates)) * 500),
            "Open": 40000 + np.cumsum(np.random.randn(len(dates)) * 500)
        }, index=dates)
    
    dataset = TimeSeriesDataset(
        data=btc_data[["Close", "Volume"]],
        lookback=60,
        horizon=1,
        target_column="Close",
        scaler_type="minmax",
        train_split=0.8,
        val_split=0.1,
        test_split=0.1
    )
    
    dataset.prepare()
    
    return dataset


def create_lstm_ready_data():
    print("\nCreating LSTM-ready sequences...")
    
    dataset = create_bitcoin_dataset()
    
    X_train, y_train = dataset.get_train()
    X_val, y_val = dataset.get_val()
    X_test, y_test = dataset.get_test()
    
    print(f"\nData shapes:")
    print(f"X_train: {X_train.shape} - (samples, timesteps, features)")
    print(f"y_train: {y_train.shape}")
    print(f"X_val: {X_val.shape}")
    print(f"y_val: {y_val.shape}")
    print(f"X_test: {X_test.shape}")
    print(f"y_test: {y_test.shape}")
    
    return X_train, y_train, X_val, y_val, X_test, y_test


def create_keras_lstm_model(X_train):
    try:
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import LSTM, Dense, Dropout
        from tensorflow.keras.optimizers import Adam
        
        n_timesteps = X_train.shape[1]
        n_features = X_train.shape[2]
        
        model = Sequential([
            LSTM(100, return_sequences=True, input_shape=(n_timesteps, n_features)),
            Dropout(0.2),
            LSTM(100, return_sequences=True),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(25),
            Dense(1)
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='mean_squared_error',
            metrics=['mae']
        )
        
        print("\nLSTM Model Architecture:")
        model.summary()
        
        return model
        
    except ImportError:
        print("\nTensorFlow not installed. Model architecture would be:")
        print("Sequential([")
        print(f"  LSTM(100, return_sequences=True, input_shape=({X_train.shape[1]}, {X_train.shape[2]})),")
        print("  Dropout(0.2),")
        print("  LSTM(100, return_sequences=True),")
        print("  Dropout(0.2),")
        print("  LSTM(50, return_sequences=False),")
        print("  Dropout(0.2),")
        print("  Dense(25),")
        print("  Dense(1)")
        print("])")
        return None


def create_pytorch_lstm_model(X_train):
    try:
        import torch
        import torch.nn as nn
        
        class BitcoinLSTM(nn.Module):
            def __init__(self, input_size, hidden_size=100, num_layers=2):
                super(BitcoinLSTM, self).__init__()
                self.hidden_size = hidden_size
                self.num_layers = num_layers
                
                self.lstm = nn.LSTM(
                    input_size,
                    hidden_size,
                    num_layers,
                    batch_first=True,
                    dropout=0.2
                )
                
                self.fc1 = nn.Linear(hidden_size, 25)
                self.fc2 = nn.Linear(25, 1)
                self.dropout = nn.Dropout(0.2)
                
            def forward(self, x):
                h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
                c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
                
                out, _ = self.lstm(x, (h0, c0))
                out = out[:, -1, :]
                out = self.dropout(out)
                out = self.fc1(out)
                out = self.dropout(out)
                out = self.fc2(out)
                
                return out
        
        model = BitcoinLSTM(input_size=X_train.shape[2])
        
        print("\nPyTorch LSTM Model:")
        print(model)
        
        return model
        
    except ImportError:
        print("\nPyTorch not installed. Model would be LSTM with:")
        print(f"  Input size: {X_train.shape[2]}")
        print(f"  Hidden size: 100")
        print(f"  Num layers: 2")
        print(f"  Dropout: 0.2")
        return None


def example_training_loop():
    X_train, y_train, X_val, y_val, X_test, y_test = create_lstm_ready_data()
    
    print("\n" + "=" * 50)
    print("Ready for training!")
    print("=" * 50)
    
    print("\nExample training code (Keras):")
    print("```python")
    print("model.fit(")
    print("    X_train, y_train,")
    print("    validation_data=(X_val, y_val),")
    print("    epochs=50,")
    print("    batch_size=32,")
    print("    verbose=1")
    print(")")
    print("```")
    
    print("\nExample training code (PyTorch):")
    print("```python")
    print("train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=32)")
    print("for epoch in range(50):")
    print("    for batch_x, batch_y in train_loader:")
    print("        optimizer.zero_grad()")
    print("        outputs = model(batch_x)")
    print("        loss = criterion(outputs, batch_y)")
    print("        loss.backward()")
    print("        optimizer.step()")
    print("```")
    
    keras_model = create_keras_lstm_model(X_train)
    pytorch_model = create_pytorch_lstm_model(X_train)
    
    return X_train, y_train, X_val, y_val, X_test, y_test


def advanced_features_example():
    print("\n" + "=" * 50)
    print("Advanced Features Example")
    print("=" * 50)
    
    dates = pd.date_range("2022-01-01", periods=1000, freq="h")
    
    btc_data = pd.DataFrame({
        "Open": 40000 + np.cumsum(np.random.randn(1000) * 100),
        "High": 41000 + np.cumsum(np.random.randn(1000) * 100),
        "Low": 39000 + np.cumsum(np.random.randn(1000) * 100),
        "Close": 40000 + np.cumsum(np.random.randn(1000) * 100),
        "Volume": np.random.uniform(1e8, 1e9, 1000)
    }, index=dates)
    
    btc_data["Returns"] = btc_data["Close"].pct_change()
    btc_data["Log_Returns"] = np.log(btc_data["Close"] / btc_data["Close"].shift(1))
    btc_data["Volatility"] = btc_data["Returns"].rolling(window=24).std()
    btc_data["MA_7"] = btc_data["Close"].rolling(window=7).mean()
    btc_data["MA_30"] = btc_data["Close"].rolling(window=30).mean()
    btc_data["Price_MA_Ratio"] = btc_data["Close"] / btc_data["MA_30"]
    
    btc_data = btc_data.dropna()
    
    feature_columns = [
        "Open", "High", "Low", "Close", "Volume",
        "Returns", "Volatility", "MA_7", "MA_30", "Price_MA_Ratio"
    ]
    
    dataset = TimeSeriesDataset(
        data=btc_data[feature_columns],
        lookback=48,
        horizon=24,
        target_column="Close",
        scaler_type="robust",
        train_split=0.7,
        val_split=0.15,
        test_split=0.15
    )
    
    dataset.prepare()
    
    X_train, y_train = dataset.get_train()
    
    print(f"Features used: {feature_columns}")
    print(f"Lookback: 48 hours")
    print(f"Prediction horizon: 24 hours")
    print(f"X_train shape: {X_train.shape}")
    print(f"y_train shape: {y_train.shape}")
    
    print("\nThis setup predicts the next 24 hours of Bitcoin prices")
    print("based on the last 48 hours of multiple features.")


if __name__ == "__main__":
    example_training_loop()
    advanced_features_example()
