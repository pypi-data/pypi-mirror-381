import numpy as np
import pandas as pd
from typing import Union, Optional, Dict, Any, Literal, Tuple
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


class Preprocessor:
    def __init__(
        self,
        scaler_type: Literal["standard", "minmax", "robust", "none"] = "minmax",
        feature_range: Tuple[float, float] = (0, 1),
        handle_missing: Literal["drop", "forward_fill", "backward_fill", "interpolate", "mean"] = "forward_fill",
        remove_outliers: bool = False,
        outlier_threshold: float = 3.0
    ):
        self.scaler_type = scaler_type
        self.feature_range = feature_range
        self.handle_missing = handle_missing
        self.remove_outliers = remove_outliers
        self.outlier_threshold = outlier_threshold
        
        self.scaler = self._create_scaler()
        self.is_fitted = False
        self.original_shape = None
        self.original_columns = None
    
    def _create_scaler(self):
        if self.scaler_type == "standard":
            return StandardScaler()
        elif self.scaler_type == "minmax":
            return MinMaxScaler(feature_range=self.feature_range)
        elif self.scaler_type == "robust":
            return RobustScaler()
        elif self.scaler_type == "none":
            return None
        else:
            raise ValueError(f"Unknown scaler type: {self.scaler_type}")
    
    def fit(self, data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> "Preprocessor":
        data = self._convert_to_dataframe(data)
        self.original_columns = data.columns.tolist()
        
        data = self._handle_missing_values(data)
        
        if self.remove_outliers:
            data = self._remove_outliers(data)
        
        if self.scaler is not None:
            self.scaler.fit(data)
            self.is_fitted = True
        
        return self
    
    def transform(self, data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> np.ndarray:
        original_type = type(data)
        data = self._convert_to_dataframe(data)
        
        data = self._handle_missing_values(data)
        
        if self.remove_outliers and self.is_fitted:
            data = self._remove_outliers(data)
        
        if self.scaler is not None and self.is_fitted:
            transformed_data = self.scaler.transform(data)
        else:
            transformed_data = data.values
        
        return transformed_data
    
    def fit_transform(self, data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> np.ndarray:
        self.fit(data)
        return self.transform(data)
    
    def inverse_transform(self, data: Union[np.ndarray, pd.DataFrame]) -> Union[np.ndarray, pd.DataFrame]:
        if not self.is_fitted and self.scaler is not None:
            raise ValueError("Preprocessor must be fitted before inverse transform")
        
        if self.scaler is not None:
            original_shape = data.shape
            if len(data.shape) == 3:
                n_samples, n_timesteps, n_features = data.shape
                data = data.reshape(-1, n_features)
                transformed = self.scaler.inverse_transform(data)
                transformed = transformed.reshape(original_shape)
            else:
                transformed = self.scaler.inverse_transform(data)
        else:
            transformed = data
        
        return transformed
    
    def _convert_to_dataframe(self, data: Union[np.ndarray, pd.DataFrame, pd.Series]) -> pd.DataFrame:
        if isinstance(data, pd.DataFrame):
            return data
        elif isinstance(data, pd.Series):
            return data.to_frame()
        elif isinstance(data, np.ndarray):
            if len(data.shape) == 1:
                return pd.DataFrame(data.reshape(-1, 1))
            return pd.DataFrame(data)
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")
    
    def _handle_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        if self.handle_missing == "drop":
            return data.dropna()
        elif self.handle_missing == "forward_fill":
            return data.ffill().bfill()
        elif self.handle_missing == "backward_fill":
            return data.bfill().ffill()
        elif self.handle_missing == "interpolate":
            return data.interpolate(method="linear").bfill().ffill()
        elif self.handle_missing == "mean":
            return data.fillna(data.mean())
        else:
            return data
    
    def _remove_outliers(self, data: pd.DataFrame) -> pd.DataFrame:
        if len(data) == 0:
            return data
        
        z_scores = np.abs((data - data.mean()) / data.std())
        mask = (z_scores < self.outlier_threshold).all(axis=1)
        return data[mask]
    
    def get_params(self) -> Dict[str, Any]:
        return {
            "scaler_type": self.scaler_type,
            "feature_range": self.feature_range,
            "handle_missing": self.handle_missing,
            "remove_outliers": self.remove_outliers,
            "outlier_threshold": self.outlier_threshold,
            "is_fitted": self.is_fitted
        }
