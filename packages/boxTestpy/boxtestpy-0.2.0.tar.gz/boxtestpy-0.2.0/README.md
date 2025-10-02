
# boxTestpy

**boxTestpy** is a beginner-friendly Python package for creating **side-by-side boxplots** and performing basic **two-sample statistical tests** (t-test or Mann–Whitney U test) with publication-ready plots. It simplifies data visualization and statistical analysis for beginners and researchers.

---

## Features

* Side-by-side boxplots for a two-level categorical variable
* Normality check using **Shapiro–Wilk test**
* Automatic selection of **independent t-test** or **Mann–Whitney U test**
* Pastel color palette for clean plots
* Optional statistical annotation on plots
* Works with **pandas DataFrames**

---

## Installation

```bash
pip install boxTestpy
```

For plotting support:

```bash
pip install matplotlib seaborn pandas
```

---

## Quick Start

```python
import pandas as pd
import matplotlib.pyplot as plt
import boxtestpy as btp

# Public health dataset: Blood Pressure (systolic)
data = {
    "group": ["Control"]*10 + ["Treatment"]*10,
    "blood_pressure": [
        120, 122, 118, 121, 119, 123, 117, 124, 120, 122,   # Control group
        115, 118, 116, 117, 119, 114, 116, 118, 117, 115    # Treatment group
    ]
}

df = pd.DataFrame(data)

# Side-by-side boxplot with statistical annotation
ax = btp.boxplot_side_by_side(df, group_col="group", value_col="blood_pressure")
plt.show()

# Statistical test
x = df[df["group"] == "Control"]["blood_pressure"]
y = df[df["group"] == "Treatment"]["blood_pressure"]
result = btp.compare_two_groups(x, y)
print("Statistical Test Results:", result)

# Custom pastel colors (optional)
colors = ["#f0106dff", "#adf010ff"]  # pastel red and blue

ax = btp.boxplot_side_by_side(
    df,
    group_col="group",
    value_col="blood_pressure",
    colors=colors
)
plt.show()

```
---

## Functions

### `boxplot_side_by_side(df, group_col, value_col)`

* Creates a side-by-side boxplot for a two-level categorical variable.
* Automatically shows a pastel-colored plot with optional statistical annotation.

### `compare_two_groups(x, y)`

* Performs Shapiro–Wilk normality tests on both groups.
* Runs **t-test** if both groups are normal, or **Mann–Whitney U test** if not.
* Returns a dictionary with test names and p-values.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions, bug reports, and feature requests are welcome. Open an issue or pull request on GitHub.

---

## Contributors

- Arkaprabha Sau (Author, Creator, Maintainer)  
- Santanu Phadikar (Contributor)  
- Ishita Bhakta (Contributor)
