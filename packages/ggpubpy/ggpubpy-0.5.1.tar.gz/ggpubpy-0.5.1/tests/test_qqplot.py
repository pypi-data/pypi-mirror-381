import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from ggpubpy import qqplot


def test_qqplot_basic():
    x = np.random.normal(size=100)
    fig, ax = plt.subplots()
    out_ax = qqplot(x, dist="norm", confidence=0.9, ax=ax)
    assert out_ax is ax
    plt.close(fig)
