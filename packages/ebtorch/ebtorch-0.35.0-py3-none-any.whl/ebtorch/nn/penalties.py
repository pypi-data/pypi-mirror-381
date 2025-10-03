#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ──────────────────────────────────────────────────────────────────────────────
#
# Copyright 2025 Emanuele Ballarin <emanuele@ballarin.cc>
# All Rights Reserved. Unless otherwise explicitly stated.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ──────────────────────────────────────────────────────────────────────────────
#
# SPDX-License-Identifier: Apache-2.0
#
# ──────────────────────────────────────────────────────────────────────────────
# ~~ Imports ~~ ────────────────────────────────────────────────────────────────
from collections.abc import Callable
from math import pow as mpow

import torch
from torch import Tensor
from torch.nn import functional as F

from ..typing import realnum

# ──────────────────────────────────────────────────────────────────────────────

# Auxiliary Functions


def _bool_one_zero(boolean: bool) -> int:
    return int(boolean)


def _bool_one_minusone(boolean: bool) -> int:
    return 1 - 2 * int(not boolean)


# ──────────────────────────────────────────────────────────────────────────────
# ~~ Exports ~~ ────────────────────────────────────────────────────────────────
__all__: list[str] = [
    "multilasso",
    "multiridge",
    "beta_gaussian_kldiv",
    "var_of_lap",
    "reco_reg",
    "reco_reg_split",
]
# ──────────────────────────────────────────────────────────────────────────────


def multilasso(
    params: Tensor | list[Tensor] | tuple[Tensor, ...],
    p_lasso: float = 1.0,
    p_ridge: float = 2.0,
    lam: float = 0.1,
    alp: float = 1,
    reg_oneminus: bool = False,
    adimensionalize: bool = False,
) -> Tensor:
    # Handle params multi-instance
    if isinstance(params, Tensor):
        params: list[Tensor] = [params]
    elif isinstance(params, tuple):
        params: list[Tensor] = list(params)

    # Preprocess params and decouple lists
    if reg_oneminus:
        params: list[Tensor] = [
            _bool_one_zero(reg_oneminus) + _bool_one_minusone(not reg_oneminus) * param for param in params
        ]
    params: list[Tensor] = [param.flatten() for param in params]

    # Compute Lasso penalty
    lpen: Tensor = torch.cat(params).norm(p=p_lasso)

    # Compute Group Lasso penalty
    gpen: Tensor = torch.tensor(
        [(param.norm(p=p_ridge) * mpow(param.numel(), (1 - 1 / p_ridge))) for param in params],
        device=lpen.device,
    ).norm(p=p_lasso)

    # Eventually adimensionalize
    if adimensionalize:
        divnorm: float = torch.pow(
            torch.tensor([param.numel() for param in params], device=lpen.device).sum(),
            1 / p_lasso,
        ).item()
    else:
        divnorm: int = 1

    # Return Sparse Group Lasso penalty
    return lam * (alp * lpen + (1 - alp) * gpen) / divnorm


# ──────────────────────────────────────────────────────────────────────────────


def multiridge(
    params: Tensor | list[Tensor] | tuple[Tensor, ...],
    p_ridge: float = 2.0,
    lam: float = 0.1,
    adimensionalize: bool = False,
) -> Tensor:
    # Handle params multi-instance
    if isinstance(params, Tensor):
        params: list[Tensor] = [params]
    elif isinstance(params, tuple):
        params: list[Tensor] = list(params)

    # Preprocess params
    params: list[Tensor] = [param.flatten() for param in params]

    # Compute penalty
    rpen: Tensor = torch.cat(params).norm(p=p_ridge)

    # Eventually adimensionalize
    if adimensionalize:
        divnorm: float = torch.pow(
            torch.tensor([param.numel() for param in params], device=rpen.device).sum(),
            1 / p_ridge,
        ).item()
    else:
        divnorm: int = 1

    # Return Ridge penalty
    return lam * rpen / divnorm


# ──────────────────────────────────────────────────────────────────────────────


def reco_reg_split(
    x_true: Tensor,
    x_pred: Tensor,
    sparsifiand: Tensor,
    *,
    lambdas: realnum | tuple[realnum, ...] = 1,
    lpows: realnum | tuple[realnum, ...] = 1,
    reco_fx: Callable[..., Tensor] = F.mse_loss,
    reduction: str = "mean",
) -> tuple[Tensor, Tensor, Tensor]:
    if not isinstance(lambdas, Tuple):
        lambdas: tuple[realnum, ...] = (lambdas,)
    if not isinstance(lpows, Tuple):
        lpows: tuple[realnum, ...] = (lpows,)

    reco: Tensor = reco_fx(x_pred, x_true, reduction=reduction)
    spar: Tensor = sum(  # type: ignore
        lam * torch.linalg.vector_norm(sparsifiand, ord=lpow) for lam, lpow in zip(lambdas, lpows)
    )
    loss: Tensor = reco + spar

    return loss, reco, spar


def reco_reg(
    x_true: Tensor,
    x_pred: Tensor,
    sparsifiand: Tensor,
    *,
    lambdas: realnum | tuple[realnum, ...] = 1,
    lpows: realnum | tuple[realnum, ...] = 1,
    reco_fx: Callable[..., Tensor] = F.mse_loss,
    reduction: str = "mean",
):
    loss: Tensor
    loss, _, _ = reco_reg_split(
        x_true,
        x_pred,
        sparsifiand,
        lambdas=lambdas,
        lpows=lpows,
        reco_fx=reco_fx,
        reduction=reduction,
    )
    return loss


# ──────────────────────────────────────────────────────────────────────────────


@torch.jit.script
def beta_gaussian_kldiv(mu: Tensor, sigma: Tensor, beta: float = 1.0) -> Tensor:
    kldiv = 0.5 * (torch.pow(mu, 2) + torch.exp(sigma) - sigma - 1).sum()
    return beta * kldiv


@torch.jit.script
def var_of_lap(img: torch.Tensor) -> torch.Tensor:
    lap_kernel = (
        torch.tensor([[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]], device=img.device)
        .expand(img.shape[-3], 3, 3)
        .unsqueeze(1)
    )
    return torch.nn.functional.conv2d(img, lap_kernel, groups=img.shape[-3]).var(dim=(-2, -1)).sum(-1)
