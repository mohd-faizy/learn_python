# autoedapkd

[![PyPI version](https://img.shields.io/pypi/v/autoedapkd.svg)](https://pypi.org/project/autoedapkd/)
[![Python versions](https://img.shields.io/pypi/pyversions/autoedapkd.svg)](https://pypi.org/project/autoedapkd/)

An Automated Exploratory Data Analysis (EDA) Tool.

You can view the package directly on **[PyPI: autoedapkd](https://pypi.org/project/autoedapkd/)**.

## Features

- **Dataset Info & Structure**: Summarizes rows, columns, and data types.
- **Missing Value Report**: Automatically identifies columns with null/missing values.
- **Descriptive Statistics**: Displays transpositions of standard summary stats for both numerical and categorical features.
- **Visualizations**: 
  - Correlation heatmaps for numerical fields.
  - Distribution plots (histograms with KDEs).
  - Outlier detection (box plots).
  - Categorical frequency plots.

## Installation

Install using `pip`:

```bash
pip install autoedapkd
```

Or using `uv`:

```bash
uv add autoedapkd
```

## Quick Start

### Python API

```python
import pandas as pd
from autoedapkd import perform_eda

# Load your dataset
df = pd.read_csv("your_data.csv")

# Perform automated analysis
perform_eda(df)
```

### CLI Command

Once installed, you can also run the analysis directly from the command line:

```bash
autoeda your_data.csv
```
