# statflow Changelog

All notable changes to this project will be documented in this file.

---

## [3.5.4] - 2025-06-27

### Fixed (3.5.4)

#### **Fields/Climatology** (fixing; 3.5.4)

- Module `indicators.py`:
  - Fixed functions `calculate_CSU` and `calculate_CWD` that were calling `consec_occurrences_maxdata` with wrong parameter `max_consecutive_days=True` → changed to `calc_max_consec=True`
  - This way, runtime errors that prevented these functions from working correctly are eliminated.

### Changed (3.5.4)

#### **Fields/Climatology** (changing; 3.5.4)

- Modules `indicators.py`, `periodic_climat_stats.py`, `representative_series.py`, `simple_bias_correction.py`:
  - **Type Hint Standardisation**
    - Standardised type hints and docstrings by capitalising typing objects (e.g. `Any`, `Callable`, `Optional`)
    - Updated all `optional` parameters in docstrings to follow lowercase convention
    - Adopted Python 3.10+ union syntax (`|`) consistently across all modules

- Module `indicators.py`:
  - **Function Enhancements**: added complete type hints to all 8 climate indicator functions:
    - `calculate_WSDI`
    - `calculate_SU`
    - `calculate_CSU`
    - `calculate_FD`
    - `calculate_TN`
    - `calculate_RR`
    - `calculate_CWD`
    - `calculate_hwd`
  - **Documentation**: enhanced with NumPy-style docstrings, parameter descriptions, and practical examples

- Module `periodic_climat_stats.py`:
  - **Internal Helper Functions**: enhanced documentation for `_process_yearly_dataframe`, `_process_other_xarray`, and `_rename_xarray_dimension`
  - **Comprehensive Docstrings**: added parameter types, return documentation, and implementation notes

- Module `representative_series.py`:
  - **Complex Function Documentation**: enhanced `calculate_HDY` with ISO 15927-4:2005 standard compliance explanation, step-by-step algorithm documentation, and practical examples
  - **Interpolation Documentation**: enhanced `hdy_interpolation` with wind direction conventions, time range format specifications, polynomial guidance, and performance considerations

- Module `simple_bias_correction.py`:
  - **Internal Helper Functions**: enhanced documentation for `_unique_sorted`, `_get_delta_format`, `_get_frequency_abbreviation`, and `_rename_xarray_dimension`
  - **Complete Documentation**: added missing docstrings, practical examples, and implementation details

#### **Core** (changing; 3.5.4)

- Module `interpolation_methods.py`: add missing 'Callable' object type import

---

## [3.5.0] - 2025-06-24

### Added (3.5.0)

#### **Utils** (adding; 3.5.0)

- Module `helpers.py`: add initial docstring as a future implementation guideline of the module

### Changed (3.5.0)

#### **General** (changing; 3.5.0)

- **PEP-604 Modernisation**: comprehensive type annotation modernisation across all core and climatology modules
- Update all union type annotations from `Union[A, B]` to modern `A | B` syntax
- Modernise docstring type descriptions from `"A or B"` to `"A | B"` format throughout codebase
- Enhanced type safety with specific generic types: `list[str]`, `dict[str, float]`, `tuple[pd.DataFrame, list[int]]`
- Improved IDE support and code reliability through comprehensive type hints

- Update variable names:
  - Changes have been made in the original file `global_parameters.py` in the `paramlib` package.
  - These include abbreviation addressing.

| Module | Old variable name | New variable name |
|:------:|:-----------------:|:-----------------:|
| `fields/climatology/representative_series.py` | `COMMON_DELIM_LIST` | `COMMON_DELIMITER_LIST` |
| `fields/climatology/periodic_climat_stats.py` | `TIME_FREQUENCIES_SHORT_1` | `TIME_FREQUENCIES_ABBREVIATED` |

#### **Core Modules** (changing; 3.5.0)

- All Core Modules (`interpolation_methods.py`, `moving_operations.py`, `signal_processing.py`, `statistical_tests.py`, `time_series.py`):
  - Add comprehensive PEP-604 type annotations to all functions
  - Update parameter types with modern union syntax: `list | np.ndarray`, `str | int`, `float | None`
  - Modernise docstring syntax: `"list or numpy.ndarray"` → `"list | numpy.ndarray"`
  - Enhanced return type annotations with specific tuple types where applicable

- Notable Specifics:
  - `time_series.py`: Most extensive modernisation with 6+ functions updated
  - `statistical_tests.py`: Complex tuple return types: `tuple[float, float, str]`, `tuple[float, float, int, np.ndarray, str]`
  - `interpolation_methods.py`: Enhanced parameter types: `callable | None`, `np.ndarray | float | tuple | str`

#### **Fields/Climatology Modules** (changing; 3.5.0)

- Climate Indicator Modules (`indicators.py`, `variables.py`):
  - Add comprehensive type annotations for all climate calculation functions
  - Remove unnecessary pandas imports used only for type hints to reduce module weight
  - Modernise docstring syntax throughout with detailed parameter descriptions
  - `variables.py`: Add 6 new meteorological calculation functions with proper documentation

- Complex Analysis Modules (`periodic_climat_stats.py`, `representative_series.py`, `simple_bias_correction.py`):
  - *Complex modernisation* with extensive helper function typing
  - Update main functions with comprehensive type annotations and specific return types
  - `periodic_climat_stats.py`: Add type hints to 15+ helper functions
  - `simple_bias_correction.py`: Complete rewrite with new bias correction functions and validation
  - `representative_series.py`: Specific tuple return types for HDY calculation functions

---

## [3.4.6] - 2025-05-10

### Fixed (3.4.6)

#### **Core** (fixing; 3.4.6)

- Module `time_series.py`:
  - Function `periodic_statistics()`:
    - Fixed groupby construction for proper time frequency handling in both pandas DataFrame and xarray objects
    - Added handling for DataFrames with non-datetime columns through proper type conversion
    - Implemented NaT value filtering to prevent groupby errors
    - Added empty result handling when no valid data remains after filtering
    - Suppressed FutureWarning by explicitly setting `numeric_only=True` in statistical methods

### Changed (3.4.6)

#### **Core** (changing; 3.4.6)

- Module `time_series.py`:
  - Function `periodic_statistics()`:
    - Refactored frequency handling by combining separate mappings into a single `FREQ_MAPPING` dictionary
    - Improved code organisation and standardised frequency references throughout the module
    - Enhanced error handling with more descriptive messages

#### **Fields/Climatology** (changing; 3.4.6)

- Module `periodic_climat_stats.py`:
  - Optimised dimension check in internal function `_format_dataframe_output`: use numpy's native `ndim` attribute instead of taking the length of the shape tuple

---

## [3.4.5] - 2025-05-06

### Changed (3.4.5)

#### **Fields/Climatology** (changing; 3.4.5)

- Module `simple_bias_correction.py`:
  - Reorganised functions into clear internal and public sections
  - Improved code structure by grouping related functions
  - Implemented array uniqueness calculation with Python's built-in set, instead of `np.unique`

---

## [3.4.4] - 2025-05-05

### Fixed (3.4.4)

#### **Fields/Climatology** (fixing; 3.4.4)

- Module `representative_series.py`:
  - Resolved circular import issue by implementing lazy import of `meteorological_wind_direction` from `climalab.meteorological_variables`

---

## [3.4.3] - 2025-05-02

### Changed (3.4.3)

#### **General** (changing; 3.4.3)

- Replace the deprecated `find_time_key` function with the new `find_dt_key` function in the following modules:
  - `core/time_series.py`
  - `fields/climatology/periodic_climat_stats.py`
  - `fields/climatology/simple_bias_correction.py`

---

## [3.4.2] - 2025-04-27

### Changed (3.4.2)

#### **General** (changing; 3.4.2)

- Modify the comment header `Import custom modules` to `Import project modules` in the remaining modules having it
- Sort project modules alphabetically where necessary

---

## [3.4.1] - 2025-04-24

### Changed (3.4.1)

#### **General** (changing; 3.4.1)

- Modify the comment header `Import custom modules` to `Import project modules` in all modules having it

#### **Core** (changing; 3.4.1)

- Convert constant names to uppercase in the following modules:
  - `interpolation_methods.py`
  - `signal_processing.py`
  - `time_series.py`

#### **Fields/Climatology** (changing; 3.4.1)

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

## [3.4.0] - 2025-04-23

### Fixed (3.4.0)

#### **Core** (fixing; 3.4.0)

- Module `time_series.py`:
  - Correct non-existent module `decompose_24h_cumulative_data` to the actual `decompose_cumulative_data`

#### **Fields/Climatology** (fixing; 3.4.0)

- Module `representative_series.py`:
  - Correct non-existent module `periodic_statkit` (old name of the project) to the actual `periodic_statistics`

### Changed (3.4.0)

#### **General** (changing; 3.4.0)

- Refactored package import structure:
  - Replace direct imports with `__all__` definitions in package initiator files:
    - `statflow/__init__.py`
    - `statflow/core/__init__.py`
    - `statflow/utils/__init__.py`
  - Improved control over exported symbols when using 'from package import *'
  - Maintained consistent public API while following Python best practices

#### **Fields/Climatology** (changing; 3.4.0)

- Module `representative_series.py`:
  - Refactor import aliasing:
    - Move import aliases to separate imports
    - Remove the aliases themselves

---

## [3.3.0] - 2025-04-17

### Fixed (3.3.0)

#### **Core** (fixing; 3.3.0)

- Module `time_series.py`:
  - Correct the path for the function `find_time_key`
  - Adapt the module to use only the `find_time_key` function instead of the removed and non-existing `find_time_dimension` function

#### **Fields/Climatology** (fixing; 3.3.0)

- Modules `periodic_climat_stats.py` and `simple_bias_correction.py`:
  - Adapt the modules to use only the `find_time_key` function instead of the removed and non-existing `find_time_dimension` function

---

## [3.2.0] - 2025-04-15

### Changed (3.2.0)

#### **Fields/Climatology** (changing; 3.2.0)

- Refactored the climatology modules for improved structure and maintainability:
  - Module `periodic_climat_stats.py`:
    - Split the monolithic `climat_periodic_statistics` function into smaller, focused functions
    - Made helper functions internal by prefixing them with underscore
    - Extracted common operations into utility functions
    - Created specialised functions for different data types and time frequencies
    - Added docstrings to all functions for better documentation
  
  - Module `simple_bias_correction.py`:
    - Refactored the `calculate_and_apply_deltas` function into logical components
    - Made helper functions internal by prefixing them with underscore
    - Improved code organisation with specialised functions for different operations
    - Enhanced error handling and validation

---

## [3.1.0] - 2025-04-05

### Changed (3.1.0)

#### **General** (changing; 3.1.0)

- Improved variable naming conventions across multiple modules:
  - Renamed `arg_tuple_*` variables to `format_args_*` in `core/time_series.py`, `core/signal_processing.py`, `fields/climatology/periodic_climat_stats.py`, and `fields/climatology/simple_bias_correction.py` to better reflect their purpose in error handling and information formatting
  - This change enhances code readability and maintainability by using more descriptive variable names

#### **Fields/Climatology** (changing; 3.1.0)

- Module `simple_bias_correction.py`:
  - Enhanced `calculate_and_apply_deltas` function:
    - Added `delta_value` parameter to control formatting precision in output messages
    - Implemented support for both integer precision and "auto" scientific notation
    - Used actual delta values in output messages instead of hardcoded placeholders
    - Improved validation for the `delta_value` parameter

---

## [3.0.6] - 2025-02-03

### Changed (3.0.6)

#### **General** (changing; 3.0.6)

- Perform several term replacements in many modules:
  - `method` with `function`, if no object is instantiated throughout the module
  - `method` with `procedure` (or `algorithm`/`module`), to more accurately describe the approach or technique used in functions
  - Additionally, this change effectively communicates that a function can employ different methods or techniques to achieve its goal

---

## [3.0.0] - 2024-11-04

### Added (3.0.0)

#### **General** (adding; 3.0.0)

- Added `__init__.py` files to all first-level and deeper sub-packages for enhanced import access

### Changed (3.0.0)

#### **General** (changing; 3.0.0)

- Remove the redundant import of the deprecated and removed `parameters_and_constants` module in all affected modules

---

## [2.1.0] - Initial Release - 2024-10-28

### Added (2.1.0)

#### **Core** (adding; 2.1.0)

- Module `regressions`: methods for performing various regression analyses
- Module `interpolation_methods`: interpolation tools for numerical data
- Module `approximation_techniques`: approximation and curve-fitting methods
- Module `moving_operations`: moving average and related operations
- Module `statistical_tests`: hypothesis tests and statistical analysis tools
- Module `time_series`: comprehensive tools for time series analysis, including trend detection and seasonal decomposition
- Module `signal_processing`: filters and tools for signal analysis, including low-pass, high-pass, and band-pass filters

#### **Distributions** (adding; 2.1.0)

- Sub-package prepared for future additions of statistical distribution functions

#### **Fields/Climatology** (adding; 2.1.0)

- Sub-package `climatology`: climate data analysis tools, including periodic statistics, climate indicators, and representative series

#### **Utils** (adding; 2.1.0)

- Helper functions to support statistical computations and operations
