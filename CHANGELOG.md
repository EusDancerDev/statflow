# statkit changelog

All notable changes to this project will be documented in this file.

---

## [v3.1.0] - 2025-04-05

### Changed

#### **General**

- Improved variable naming conventions across multiple modules:
  - Renamed `arg_tuple_*` variables to `format_args_*` in `core/time_series.py`, `core/signal_processing.py`, `fields/climatology/periodic_climat_stats.py`, and `fields/climatology/simple_bias_correction.py` to better reflect their purpose in error handling and information formatting.
  - This change enhances code readability and maintainability by using more descriptive variable names.

#### **Fields/Climatology**

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
