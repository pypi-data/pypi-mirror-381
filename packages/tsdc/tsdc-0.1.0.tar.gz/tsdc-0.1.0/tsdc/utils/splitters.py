import numpy as np
from typing import Tuple, List, Generator


def time_series_split(
    X: np.ndarray,
    y: np.ndarray,
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15
) -> Tuple[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]:
    n_samples = len(X)
    
    train_size = int(n_samples * train_ratio)
    val_size = int(n_samples * val_ratio)
    
    X_train = X[:train_size]
    y_train = y[:train_size]
    
    X_val = X[train_size:train_size + val_size]
    y_val = y[train_size:train_size + val_size]
    
    X_test = X[train_size + val_size:]
    y_test = y[train_size + val_size:]
    
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)


def walk_forward_validation(
    X: np.ndarray,
    y: np.ndarray,
    n_splits: int = 5,
    test_size: int = None,
    train_size: int = None,
    gap: int = 0
) -> Generator[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray], None, None]:
    n_samples = len(X)
    
    if test_size is None:
        test_size = n_samples // (n_splits + 1)
    
    if train_size is None:
        train_size = test_size * 2
    
    if train_size + test_size + gap > n_samples:
        raise ValueError(
            f"train_size ({train_size}) + test_size ({test_size}) + gap ({gap}) "
            f"exceeds data length ({n_samples})"
        )
    
    for i in range(n_splits):
        test_start = n_samples - test_size * (n_splits - i)
        test_end = test_start + test_size
        
        train_end = test_start - gap
        train_start = max(0, train_end - train_size)
        
        if train_start >= train_end:
            continue
        
        X_train_fold = X[train_start:train_end]
        y_train_fold = y[train_start:train_end]
        X_test_fold = X[test_start:test_end]
        y_test_fold = y[test_start:test_end]
        
        yield X_train_fold, y_train_fold, X_test_fold, y_test_fold


def expanding_window_split(
    X: np.ndarray,
    y: np.ndarray,
    initial_train_size: int,
    test_size: int,
    step: int = 1
) -> Generator[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray], None, None]:
    n_samples = len(X)
    
    if initial_train_size + test_size > n_samples:
        raise ValueError(
            f"initial_train_size ({initial_train_size}) + test_size ({test_size}) "
            f"exceeds data length ({n_samples})"
        )
    
    current_train_size = initial_train_size
    
    while current_train_size + test_size <= n_samples:
        X_train_fold = X[:current_train_size]
        y_train_fold = y[:current_train_size]
        X_test_fold = X[current_train_size:current_train_size + test_size]
        y_test_fold = y[current_train_size:current_train_size + test_size]
        
        yield X_train_fold, y_train_fold, X_test_fold, y_test_fold
        
        current_train_size += step


def sliding_window_split(
    X: np.ndarray,
    y: np.ndarray,
    window_size: int,
    test_size: int,
    step: int = 1
) -> Generator[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray], None, None]:
    n_samples = len(X)
    
    if window_size + test_size > n_samples:
        raise ValueError(
            f"window_size ({window_size}) + test_size ({test_size}) "
            f"exceeds data length ({n_samples})"
        )
    
    start = 0
    
    while start + window_size + test_size <= n_samples:
        train_end = start + window_size
        test_end = train_end + test_size
        
        X_train_fold = X[start:train_end]
        y_train_fold = y[start:train_end]
        X_test_fold = X[train_end:test_end]
        y_test_fold = y[train_end:test_end]
        
        yield X_train_fold, y_train_fold, X_test_fold, y_test_fold
        
        start += step


def get_temporal_indices(
    n_samples: int,
    train_ratio: float,
    val_ratio: float,
    test_ratio: float
) -> Tuple[List[int], List[int], List[int]]:
    train_size = int(n_samples * train_ratio)
    val_size = int(n_samples * val_ratio)
    
    train_indices = list(range(0, train_size))
    val_indices = list(range(train_size, train_size + val_size))
    test_indices = list(range(train_size + val_size, n_samples))
    
    return train_indices, val_indices, test_indices
