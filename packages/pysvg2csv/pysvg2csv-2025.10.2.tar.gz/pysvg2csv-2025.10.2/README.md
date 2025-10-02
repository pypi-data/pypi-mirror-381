[![PyPI](https://img.shields.io/pypi/v/pysvg2csv)](https://pypi.org/project/PySvg2Csv/)&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-maroon.svg)](https://opensource.org/licenses/MIT)&nbsp;
[![Static Badge](https://img.shields.io/badge/Test-Passing-teal)](https://github.com/manthanwar/PySvg2Csv)&nbsp;

<!-- [![PyPI - Downloads](https://img.shields.io/pypi/dm/pysvg2csv)](https://pypistats.org/packages/pysvg2csv)&nbsp; -->
<!-- [![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/manthanwar/PySvg2Csv/total?logo=github)](https://github.com/manthanwar/PySvg2Csv)&nbsp; -->
<!-- [![GitHub repo size](https://img.shields.io/github/repo-size/manthanwar/PySvg2Csv?&color=purple&logo=github)](https://github.com/manthanwar/PySvg2Csv)&nbsp; -->

# PySvg2Csv

**Amit M. Manthanwar** _02 October 2025_

```sh
pip install pysvg2csv
```

## Introduction

PySvg2Csv is a package for graphic object conversion and data transformation with Python. This simple program converts graphic paths from an SVG file to a corresponding CSV data and equivalent Bézier paths used by LaTeX and PostScript.

It provides:

- a powerful data extraction and format conversion capabilities
- sophisticated (transformation) functions
- tools for integrating LaTeX, PostScript, and JavaScript  code

## Description

The `path` element is the most powerful element in the SVG library of basic shapes. It can be used to create lines, curves, arcs, and more. There are three different commands that can be used to create smooth curves. Two of those curves are Bézier curves, and the third is an "arc" or part of a circle. There are an infinite number of Bézier curves, but only two are available in `path` elements: a cubic one, called with `C`, and a quadratic one, called with `Q`. A Bézier curve is a mathematically defined, smooth curve used in computer graphics, design, and animation, determined by a set of discrete control points. These control points dictate the curve's shape, with the curve passing through the first and last points but being "pulled" toward the intermediate points. The cubic curve, C, also known as the Cubic Bézier take in two control points for each point. Therefore, to create a cubic Bézier, three sets of coordinates need to be specified. Including the starting point, there are four points for any given cubic Bézier path. The endeavor is to extract these points for every path in the SVG file and store them as CSV data and LaTeX PSTricks commands.

## Quick Start

### Example 1: file containing three curves

![Simple Curves](https://raw.githubusercontent.com/manthanwar/PySvg2Csv/refs/heads/main/data/curves.svg)


```python
from pysvg2csv import *

node_coords = extract_node_coordinates("data-svg/curves.svg")
print("Node Coordinates:", *node_coords, sep='\n')

latex_paths = create_latex_paths(node_coords)
print("LaTeX Paths:", *latex_paths, sep='\n')
```

### Example 2: file containing multiple Bézier paths

![Trident](https://raw.githubusercontent.com/manthanwar/PySvg2Csv/refs/heads/main/data/trident.svg)

```python
from pysvg2csv import *

node_coords = extract_node_coordinates("data-svg/trident.svg")
print("Node Coordinates:", *node_coords, sep='\n')

latex_paths = create_latex_paths(node_coords)
print("LaTeX Paths:", *latex_paths, sep='\n')
```

The SVG files used in the above examples are located in the project's data folder.

## Testing

PySvg2Csv requires `pytest` and `pytest-cov`.  Tests can then be run after installation with any one of the following command of your choice:

```sh
pytest
pytest --cache-clear
pytest --cov=tests
pytest --cov=tests --cov-report=html:coverage_html_report
```

## Call for Contributions

The PySvg2Csv project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions
to the source code, please contact us by emailing.
 through the [mailing
list](https://mail.python.org/archives/list/python-list@python.org/) first or join the [discussions](https://github.com/manthanwar/PySvg2Csv/discussions).

<!-- (https://mail.python.org/mailman/listinfo/PySvg2Csv-discussion) -->

Writing code isn’t the only way to contribute to PySvg2Csv. You can also:

- review pull requests
- help us stay on top of new and old issues
- develop tutorials, presentations, and other educational materials
- maintain and improve our website
- develop graphic design for our projects and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

For more information about the ways you can contribute to PySvg2CSV, visit [Contribute](CONTRIBUTING.md). If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

<!-- Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at
<PySvg2Csv-team@googlegroups.com> or on Slack (write <PySvg2Csv-team@googlegroups.com> for
an invitation). -->

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what, and how to successfully get involved.

Feel free to [ask questions](https://github.com/manthanwar/PySvg2Csv/discussions), [post issues](https://github.com/manthanwar/PySvg2Csv/issues), [submit pull request](https://github.com/manthanwar/PySvg2Csv/pulls), and [request new features](https://github.com/manthanwar/PySvg2Csv/discussions/categories/ideas).

For more information about this project and how to use this package, please check out our detailed [documentation](README.md).

## Languages we support

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)&nbsp;
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) &nbsp;
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)&nbsp;
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)&nbsp;
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)&nbsp;
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)

## Code of Conduct

PySvg2Csv is a community-driven open source project developed by a diverse group of
[contributors](CONTRIBUTING.md). The PySvg2Csv leadership has made a strong
commitment to creating an open, inclusive, and positive community. Please read the
[PySvg2Csv Code of Conduct](CODE_OF_CONDUCT.md) for guidance on how to interact with others in a way that makes our community thrive.

## Support this work

Support this project and its continued development, by sponsoring us!

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/manthanwar)
&nbsp;&nbsp;
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/manthanwar)&nbsp;&nbsp;
[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub&logoColor=#EA4AAA)](https://github.com/sponsors/manthanwar)
