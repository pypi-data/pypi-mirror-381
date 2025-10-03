# DeePMD-kit plugin for various graph neural network models

[![DOI:10.1021/acs.jcim.4c02441](https://img.shields.io/badge/DOI-10.1021%2Facs.jcim.4c02441-blue)](https://doi.org/10.1021/acs.jcim.4c02441)
[![Citations](https://citations.njzjz.win/10.1021/acs.jcim.4c02441)](https://doi.org/10.1021/acs.jcim.4c02441)
[![conda install](https://img.shields.io/conda/dn/conda-forge/deepmd-gnn?label=conda%20install)](https://anaconda.org/conda-forge/deepmd-gnn)
[![PyPI - Version](https://img.shields.io/pypi/v/deepmd-gnn)](https://pypi.org/p/deepmd-gnn)

`deepmd-gnn` is a [DeePMD-kit](https://github.com/deepmodeling/deepmd-kit) plugin for various graph neural network (GNN) models, which connects DeePMD-kit and atomistic GNN packages by enabling GNN models in DeePMD-kit.

Supported packages and models include:

- [MACE](https://github.com/ACEsuit/mace) (PyTorch version)
- [NequIP](https://github.com/mir-group/nequip) (PyTorch version)

After [installing the plugin](#installation), you can train the GNN models using DeePMD-kit, run active learning cycles for the GNN models using [DP-GEN](https://github.com/deepmodeling/dpgen), perform simulations with the MACE model using molecular dynamic packages supported by DeePMD-kit, such as [LAMMPS](https://github.com/lammps/lammps) and [AMBER](https://ambermd.org/).
You can follow [DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/latest/) to train the GNN models using its PyTorch backend, after using the specific [model parameters](#parameters).

## Credits

If you use this software, please cite the following paper:

- Jinzhe Zeng, Timothy J. Giese, Duo Zhang, Han Wang, Darrin M. York, DeePMD-GNN: A DeePMD-kit Plugin for External Graph Neural Network Potentials, _J. Chem. Inf. Model._, 2025, 65, 7, 3154-3160, DOI: [10.1021/acs.jcim.4c02441](https://doi.org/10.1021/acs.jcim.4c02441). [![Citations](https://citations.njzjz.win/10.1021/acs.jcim.4c02441)](https://badge.dimensions.ai/details/doi/10.1021/acs.jcim.4c02441)

## Installation

### Install via conda

If you are in a [conda environment](https://docs.deepmodeling.com/faq/conda.html) where DeePMD-kit is already installed from the conda-forge channel,
you can use `conda` to install the DeePMD-GNN plugin:

```sh
conda install deepmd-gnn -c conda-forge
```

### Build from source

First, clone this repository:

```sh
git clone https://gitlab.com/RutgersLBSR/deepmd-gnn
cd deepmd-gnn
```

#### Python interface plugin

Python 3.9 or above is required. A C++ compiler that supports C++ 14 (for PyTorch 2.0) or C++ 17 (for PyTorch 2.1 or above) is required.

Assume you have installed [DeePMD-kit](https://github.com/deepmodeling/deepmd-kit) (v3.0.0b2 or above) and [PyTorch](https://github.com/pytorch/pytorch) in an environment, then execute

```sh
# expose PyTorch CMake modules
export CMAKE_PREFIX_PATH=$(python -c "import torch;print(torch.utils.cmake_prefix_path)")

pip install .
```

#### C++ interface plugin

DeePMD-kit version should be v3.0.0b4 or later.

Follow [DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/latest/install/install-from-source.html#install-the-c-interface) to install DeePMD-kit C++ interface with PyTorch backend support and other related MD packages.
After that, you can build the plugin

```sh
# Assume libtorch has been contained in CMAKE_PREFIX_PATH
mkdir -p build
cd build
cmake .. -D CMAKE_INSTALL_PREFIX=/prefix/to/install
cmake --build . -j8
cmake --install .
```

`libdeepmd_gnn.so` will be installed into the directory you assign.
When using any DeePMD-kit C++ interface, set the following environment variable in advance:

```sh
export DP_PLUGIN_PATH=/prefix/to/install/lib/libdeepmd_gnn.so
```

## Usage

Follow [Parameters section](#parameters) to prepare a DeePMD-kit input file.

```sh
dp --pt train input.json
dp --pt freeze
```

A frozen model file named `frozen_model.pth` will be generated. You can use it in the MD packages or other interfaces.
For details, follow [DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/latest/).

### Running LAMMPS + MACE with period boundary conditions

GNN models use message passing neural networks,
so the neighbor list built with traditional cutoff radius will not work,
since the ghost atoms also need to build neighbor list.
By default, the model requests the neighbor list with a cutoff radius of $r_c \times N_{L}$,
where $r_c$ is set by `r_max` and $N_L$ is set by `num_interactions` (MACE) / `num_layers` (NequIP),
and rebuilds the neighbor list for ghost atoms.
However, this approach is very inefficient.

The alternative approach for the MACE model (note: NequIP doesn't support such approach) is to use the mapping passed from LAMMPS, which does not support MPI.
One needs to set `DP_GNN_USE_MAPPING` when freezing the models,

```sh
DP_GNN_USE_MAPPING=1 dp --pt freeze
```

and request the mapping when using LAMMPS (also requires DeePMD-kit v3.0.0rc0 or above).
By using the mapping, the ghost atoms will be mapped to the real atoms,
so the regular neighbor list with a cutoff radius of $r_c$ can be used.

```lammps
atom_modify map array
```

In the future, we will explore utilizing the MPI to communicate the neighbor list,
while this approach requires a deep hack for external packages.

## Parameters

### MACE

To use the MACE model, set `"type": "mace"` in the `model` section of the training script.
Below is default values for the MACE model, most of which follows default values in the MACE package:

```json
"model": {
  "type": "mace",
  "type_map": [
    "O",
    "H"
  ],
  "r_max": 5.0,
  "sel": "auto",
  "num_radial_basis": 8,
  "num_cutoff_basis": 5,
  "max_ell": 3,
  "interaction": "RealAgnosticResidualInteractionBlock",
  "num_interactions": 2,
  "hidden_irreps": "128x0e + 128x1o",
  "pair_repulsion": false,
  "distance_transform": "None",
  "correlation": 3,
  "gate": "silu",
  "MLP_irreps": "16x0e",
  "radial_type": "bessel",
  "radial_MLP": [64, 64, 64],
  "std": 1.0,
  "precision": "float32"
}
```

### NequIP

```json
"model": {
  "type": "nequip",
  "type_map": [
    "O",
    "H"
  ],
  "r_max": 5.0,
  "sel": "auto",
  "num_layers": 4,
  "l_max": 2,
  "num_features": 32,
  "nonlinearity_type": "gate",
  "parity": true,
  "num_basis": 8,
  "BesselBasis_trainable": true,
  "PolynomialCutoff_p": 6,
  "invariant_layers": 2,
  "invariant_neurons": 64,
  "use_sc": true,
  "irreps_edge_sh": "0e + 1e",
  "feature_irreps_hidden": "32x0o + 32x0e + 32x1o + 32x1e",
  "chemical_embedding_irreps_out": "32x0e",
  "conv_to_output_hidden_irreps_out": "16x0e",
  "precision": "float32"
}
```

## DPRc support

In `deepmd-gnn`, the GNN model can be used in a [DPRc](https://docs.deepmodeling.com/projects/deepmd/en/latest/model/dprc.html) way.
Type maps that starts with `m` (such as `mH`) or `OW` or `HW` will be recognized as MM types.
Two MM atoms will not build edges with each other.
Such GNN+DPRc model can be directly used in AmberTools24.

## Examples

- [examples/water](examples/water)
- [examples/dprc](examples/dprc)
