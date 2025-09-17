import os
from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from utils import sanitize

# ---------- Gráficas ----------
def plot_histograms(df: pd.DataFrame, outdir: str, bins: int = 30, show: bool = False):
    for col in df.columns:
        plt.figure()
        df[col].plot(kind="hist", bins=bins, title=f"Histograma - {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        fname = os.path.join(outdir, f"hist_{sanitize(col)}.png")
        plt.tight_layout()
        plt.savefig(fname, dpi=150)
        if show:
            plt.show()
        plt.close()


def plot_boxplots(df: pd.DataFrame, outdir: str, show: bool = False):
    for col in df.columns:
        plt.figure()
        df[col].plot(kind="box", title=f"Boxplot - {col}")
        fname = os.path.join(outdir, f"box_{sanitize(col)}.png")
        plt.tight_layout()
        plt.savefig(fname, dpi=150)
        if show:
            plt.show()
        plt.close()


def plot_scatter_matrix(df: pd.DataFrame, outdir: str, show: bool = False):
    axarr = scatter_matrix(df, alpha=0.7, diagonal="hist", figsize=(8, 8))
    # Ajuste de etiquetas
    for ax in axarr.flatten():
        ax.xaxis.label.set_rotation(45)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha("right")
    plt.suptitle("Matriz de dispersión", y=1.02)
    fname = os.path.join(outdir, "scatter_matrix.png")
    plt.tight_layout()
    plt.savefig(fname, dpi=150)
    if show:
        plt.show()
    plt.close()
