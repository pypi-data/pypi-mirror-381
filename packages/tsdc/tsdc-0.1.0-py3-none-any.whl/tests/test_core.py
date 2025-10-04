import unittest
import numpy as np
import pandas as pd
from tsdc import TimeSeriesDataset, Sequencer, Preprocessor


class TestSequencer(unittest.TestCase):
    def setUp(self):
        self.data = np.arange(100).reshape(-1, 1)
        self.sequencer = Sequencer(lookback=10, horizon=5, stride=1)
    
    def test_create_sequences_shape(self):
        X, y = self.sequencer.create_sequences(self.data)
        
        expected_samples = (len(self.data) - 10 - 5 + 1) // 1
        
        self.assertEqual(X.shape, (expected_samples, 10, 1))
        self.assertEqual(y.shape, (expected_samples, 5, 1))
    
    def test_create_sequences_values(self):
        X, y = self.sequencer.create_sequences(self.data)
        
        np.testing.assert_array_equal(X[0].flatten(), np.arange(10))
        np.testing.assert_array_equal(y[0].flatten(), np.arange(10, 15))
    
    def test_stride(self):
        sequencer = Sequencer(lookback=5, horizon=2, stride=3)
        X, y = sequencer.create_sequences(self.data)
        
        self.assertEqual(X[1, 0, 0], 3)
        self.assertEqual(X[2, 0, 0], 6)
    
    def test_multivariate(self):
        data = np.arange(200).reshape(-1, 2)
        X, y = self.sequencer.create_sequences(data)
        
        self.assertEqual(X.shape[2], 2)
        self.assertEqual(y.shape[2], 2)
    
    def test_target_column(self):
        data = np.arange(200).reshape(-1, 2)
        X, y = self.sequencer.create_sequences(data, target_column=1)
        
        self.assertEqual(X.shape[2], 2)
        self.assertEqual(len(y.shape), 2)
        self.assertEqual(y.shape[1], 5)
    
    def test_invalid_params(self):
        with self.assertRaises(ValueError):
            Sequencer(lookback=0, horizon=1)
        
        with self.assertRaises(ValueError):
            Sequencer(lookback=1, horizon=0)
        
        with self.assertRaises(ValueError):
            Sequencer(lookback=1, horizon=1, stride=0)
    
    def test_insufficient_data(self):
        small_data = np.arange(5).reshape(-1, 1)
        
        with self.assertRaises(ValueError):
            self.sequencer.create_sequences(small_data)


class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "value1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "value2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        })
    
    def test_minmax_scaler(self):
        preprocessor = Preprocessor(scaler_type="minmax")
        scaled = preprocessor.fit_transform(self.data)
        
        self.assertTrue(np.all(scaled >= 0))
        self.assertTrue(np.all(scaled <= 1))
        
        inverse = preprocessor.inverse_transform(scaled)
        np.testing.assert_array_almost_equal(inverse, self.data.values, decimal=5)
    
    def test_standard_scaler(self):
        preprocessor = Preprocessor(scaler_type="standard")
        scaled = preprocessor.fit_transform(self.data)
        
        np.testing.assert_almost_equal(scaled.mean(axis=0), [0, 0], decimal=5)
        np.testing.assert_almost_equal(scaled.std(axis=0), [1, 1], decimal=5)
    
    def test_handle_missing(self):
        data_with_nan = self.data.copy()
        data_with_nan.loc[2, "value1"] = np.nan
        
        preprocessor = Preprocessor(handle_missing="forward_fill")
        processed = preprocessor.fit_transform(data_with_nan)
        
        self.assertFalse(np.any(np.isnan(processed)))
    
    def test_remove_outliers(self):
        data_with_outlier = self.data.copy()
        data_with_outlier.loc[5, "value1"] = 1000
        
        preprocessor = Preprocessor(remove_outliers=True, outlier_threshold=2.0)
        processed = preprocessor.fit_transform(data_with_outlier)
        
        self.assertLess(len(processed), len(data_with_outlier))
    
    def test_3d_inverse_transform(self):
        preprocessor = Preprocessor(scaler_type="minmax")
        preprocessor.fit(self.data)
        
        data_3d = np.random.randn(10, 5, 2)
        scaled_3d = preprocessor.transform(data_3d.reshape(-1, 2))
        scaled_3d = scaled_3d.reshape(10, 5, 2)
        
        inverse = preprocessor.inverse_transform(scaled_3d)
        
        self.assertEqual(inverse.shape, (10, 5, 2))


class TestTimeSeriesDataset(unittest.TestCase):
    def setUp(self):
        self.data = np.sin(np.linspace(0, 20, 500)) + np.random.normal(0, 0.1, 500)
    
    def test_basic_creation(self):
        dataset = TimeSeriesDataset(
            data=self.data,
            lookback=20,
            horizon=5,
            stride=1
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        X_val, y_val = dataset.get_val()
        X_test, y_test = dataset.get_test()
        
        self.assertIsNotNone(X_train)
        self.assertIsNotNone(y_train)
        self.assertIsNotNone(X_val)
        self.assertIsNotNone(y_val)
        self.assertIsNotNone(X_test)
        self.assertIsNotNone(y_test)
        
        total_samples = len(X_train) + len(X_val) + len(X_test)
        expected_samples = (len(self.data) - 20 - 5 + 1) // 1
        
        self.assertEqual(total_samples, expected_samples)
    
    def test_splits(self):
        dataset = TimeSeriesDataset(
            data=self.data,
            lookback=10,
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
        
        train_ratio = len(X_train) / total
        val_ratio = len(X_val) / total
        test_ratio = len(X_test) / total
        
        self.assertAlmostEqual(train_ratio, 0.6, delta=0.05)
        self.assertAlmostEqual(val_ratio, 0.2, delta=0.05)
        self.assertAlmostEqual(test_ratio, 0.2, delta=0.05)
    
    def test_multivariate_with_target(self):
        data = pd.DataFrame({
            "feature1": np.random.randn(100),
            "feature2": np.random.randn(100),
            "target": np.random.randn(100)
        })
        
        dataset = TimeSeriesDataset(
            data=data,
            lookback=10,
            horizon=3,
            target_column="target"
        )
        
        dataset.prepare()
        
        X_train, y_train = dataset.get_train()
        
        self.assertEqual(X_train.shape[2], 3)
        self.assertEqual(len(y_train.shape), 2)
        self.assertEqual(y_train.shape[1], 3)
    
    def test_no_preprocessing(self):
        dataset = TimeSeriesDataset(
            data=self.data,
            lookback=10,
            horizon=1
        )
        
        dataset.prepare(preprocess=False)
        
        X_train, _ = dataset.get_train()
        
        original_min = self.data.min()
        original_max = self.data.max()
        
        train_min = X_train.min()
        train_max = X_train.max()
        
        self.assertAlmostEqual(original_min, train_min, delta=0.1)
        self.assertAlmostEqual(original_max, train_max, delta=0.1)
    
    def test_get_info(self):
        dataset = TimeSeriesDataset(
            data=self.data,
            lookback=15,
            horizon=3
        )
        
        dataset.prepare()
        
        info = dataset.get_info()
        
        self.assertEqual(info["lookback"], 15)
        self.assertEqual(info["horizon"], 3)
        self.assertTrue(info["is_prepared"])
        self.assertIn("shapes", info)
    
    def test_invalid_splits(self):
        with self.assertRaises(ValueError):
            TimeSeriesDataset(
                data=self.data,
                train_split=0.5,
                val_split=0.3,
                test_split=0.3
            )


class TestValidators(unittest.TestCase):
    def test_validate_sequence_params(self):
        from tsdc.utils.validators import validate_sequence_params
        
        self.assertTrue(validate_sequence_params(100, 10, 5, 1))
        
        with self.assertRaises(ValueError):
            validate_sequence_params(10, 0, 5, 1)
        
        with self.assertRaises(ValueError):
            validate_sequence_params(10, 10, 5, 1)
    
    def test_validate_splits(self):
        from tsdc.utils.validators import validate_splits
        
        self.assertTrue(validate_splits(0.7, 0.2, 0.1))
        
        with self.assertRaises(ValueError):
            validate_splits(0.5, 0.3, 0.3)
        
        with self.assertRaises(ValueError):
            validate_splits(1.1, 0, 0)


class TestSplitters(unittest.TestCase):
    def test_time_series_split(self):
        from tsdc.utils.splitters import time_series_split
        
        X = np.arange(100).reshape(-1, 1)
        y = np.arange(100)
        
        (X_train, y_train), (X_val, y_val), (X_test, y_test) = time_series_split(
            X, y, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15
        )
        
        self.assertEqual(len(X_train), 70)
        self.assertEqual(len(X_val), 15)
        self.assertEqual(len(X_test), 15)
        
        self.assertTrue(np.all(X_train < X_val[0]))
        self.assertTrue(np.all(X_val < X_test[0]))
    
    def test_walk_forward_validation(self):
        from tsdc.utils.splitters import walk_forward_validation
        
        X = np.arange(100).reshape(-1, 1)
        y = np.arange(100)
        
        splits = list(walk_forward_validation(X, y, n_splits=3))
        
        self.assertEqual(len(splits), 3)
        
        for X_train, y_train, X_test, y_test in splits:
            self.assertTrue(len(X_train) > 0)
            self.assertTrue(len(X_test) > 0)
            self.assertTrue(np.all(X_train < X_test[0]))


if __name__ == "__main__":
    unittest.main()
