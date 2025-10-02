# plotting_utils

A Python package providing elegant wrappers around matplotlib and seaborn functions to make scientific plotting easier and more consistent.

## Features

### 🎨 Color Palettes
- **Custom color schemes**: `ten_godisnot`, `darjeeling`, `fantastic_fox`
- **Palette creation utilities**: `create_palette()` for generating custom color schemes

### 📊 Plotting Functions
High-level plotting functions with sensible defaults:
- **Basic plots**: `scatter()`, `bar()`, `box()`, `strip()`, `violin()`
- **Distribution plots**: `dist()`, `counts_plot()`
- **Specialized plots**: `heatmap()`, `dotplot()`, `volcano()`, `stem_plot()`, `rank_plot()`
- **Statistical plots**: Built-in support for statistical annotations with `add_wilcox()`

### 🛠 Utility Functions
- **Styling**: `set_rcParams()` for Nature journal-style settings
- **Plot enhancement**: `format_ax()`, `add_legend()`, `add_cbar()`
- **File operations**: `save_best_pdf_quality()`, `make_folder()`
- **Performance**: `Timer` class for benchmarking

## Installation

```bash
pip install plotting_utils
```

## Quick Start

```python
import plotting_utils as plu
import matplotlib.pyplot as plt
import pandas as pd

# Set journal-style parameters
plu.set_rcParams()

# Create a scatter plot with custom styling
fig, ax = plt.subplots(figsize=(6, 4))
plu.scatter(x, y, c=plu.darjeeling[0], ax=ax)
plu.format_ax(ax, xlabel='X values', ylabel='Y values')

# Save with best quality
plu.save_best_pdf_quality(fig, 'my_plot.pdf')
```

## Dependencies

- matplotlib
- seaborn  
- statannotations
- textalloc
- joblib
- scikit-learn

## Release History

### 0.1.4 (2025-09-11)
- Enhanced README with comprehensive documentation
- Added proper package metadata (long_description, author, classifiers)
- Improved PyPI package presentation

### 0.1.3
- Previous stable release

## License

See LICENSE file for details.

## Version

Current version: 0.1.4
