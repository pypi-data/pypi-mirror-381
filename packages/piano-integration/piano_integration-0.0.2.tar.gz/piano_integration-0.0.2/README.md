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

# README
This repository contains the source code for PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics.

## Installation:
Create an uv environment as follows (strongly recommended):
```
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'cache-dir = "/path/to/cache/directory/uv_cache"' >>~/.config/uv/uv.toml

# Create uv environment
uv venv --python 3.10
source .venv/bin/activate
uv pip install piano-integration[rapids]

# If not using rapids single cell, use the following:
uv pip install piano-integration

If you have issues with installation, you can add the following flag: ` --index-strategy unsafe-best-match`, e.g.
`uv pip install piano-integration[rapids] --index-strategy unsafe-best-match`
`uv pip install piano-integration --index-strategy unsafe-best-match`
`uv pip install piano-integration[all] --index-strategy unsafe-best-match`

# Alternative installation methods:
`uv pip install .[rapids]`  # Using rapids
`uv pip install .`  # Not using rapids
`uv pip install -r requirements_rapids.txt --index-strategy unsafe-best-match`  # Including rapids
`uv pip install -r requirements_lite.txt --index-strategy unsafe-best-match`  # Minimal installation
`uv pip install -r requirements.txt --index-strategy unsafe-best-match`  # Containing all optional libraries
```

Or, create a conda environment as follows (much slower than uv):
```
# Install miniconda if not already installed
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

# Create conda environment in a new terminal
conda create -n piano python=3.10.18 -y
conda activate piano
pip install piano-integration[rapids]

# Similar options are available as those listed above for uv
```

### Triton (torch.compile) compilation for ARM architectures:
```
# Instructions for compiling triton from scratch
git clone https://github.com/triton-lang/triton.git
cd triton
uv pip install -r python/requirements.txt # Using uv installed for ARM
uv pip install -e .
```

## Code Overview:
### Pipeline:
A simple use case is provided in run_piano_integration.py  
You can call run this script as follows:
```
python3 run_piano_integration.py \
    --version 0.0_piano_integration \
    --adata_path /path/to/adata.h5ad \
    --outdir ../results \
    --categorical_covariate_keys your covariates here \
    --batch_key your_primary_hvg_batch_key_here \
    --umap_labels your umap labels here
```
You can add additional command line arguments using argparse or modifying directly in the script to customize the parameters used for training.

The PIANO pipeline works as follows:
1. First, the model hyperparameters are specified. The most important parameters are the model size, covariates, training epochs, and KL divergence weight.  
2. Next, a `Composer` class is initialized to hold all the parameters for the model and training.  
3. The composer calls `.run_pipeline()`, which handles the following details:
  - The composer uses `.initialize_features()` to encode the covariates and to select highly variable genes for the data.  
  - The composer uses `.prepare_data()` to prepare the AnnDatasets for the data.  
  - The composer uses `.prepare_model(**self.model_kwargs)` to prepare the `Etude` model using the appropriate genes and covariates.  
  - The composer uses `.train_model()` to train the `Etude` model.  
4. We then call `.get_latent_representation(adata)` to retrieve an integrated latent space.  
5. Finally, we visualize the results by plotting the integrated UMAPs.  

### Relevant Classes:
#### AnnDataset:
Takes in an input AnnData object and creates a PyTorch Dataset. 
The counts matrix in .X is forced into non-sparse tensor.
Then, batch columns from .obs are integer-encoded if categorical and concatenated to the counts.

#### Etude:
The Etude class is a PyTorch module that implements a variational autoencoder (VAE).
The input to the encoder are the gene counts and batch columns, which are reconstructed by the decoder.
This model differs from the original VAE by also including sets of weights for each gene using a generalized linear model (GLM).
These weights mitigate the influence of batch effects, continuous or categorical keys in the latent space representation.
For these covariates, continous values are kept in one column, while categorical keys are one-hot encoded.
These batch keys are stored as augmented columns of the AnnDataset object used for training.

#### Composer:
This class handles the pipeline of training the model, saving or loading a trained model, and retrieving integrated latent spaces.  
It parses the data to obtain how many columns to use for genes after selecting for highly variable genes using the batch_key.  
Alternatively, you can pass in a set of genes in a text file, which is loaded using pd.read_csv(path_to_gene_set, index_col=0).values.ravel()  
Shown below are the some of the recommended parameters with descriptions. Full parameters can be found in `utils/composer`.  
The main parameters to change are the gene selection, covariates, and number of layers, hidden nodes, and latent dimensions.  

```
# Training data
adata, # Must pass in training data

# Composer arguments
memory_mode: Literal['GPU', 'SparseGPU', 'CPU'] = 'GPU',  # Use GPU mode for fastest training
compile_model: bool = True,  # Set to True for fastest training (hardware dependent)
use_padding: bool = False,  # Set to True if hardware complains that the number of genes is not a multiple of 4
distribution: Literal['nb', 'zinb'] = 'nb',
categorical_covariate_keys=None,  # Use a list of the most important categorical sources of variation
continuous_covariate_keys=None,

# Gene selection
flavor: str = 'seurat_v3',  # Highly variable gene (HVG) selection (default)
n_top_genes: int = 4096,
hvg_batch_key=None,  # Use most important batch key for Seurat_v3 highly variable gene selection ()
geneset_path=None,  # If using a file with gene names in each line instead of HVG selection

# Model kwargs
input_size: int = 4096,  # Must be Python int
n_hidden: int = 256,
n_layers: int = 3,
latent_size: int = 32,
dropout_rate: float = 0.1,
batchnorm_eps: float = 1e-5,       # Torch default is 1e-5
batchnorm_momentum: float = 1e-1,  # Torch default is 1e-1
epsilon: float = 1e-5,             # Torch default is 1e-5

# Training
max_epochs: int = 200,
batch_size: int = 128,
min_weight: float = 0.00,
max_weight: float = 1.00,
cyclic_annealing_m: int = 400,
anneal_batches: bool = True,
lr: float = 2e-4,
weight_decay: float = 0.00,
save_initial_weights: bool = False,
checkpoint_every_n_epochs = None,  # Save model weights every n epochs
early_stopping: bool = True,  # Whether to stop training if model converges
min_delta: float = 1.00,  # Minimum improvement to keep training if early stopping
patience: int = 5,  # Number of epochs to check for improvement
shuffle: bool = True,  # Shuffle traiing data
drop_last: bool = True,  # Ensure fixed size for mini-batch updates
num_workers: int = 0,  # Set to 0 if using GPU or SparseGPU mode

# Reproducibility
deterministic: bool = True,  # Reproducibility is hardware dependent before compilation
random_seed: int = 0,

# Output
run_name: str = 'piano_integration',
outdir: str = './results/',
```

## Contact:
nw8333 at princeton dot edu
