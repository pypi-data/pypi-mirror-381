# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-10-03

### Added
- Initial release of TSDC
- Core `TimeSeriesDataset` class for automatic dataset creation
- `Sequencer` class for sliding window operations
- `Preprocessor` class with multiple scaling methods
- `FinancialLoader` for loading financial data from Yahoo Finance
- Support for univariate and multivariate time series
- Target column selection for multivariate inputs
- Walk-forward validation utilities
- Expanding and sliding window split methods
- Missing value handling (forward fill, backward fill, interpolate)
- Outlier detection and removal
- Inverse transform for predictions
- Comprehensive test suite
- Documentation and examples
- Bitcoin prediction example with LSTM
- Basic usage examples

### Features
- Support for numpy arrays, pandas DataFrames, and Series
- Multiple scaling options (MinMax, Standard, Robust)
- Proper temporal train/val/test splitting
- Configurable lookback, horizon, and stride parameters
- Technical indicators for financial data (SMA, EMA, RSI, MACD)
- Data validation utilities

### Documentation
- Comprehensive README with examples
- API reference documentation
- Contributing guidelines
- MIT License

## [Unreleased]

### Planned
- PyTorch DataLoader integration
- Additional data loaders (crypto APIs, weather data)
- Data augmentation techniques
- Irregular time series support
- Built-in visualization tools
- Automated hyperparameter tuning
- More preprocessing options
- GPU acceleration support
