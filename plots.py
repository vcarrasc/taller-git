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


def plot_lines(df: pd.DataFrame, outdir: str, index_col: Optional[str], show: bool = False):
    # Si se especifica index_col y existe, úsala como índice (ideal para series temporales)
    if index_col and index_col in df.columns:
        df_plot = df.set_index(index_col)
    else:
        df_plot = df

    plt.figure()
    df_plot.plot(title="Serie(s) temporal(es) / Line Plot")
    plt.xlabel("Índice" if not index_col else index_col)
    plt.ylabel("Valor")
    fname = os.path.join(outdir, "line_plot.png")
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


def plot_corr_heatmap(df: pd.DataFrame, outdir: str, show: bool = False):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(6, 5))
    im = plt.imshow(corr, interpolation="nearest")
    plt.title("Mapa de calor de correlaciones")
    plt.colorbar(im, fraction=0.046, pad=0.04)
    ticks = range(len(corr.columns))
    plt.xticks(ticks, corr.columns, rotation=45, ha="right")
    plt.yticks(ticks, corr.columns)
    fname = os.path.join(outdir, "correlation_heatmap.png")
    plt.tight_layout()
    plt.savefig(fname, dpi=150)
    if show:
        plt.show()
    plt.close()