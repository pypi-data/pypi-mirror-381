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

print(f"Training: {X_train.shape}")
print(f"Ready for LSTM!")
