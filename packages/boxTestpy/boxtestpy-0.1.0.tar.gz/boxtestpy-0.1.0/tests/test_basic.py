import pandas as pd
from boxtestpy import compare_two_groups, boxplot_side_by_side

def test_compare_two_groups_small():
    a = [1,2,3,4,5]
    b = [2,3,4,5,6]
    res = compare_two_groups(a,b)
    assert "pvalue" in res

def test_plot_runs(tmp_path):
    df = pd.DataFrame({"group": ["A"]*5 + ["B"]*5, "value": list(range(10))})
    ax = boxplot_side_by_side(df, "group", "value")
    fig = ax.get_figure()
    out = tmp_path / "plot.png"
    fig.savefig(out)
    assert out.exists()
