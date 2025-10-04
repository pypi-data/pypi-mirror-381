import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from typing import Union, Optional, Dict, Any


class BaseLoader(ABC):
    def __init__(self):
        self.data = None
        self.metadata = {}
    
    @abstractmethod
    def load(self, *args, **kwargs) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def validate(self, data: pd.DataFrame) -> bool:
        pass
    
    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        return data
    
    def get_data(self) -> Optional[pd.DataFrame]:
        return self.data
    
    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata
    
    def save(self, path: str, format: str = "csv") -> None:
        if self.data is None:
            raise ValueError("No data to save")
        
        if format == "csv":
            self.data.to_csv(path, index=False)
        elif format == "parquet":
            self.data.to_parquet(path, index=False)
        elif format == "json":
            self.data.to_json(path, orient="records")
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    @staticmethod
    def from_csv(path: str, **kwargs) -> pd.DataFrame:
        return pd.read_csv(path, **kwargs)
    
    @staticmethod
    def from_parquet(path: str, **kwargs) -> pd.DataFrame:
        return pd.read_parquet(path, **kwargs)
    
    @staticmethod
    def from_json(path: str, **kwargs) -> pd.DataFrame:
        return pd.read_json(path, **kwargs)
    
    @staticmethod
    def from_array(
        data: np.ndarray,
        columns: Optional[list] = None,
        index: Optional[Union[list, pd.DatetimeIndex]] = None
    ) -> pd.DataFrame:
        return pd.DataFrame(data, columns=columns, index=index)
