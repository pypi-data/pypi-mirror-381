import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from scipy import stats
import pandas as pd
from typing import Tuple


def _validate_inputs(x, y, xaxis: str) -> Tuple[np.ndarray, np.ndarray, str, str]:
    assert xaxis in ["mean", "x", "y"]
    xname = x.name if isinstance(x, pd.Series) else "x"
    yname = y.name if isinstance(y, pd.Series) else "y"
    x = np.asarray(x)
    y = np.asarray(y)
    assert x.ndim == 1 and y.ndim == 1
    assert x.size == y.size
    assert not np.isnan(x).any(), "Missing values in x or y are not supported."
    assert not np.isnan(y).any(), "Missing values in x or y are not supported."
    return x, y, xname, yname


def _compute_stats(x: np.ndarray, y: np.ndarray, agreement: float):
    diff = x - y
    n = diff.size
    dof = n - 1
    mean_diff = float(np.mean(diff))
    std_diff = float(np.std(diff, ddof=1))
    mean_diff_se = float(np.sqrt(std_diff**2 / n))
    high = mean_diff + agreement * std_diff
    low = mean_diff - agreement * std_diff
    high_low_se = float(np.sqrt(3 * std_diff**2 / n))
    return diff, dof, mean_diff, std_diff, mean_diff_se, high, low, high_low_se


def _x_values(x: np.ndarray, y: np.ndarray, xaxis: str, xname: str, yname: str):
    if xaxis == "mean":
        xval = np.vstack((x, y)).mean(0)
        xlabel = f"Mean of {xname} and {yname}"
    elif xaxis == "x":
        xval = x
        xlabel = xname
    else:
        xval = y
        xlabel = yname
    return xval, xlabel


def _annotate(ax, mean_diff: float, high: float, low: float, agreement: float):
    loa_range = high - low
    offset = (loa_range / 100.0) * 1.5
    trans = transforms.blended_transform_factory(ax.transAxes, ax.transData)
    xloc = 0.98
    ax.text(xloc, mean_diff + offset, "Mean", ha="right", va="bottom", transform=trans)
    ax.text(xloc, mean_diff - offset, f"{mean_diff:.2f}", ha="right", va="top", transform=trans)
    ax.text(xloc, high + offset, f"+{agreement:.2f} SD", ha="right", va="bottom", transform=trans)
    ax.text(xloc, high - offset, f"{high:.2f}", ha="right", va="top", transform=trans)
    ax.text(xloc, low - offset, f"-{agreement:.2f} SD", ha="right", va="top", transform=trans)
    ax.text(xloc, low + offset, f"{low:.2f}", ha="right", va="bottom", transform=trans)


def plot_blandaltman(
    x,
    y,
    agreement: float = 1.96,
    xaxis: str = "mean",
    confidence: float = 0.95,
    annotate: bool = True,
    ax=None,
    **kwargs,
):
    """Create a Bland–Altman agreement plot between two measurements.

    Returns the Matplotlib Axes for further customization.
    """
    x, y, xname, yname = _validate_inputs(x, y, xaxis)

    scatter_kwargs = {"color": "tab:blue", "alpha": 0.8}
    scatter_kwargs.update(kwargs)

    (
        diff,
        dof,
        mean_diff,
        std_diff,
        mean_diff_se,
        high,
        low,
        high_low_se,
    ) = _compute_stats(x, y, agreement)

    xval, xlabel = _x_values(x, y, xaxis, xname, yname)

    if ax is None:
        ax = plt.gca()

    ax.scatter(xval, diff, **scatter_kwargs)
    ax.axhline(mean_diff, color="k", linestyle="-", lw=2)
    ax.axhline(high, color="k", linestyle=":", lw=1.5)
    ax.axhline(low, color="k", linestyle=":", lw=1.5)

    if annotate:
        _annotate(ax, mean_diff, high, low, agreement)

    if confidence is not None:
        assert 0 < confidence < 1
        ci_mean = stats.t.interval(confidence, dof, loc=mean_diff, scale=mean_diff_se)
        ci_high = stats.t.interval(confidence, dof, loc=high, scale=high_low_se)
        ci_low = stats.t.interval(confidence, dof, loc=low, scale=high_low_se)
        ax.axhspan(ci_mean[0], ci_mean[1], facecolor="tab:grey", alpha=0.2)
        ax.axhspan(ci_high[0], ci_high[1], facecolor=scatter_kwargs["color"], alpha=0.2)
        ax.axhspan(ci_low[0], ci_low[1], facecolor=scatter_kwargs["color"], alpha=0.2)

    ax.set_ylabel(f"{xname} - {yname}")
    ax.set_xlabel(xlabel)
    return ax

