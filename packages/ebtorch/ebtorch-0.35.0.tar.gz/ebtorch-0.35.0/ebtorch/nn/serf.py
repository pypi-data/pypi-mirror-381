#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
#
# Copyright (c) 2021-2025 Emanuele Ballarin <emanuele@ballarin.cc>
#                         All Rights Reserved.
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
# SPDX-License-Identifier: Apache-2.0
# ~~ Imports ~~ ────────────────────────────────────────────────────────────────
import torch
from torch import Tensor

from .functional import serf as fserf

# ~~ Exports ~~ ────────────────────────────────────────────────────────────────
__all__: list[str] = ["ScaledERF"]


class ScaledERF(torch.nn.Module):
    """Scaled ERror Function."""

    def __init__(self) -> None:
        super(ScaledERF, self).__init__()

    # noinspection PyMethodMayBeStatic
    def forward(self, x: Tensor) -> Tensor:
        return fserf(x)
