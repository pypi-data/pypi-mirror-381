# -*- coding: utf-8 -*-

# (C) Copyright 2025 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import torch
import numpy as np
from twisterl import twisterl
from twisterl.nn.utils import make_sequential, embeddingbag_to_rust, sequential_to_rust


class BasicPolicy(torch.nn.Module):
    def __init__(
        self,
        obs_shape: list[int],
        num_actions: int,
        embedding_size: int,
        common_layers=(256,),
        policy_layers=tuple(),
        value_layers=tuple(),
        obs_perms=tuple(),
        act_perms=tuple(),
        device="cuda",
    ):
        super().__init__()
        self.obs_shape = obs_shape
        self.obs_size = np.prod(obs_shape)
        self.embeddings = torch.nn.Linear(self.obs_size, embedding_size)
        self.device = device

        in_size = embedding_size
        if len(common_layers) > 0:
            self.common = make_sequential(in_size, common_layers)
            in_size = common_layers[-1]
        else:
            self.common = torch.nn.Sequential()

        self.action = make_sequential(
            in_size, tuple(policy_layers) + (num_actions,), final_relu=False
        )
        self.value = make_sequential(
            in_size, tuple(value_layers) + (1,), final_relu=False
        )
        self.obs_perms = list(obs_perms)
        self.act_perms = list(act_perms)

    def forward(self, x):
        common = self.common(torch.nn.functional.relu(self.embeddings(x)))
        return self.action(common), self.value(common)

    def predict(self, obs):
        torch_obs = torch.tensor(obs, device=self.device, dtype=torch.float).unsqueeze(
            0
        )
        actions, value = self.forward(torch_obs)
        actions_np = torch.softmax(actions, axis=1).squeeze(0).cpu().numpy()
        value_np = value.squeeze(0).cpu().numpy()

        return actions_np, value_np

    def to_rust(self):
        return twisterl.nn.Policy(
            embeddingbag_to_rust(self.embeddings, [self.obs_size], 0),
            sequential_to_rust(self.common),
            sequential_to_rust(self.action),
            sequential_to_rust(self.value),
            self.obs_perms,
            self.act_perms,
        )


class Transpose(torch.nn.Module):
    def forward(self, x: torch.Tensor):
        return x.permute((0, 2, 1))


class Conv1dPolicy(BasicPolicy):
    def __init__(
        self,
        obs_shape: list[int],
        num_actions: int,
        embedding_size: int,
        conv_dim: int = 0,
        common_layers=(256,),
        policy_layers=tuple(),
        value_layers=tuple(),
        obs_perms=tuple(),
        act_perms=tuple(),
    ):
        super().__init__(
            obs_shape,
            num_actions,
            embedding_size,
            common_layers,
            policy_layers,
            value_layers,
            obs_perms,
            act_perms,
        )
        self.conv_dim = conv_dim

        layers = []
        if conv_dim == 1:
            layers.append(Transpose())

        self.conv_layer = torch.nn.Conv1d(
            obs_shape[conv_dim],
            embedding_size // obs_shape[1 - conv_dim],
            kernel_size=1,
            bias=False,
        )
        layers.append(self.conv_layer)
        layers.append(Transpose())
        layers.append(torch.nn.Flatten())

        self.embeddings = torch.nn.Sequential(*layers)

    def forward(self, x: torch.Tensor):
        if x.shape[1:] != self.obs_shape:
            x = x.reshape((-1, *self.obs_shape))
        return super().forward(x)

    def to_rust(self):
        return twisterl.nn.Policy(
            embeddingbag_to_rust(self.conv_layer, self.obs_shape, self.conv_dim),
            sequential_to_rust(self.common),
            sequential_to_rust(self.action),
            sequential_to_rust(self.value),
            self.obs_perms,
            self.act_perms,
        )
