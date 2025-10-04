import numpy as np
import pandas as pd
from typing import Union, Tuple, Optional, List


class Sequencer:
    def __init__(self, lookback: int, horizon: int = 1, stride: int = 1):
        if lookback < 1:
            raise ValueError("lookback must be at least 1")
        if horizon < 1:
            raise ValueError("horizon must be at least 1")
        if stride < 1:
            raise ValueError("stride must be at least 1")
        
        self.lookback = lookback
        self.horizon = horizon
        self.stride = stride
    
    def create_sequences(
        self,
        data: Union[np.ndarray, pd.DataFrame, pd.Series, list],
        target_column: Optional[Union[int, str]] = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        data_array = self._convert_to_array(data)
        
        if len(data_array.shape) == 1:
            data_array = data_array.reshape(-1, 1)
        
        n_samples = (len(data_array) - self.lookback - self.horizon + 1) // self.stride
        
        if n_samples <= 0:
            raise ValueError(
                f"Not enough data points. Need at least {self.lookback + self.horizon} points, "
                f"but got {len(data_array)}"
            )
        
        X = np.zeros((n_samples, self.lookback, data_array.shape[1]))
        
        if target_column is not None:
            if isinstance(target_column, str) and isinstance(data, pd.DataFrame):
                target_idx = data.columns.get_loc(target_column)
            else:
                target_idx = int(target_column)
            y = np.zeros((n_samples, self.horizon))
        else:
            y = np.zeros((n_samples, self.horizon, data_array.shape[1]))
        
        for i in range(n_samples):
            start_idx = i * self.stride
            end_idx = start_idx + self.lookback
            
            X[i] = data_array[start_idx:end_idx]
            
            if target_column is not None:
                y[i] = data_array[end_idx:end_idx + self.horizon, target_idx]
            else:
                y[i] = data_array[end_idx:end_idx + self.horizon]
        
        if self.horizon == 1:
            y = y.squeeze(axis=1)
        
        return X, y
    
    def create_sequences_with_indices(
        self,
        data: Union[np.ndarray, pd.DataFrame, pd.Series, list],
        target_column: Optional[Union[int, str]] = None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        X, y = self.create_sequences(data, target_column)
        
        n_samples = X.shape[0]
        indices = np.zeros((n_samples, 2), dtype=int)
        
        for i in range(n_samples):
            start_idx = i * self.stride
            end_idx = start_idx + self.lookback + self.horizon
            indices[i] = [start_idx, end_idx]
        
        return X, y, indices
    
    def _convert_to_array(self, data: Union[np.ndarray, pd.DataFrame, pd.Series, list]) -> np.ndarray:
        if isinstance(data, np.ndarray):
            return data
        elif isinstance(data, (pd.DataFrame, pd.Series)):
            return data.values
        elif isinstance(data, list):
            return np.array(data)
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")
    
    def inverse_sequences(
        self,
        sequences: np.ndarray,
        original_shape: Optional[Tuple[int, ...]] = None
    ) -> np.ndarray:
        if len(sequences.shape) == 3:
            n_samples, lookback, n_features = sequences.shape
            if original_shape:
                reconstructed = np.zeros(original_shape)
            else:
                total_length = n_samples * self.stride + lookback
                reconstructed = np.zeros((total_length, n_features))
            
            counts = np.zeros(reconstructed.shape[0])
            
            for i in range(n_samples):
                start_idx = i * self.stride
                end_idx = start_idx + lookback
                reconstructed[start_idx:end_idx] += sequences[i]
                counts[start_idx:end_idx] += 1
            
            counts[counts == 0] = 1
            reconstructed = reconstructed / counts.reshape(-1, 1)
            
            return reconstructed
        else:
            raise ValueError("Input must be 3D array (n_samples, lookback, n_features)")
