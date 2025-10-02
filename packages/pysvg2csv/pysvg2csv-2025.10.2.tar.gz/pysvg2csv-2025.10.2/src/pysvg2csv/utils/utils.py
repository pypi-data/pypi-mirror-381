#! python3qgis
#! /c/Users/amit/AppData/Local/Programs/Python/Python312/python
#! /usr/bin/env python3
#! /c/Program Files/QGIS 3.26.0/apps/Python39/python
# ==============================================================================
# File Name     : utils.py
# Date Created  : 2025-09-23 23:50 UTC +02:00
# description   : Utility Functions
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

import os
import shutil
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def clear_pycache(directory) -> None:
    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
            print(f"Removed __pycache__ in: {root}")
