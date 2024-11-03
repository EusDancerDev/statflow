# statkit changelog

All notable changes to this project will be documented in this file.

## [v3.2.0] - 2024-11-03

### Added

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules.

---

## [v2.1.0] - Initial Release - 2024-10-28

### Added

- The following **sub-packages** and `modules` were added:

- **core** 
	- `regressions`: methods for performing various regression analyses
	- `interpolation_methods`: interpolation tools for numerical data
	- `approximation_techniques`: approximation and curve-fitting methods
	- `moving_operations`: moving average and related operations
	- `statistical_tests`: hypothesis tests and statistical analysis tools
	- `time_series`: comprehensive tools for time series analysis, including trend detection and seasonal decomposition
	- `signal_processing`: filters and tools for signal analysis, including low-pass, high-pass, and band-pass filters
- **distributions**
	- Sub-package prepared for future additions of statistical distribution functions
- **fields**
	- `climatology`: climate data analysis tools, including periodic statistics, climate indicators, and representative series
- **utils**: helper functions to support statistical computations and operations
