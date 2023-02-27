# BatMania - The Battery Modeling Collection in Python

This repo collects battery models from different publications, implements them in Python.
Further details are explained and if changes in regards to the source material should happen they will be explained.

The aim of this project is to give an extensive overview and introduction to the development and implementation of battery modeling.


## General

The
- ``data.py`` contains the data for the current example
- ``sol_XXX.py`` contians
- ``plots`` contains scripts for visualising different aspects of the solution
    - ``pt_XXX.py`` are static plots made with ``plotly``
    - ``ipt`` are interactive plots made with `dash``


- Single Particle Model
    - books/bms1/micro
    - papers/spm
    - papers/spme
- Doyler-Fuller-Newman or Pseudo-2D-Model
