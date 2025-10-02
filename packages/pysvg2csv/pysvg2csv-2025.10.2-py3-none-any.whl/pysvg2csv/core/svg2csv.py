#! /c/Users/amit/AppData/Local/Programs/Python/Python312/python
#! python3qgis
#! /usr/bin/env python3
#! /c/Program Files/QGIS 3.26.0/apps/Python39/python
# ==============================================================================
# File Name     : svg2csv.py
# Date Created  : 2025-09-11 00:20 UTC +02:00
# description   : Extract Nodes of SVG and save as CSV
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
# 11-Sep-2025   | AMM     | Initial Version
# --------------+---------+-----------------------------------------------------
# ==============================================================================

from pathlib import Path
import xml.etree.ElementTree as ET
# from typing import List

# Path Data Commands
# M = moveto(move from one point to another point)
# L = lineto(create a line)
# H = horizontal lineto(create a horizontal line)
# V = vertical lineto(create a vertical line)
# C = curveto(create a curve)
# S = smooth curveto(create a smooth curve)
# Q = quadratic Bézier curve(create a quadratic Bézier curve)
# T = smooth quadratic Bézier curveto(create a smooth quadratic Bézier curve)
# A = elliptical Arc(create a elliptical arc)
# Z = closepath(close the path)


def extract_node_coordinates(svg_file_path) -> list[float]:
    tree = ET.parse(svg_file_path)
    root = tree.getroot()

    # Namespace handling for Inkscape SVG files
    # You might need to adjust the namespace depending on the SVG file
    namespace = {'svg': 'http://www.w3.org/2000/svg'}

    coordinates = []
    for path in root.findall('.//svg:path', namespace):
        d_attribute = path.get('d')
        if d_attribute:
            # Parse the 'd' attribute string to extract coordinates
            # This requires more complex parsing logic to handle different SVG commands
            # For example, splitting by commands (M, L, C, Z) and then extracting numbers
            # A dedicated SVG parsing library would simplify this significantly

            # Simple example for straight lines (M, L commands)
            parts = d_attribute.split(' ')

            current_coords = []
            # for i, part in enumerate(parts):
            #     if part in ['M', 'L', 'C']:
            #         # print(part)
            #         # Assuming absolute coordinates, adjust for relative if needed
            #         x = float(parts[i+1].split(',')[0])
            #         y = float(parts[i+1].split(',')[1])
            #         current_coords.append((x, y))

            for point_str in parts:
                if ',' in point_str:
                    x_str, y_str = point_str.split(',')
                    decP: int = 3
                    x = round(float(x_str), decP)
                    y = round(float(y_str) * -1, decP)
                    current_coords.append((x, y))

            if current_coords:
                coordinates.append(current_coords)

    return coordinates


def create_latex_paths(node_coords) -> list[str]:
    latex_paths = []
    for path_coords in node_coords:
        numbers_as_strings = list(map(str, path_coords))
        latex_paths.append('\\psbezier' + ''.join(numbers_as_strings))
    return latex_paths
