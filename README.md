# Kievits-FASTEM-array-tomography-2024
Repository for Python code and JuPyter notebook used for analyzing performance metrics of MitoNet on FAST-EM array tomography data. Outputs performance metrics as listed in Table 2 in the publication

## Installation
Install in `conda` environment with Python 3.9
```
conda create -n mito-analysis python=3.9
```

```
conda activate mito-analysis
```

Install dependencies with `pip`
```
pip install https://github.com/hoogenboom-group/Kievits-FASTEM-array-tomography-2024
```
or clone repo and
```
pip install .
```

## Usage
`mito-segmentation-calculate-statistics.ipynb` To calculate performance metrics as listed in Table 2 in the article  
`mito-segmentation-check.ipynb` To generate views from Figure 6 and Figure S5
