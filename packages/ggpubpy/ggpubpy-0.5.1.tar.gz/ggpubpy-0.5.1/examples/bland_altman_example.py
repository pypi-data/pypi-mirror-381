import matplotlib.pyplot as plt
from ggpubpy import plot_blandaltman, load_iris

if __name__ == "__main__":
    iris = load_iris()
    fig, ax = plt.subplots(figsize=(6, 4))
    plot_blandaltman(
        iris["sepal_length"].values,
        iris["petal_length"].values,
        agreement=1.96,
        confidence=0.95,
        annotate=True,
        ax=ax,
    )
    ax.set_title("Iris: Bland–Altman (Sepal Length vs Petal Length)")
    fig.savefig("examples/bland_altman_example.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
