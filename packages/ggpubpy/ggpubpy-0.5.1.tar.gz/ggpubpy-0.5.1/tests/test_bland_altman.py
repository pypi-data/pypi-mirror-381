import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from ggpubpy import plot_blandaltman


def test_bland_altman_basic():
    rng = np.random.default_rng(0)
    x = rng.normal(10, 2, 120)
    y = x + rng.normal(0.2, 1.0, 120)
    fig, ax = plt.subplots()
    out_ax = plot_blandaltman(x, y, agreement=1.96, confidence=0.9, annotate=False, ax=ax)
    assert out_ax is ax
    plt.close(fig)
