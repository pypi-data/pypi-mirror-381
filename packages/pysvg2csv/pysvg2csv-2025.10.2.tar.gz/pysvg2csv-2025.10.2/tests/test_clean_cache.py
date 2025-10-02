#! /c/Users/amit/AppData/Local/Programs/Python/Python312/python
#! /usr/bin/env python3
# ==============================================================================
# File Name     : clean_cache.py
# Date Created  : 2025-09-23 22:55 UTC +02:00
# description   : clean cache files and folers
# ------------------------------------------------------------------------------
# Author        : Amit Manohar Manthanwar
# Mailer        : manthanwar@hotmail.com
# WebURL        : https:#manthanwar.github.io
# ------------------------------------------------------------------------------
# Copyright     : (c) 2025 Amit Manohar Manthanwar
# License       : LICENSE.md
# ==============================================================================
# Revision Log  | Author  | Description
# --------------+---------+-----------------------------------------------------
# 23-Sep-2025   | AMM     | Initial Version
# --------------+---------+-----------------------------------------------------
# ==============================================================================

from pysvg2csv.utils import *

# clear_pycache(".")


def test_clear_pycache() -> None:
    result = clear_pycache(".")
    assert result is None
