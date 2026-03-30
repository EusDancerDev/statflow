#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optional dependency bootstrap for climatology modules that need xarray and climarraykit.

Core ``statflow`` installs avoid these; install the climate extra:

    pip install 'statflow[climate]'
"""

_INSTALL_MSG = (
    "Climatology helpers that use xarray or climarraykit require optional "
    "dependencies. Install them with: pip install 'statflow[climate]'"
)

try:
    import xarray as xr
except ImportError as exc:
    raise ImportError(_INSTALL_MSG) from exc

try:
    from climarraykit.patterns import rename_xarray_dimension
except ImportError as exc:
    raise ImportError(_INSTALL_MSG) from exc

__all__ = ["rename_xarray_dimension", "xr"]
