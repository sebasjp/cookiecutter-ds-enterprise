# Cookiecutter for Data Science Projects

`This is a template for data science projects in a company where you extract the data directly from a DataLake and you don't storage them in your workspace, but in S3 or something like that.`

## Requirements

* [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): This can be installed with pip by or conda depending on how you manage your Python packages:

```
pip install cookiecutter
```
or

```
conda install -c conda-forge cookiecutter
```

## Create a new project

```
cookiecutter https://github.com/sebasjp/cookiecutter-ds-enterprise
```

## Resulting directory structure

```
├── 00-first-exploration                 <- Where first exploration of data will be located.
│   └── 01-source1.ipynb                 <- An example of naming convention.
│
├── 01-target-variable                   <- Where the target variable analysis will be located.
│   └── 01-build-target-variable.ipynb   <- An example of naming convention.
│
├── 02-process-data                      <- Where the process data source will be located.
│   └── 01-process-source1.ipynb         <- An example of naming convention.
│
├── 03-exploratory-data-analysis         <- Where the EDA stage will be located.
│   └── eda-v1.ipynb                     <- An example of naming convention.
│
├── 04-feature-selection                 <- Where the feature selection stage will be located.
│   └── feature-selection-v1.ipynb       <- An example of naming convention.
│
├── 05-training-evaluation               <- Where the training and evaluation will be located.
│   └── 01-training.ipynb                <- An example of naming convention.
│
└──  environment.yml    <- The requirements file for reproducing the analysis environment.
```