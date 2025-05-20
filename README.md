

This repo is based on the experimentation of prediction of streamflow of an upstream basin with combined environmental data of upstream basin and downstream basin with the help of Neuralhydrology library. 
This repo looks exactly like Neuralhydrology's library, but we have added a nwm-analysis directory where we perform the experiment explained above in conus and alabama dataset.
This repo has also added a few custom classes and a few features to improve the performance of our experiment.

What does nwm-analysis directory contain?
  - nwm-configs: This directory contains config files, where you define all the parameters necessary for training the model
  - nwm-data: This directory contains two directories al_runs, conus_rus, test, and a file.
      - al_runs: This directory contains .txt files with the information of alabama catchments used for training, validating, and testing.
      - conus_runs:  This directory contains .txt files with the information of conus catchments used for training, validating, and testing.
      - randomdata.py: This code selects the basin pairs randomly and helps to create the txt files in the above 2 directoris.

We also have an Archive directory that contains codes we worked on the past that might be of some use in the future, but is not too important right now.



Below this line, there is a a description about Neuralhydrology.

![#](docs/source/_static/img/neural-hyd-logo-black.png)
Python library to train neural networks with a strong focus on hydrological applications.

This package has been used extensively in research over the last years and was used in various academic publications. 
The core idea of this package is modularity in all places to allow easy integration of new datasets, new model 
architectures or any training-related aspects (e.g. loss functions, optimizer, regularization). 
One of the core concepts of this code base are configuration files, which let anyone train neural networks without
touching the code itself. The NeuralHydrology package is built on top of the deep learning framework 
[PyTorch](https://pytorch.org/), since it has proven to be the most flexible and useful for research purposes.

We (the AI for Earth Science group at the Institute for Machine Learning, Johannes Kepler University, Linz, Austria) are using
this code in our day-to-day research and will continue to integrate our new research findings into this public repository.

- Documentation: [neuralhydrology.readthedocs.io](https://neuralhydrology.readthedocs.io)
- Research Blog: [neuralhydrology.github.io](https://neuralhydrology.github.io)
- Bug reports/Feature requests [https://github.com/neuralhydrology/neuralhydrology/issues](https://github.com/neuralhydrology/neuralhydrology/issues)

# Cite NeuralHydrology

In case you use NeuralHydrology in your research or work, it would be highly appreciated if you include a reference to our [JOSS paper](https://joss.theoj.org/papers/10.21105/joss.04050#) in any kind of publication.

```bibtex
@article{kratzert2022joss,
  title = {NeuralHydrology --- A Python library for Deep Learning research in hydrology},
  author = {Frederik Kratzert and Martin Gauch and Grey Nearing and Daniel Klotz},
  journal = {Journal of Open Source Software},
  publisher = {The Open Journal},
  year = {2022},
  volume = {7},
  number = {71},
  pages = {4050},
  doi = {10.21105/joss.04050},
  url = {https://doi.org/10.21105/joss.04050},
}
```

# Contact

For questions or comments regarding the usage of this repository, please use the [discussion section](https://github.com/neuralhydrology/neuralhydrology/discussions) on Github. For bug reports and feature requests, please open an [issue](https://github.com/neuralhydrology/neuralhydrology/issues) on GitHub.
In special cases, you can also reach out to us by email: neuralhydrology(at)googlegroups.com
