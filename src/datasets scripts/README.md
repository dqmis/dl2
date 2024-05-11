# Dataset wrappers
These classes are used to extract the data from the datasets so it can be used as input to a Large Language Model (LLM). Therefore the code within these classes are meant to be LLM-independent.

This folder contains the base class in `dataset_wrapper.py`. The other files contain a class specific to a certain dataset.

The functions within the child classes are adapted from the original scripts of the corresponding dataset repository.

# Adding a dataset
The repository of a dataset is added to the folder `src/data`. A new class should be made within the folder `src/datasets scripts`, which inherits the `DatasetWrapper` class from `src/datasets scripts/dataset_wrapper.py`. The `evaluate` function should be overridden.
