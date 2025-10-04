import unittest
import numpy as np
import pandas as pd
from tsdc import TimeSeriesDataset, Sequencer, Preprocessor
from tsdc.utils.validators import validate_sequence_params, validate_splits


class TestEdgeCases(unittest.TestCase):
    def test_very_small_dataset(self):
        data = np.array([1, 2, 3, 4, 5])
        
        with self.assertRaises(ValueError):
            dataset = TimeSeriesDataset(data, lookback=10, horizon=1)
            dataset.prepare()
    
    def test_single_feature_data(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertEqual(X_train.shape[2], 1)
    
    def test_large_stride(self):
        data = np.arange(100)
        sequencer = Sequencer(lookback=5, horizon=2, stride=10)
        X, y = sequencer.create_sequences(data)
        
        self.assertLess(X.shape[0], 10)
        self.assertEqual(X[0, 0, 0], 0)
        self.assertEqual(X[1, 0, 0], 10)
    
    def test_lookback_equals_horizon(self):
        data = np.arange(50)
        sequencer = Sequencer(lookback=5, horizon=5)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(X.shape[1], 5)
        self.assertEqual(y.shape[1], 5)
    
    def test_horizon_larger_than_lookback(self):
        data = np.arange(100)
        sequencer = Sequencer(lookback=5, horizon=20)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(X.shape[1], 5)
        self.assertEqual(y.shape[1], 20)
    
    def test_all_zeros_data(self):
        data = np.zeros(100)
        dataset = TimeSeriesDataset(data, lookback=10, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertTrue(np.all(X_train == 0))
    
    def test_all_same_values(self):
        data = np.ones(100) * 42
        dataset = TimeSeriesDataset(data, lookback=10, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsNotNone(X_train)
    
    def test_extreme_values(self):
        data = np.array([1e10, 1e-10, 1e10, 1e-10] * 25)
        dataset = TimeSeriesDataset(data, lookback=5, horizon=1, scaler_type='minmax')
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertTrue(np.all(X_train >= 0))
        self.assertTrue(np.all(X_train <= 1))
    
    def test_negative_values(self):
        data = np.array([-100, -50, -25, -10, -5, 0, 5, 10, 25, 50] * 10)
        dataset = TimeSeriesDataset(data, lookback=5, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsNotNone(X_train)
    
    def test_nan_in_middle(self):
        data = pd.Series([1, 2, 3, np.nan, 5, 6, 7, 8, 9, 10])
        preprocessor = Preprocessor(handle_missing='interpolate')
        processed = preprocessor.fit_transform(data)
        
        self.assertFalse(np.any(np.isnan(processed)))
    
    def test_multiple_consecutive_nans(self):
        data = pd.Series([1, 2, np.nan, np.nan, np.nan, 6, 7, 8, 9, 10])
        preprocessor = Preprocessor(handle_missing='forward_fill')
        processed = preprocessor.fit_transform(data)
        
        self.assertFalse(np.any(np.isnan(processed)))
    
    def test_nan_at_start(self):
        data = pd.Series([np.nan, np.nan, 3, 4, 5, 6, 7, 8, 9, 10])
        preprocessor = Preprocessor(handle_missing='backward_fill')
        processed = preprocessor.fit_transform(data)
        
        self.assertFalse(np.any(np.isnan(processed)))
    
    def test_nan_at_end(self):
        data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, np.nan, np.nan])
        preprocessor = Preprocessor(handle_missing='forward_fill')
        processed = preprocessor.fit_transform(data)
        
        self.assertFalse(np.any(np.isnan(processed)))
    
    def test_single_outlier(self):
        data = pd.DataFrame({'value': [10, 11, 12, 1000, 13, 14, 15, 16, 17, 18]})
        preprocessor = Preprocessor(remove_outliers=True, outlier_threshold=2.0)
        processed = preprocessor.fit_transform(data)
        
        self.assertLess(len(processed), len(data))
    
    def test_multiple_outliers(self):
        data = pd.DataFrame({'value': [10, 1000, 12, 13, -1000, 15, 16, 2000, 18, 19]})
        preprocessor = Preprocessor(remove_outliers=True, outlier_threshold=2.0)
        processed = preprocessor.fit_transform(data)
        
        self.assertLess(len(processed), len(data))
    
    def test_very_small_train_split(self):
        data = np.arange(100)
        dataset = TimeSeriesDataset(
            data, 
            lookback=5, 
            horizon=1,
            train_split=0.1,
            val_split=0.1,
            test_split=0.8
        )
        dataset.prepare()
        
        X_train, _ = dataset.get_train()
        X_test, _ = dataset.get_test()
        
        self.assertLess(len(X_train), len(X_test))
    
    def test_no_validation_set(self):
        data = np.arange(100)
        dataset = TimeSeriesDataset(
            data,
            lookback=5,
            horizon=1,
            train_split=0.8,
            val_split=0.0,
            test_split=0.2
        )
        dataset.prepare()
        
        X_val, y_val = dataset.get_val()
        
        self.assertEqual(len(X_val), 0)
        self.assertEqual(len(y_val), 0)
    
    def test_dataframe_with_datetime_index(self):
        dates = pd.date_range('2023-01-01', periods=100, freq='D')
        data = pd.DataFrame({
            'value': np.arange(100)
        }, index=dates)
        
        dataset = TimeSeriesDataset(data, lookback=10, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsNotNone(X_train)
    
    def test_multivariate_all_nan_column(self):
        data = pd.DataFrame({
            'good': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'bad': [np.nan] * 10
        })
        preprocessor = Preprocessor(handle_missing='drop', scaler_type='none')
        processed = preprocessor.fit_transform(data)
        
        self.assertEqual(len(processed), 0)
    
    def test_target_column_with_string_on_array(self):
        data = np.arange(100).reshape(-1, 2)
        
        with self.assertRaises(ValueError):
            dataset = TimeSeriesDataset(
                data,
                lookback=5,
                horizon=1,
                target_column='column_name'
            )
            dataset.prepare()
    
    def test_target_column_out_of_range(self):
        data = pd.DataFrame({
            'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        })
        
        with self.assertRaises((ValueError, IndexError)):
            dataset = TimeSeriesDataset(
                data,
                lookback=3,
                horizon=1,
                target_column=5
            )
            dataset.prepare()
    
    def test_nonexistent_target_column_name(self):
        data = pd.DataFrame({
            'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        })
        
        with self.assertRaises(KeyError):
            dataset = TimeSeriesDataset(
                data,
                lookback=3,
                horizon=1,
                target_column='nonexistent'
            )
            dataset.prepare()
    
    def test_empty_dataframe(self):
        data = pd.DataFrame()
        
        with self.assertRaises(Exception):
            dataset = TimeSeriesDataset(data, lookback=5, horizon=1)
            dataset.prepare()
    
    def test_scaler_none(self):
        data = np.arange(50)
        dataset = TimeSeriesDataset(data, lookback=5, horizon=1, scaler_type='none')
        dataset.prepare()
        
        X_train, _ = dataset.get_train()
        
        self.assertTrue(np.any(X_train > 1))
    
    def test_get_data_before_prepare(self):
        data = np.arange(50)
        dataset = TimeSeriesDataset(data, lookback=5, horizon=1)
        
        with self.assertRaises(ValueError):
            dataset.get_train()
    
    def test_inverse_transform_without_fit(self):
        preprocessor = Preprocessor(scaler_type='minmax')
        data = np.array([[1, 2], [3, 4]])
        
        with self.assertRaises(ValueError):
            preprocessor.inverse_transform(data)
    
    def test_transform_without_fit(self):
        preprocessor = Preprocessor(scaler_type='standard')
        data = pd.DataFrame({'a': [1, 2, 3, 4, 5]})
        
        result = preprocessor.transform(data)
        
        self.assertIsNotNone(result)


class TestBoundaryConditions(unittest.TestCase):
    def test_minimum_valid_dataset(self):
        data = np.array([1, 2, 3])
        sequencer = Sequencer(lookback=1, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(len(X), 2)
        self.assertEqual(X[0, 0, 0], 1)
        self.assertEqual(y[0], 2)
        self.assertEqual(X[1, 0, 0], 2)
        self.assertEqual(y[1], 3)
    
    def test_lookback_one(self):
        data = np.arange(20)
        sequencer = Sequencer(lookback=1, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(X.shape[1], 1)
        self.assertGreater(len(X), 0)
    
    def test_horizon_one(self):
        data = np.arange(20)
        sequencer = Sequencer(lookback=5, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(len(y.shape), 2)
    
    def test_stride_equals_lookback(self):
        data = np.arange(100)
        sequencer = Sequencer(lookback=10, horizon=1, stride=10)
        X, y = sequencer.create_sequences(data)
        
        self.assertEqual(X[1, 0, 0], 10)
        self.assertEqual(X[2, 0, 0], 20)
    
    def test_exact_split_sizes(self):
        data = np.arange(100)
        dataset = TimeSeriesDataset(
            data,
            lookback=5,
            horizon=1,
            train_split=0.6,
            val_split=0.2,
            test_split=0.2
        )
        dataset.prepare()
        
        X_train, _ = dataset.get_train()
        X_val, _ = dataset.get_val()
        X_test, _ = dataset.get_test()
        
        total = len(X_train) + len(X_val) + len(X_test)
        
        self.assertAlmostEqual(len(X_train) / total, 0.6, delta=0.1)
        self.assertAlmostEqual(len(X_val) / total, 0.2, delta=0.1)
        self.assertAlmostEqual(len(X_test) / total, 0.2, delta=0.1)


class TestDataTypes(unittest.TestCase):
    def test_numpy_array_input(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsInstance(X_train, np.ndarray)
    
    def test_pandas_series_input(self):
        data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsInstance(X_train, np.ndarray)
    
    def test_pandas_dataframe_input(self):
        data = pd.DataFrame({
            'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        })
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsInstance(X_train, np.ndarray)
    
    def test_list_input_to_sequencer(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sequencer = Sequencer(lookback=3, horizon=1)
        X, y = sequencer.create_sequences(data)
        
        self.assertIsInstance(X, np.ndarray)
        self.assertIsInstance(y, np.ndarray)
    
    def test_integer_data(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=int)
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsNotNone(X_train)
    
    def test_float_data(self):
        data = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
        dataset = TimeSeriesDataset(data, lookback=3, horizon=1)
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        self.assertIsNotNone(X_train)


if __name__ == '__main__':
    unittest.main()
