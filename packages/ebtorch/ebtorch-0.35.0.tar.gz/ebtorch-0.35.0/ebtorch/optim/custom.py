#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
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
# ==============================================================================
#
# SPDX-License-Identifier: Apache-2.0
#
# ~~ Imports ~~ ────────────────────────────────────────────────────────────────
from collections.abc import Callable
from collections.abc import Iterable
from math import ceil

import torch as th
import torch.optim
from torch import Tensor
from torch.optim import Adam

from .adopt import ADOPT
from .lookahead import Lookahead
from .radam import RAdam

# ~~ Exports ~~ ────────────────────────────────────────────────────────────────
__all__: list[str] = [
    "ralah_optim",
    "alah_optim",
    "wfneal",
    "tricyc1c",
    "epochwise_onecycle",
    "onecycle_lincos",
    "onecycle_linlin",
    "onecycle_linlin_updown",
    "warmed_up_annealer",
    "warmed_up_linneal",
    "make_beta_scheduler",
    "lahdopt",
]


# ==============================================================================


def ralah_optim(
    parameters: Iterable[Tensor] | Iterable[dict],
    radam_lr: float = 1e-3,
    la_steps: int = 5,
    la_alpha: float = 0.8,
    radam_betas: tuple[float, float] = (0.9, 0.999),
    radam_eps: float = 1e-8,
    radam_wd: float = 0.0,
    radam_degenerate_to_sgd: bool = True,
    la_pullback_momentum: str = "none",
) -> Lookahead:
    """RAdam + Lookahead optimizer"""
    return Lookahead(
        RAdam(
            params=parameters,
            lr=radam_lr,
            betas=radam_betas,
            eps=radam_eps,
            weight_decay=radam_wd,
            degenerated_to_sgd=radam_degenerate_to_sgd,
        ),
        la_steps=la_steps,
        la_alpha=la_alpha,
        pullback_momentum=la_pullback_momentum,
    )


def alah_optim(
    parameters: Iterable[Tensor] | Iterable[dict],
    adam_lr: float = 1e-3,
    la_steps: int = 5,
    la_alpha: float = 0.8,
    adam_betas: tuple[float, float] = (0.9, 0.999),
    adam_eps: float = 1e-8,
    adam_wd: float = 0.0,
    la_pullback_momentum: str = "none",
) -> Lookahead:
    """Adam + Lookahead optimizer"""
    return Lookahead(
        Adam(
            params=parameters,
            lr=adam_lr,
            betas=adam_betas,
            eps=adam_eps,
            weight_decay=adam_wd,
        ),
        la_steps=la_steps,
        la_alpha=la_alpha,
        pullback_momentum=la_pullback_momentum,
    )


def lahdopt(
    parameters: Iterable[Tensor] | Iterable[dict],
    ad_lr: float | Tensor = 1e-3,
    la_steps: int = 5,
    la_alpha: float = 0.8,
    ad_betas: tuple[float, float] = (0.9, 0.9999),
    ad_eps: float = 1e-6,
    ad_clip_exp: float | None = 0.25,
    ad_weight_decay: float = 0.0,
    ad_decouple: bool = False,
    ad_caution: bool = False,
    ad_foreach: bool | None = False,
    la_pullback_momentum: str = "none",
) -> Lookahead:
    """ADOPT + Lookahead optimizer"""
    return Lookahead(
        ADOPT(
            params=parameters,
            lr=ad_lr,
            betas=ad_betas,
            eps=ad_eps,
            clip_exp=ad_clip_exp,
            weight_decay=ad_weight_decay,
            decouple=ad_decouple,
            caution=ad_caution,
            foreach=ad_foreach,
        ),
        la_steps=la_steps,
        la_alpha=la_alpha,
        pullback_momentum=la_pullback_momentum,
    )


# ==============================================================================


def wfneal(
    optim: torch.optim.Optimizer,
    lr: float,
    epochs: int,
    magic_fraction: float = 0.56,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler, int]:
    # Durations
    steady_epochs: int = int((epochs - 2) * magic_fraction)
    anneal_epochs: int = epochs - 2 - steady_epochs

    # Seethrough early stopping
    stes_epoch: int = epochs - max(20, int(anneal_epochs / 4)) - 1

    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = lr

    # Schedulers
    warmup_scheduler = th.optim.lr_scheduler.LinearLR(
        optimizer=optim,
        start_factor=0.5,
        end_factor=1.0,
        total_iters=2,
        last_epoch=-1,
    )
    steady_scheduler = th.optim.lr_scheduler.ConstantLR(
        optimizer=optim,
        factor=1.0,
        total_iters=steady_epochs,
        last_epoch=-1,
    )
    anneal_scheduler = th.optim.lr_scheduler.CosineAnnealingLR(
        optimizer=optim,
        T_max=anneal_epochs,
        eta_min=lr * 1e-4,
        last_epoch=-1,
    )

    # Prepare scheduler
    sched = th.optim.lr_scheduler.SequentialLR(
        optim,
        schedulers=[warmup_scheduler, steady_scheduler, anneal_scheduler],
        milestones=[2, 2 + steady_epochs],
        last_epoch=-1,
    )

    # Return
    return optim, sched, stes_epoch


def tricyc1c(
    optim: torch.optim.Optimizer,
    min_lr: float,
    max_lr: float,
    up_frac: float,
    total_steps: int,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler]:
    """One-cycle, cyclical (triangular) learning rate scheduler."""
    # Compute durations
    up_steps = int(up_frac * total_steps)
    down_steps = int(total_steps) - up_steps

    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = min_lr

    sched = torch.optim.lr_scheduler.CyclicLR(
        optim,
        base_lr=min_lr,
        max_lr=max_lr,
        step_size_up=up_steps,
        step_size_down=down_steps,
        cycle_momentum=False,
        mode="triangular",
    )

    # Return
    return optim, sched


def epochwise_onecycle(
    optim: torch.optim.Optimizer,
    init_lr: float,
    max_lr: float,
    final_lr: float,
    up_frac: float,
    total_steps: int,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler]:
    """Epochwise OneCycleLR learning rate scheduler."""

    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = init_lr

    sched = torch.optim.lr_scheduler.OneCycleLR(
        optimizer=optim,
        max_lr=max_lr,
        total_steps=total_steps,
        epochs=total_steps,
        steps_per_epoch=1,
        pct_start=up_frac,
        anneal_strategy="cos",
        cycle_momentum=False,
        div_factor=max_lr / init_lr,
        final_div_factor=init_lr / final_lr,
        three_phase=False,
    )

    # Return
    return optim, sched


def onecycle_lincos(
    optim: torch.optim.Optimizer,
    init_lr: float,
    max_lr: float,
    final_lr: float,
    up_frac: float,
    total_steps: int,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler]:
    """Epochwise OneCycleLR learning rate scheduler, with linear warmup and cosine annealing."""

    # Compute constants
    warmup_lr_ratio = init_lr / max_lr
    warmup_steps = int(up_frac * total_steps)
    anneal_steps = total_steps - warmup_steps

    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = max_lr

    # Schedulers
    warmup_scheduler = th.optim.lr_scheduler.LinearLR(
        optimizer=optim,
        start_factor=warmup_lr_ratio,
        end_factor=1.0,
        total_iters=warmup_steps,
        last_epoch=-1,
    )
    anneal_scheduler = th.optim.lr_scheduler.CosineAnnealingLR(
        optimizer=optim,
        T_max=anneal_steps,
        eta_min=final_lr,
        last_epoch=-1,
    )

    # Prepare scheduler
    sched = th.optim.lr_scheduler.SequentialLR(
        optim,
        schedulers=[warmup_scheduler, anneal_scheduler],
        milestones=[warmup_steps],
        last_epoch=-1,
    )

    # Return
    return optim, sched


def onecycle_linlin(
    optim: torch.optim.Optimizer,
    init_lr: float,
    max_lr: float,
    final_lr: float,
    up_frac: float,
    total_steps: int,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler]:
    """Epochwise OneCycleLR learning rate scheduler, with linear warmup and linear annealing."""

    # Compute constants
    warmup_steps = int(up_frac * total_steps)
    anneal_steps = total_steps - warmup_steps

    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = max_lr

    # Schedulers
    warmup_scheduler = th.optim.lr_scheduler.LinearLR(
        optimizer=optim,
        start_factor=init_lr / max_lr,
        end_factor=1.0,
        total_iters=warmup_steps,
        last_epoch=-1,
    )
    anneal_scheduler = th.optim.lr_scheduler.LinearLR(
        optimizer=optim,
        start_factor=1.0,
        end_factor=final_lr / max_lr,
        total_iters=anneal_steps,
        last_epoch=-1,
    )

    # Prepare scheduler
    sched = th.optim.lr_scheduler.SequentialLR(
        optim,
        schedulers=[warmup_scheduler, anneal_scheduler],
        milestones=[warmup_steps],
        last_epoch=-1,
    )

    # Return
    return optim, sched


def onecycle_linlin_updown(
    optim: torch.optim.Optimizer,
    init_lr: float,
    max_lr: float,
    final_lr: float,
    up_steps: int,
    down_steps: int,
) -> tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LRScheduler]:
    """
    Epochwise OneCycleLR learning rate scheduler, with linear warmup and linear annealing.
    Up/Down steps parameterization.
    """
    total_steps: int = up_steps + down_steps
    up_frac: float = up_steps / total_steps
    return onecycle_linlin(
        optim=optim,
        init_lr=init_lr,
        max_lr=max_lr,
        final_lr=final_lr,
        up_frac=up_frac,
        total_steps=total_steps,
    )


def warmed_up_annealer(
    optim: torch.optim.Optimizer,
    init_lr: float,
    steady_lr: float,
    final_lr: float,
    warmup_epochs: int,
    steady_epochs: int,
    anneal_epochs: int,
    cos_annealing: bool = False,
):
    # Prepare optim
    for grp in optim.param_groups:
        grp["lr"] = steady_lr

    milestones: list[int] = [
        mwue := max(3, warmup_epochs),
        mwue + max(1, steady_epochs),
    ]

    # Schedulers
    warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
        optimizer=optim,
        start_factor=init_lr / steady_lr,
        end_factor=1.0,
        total_iters=milestones[0],
        last_epoch=-1,
    )
    steady_scheduler = torch.optim.lr_scheduler.ConstantLR(
        optimizer=optim,
        factor=1.0,
        total_iters=milestones[1],
        last_epoch=-1,
    )
    if not cos_annealing:
        anneal_scheduler = torch.optim.lr_scheduler.LinearLR(
            optimizer=optim,
            start_factor=1.0,
            end_factor=final_lr / steady_lr,
            total_iters=max(3, anneal_epochs),
            last_epoch=-1,
        )
    else:
        anneal_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer=optim,
            T_max=max(3, anneal_epochs),
            eta_min=final_lr,
            last_epoch=-1,
        )

    # Prepare scheduler
    sched = torch.optim.lr_scheduler.SequentialLR(
        optim,
        schedulers=[warmup_scheduler, steady_scheduler, anneal_scheduler],
        milestones=milestones,
        last_epoch=-1,
    )

    # Return
    return optim, sched


# Legacy alias
warmed_up_linneal = warmed_up_annealer


def make_beta_scheduler(target: float, lag_ratio: float, wu_ratio: float) -> Callable[[int, int], float]:
    def beta_scheduler(step: int, total: int) -> float:
        if step < (lag_steps := ceil(total * lag_ratio)):
            return 0.0
        if step < lag_steps + (wu_steps := ceil(total * wu_ratio)):
            return target * (step - lag_steps) / wu_steps
        return target

    return beta_scheduler
