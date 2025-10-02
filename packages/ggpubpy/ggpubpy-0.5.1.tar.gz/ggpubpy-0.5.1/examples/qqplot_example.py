import matplotlib.pyplot as plt
from ggpubpy import qqplot, load_iris

if __name__ == "__main__":
    iris = load_iris()
    fig, ax = plt.subplots(figsize=(5, 5))
    qqplot(iris["sepal_length"].values, dist="norm", confidence=0.95, ax=ax)
    ax.set_title("Iris: QQ Plot (Sepal Length vs Normal)")
    fig.savefig("examples/qqplot_example.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
