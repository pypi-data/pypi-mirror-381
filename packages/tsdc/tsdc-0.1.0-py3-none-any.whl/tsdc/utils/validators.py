import numpy as np
import pandas as pd
from typing import Union, Tuple


def validate_sequence_params(
    data_length: int,
    lookback: int,
    horizon: int,
    stride: int = 1
) -> bool:
    if lookback < 1:
        raise ValueError(f"lookback must be at least 1, got {lookback}")
    
    if horizon < 1:
        raise ValueError(f"horizon must be at least 1, got {horizon}")
    
    if stride < 1:
        raise ValueError(f"stride must be at least 1, got {stride}")
    
    min_required = lookback + horizon
    if data_length < min_required:
        raise ValueError(
            f"Insufficient data length. Need at least {min_required} points, "
            f"but got {data_length}"
        )
    
    n_sequences = (data_length - lookback - horizon + 1) // stride
    if n_sequences < 1:
        raise ValueError(
            f"Cannot create any sequences with given parameters. "
            f"Data length: {data_length}, lookback: {lookback}, "
            f"horizon: {horizon}, stride: {stride}"
        )
    
    return True


def validate_data_shape(
    data: Union[np.ndarray, pd.DataFrame, pd.Series],
    expected_dims: int = None
) -> Tuple[int, int]:
    if isinstance(data, pd.Series):
        data = data.values.reshape(-1, 1)
    elif isinstance(data, pd.DataFrame):
        data = data.values
    elif not isinstance(data, np.ndarray):
        raise TypeError(f"Unsupported data type: {type(data)}")
    
    if len(data.shape) == 1:
        data = data.reshape(-1, 1)
    
    if expected_dims is not None and len(data.shape) != expected_dims:
        raise ValueError(
            f"Expected {expected_dims}D array, got {len(data.shape)}D"
        )
    
    return data.shape


def validate_splits(
    train_split: float,
    val_split: float,
    test_split: float
) -> bool:
    if train_split <= 0 or train_split >= 1:
        raise ValueError(f"train_split must be between 0 and 1, got {train_split}")
    
    if val_split < 0 or val_split >= 1:
        raise ValueError(f"val_split must be between 0 and 1, got {val_split}")
    
    if test_split < 0 or test_split >= 1:
        raise ValueError(f"test_split must be between 0 and 1, got {test_split}")
    
    total = train_split + val_split + test_split
    if abs(total - 1.0) > 0.001:
        raise ValueError(
            f"Split ratios must sum to 1.0, got {total:.3f} "
            f"(train: {train_split}, val: {val_split}, test: {test_split})"
        )
    
    return True


def validate_target_column(
    data: Union[pd.DataFrame, np.ndarray],
    target_column: Union[int, str]
) -> int:
    if isinstance(data, pd.DataFrame):
        if isinstance(target_column, str):
            if target_column not in data.columns:
                raise ValueError(f"Column '{target_column}' not found in DataFrame")
            return data.columns.get_loc(target_column)
        elif isinstance(target_column, int):
            if target_column >= len(data.columns):
                raise ValueError(
                    f"Column index {target_column} out of range. "
                    f"DataFrame has {len(data.columns)} columns"
                )
            return target_column
    elif isinstance(data, np.ndarray):
        if isinstance(target_column, str):
            raise TypeError("Cannot use string column name with numpy array")
        if len(data.shape) == 1:
            n_features = 1
        else:
            n_features = data.shape[1]
        
        if target_column >= n_features:
            raise ValueError(
                f"Column index {target_column} out of range. "
                f"Array has {n_features} features"
            )
        return target_column
    
    return target_column
