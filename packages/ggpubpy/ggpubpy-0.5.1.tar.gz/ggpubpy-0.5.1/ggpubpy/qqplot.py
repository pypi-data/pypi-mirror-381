import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from typing import Tuple, Optional


def _ppoints(n: int) -> np.ndarray:
    """Return plotting positions (i - 0.5) / n for i in 1..n."""
    if n <= 0:
        return np.array([])
    return (np.arange(1, n + 1) - 0.5) / float(n)


def _ensure_distribution(dist: "str | object"):
    return getattr(stats, dist) if isinstance(dist, str) else dist


def _clean_sample(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    return x[~np.isnan(x)]


def _validate_sparams(dist, sparams) -> Tuple[tuple, int]:
    if not isinstance(sparams, (tuple, list)):
        sparams = (sparams,)
    if len(sparams) < dist.numargs:
        raise ValueError(
            "Missing required shape parameters for distribution %s. See scipy.stats.%s." % (
                dist.shapes,
                dist.name,
            )
        )
    return tuple(sparams), dist.numargs


def _compute_quantiles(x: np.ndarray, dist, sparams: tuple) -> Tuple[np.ndarray, np.ndarray, Tuple]:
    theor, observed = stats.probplot(x, sparams=sparams, dist=dist, fit=False)
    fit_params = dist.fit(x)
    loc, scale = fit_params[-2], fit_params[-1]
    shape = fit_params[:-2] if len(fit_params) > 2 else None
    if loc != 0 and scale != 1:
        observed = (np.sort(observed) - loc) / scale
    return theor, observed, (shape, loc, scale)


def _fit_regression(x: np.ndarray, y: np.ndarray) -> Tuple[float, float, float]:
    slope, intercept, r, _, _ = stats.linregress(x, y)
    return slope, intercept, r**2


def _confidence_envelope(
    theor: np.ndarray,
    slope: float,
    dist,
    shape: Optional[tuple],
    n: int,
    confidence: float,
) -> Tuple[np.ndarray, np.ndarray]:
    P = _ppoints(n)
    crit = stats.norm.ppf(1 - (1 - confidence) / 2)
    pdf = dist.pdf(theor) if shape in (None, ()) else dist.pdf(theor, *shape)
    se = (slope / pdf) * np.sqrt(P * (1 - P) / n)
    return crit * se, -crit * se


def qqplot(
    x,
    dist: "str | object" = "norm",
    sparams=(),
    confidence: "float | bool" = 0.95,
    square: bool = True,
    ax=None,
    **kwargs,
):
    """Create a Q–Q plot with optional confidence envelope and regression line.

    Parameters are consistent with scipy-based Q–Q plots. Returns the Matplotlib Axes.
    """
    scatter_kwargs = {"marker": "o", "color": "blue"}
    scatter_kwargs.update(kwargs)

    dist = _ensure_distribution(dist)
    x = _clean_sample(x)
    sparams, _ = _validate_sparams(dist, sparams)

    theor, observed, (shape, _, _) = _compute_quantiles(x, dist, sparams)
    slope, intercept, r2 = _fit_regression(theor, observed)

    if ax is None:
        ax = plt.gca()

    ax.scatter(theor, observed, **scatter_kwargs)
    ax.set_xlabel("Theoretical quantiles")
    ax.set_ylabel("Ordered quantiles")

    # 45-degree line bounds
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    low = min(xlim[0], ylim[0])
    high = max(xlim[1], ylim[1])
    ax.plot([low, high], [low, high], color="slategrey", lw=1.5)
    ax.set_xlim((low, high))
    ax.set_ylim((low, high))

    # Regression line and R^2
    fit_val = slope * theor + intercept
    ax.plot(theor, fit_val, "r-", lw=2)
    posx = low + 0.60 * (high - low)
    posy = low + 0.10 * (high - low)
    ax.text(posx, posy, f"$R^2={r2:.3f}$")

    if confidence is not False:
        conf = float(confidence)
        delta_up, delta_low = _confidence_envelope(theor, slope, dist, shape, x.size, conf)
        upper = fit_val + delta_up
        lower = fit_val + delta_low
        ax.plot(theor, upper, "r--", lw=1.25)
        ax.plot(theor, lower, "r--", lw=1.25)

    if square:
        ax.set_aspect("equal")

    return ax
