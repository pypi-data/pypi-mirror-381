# OT-knn
OT-knn is a computational method to align spatial transcriptomics (ST) slices using an optimal transport framework that incorporates local neighborhood structure.

## Installation

Install OT-knn via pip:

```bash
pip install OT-knn
```

## Input & Output

###**Input**:

The inputs to OT-knn are two spatial transcriptomics datasets in AnnData format.

Data stored in CSV files can also be converted to AnnData as shown below:

```python

import numpy as np
import scanpy as sc
from numpy import genfromtxt
import OT_knn as okn

# Load Slices
data_dir = './sample_data/' # change this path to your dataset

def load_slices(data_dir, slice_names=["slice1", "slice2"]):
    slices = []  
    for slice_name in slice_names:
        slice_i = sc.read_csv(data_dir + slice_name + ".csv")
        slice_i_coor = np.genfromtxt(data_dir + slice_name + "_imagecoor.csv", delimiter = ',')
        slice_i.obsm['spatial'] = slice_i_coor
        # Preprocess slices
        sc.pp.filter_genes(slice_i, min_counts = 15)
        sc.pp.filter_cells(slice_i, min_counts = 0)
        slices.append(slice_i)
    return slices

slices = load_slices(data_dir)
sliceA, sliceB = slices
```

###**Output**:

OT-knn produces two types of outputs:

1. **Mapping probability matrix** – a matrix of probabilities for all spot-to-spot correspondences between the two slices.

2. **Best-matching pairs** – a two-column DataFrame listing the matched spot labels from each slice.

```python

# Mapping probability matrix
pi = okn.OT_knn(sliceA, sliceB)[0]

# Best-matching pairs
best_match = okn.OT_knn(sliceA, sliceB)[1]
```


