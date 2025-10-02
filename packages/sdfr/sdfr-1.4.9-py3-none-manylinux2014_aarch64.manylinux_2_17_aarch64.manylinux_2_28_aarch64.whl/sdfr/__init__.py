#!/usr/bin/env python
# coding: utf-8

# Copyright 2022 University of Warwick, University of York
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

from .SDF import (
    new,
    read,
    SdfBlockType,
    SdfGeometry,
    SdfStagger,
    SdfDataType,
    SdfBlock,
    SdfFile,
    RunInfo,
    BlockList,
    Block,
    BlockConstant,
    BlockPlainVariable,
    BlockPlainMesh,
    BlockLagrangianMesh,
    BlockPointMesh,
    BlockPointVariable,
    BlockNameValue,
    BlockArray,
    BlockData,
    BlockStitched,
    BlockStitchedPath,
    BlockStitchedMaterial,
    BlockStitchedMatvar,
    BlockStitchedSpecies,
    BlockStitchedTensor,
)
from . import sdf_helper
from ._commit_info import (
    __commit_date__,
    __commit_id__,
)
from .loadlib import (
    __library_commit_date__,
    __library_commit_id__,
)

from importlib.metadata import version

_module_name = "sdfr"

try:
    __version__ = version(_module_name)
except Exception:
    __version__ = "0.0.0"

__all__ = [
    "SDF",
    "new",
    "read",
    "sdf_helper",
    "SdfBlockType",
    "SdfGeometry",
    "SdfStagger",
    "SdfDataType",
    "SdfBlock",
    "SdfFile",
    "RunInfo",
    "BlockList",
    "Block",
    "BlockConstant",
    "BlockPlainVariable",
    "BlockPlainMesh",
    "BlockLagrangianMesh",
    "BlockPointMesh",
    "BlockPointVariable",
    "BlockNameValue",
    "BlockArray",
    "BlockData",
    "BlockStitched",
    "BlockStitchedPath",
    "BlockStitchedMaterial",
    "BlockStitchedMatvar",
    "BlockStitchedSpecies",
    "BlockStitchedTensor",
    "__library_commit_date__",
    "__library_commit_id__",
    "__version__",
    "__commit_date__",
    "__commit_id__",
]
