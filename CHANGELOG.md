# statflow changelog

All notable changes to this project will be documented in this file.

---

## [v3.4.2] - 2025-04-27

### Changed

#### **General**

- Modify the comment header `Import custom modules` to `Import project modules` in the remaining modules having it.
- Sort project modules alphabetically where necessary.

---

## [v3.4.1] - 2025-04-24

### Changed (v3.4.1)

#### **General** (v3.4.1)

- Modify the comment header `Import custom modules` to `Import project modules` in all modules having it.

#### **Core**

- Convert constant names to uppercase in the following modules:
  - `interpolation_methods.py`
  - `signal_processing.py`
  - `time_series.py`

#### **Fields/Climatology**

- Convert constant names to uppercase and improve code consistency:
  - Module `periodic_climat_stats.py`:
    - Convert all constant names to uppercase
    - Add validation for statistic parameter using `STATISTICS` constant
  - Module `simple_bias_correction.py`:
    - Add validation for statistic parameter using `STATISTICS` constant
    - Convert all constant names to uppercase
  - Module `representative_series.py`:
    - Convert constant names to uppercase
    - Use `SPLIT_DELIM` constant for time range parsing instead of hardcoded colon

---

## [v3.4.0] - 2025-04-23

### Changed (v3.4.0)

#### **General** (v3.4.0)

- Refactored package import structure:
  - Replace direct imports with `__all__` definitions in package initiator files:
    - `statflow/__init__.py`
    - `statflow/core/__init__.py`
    - `statflow/utils/__init__.py`
  - Improved control over exported symbols when using 'from package import *'
  - Maintained consistent public API while following Python best practices

#### **Core** (v3.4.0)

- Module `time_series.py`:
  - Correct non-existent module `decompose_24h_cumulative_data` to the actual `decompose_cumulative_data`

#### **Fields/Climatology** (v3.4.0)

- Module `representative_series.py`:
  - Correct non-existent module `periodic_statkit` (old name of the project) to the actual `periodic_statistics`
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
