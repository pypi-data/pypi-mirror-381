import pandas as pd
import numpy as np
from typing import Optional, Union, List
from datetime import datetime, timedelta
from .base import BaseLoader


class FinancialLoader(BaseLoader):
    def __init__(self):
        super().__init__()
        self.symbol = None
        self.start_date = None
        self.end_date = None
    
    def load(
        self,
        symbol: str = None,
        start_date: Union[str, datetime] = None,
        end_date: Union[str, datetime] = None,
        source: str = "yahoo"
    ) -> pd.DataFrame:
        if source == "yahoo":
            return self._load_from_yahoo(symbol, start_date, end_date)
        elif source == "csv":
            return self._load_from_csv(symbol)
        else:
            raise ValueError(f"Unsupported source: {source}")
    
    def _load_from_yahoo(
        self,
        symbol: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime]
    ) -> pd.DataFrame:
        try:
            import yfinance as yf
        except ImportError:
            raise ImportError("yfinance not installed. Install with: pip install yfinance")
        
        if symbol is None:
            raise ValueError("Symbol is required for Yahoo Finance")
        
        ticker = yf.Ticker(symbol)
        
        if start_date is None:
            start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        
        self.data = ticker.history(start=start_date, end=end_date)
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        
        self.metadata = {
            "symbol": symbol,
            "start_date": start_date,
            "end_date": end_date,
            "source": "yahoo",
            "columns": list(self.data.columns)
        }
        
        return self.data
    
    def _load_from_csv(self, path: str) -> pd.DataFrame:
        self.data = pd.read_csv(path, parse_dates=True, index_col=0)
        self.metadata = {
            "source": "csv",
            "path": path,
            "columns": list(self.data.columns)
        }
        return self.data
    
    def validate(self, data: pd.DataFrame) -> bool:
        required_columns = ["Open", "High", "Low", "Close", "Volume"]
        
        for col in required_columns:
            if col not in data.columns:
                return False
        
        if data.isnull().any().any():
            return False
        
        if not isinstance(data.index, pd.DatetimeIndex):
            return False
        
        return True
    
    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data.copy()
        
        if "Adj Close" in data.columns:
            data = data.drop(columns=["Adj Close"])
        
        if "Dividends" in data.columns:
            data = data.drop(columns=["Dividends"])
        
        if "Stock Splits" in data.columns:
            data = data.drop(columns=["Stock Splits"])
        
        data = data.ffill().bfill()
        
        return data
    
    def add_technical_indicators(
        self,
        sma_periods: List[int] = [20, 50],
        ema_periods: List[int] = [12, 26],
        rsi_period: int = 14,
        macd: bool = True
    ) -> pd.DataFrame:
        if self.data is None:
            raise ValueError("No data loaded")
        
        data = self.data.copy()
        
        for period in sma_periods:
            data[f"SMA_{period}"] = data["Close"].rolling(window=period).mean()
        
        for period in ema_periods:
            data[f"EMA_{period}"] = data["Close"].ewm(span=period, adjust=False).mean()
        
        if rsi_period:
            data[f"RSI_{rsi_period}"] = self._calculate_rsi(data["Close"], rsi_period)
        
        if macd:
            data["MACD"], data["MACD_signal"], data["MACD_diff"] = self._calculate_macd(data["Close"])
        
        data["Returns"] = data["Close"].pct_change()
        
        data["Volume_SMA"] = data["Volume"].rolling(window=20).mean()
        
        self.data = data
        return data
    
    def _calculate_rsi(self, prices: pd.Series, period: int = 14) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def _calculate_macd(
        self,
        prices: pd.Series,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9
    ) -> tuple:
        ema_fast = prices.ewm(span=fast, adjust=False).mean()
        ema_slow = prices.ewm(span=slow, adjust=False).mean()
        
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        macd_diff = macd_line - signal_line
        
        return macd_line, signal_line, macd_diff
    
    def get_ohlcv(self) -> pd.DataFrame:
        if self.data is None:
            raise ValueError("No data loaded")
        
        ohlcv_columns = ["Open", "High", "Low", "Close", "Volume"]
        available_columns = [col for col in ohlcv_columns if col in self.data.columns]
        
        return self.data[available_columns]
    
    def resample(self, freq: str) -> pd.DataFrame:
        if self.data is None:
            raise ValueError("No data loaded")
        
        resampled = pd.DataFrame()
        resampled["Open"] = self.data["Open"].resample(freq).first()
        resampled["High"] = self.data["High"].resample(freq).max()
        resampled["Low"] = self.data["Low"].resample(freq).min()
        resampled["Close"] = self.data["Close"].resample(freq).last()
        resampled["Volume"] = self.data["Volume"].resample(freq).sum()
        
        return resampled
