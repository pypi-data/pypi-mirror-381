"""
PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics
Copyright (C) 2025 Ning Wang

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# piano/utils/__init__.py

# Import all modules
from .composer import Composer
from .data import AnnDataset, SparseGPUAnnDataset, BackedAnnDataset, GPUBatchSampler, streaming_hvg_indices
from .timer import time_code
from .triton_sparse import SparseTritonMatrix

# Specify all imports (i.e. `from piano.utils import *`)
__all__ = [
    # .utils
    # # .composer
    'Composer',
    # # .data
    'AnnDataset',
    'SparseGPUAnnDataset',
    'BackedAnnDataset',
    'GPUBatchSampler',
    'streaming_hvg_indices',
    # # .timer
    'time_code',
    # # .triton_sparse
    'SparseTritonMatrix',
]
