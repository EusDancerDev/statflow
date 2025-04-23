# statkit changelog

All notable changes to this project will be documented in this file.

---

## [v3.4.0] - 2025-04-23

### Changed (v3.4.0)

#### **General**

- Refactored package import structure:
  - Replace direct imports with `__all__` definitions in package initiator files
  - Improved control over exported symbols in `statkit/__init__.py`, `statkit/core/__init__.py` and `statkit/utils/__init__.py`
  - Maintain consistent public API while following Python best practices

#### **Core**

- Module `time_series.py`:
  - Correct non-existent module `decompose_24h_cumulative_data` to the actual `decompose_cumulative_data`

#### **Fields/Climatology**

- Module `representative_series.py`:
  - Correct non-existent module `periodic_statkit` to the actual `periodic_statistics`
  - Refactor import aliasing:
    - Move import aliases to separate imports
    - Remove the aliases themselves

---

## [v3.3.0] - 2025-04-17

### Changed (v3.3.0)

#### **Core** (v3.3.0)

- Module `time_series.py`:
  - Correct the path for the function `find_time_key`.
  - Adapt the module to use only the `find_time_key` function instead of the removed and non-existing `find_time_dimension` function, as the former `find_time_key` and already supports the following top-level objects:
  - pandas.DataFrame
  - xarray.Dataset
  - xarray.DataArray

#### **Fields/Climatology** (v3.3.0)

- Modules `periodic_climat_stats.py` and `simple_bias_correction.py`:
  - Adapt the modules to use only the `find_time_key` function instead of the removed and non-existing `find_time_dimension` function, as the former `find_time_key` and already supports the following top-level objects:
    - pandas.DataFrame
    - xarray.Dataset
    - xarray.DataArray
  
---

## [v3.2.0] - 2025-04-15

### Changed (v3.2.0)

#### **Fields/Climatology** (v3.2.0)

- Refactored the climatology modules for improved structure and maintainability:
  - Module `periodic_climat_stats.py`:
    - Split the monolithic `climat_periodic_statistics` function into smaller, focused functions
    - Made helper functions internal by prefixing them with underscore
    - Extracted common operations into utility functions
    - Created specialized functions for different data types and time frequencies
    - Added docstrings to all functions for better documentation
  
  - Module `simple_bias_correction.py`:
    - Refactored the `calculate_and_apply_deltas` function into logical components
    - Made helper functions internal by prefixing them with underscore
    - Improved code organization with specialized functions for different operations
    - Enhanced error handling and validation

---

## [v3.1.0] - 2025-04-05

### Changed (v3.1.0)

#### **General** (v3.1.0)

- Improved variable naming conventions across multiple modules:
  - Renamed `arg_tuple_*` variables to `format_args_*` in `core/time_series.py`, `core/signal_processing.py`, `fields/climatology/periodic_climat_stats.py`, and `fields/climatology/simple_bias_correction.py` to better reflect their purpose in error handling and information formatting.
  - This change enhances code readability and maintainability by using more descriptive variable names.

#### **Fields/Climatology** (v3.1.0)

- Module `simple_bias_correction.py`:
  - Enhanced `calculate_and_apply_deltas` function:
    - Added `delta_value` parameter to control formatting precision in output messages
  - Implemented support for both integer precision and "auto" scientific notation
  - Used actual delta values in output messages instead of hardcoded placeholders
  - Improved validation for the `delta_value` parameter.
  
---

## [v3.0.6] - 2025-02-03

### Changed (v3.0.6)

#### **General** (v3.0.6)

- Peform several term replacements in many modules:
  - `method` with `function`, if no object is instantiated throughout the module.
  - `method` with `procedure` (or `algorithm`/`module`), to more accurately describe the approach or technique used in functions.
  Additionally, this change effectively communicates that a function can employ different methods or techniques to achieve its goal.

---

## [v3.0.0] - 2024-11-04

### Added (v3.0.6)

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed (v3.0.0)

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules.

---

## [v2.1.0] - Initial Release - 2024-10-28

### Added (v2.1.0)

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
