#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ──────────────────────────────────────────────────────────────────────────────
# ~~ Imports ~~ ────────────────────────────────────────────────────────────────
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────────────────────────
# ~~ Exports ~~ ────────────────────────────────────────────────────────────────
__all__: list[str] = ["custom_plot_setup", "plot_out"]
# ──────────────────────────────────────────────────────────────────────────────


def custom_plot_setup(usetex: bool = True) -> None:
    plt.rcParams["text.usetex"] = usetex
    plt.style.use("ggplot")
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["xtick.color"] = "black"
    plt.rcParams["ytick.color"] = "black"
    plt.rcParams["axes.labelcolor"] = "black"
    plt.rcParams["grid.color"] = "gainsboro"


# ──────────────────────────────────────────────────────────────────────────────


def plot_out(savepath: str | None = None) -> None:
    if savepath:
        plt.savefig(savepath, dpi=400, bbox_inches="tight")
    else:
        plt.show()
