# src/boxtest/plotting.py
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .stats import compare_two_groups
import warnings

def boxplot_side_by_side(
    df: pd.DataFrame,
    group_col: str,
    value_col: str,
    annotate_test: bool = True,
    ax: Optional[plt.Axes] = None,
    colors: Optional[list] = None  # Optional: user can pass colors
) -> plt.Axes:
    """
    Create a side-by-side boxplot for a two-level categorical variable.
    Annotates statistical test results if annotate_test=True.
    
    colors: list of two colors, e.g., ['#FF9999', '#9999FF'] for pastel red & blue
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6,4))
    
    if colors is None:
        colors = ['#FF9999', '#9999FF']  # default pastel colors

    # Seaborn recommends using 'hue' for palette
    # We create a copy of the group column as hue
    df['_hue'] = df[group_col]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=PendingDeprecationWarning)
        warnings.simplefilter("ignore", category=FutureWarning)
        sns.boxplot(
            x=group_col,
            y=value_col,
            hue='_hue',          # assign hue to same as group
            data=df,
            ax=ax,
            orient='vertical',
            palette=colors,
            dodge=False,         # prevents Seaborn from separating boxes by hue
            legend=False         # hide extra legend
        )

    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)

    # Annotate statistical test
    if annotate_test:
        groups = df[group_col].dropna().unique()
        if len(groups) == 2:
            a, b = groups
            x = df.loc[df[group_col] == a, value_col].dropna()
            y = df.loc[df[group_col] == b, value_col].dropna()
            res = compare_two_groups(x, y)
            p = res.get("pvalue")
            ax.set_title(f"{res['test']}, p={p:.3g}" if p is not None else res['test'])

    # Remove temporary hue column
    df.drop(columns=['_hue'], inplace=True)

    return ax
