# BatMania - The Battery Modeling Collection in Python

[![DOI](https://zenodo.org/badge/605480587.svg)](https://zenodo.org/badge/latestdoi/605480587)

---

This repo collects battery models from different publications, implements them in Python.
The details of the implementation are explained.
Further, if changes with regard to the source material are made, they will be explained.

The aim of this project is to give an extensive overview and introduction to the development and implementation of battery modeling.
While the Python code is good for prototyping and allows for a simple-to-read structure it is not meant for production or use in high-performance applications.
This repo is mainly meant for learning and reference.
All code is open-source and free to use.

## Model List

- [X] Single Particle Model (SPM)
    - [X] SPM on a Halfcell (see: [SPM_Zhang.ipynb](SPM_Zhang.ipynb))
    - [X] SPM with electrolyte dynamics (see: [SPMe.ipynb](SPMe.ipynb))
- [ ] Doyler-Fuller-Newmann (DFN) model
    - [ ] Standard DFN model (see: [DFN_Plett.ipynb](DFN_Plett.ipynb))
- [ ] Full-homogenized macroscale (FHM) model
    - [ ] Standard FHM model (see: [FHM_Arunachalam.ipynb](FHM_Arunachalam.ipynb))


## Citing

If you use ``BatMania`` for research and would like to cite the module
and source, you can visit [BatMania Zenodo](https://zenodo.org/badge/latestdoi/7684688) and generate the correct citation.  
For example, the BibTex citation is:
```bibtex
@software{BatMania2023,
  author       = {Willi Zschiebsch},
  title        = {BatMania},
  month        = feb,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.7684688},
  url          = {https://doi.org/10.5281/zenodo.7684688}
}
```

## Contribution

This project is tries to be part of [NASA's Transform to Open Science Mission](https://nasa.github.io/Transform-to-Open-Science/year-of-open-science/), which tries to make science more openly available.
Therefore, it follows the [NASA's Guide for Your Open Science Journey](https://nasa.github.io/Transform-to-Open-Science-Book/Open_Science_Cookbook/Your_Open_Science_Journey.html#section-3-open-science-at-work).
For beginners to the contribution process, we recommend [this](https://github.com/firstcontributions/first-contributions) starter guide.
