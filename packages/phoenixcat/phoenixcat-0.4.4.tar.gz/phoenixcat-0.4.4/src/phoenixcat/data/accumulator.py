# Copyright 2024 Hongyao Yu and Sijin Yu.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
from typing import Literal
from collections import defaultdict, OrderedDict

try:
    import torch

    _has_torch = True
except:
    _has_torch = False


class ListAccumulator:
    """For accumulating sums over `n` variables."""

    def __init__(self, n: int):
        self.data = [0] * n
        self.num = 0

    def add(self, *args, add_num: int = 1, add_type: Literal['mean', 'sum'] = 'mean'):
        """adding data to the data list"""
        assert len(args) == len(self.data)
        mul_coef = add_num if add_type == 'mean' else 1
        self.num += add_num
        for i, add_item in enumerate(args):
            if _has_torch and isinstance(add_item, torch.Tensor):
                add_item = add_item.item()
            self.data[i] += add_item * mul_coef

    def reset(self):
        """reset all data to 0"""
        self.data = [0] * len(self.data)
        self.num = 0

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def avg(self, idx=None):
        """Calculate average of the data specified by `idx`. If idx is None, it will calculate average of all data.

        Args:
            idx (int, optional): subscript for the data list. Defaults to None.

        Returns:
            int | list: list if idx is None else int
        """
        num = 1 if self.num == 0 else self.num
        if idx is None:
            return [d / num for d in self.data]
        else:
            return self.data[idx] / num


class DictAccumulator:
    def __init__(self) -> None:
        self.data = OrderedDict()  # defaultdict(lambda : 0)
        self.num = 0

    def reset(self):
        """reset all data to 0"""
        self.data = OrderedDict()  # defaultdict(lambda : 0)
        self.num = 0

    def add(
        self, add_dic: OrderedDict, add_num=1, add_type: Literal['mean', 'sum'] = 'mean'
    ):
        mul_coef = add_num if add_type == 'mean' else 1
        self.num += add_num
        for key, val in add_dic.items():
            if _has_torch and isinstance(val, torch.Tensor):
                val = val.item()
            if key not in self.data.keys():
                self.data[key] = 0
            self.data[key] += val * mul_coef

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)

    def avg(self, key=None):
        num = 1 if self.num == 0 else self.num
        if key is None:
            res = copy.deepcopy(self.data)
            for k in self.data:
                res[k] /= num
            return res
        else:
            return self.data[key] / num
