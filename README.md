# statkit

**statkit** is a Python library offering a robust toolkit for statistical analysis and data manipulation. With modules covering essential techniques like regression, interpolation, signal processing, and climatology, StatKit is designed to streamline statistical workflows across diverse fields.

## Features

- **Core Statistical Methods**:
  - Modules for regression, moving averages, and statistical testing.
- **Time Series Analysis**:
  - Specialized methods for analyzing time-dependent data.
- **Signal Processing**:
  - Functions for signal filtering, interpolation, and approximation.
- **Climatology Tools**:
  - Methods tailored to climate data, including periodic statistics, representative series calculation, and bias correction.

---

## Installation Guide

### Dependency Notice
Before installing, please ensure the following dependencies are available on your system:

- **Required Third-Party Libraries**: common dependencies include the latest versions of the following:
  * numpy
  * pandas
  * scikit-learn
  * scipy

  - You can install them via pip:
    ```bash
    pip3 install numpy pandas scikit-learn scipy
    ```
    
  - Alternatively, you can install them via Anaconda. Currenlty, the recommended channel from where to install for best practices is `conda-forge`:
    ```bash
    conda install -c conda-forge numpy pandas scikit-learn scipy
    ```

- **Other Internal Packages**: these are other packages created by the same author. To install them as well as the required third-party packages, refer to the README.md document of the corresponding package:
  * climalab
  * filewise
  * paramlib
  * pygenutils

**Note**: In the future, this package will be available via PyPI and Anaconda, where dependencies will be handled automatically.

### Unconventional Installation Instructions

Until this package is available on PyPI or Anaconda, please follow these steps:

1. **Clone the Repository**: Download the repository to your local machine by running:
   ```bash
   git clone https://github.com/EusDancerDev/statkit.git
   ```

2. **Check the Latest Version**: Open the `CHANGELOG.md` file in the repository to see the latest version information.

3. **Build the Package**: Navigate to the repository directory and run:
   ```bash
   python setup.py sdist
   ```
   This will create a `dist/` directory containing the package tarball.

4. **Install the Package**:
   - Navigate to the `dist/` directory.
   - Run the following command to install the package:
     ```bash
     pip3 install statkit-<latest_version>.tar.gz
     ```
     Replace `<latest_version>` with the version number from `CHANGELOG.md`.

**Note**: Once available on PyPI and Anaconda, installation will be simpler and more conventional.

---

### Package Updates

To stay up-to-date with the latest version of this package, follow these steps:

1. **Check the Latest Version**: Open the `CHANGELOG.md` file in this repository to see if a new version has been released.

2. **Pull the Latest Version**:
   - Navigate to the directory where you initially cloned the repository.
   - Run the following command to update your local copy:
     ```bash
     git pull origin main
     ```

This will download the latest changes from the main branch of the repository. After updating, you may need to rebuild and reinstall the package as described in the [Installation Guide](#installation-guide) above.