# src/boxtest/stats.py
from typing import Dict, Any
import numpy as np
from scipy import stats

def check_normality(arr: np.ndarray, alpha: float = 0.05) -> Dict[str, Any]:
    arr = np.asarray(arr, dtype=float)
    if arr.size < 3:
        return {"test": "shapiro", "statistic": None, "pvalue": None, "is_normal": False}
    stat, p = stats.shapiro(arr)
    return {"test": "shapiro", "statistic": float(stat), "pvalue": float(p), "is_normal": bool(p > alpha)}

def cohen_d(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    nx, ny = x.size, y.size
    sx = x.var(ddof=1); sy = y.var(ddof=1)
    pooled_sd = (( (nx-1)*sx + (ny-1)*sy ) / (nx+ny-2)) ** 0.5
    return float((x.mean() - y.mean()) / pooled_sd)

def compare_two_groups(x, y, alpha: float = 0.05) -> Dict[str, Any]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n1 = check_normality(x, alpha)
    n2 = check_normality(y, alpha)

    if n1["is_normal"] and n2["is_normal"]:
        lev_s, lev_p = stats.levene(x, y)
        equal_var = bool(lev_p > alpha)
        tstat, p = stats.ttest_ind(x, y, equal_var=equal_var)
        return {
            "test": "t-test",
            "statistic": float(tstat),
            "pvalue": float(p),
            "equal_var": equal_var,
            "effect_size_cohen_d": cohen_d(x, y),
            "normality": (n1, n2),
            "levene": {"statistic": float(lev_s), "pvalue": float(lev_p)},
        }
    else:
        ustat, p = stats.mannwhitneyu(x, y, alternative="two-sided")
        return {
            "test": "mannwhitneyu",
            "statistic": float(ustat),
            "pvalue": float(p),
            "normality": (n1, n2),
        }
