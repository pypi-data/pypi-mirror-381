import unittest
import numpy as np
import pandas as pd
from tsdc import TimeSeriesDataset, Sequencer, Preprocessor
from tsdc.loaders import FinancialLoader
from tsdc.utils.splitters import walk_forward_validation, expanding_window_split, sliding_window_split


class TestEndToEndWorkflow(unittest.TestCase):
    def test_complete_workflow_simple(self):
        np.random.seed(42)
        data = np.cumsum(np.random.randn(1000)) + 100
        
        dataset = TimeSeriesDataset(
            data=data,
            lookback=60,
            horizon=1,
            scaler_type='minmax',
            train_split=0.7,
            val_split=0.15,
            test_split=0.15
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        X_val, y_val = dataset.get_val()
        X_test, y_test = dataset.get_test()
        
        self.assertEqual(X_train.shape[1], 60)
        self.assertEqual(X_train.shape[2], 1)
        self.assertGreater(len(X_train), len(X_val))
        self.assertGreater(len(X_train), len(X_test))
        
        self.assertTrue(np.all(X_train >= 0))
        self.assertTrue(np.all(X_train <= 1))
    
    def test_complete_workflow_multivariate(self):
        np.random.seed(42)
        dates = pd.date_range('2020-01-01', periods=1000, freq='h')
        data = pd.DataFrame({
            'temperature': np.sin(np.linspace(0, 20, 1000)) * 10 + 20,
            'humidity': np.cos(np.linspace(0, 20, 1000)) * 20 + 60,
            'pressure': np.random.randn(1000) * 5 + 1013
        }, index=dates)
        
        dataset = TimeSeriesDataset(
            data=data,
            lookback=24,
            horizon=6,
            target_column='temperature',
            scaler_type='standard'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertEqual(X_train.shape[1], 24)
        self.assertEqual(X_train.shape[2], 3)
        self.assertEqual(y_train.shape[1], 6)
        
        info = dataset.get_info()
        self.assertEqual(info['lookback'], 24)
        self.assertEqual(info['horizon'], 6)
        self.assertTrue(info['is_prepared'])
    
    def test_workflow_with_financial_loader(self):
        dates = pd.date_range('2023-01-01', periods=200, freq='D')
        data = pd.DataFrame({
            'Open': np.random.uniform(100, 200, 200),
            'High': np.random.uniform(100, 200, 200),
            'Low': np.random.uniform(100, 200, 200),
            'Close': np.random.uniform(100, 200, 200),
            'Volume': np.random.uniform(1e6, 1e8, 200)
        }, index=dates)
        
        loader = FinancialLoader()
        loader.data = data
        
        enriched_data = loader.add_technical_indicators(
            sma_periods=[20, 50],
            ema_periods=[12, 26],
            rsi_period=14,
            macd=True
        )
        
        enriched_data = enriched_data.dropna()
        
        dataset = TimeSeriesDataset(
            data=enriched_data,
            lookback=30,
            horizon=5,
            target_column='Close',
            scaler_type='minmax'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertGreater(X_train.shape[2], 5)
        self.assertEqual(y_train.shape[1], 5)
    
    def test_preprocessing_then_sequencing(self):
        data = pd.DataFrame({
            'a': [1, 2, np.nan, 4, 5, 100, 7, 8, 9, 10] * 10,
            'b': [10, 20, 30, np.nan, 50, 60, 70, 80, 90, 1000] * 10
        })
        
        preprocessor = Preprocessor(
            scaler_type='robust',
            handle_missing='interpolate',
            remove_outliers=True,
            outlier_threshold=2.5
        )
        
        processed = preprocessor.fit_transform(data)
        
        sequencer = Sequencer(lookback=10, horizon=3)
        X, y = sequencer.create_sequences(processed)
        
        self.assertGreater(len(X), 0)
        self.assertEqual(X.shape[1], 10)
        self.assertEqual(X.shape[2], 2)
    
    def test_walk_forward_validation_workflow(self):
        data = np.random.randn(500)
        
        dataset = TimeSeriesDataset(data, lookback=20, horizon=1)
        dataset.prepare(preprocess=False)
        
        X_train, y_train = dataset.get_train()
        
        fold_count = 0
        for X_tr, y_tr, X_te, y_te in walk_forward_validation(X_train, y_train, n_splits=3):
            fold_count += 1
            self.assertGreater(len(X_tr), 0)
            self.assertGreater(len(X_te), 0)
        
        self.assertEqual(fold_count, 3)
    
    def test_expanding_window_workflow(self):
        data = np.random.randn(300)
        sequencer = Sequencer(lookback=10, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        fold_count = 0
        for X_tr, y_tr, X_te, y_te in expanding_window_split(
            X, y,
            initial_train_size=50,
            test_size=20,
            step=20
        ):
            fold_count += 1
            self.assertGreaterEqual(len(X_tr), 50)
            self.assertEqual(len(X_te), 20)
        
        self.assertGreater(fold_count, 0)
    
    def test_sliding_window_workflow(self):
        data = np.random.randn(300)
        sequencer = Sequencer(lookback=10, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        fold_count = 0
        for X_tr, y_tr, X_te, y_te in sliding_window_split(
            X, y,
            window_size=50,
            test_size=20,
            step=10
        ):
            fold_count += 1
            self.assertEqual(len(X_tr), 50)
            self.assertEqual(len(X_te), 20)
        
        self.assertGreater(fold_count, 5)
    
    def test_inverse_transform_workflow(self):
        data = np.random.uniform(100, 200, 100)
        
        dataset = TimeSeriesDataset(
            data=data,
            lookback=10,
            horizon=1,
            scaler_type='minmax'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        predictions = y_train[:5]
        
        original_scale = dataset.inverse_transform_predictions(predictions)
        
        self.assertTrue(np.all(original_scale >= 100))
        self.assertTrue(np.all(original_scale <= 200))
    
    def test_create_sliding_window_on_new_data(self):
        train_data = np.random.randn(100)
        test_data = np.random.randn(50)
        
        dataset = TimeSeriesDataset(
            data=train_data,
            lookback=10,
            horizon=1
        )
        dataset.prepare()
        
        X_new, y_new = dataset.create_sliding_window(test_data)
        
        self.assertEqual(X_new.shape[1], 10)
        self.assertGreater(len(X_new), 0)
    
    def test_get_all_splits(self):
        data = np.random.randn(200)
        
        dataset = TimeSeriesDataset(data, lookback=10, horizon=1)
        dataset.prepare()
        
        all_splits = dataset.get_all()
        
        self.assertIn('train', all_splits)
        self.assertIn('val', all_splits)
        self.assertIn('test', all_splits)
        
        X_train, y_train = all_splits['train']
        X_val, y_val = all_splits['val']
        X_test, y_test = all_splits['test']
        
        self.assertIsNotNone(X_train)
        self.assertIsNotNone(y_train)
        self.assertIsNotNone(X_val)
        self.assertIsNotNone(y_val)
        self.assertIsNotNone(X_test)
        self.assertIsNotNone(y_test)


class TestRealWorldScenarios(unittest.TestCase):
    def test_bitcoin_price_prediction_scenario(self):
        dates = pd.date_range('2023-01-01', periods=365, freq='D')
        btc_data = pd.DataFrame({
            'Close': 40000 + np.cumsum(np.random.randn(365) * 500),
            'Volume': np.random.uniform(1e9, 3e9, 365),
            'High': 41000 + np.cumsum(np.random.randn(365) * 500),
            'Low': 39000 + np.cumsum(np.random.randn(365) * 500),
            'Open': 40000 + np.cumsum(np.random.randn(365) * 500)
        }, index=dates)
        
        dataset = TimeSeriesDataset(
            data=btc_data[['Close', 'Volume']],
            lookback=60,
            horizon=1,
            target_column='Close',
            scaler_type='minmax'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        X_val, y_val = dataset.get_val()
        X_test, y_test = dataset.get_test()
        
        self.assertEqual(X_train.shape[1], 60)
        self.assertEqual(X_train.shape[2], 2)
        self.assertEqual(len(y_train.shape), 1)
    
    def test_weather_forecasting_scenario(self):
        hours = pd.date_range('2023-01-01', periods=8760, freq='h')
        weather_data = pd.DataFrame({
            'temperature': 15 + 10 * np.sin(np.linspace(0, 4*np.pi, 8760)) + np.random.randn(8760) * 2,
            'humidity': 60 + 20 * np.cos(np.linspace(0, 4*np.pi, 8760)) + np.random.randn(8760) * 5,
            'pressure': 1013 + np.random.randn(8760) * 3,
            'wind_speed': np.abs(np.random.randn(8760) * 5)
        }, index=hours)
        
        dataset = TimeSeriesDataset(
            data=weather_data,
            lookback=48,
            horizon=24,
            target_column='temperature',
            scaler_type='standard'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertEqual(X_train.shape[1], 48)
        self.assertEqual(X_train.shape[2], 4)
        self.assertEqual(y_train.shape[1], 24)
    
    def test_sales_forecasting_scenario(self):
        days = pd.date_range('2020-01-01', periods=1000, freq='D')
        sales_data = pd.DataFrame({
            'sales': np.abs(100 + 50 * np.sin(np.linspace(0, 20, 1000)) + np.random.randn(1000) * 10),
            'marketing_spend': np.random.uniform(1000, 5000, 1000),
            'day_of_week': [d.dayofweek for d in days],
            'is_holiday': np.random.choice([0, 1], 1000, p=[0.95, 0.05])
        }, index=days)
        
        dataset = TimeSeriesDataset(
            data=sales_data,
            lookback=30,
            horizon=7,
            target_column='sales',
            scaler_type='minmax'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertEqual(X_train.shape[1], 30)
        self.assertEqual(y_train.shape[1], 7)
    
    def test_energy_consumption_scenario(self):
        hours = pd.date_range('2023-01-01', periods=2000, freq='h')
        energy_data = pd.DataFrame({
            'consumption': 500 + 200 * np.sin(np.linspace(0, 8*np.pi, 2000)) + np.random.randn(2000) * 50,
            'temperature': 20 + 10 * np.cos(np.linspace(0, 8*np.pi, 2000)),
            'hour_of_day': [h.hour for h in hours]
        }, index=hours)
        
        dataset = TimeSeriesDataset(
            data=energy_data,
            lookback=24,
            horizon=12,
            target_column='consumption',
            scaler_type='robust'
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertEqual(X_train.shape[1], 24)
        self.assertEqual(y_train.shape[1], 12)


class TestPerformance(unittest.TestCase):
    def test_large_dataset_performance(self):
        data = np.random.randn(10000)
        
        import time
        start = time.time()
        
        dataset = TimeSeriesDataset(data, lookback=100, horizon=10)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        end = time.time()
        
        self.assertLess(end - start, 5.0)
        self.assertGreater(len(X_train), 0)
    
    def test_high_dimensional_data(self):
        data = np.random.randn(1000, 50)
        
        sequencer = Sequencer(lookback=20, horizon=5)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(X.shape[2], 50)
        self.assertEqual(y.shape[2], 50)


if __name__ == '__main__':
    unittest.main()
