# Dataset wrappers
The classes within the .py files are used to extract the data from the datasets so it can be used as input to a Large Language Model (LLM). Therefore the code within these classes are meant to be LLM-independent.

This folder contains the base class in `dataset_wrapper.py`. The other .py files contain a class specific to a certain dataset.

# Adding a dataset
The functions within the dataset classes are adapted from the original scripts of the corresponding dataset repository. These repositories are also included as submodules. If these repositories are used 'as is', they can be included directly as subfolders. Otherwise, a parent folder is needed, for example, for the generation of the data based on the scripts within a repository.

When creating the new class, it should inherit from the `DatasetWrapper` class in `dataset_wrapper.py`. The `__init__` and `evaluate` methods should be overridden.
