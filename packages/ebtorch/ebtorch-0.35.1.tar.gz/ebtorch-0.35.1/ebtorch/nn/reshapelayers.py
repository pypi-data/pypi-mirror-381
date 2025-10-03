#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
#
# Copyright (c) 2020-2025 Emanuele Ballarin <emanuele@ballarin.cc>
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
from torch import nn

# ~~ Exports ~~ ────────────────────────────────────────────────────────────────
__all__: list[str] = [
    "ReshapeLayer",
    "FlatChannelize2DLayer",
]


class ReshapeLayer(nn.Module):
    def __init__(self, shape: tuple):
        super().__init__()
        self.shape = shape

    def forward(self, x):
        return x.reshape(self.shape)


class FlatChannelize2DLayer(nn.Module):
    def __init__(self):
        super().__init__()

    # noinspection PyMethodMayBeStatic
    def forward(self, x):
        return x.reshape(*x.shape, 1, 1)
