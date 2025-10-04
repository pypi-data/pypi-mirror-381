import unittest
import numpy as np
import pandas as pd
from tsdc.loaders import BaseLoader, FinancialLoader
import tempfile
import os


class TestBaseLoader(unittest.TestCase):
    def test_from_csv(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("date,value\n2023-01-01,100\n2023-01-02,200\n")
            temp_file = f.name
        
        try:
            df = BaseLoader.from_csv(temp_file)
            self.assertEqual(len(df), 2)
            self.assertIn('date', df.columns)
            self.assertIn('value', df.columns)
        finally:
            os.unlink(temp_file)
    
    def test_from_array(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df = BaseLoader.from_array(data, columns=['A', 'B'])
        
        self.assertEqual(df.shape, (3, 2))
        self.assertListEqual(list(df.columns), ['A', 'B'])
        self.assertEqual(df.iloc[0, 0], 1)
    
    def test_from_array_with_index(self):
        data = np.array([[1, 2], [3, 4]])
        dates = pd.date_range('2023-01-01', periods=2)
        df = BaseLoader.from_array(data, columns=['A', 'B'], index=dates)
        
        self.assertIsInstance(df.index, pd.DatetimeIndex)
        self.assertEqual(len(df), 2)
    
    def test_save_csv(self):
        loader = FinancialLoader()
        loader.data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_file = f.name
        
        try:
            loader.save(temp_file, format='csv')
            self.assertTrue(os.path.exists(temp_file))
            
            loaded = pd.read_csv(temp_file)
            self.assertEqual(len(loaded), 3)
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_save_without_data(self):
        loader = FinancialLoader()
        
        with self.assertRaises(ValueError):
            loader.save('test.csv')


class TestFinancialLoader(unittest.TestCase):
    def setUp(self):
        self.loader = FinancialLoader()
        dates = pd.date_range('2023-01-01', periods=100, freq='D')
        self.sample_data = pd.DataFrame({
            'Open': np.random.uniform(100, 200, 100),
            'High': np.random.uniform(100, 200, 100),
            'Low': np.random.uniform(100, 200, 100),
            'Close': np.random.uniform(100, 200, 100),
            'Volume': np.random.uniform(1e6, 1e8, 100)
        }, index=dates)
        self.loader.data = self.sample_data
    
    def test_validate_valid_data(self):
        result = self.loader.validate(self.sample_data)
        self.assertTrue(result)
    
    def test_validate_missing_columns(self):
        invalid_data = pd.DataFrame({
            'Open': [1, 2, 3],
            'Close': [4, 5, 6]
        })
        result = self.loader.validate(invalid_data)
        self.assertFalse(result)
    
    def test_validate_with_nan(self):
        data_with_nan = self.sample_data.copy()
        data_with_nan.loc[0, 'Close'] = np.nan
        result = self.loader.validate(data_with_nan)
        self.assertFalse(result)
    
    def test_validate_without_datetime_index(self):
        data_no_index = self.sample_data.reset_index(drop=True)
        result = self.loader.validate(data_no_index)
        self.assertFalse(result)
    
    def test_preprocess(self):
        data_with_extra = self.sample_data.copy()
        data_with_extra['Adj Close'] = data_with_extra['Close'] * 1.1
        data_with_extra['Dividends'] = 0
        data_with_extra['Stock Splits'] = 0
        
        processed = self.loader.preprocess(data_with_extra)
        
        self.assertNotIn('Adj Close', processed.columns)
        self.assertNotIn('Dividends', processed.columns)
        self.assertNotIn('Stock Splits', processed.columns)
    
    def test_add_technical_indicators(self):
        result = self.loader.add_technical_indicators(
            sma_periods=[5, 10],
            ema_periods=[5, 10],
            rsi_period=14,
            macd=True
        )
        
        self.assertIn('SMA_5', result.columns)
        self.assertIn('SMA_10', result.columns)
        self.assertIn('EMA_5', result.columns)
        self.assertIn('EMA_10', result.columns)
        self.assertIn('RSI_14', result.columns)
        self.assertIn('MACD', result.columns)
        self.assertIn('MACD_signal', result.columns)
        self.assertIn('MACD_diff', result.columns)
        self.assertIn('Returns', result.columns)
        self.assertIn('Volume_SMA', result.columns)
    
    def test_add_indicators_without_data(self):
        empty_loader = FinancialLoader()
        
        with self.assertRaises(ValueError):
            empty_loader.add_technical_indicators()
    
    def test_get_ohlcv(self):
        ohlcv = self.loader.get_ohlcv()
        
        self.assertEqual(len(ohlcv.columns), 5)
        self.assertIn('Open', ohlcv.columns)
        self.assertIn('High', ohlcv.columns)
        self.assertIn('Low', ohlcv.columns)
        self.assertIn('Close', ohlcv.columns)
        self.assertIn('Volume', ohlcv.columns)
    
    def test_get_ohlcv_without_data(self):
        empty_loader = FinancialLoader()
        
        with self.assertRaises(ValueError):
            empty_loader.get_ohlcv()
    
    def test_resample_daily_to_weekly(self):
        resampled = self.loader.resample('W')
        
        self.assertLess(len(resampled), len(self.sample_data))
        self.assertIn('Open', resampled.columns)
        self.assertIn('High', resampled.columns)
        self.assertIn('Low', resampled.columns)
        self.assertIn('Close', resampled.columns)
        self.assertIn('Volume', resampled.columns)
    
    def test_resample_without_data(self):
        empty_loader = FinancialLoader()
        
        with self.assertRaises(ValueError):
            empty_loader.resample('W')
    
    def test_metadata_storage(self):
        self.loader.metadata = {
            'symbol': 'TEST',
            'source': 'test'
        }
        
        metadata = self.loader.get_metadata()
        
        self.assertEqual(metadata['symbol'], 'TEST')
        self.assertEqual(metadata['source'], 'test')
    
    def test_rsi_calculation(self):
        prices = pd.Series([100, 105, 103, 108, 110, 107, 112, 115, 113, 118, 120, 119, 122, 125, 123])
        rsi = self.loader._calculate_rsi(prices, period=14)
        
        self.assertIsInstance(rsi, pd.Series)
        self.assertEqual(len(rsi), len(prices))
        
        valid_rsi = rsi.dropna()
        self.assertTrue(all(valid_rsi >= 0))
        self.assertTrue(all(valid_rsi <= 100))
    
    def test_macd_calculation(self):
        prices = pd.Series(np.random.uniform(100, 200, 50))
        macd, signal, diff = self.loader._calculate_macd(prices)
        
        self.assertIsInstance(macd, pd.Series)
        self.assertIsInstance(signal, pd.Series)
        self.assertIsInstance(diff, pd.Series)
        self.assertEqual(len(macd), len(prices))
    
    def test_load_from_csv(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            self.sample_data.to_csv(f.name)
            temp_file = f.name
        
        try:
            loader = FinancialLoader()
            data = loader._load_from_csv(temp_file)
            
            self.assertIsInstance(data, pd.DataFrame)
            self.assertEqual(len(data), len(self.sample_data))
            self.assertIn('Close', data.columns)
        finally:
            os.unlink(temp_file)


class TestLoaderIntegration(unittest.TestCase):
    def test_loader_with_dataset(self):
        from tsdc import TimeSeriesDataset
        
        dates = pd.date_range('2023-01-01', periods=100, freq='D')
        data = pd.DataFrame({
            'Open': np.random.uniform(100, 200, 100),
            'High': np.random.uniform(100, 200, 100),
            'Low': np.random.uniform(100, 200, 100),
            'Close': np.random.uniform(100, 200, 100),
            'Volume': np.random.uniform(1e6, 1e8, 100)
        }, index=dates)
        
        loader = FinancialLoader()
        loader.data = data
        loader.add_technical_indicators()
        
        dataset = TimeSeriesDataset(
            data=loader.get_ohlcv(),
            lookback=10,
            horizon=1
        )
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertIsNotNone(X_train)
        self.assertIsNotNone(y_train)
        self.assertEqual(X_train.shape[1], 10)
        self.assertEqual(X_train.shape[2], 5)


if __name__ == '__main__':
    unittest.main()
