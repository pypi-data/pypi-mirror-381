import numpy as np
import pandas as pd
from typing import Union, Optional, Tuple, Dict, Any, List
from .sequencer import Sequencer
from .preprocessor import Preprocessor


class TimeSeriesDataset:
    def __init__(
        self,
        data: Union[np.ndarray, pd.DataFrame, pd.Series, str],
        lookback: int = 10,
        horizon: int = 1,
        stride: int = 1,
        target_column: Optional[Union[int, str]] = None,
        scaler_type: str = "minmax",
        train_split: float = 0.7,
        val_split: float = 0.15,
        test_split: float = 0.15
    ):
        if isinstance(data, str):
            self.data = self._load_data(data)
        else:
            self.data = data
        
        self.lookback = lookback
        self.horizon = horizon
        self.stride = stride
        self.target_column = target_column
        self.scaler_type = scaler_type
        
        if abs(train_split + val_split + test_split - 1.0) > 0.001:
            raise ValueError("Split ratios must sum to 1.0")
        
        self.train_split = train_split
        self.val_split = val_split
        self.test_split = test_split
        
        self.sequencer = Sequencer(lookback, horizon, stride)
        self.preprocessor = Preprocessor(scaler_type=scaler_type)
        
        self.X_train = None
        self.y_train = None
        self.X_val = None
        self.y_val = None
        self.X_test = None
        self.y_test = None
        
        self.is_prepared = False
    
    def prepare(self, preprocess: bool = True) -> "TimeSeriesDataset":
        target_idx = None
        if self.target_column is not None:
            if isinstance(self.target_column, str):
                if isinstance(self.data, pd.DataFrame):
                    target_idx = self.data.columns.get_loc(self.target_column)
                else:
                    raise ValueError(f"Cannot use string column name '{self.target_column}' with non-DataFrame data")
            else:
                target_idx = self.target_column
        
        if preprocess:
            processed_data = self.preprocessor.fit_transform(self.data)
        else:
            processed_data = self._convert_to_array(self.data)
        
        X, y = self.sequencer.create_sequences(processed_data, target_idx)
        
        n_samples = len(X)
        train_size = int(n_samples * self.train_split)
        val_size = int(n_samples * self.val_split)
        
        self.X_train = X[:train_size]
        self.y_train = y[:train_size]
        
        self.X_val = X[train_size:train_size + val_size]
        self.y_val = y[train_size:train_size + val_size]
        
        self.X_test = X[train_size + val_size:]
        self.y_test = y[train_size + val_size:]
        
        self.is_prepared = True
        return self
    
    def get_train(self) -> Tuple[np.ndarray, np.ndarray]:
        if not self.is_prepared:
            raise ValueError("Dataset not prepared. Call prepare() first.")
        return self.X_train, self.y_train
    
    def get_val(self) -> Tuple[np.ndarray, np.ndarray]:
        if not self.is_prepared:
            raise ValueError("Dataset not prepared. Call prepare() first.")
        return self.X_val, self.y_val
    
    def get_test(self) -> Tuple[np.ndarray, np.ndarray]:
        if not self.is_prepared:
            raise ValueError("Dataset not prepared. Call prepare() first.")
        return self.X_test, self.y_test
    
    def get_all(self) -> Dict[str, Tuple[np.ndarray, np.ndarray]]:
        if not self.is_prepared:
            raise ValueError("Dataset not prepared. Call prepare() first.")
        return {
            "train": (self.X_train, self.y_train),
            "val": (self.X_val, self.y_val),
            "test": (self.X_test, self.y_test)
        }
    
    def create_sliding_window(
        self,
        data: Optional[Union[np.ndarray, pd.DataFrame, pd.Series]] = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        if data is None:
            data = self.data
        
        target_idx = None
        if self.target_column is not None:
            if isinstance(self.target_column, str):
                if isinstance(data, pd.DataFrame):
                    target_idx = data.columns.get_loc(self.target_column)
                else:
                    raise ValueError(f"Cannot use string column name '{self.target_column}' with non-DataFrame data")
            else:
                target_idx = self.target_column
        
        processed_data = self.preprocessor.transform(data)
        return self.sequencer.create_sequences(processed_data, target_idx)
    
    def inverse_transform_predictions(self, predictions: np.ndarray) -> np.ndarray:
        if len(predictions.shape) == 1:
            predictions = predictions.reshape(-1, 1)
        
        return self.preprocessor.inverse_transform(predictions)
    
    def _load_data(self, path: str) -> pd.DataFrame:
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith('.parquet'):
            return pd.read_parquet(path)
        elif path.endswith('.json'):
            return pd.read_json(path)
        else:
            raise ValueError(f"Unsupported file format: {path}")
    
    def _convert_to_array(self, data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> np.ndarray:
        if isinstance(data, np.ndarray):
            return data
        elif isinstance(data, (pd.DataFrame, pd.Series)):
            return data.values
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")
    
    def get_info(self) -> Dict[str, Any]:
        info = {
            "lookback": self.lookback,
            "horizon": self.horizon,
            "stride": self.stride,
            "target_column": self.target_column,
            "scaler_type": self.scaler_type,
            "splits": {
                "train": self.train_split,
                "val": self.val_split,
                "test": self.test_split
            },
            "is_prepared": self.is_prepared
        }
        
        if self.is_prepared:
            info["shapes"] = {
                "X_train": self.X_train.shape,
                "y_train": self.y_train.shape,
                "X_val": self.X_val.shape,
                "y_val": self.y_val.shape,
                "X_test": self.X_test.shape,
                "y_test": self.y_test.shape
            }
        
        return info
    
    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "TimeSeriesDataset":
        return cls(**config)
