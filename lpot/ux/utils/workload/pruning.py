# -*- coding: utf-8 -*-
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""LPOT configuration pruning module."""

from typing import Any, Dict, List, Optional

from lpot.ux.utils.json_serializer import JsonSerializer


class Magnitude(JsonSerializer):
    """LPOT configuration Magnitude class."""

    def __init__(self, data: Dict[str, Any] = {}):
        """Initialize LPOT configuration Magnitude class."""
        super().__init__()
        # [Optional]
        self.weights: Optional[List[Any]] = data.get("weights", None)
        # [Optional] One of "per_channel", "per_tensor"
        self.method = data.get("method", None)
        # [Optional] 0 <= s < 1
        self.init_sparsity = data.get("init_sparsity", None)
        # [Optional] # 0 <= s < 1
        self.target_sparsity = data.get("target_sparsity", None)
        # [Optional]
        self.start_epoch = data.get("start_epoch", None)
        # [Optional]
        self.end_epoch = data.get("end_epoch", None)


class Pruning(JsonSerializer):
    """LPOT configuration Pruning class."""

    def __init__(self, data: Dict[str, Any] = {}):
        """Initialize LPOT configuration Pruning class."""
        super().__init__()
        # [Optional]
        self.magnitude = Magnitude(data.get("magnitude", {}))
        # [Optional]
        self.start_epoch = data.get("start_epoch", None)
        # [Optional]
        self.end_epoch = data.get("end_epoch", None)
        # [Optional]
        self.frequency = data.get("frequency", None)
        # [Optional] 0 <= s < 1
        self.init_sparsity = data.get("init_sparsity", None)
        # [Optional] 0 <= s < 1
        self.target_sparsity = data.get("target_sparsity", None)
