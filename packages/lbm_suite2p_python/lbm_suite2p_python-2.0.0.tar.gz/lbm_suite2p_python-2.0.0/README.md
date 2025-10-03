# Light Beads Microscopy (LBM) Pipeline: Suite2p

[![PyPI - Version](https://img.shields.io/pypi/v/lbm-suite2p-python)](https://pypi.org/project/lbm-suite2p-python/)

[![Documentation](https://img.shields.io/badge/Documentation-blue?style=for-the-badge&logo=readthedocs&logoColor=white)](https://millerbrainobservatory.github.io/LBM-Suite2p-Python/index.html)

This package is still in a *beta* stage of development.

A pipeline for processing 2-photon Light Beads Microscopy (LBM) datasets.

This pipeline uses the following software:

- [suite2p](https://github.com/MouseLand/suite2p)
- [cellpose](https://github.com/MouseLand/cellpose)
- [rastermap](https://github.com/MouseLand/rastermap)
- [mbo_utilities](https://github.com/MillerBrainObservatory/mbo_utilities)
- [scanreader](https://github.com/atlab/scanreader)


[![LBM](https://zenodo.org/badge/DOI/10.1007/978-3-319-76207-4_15.svg)](https://doi.org/10.1038/s41592-021-01239-8)

---

## Installation

See the [installation documentation](https://millerbrainobservatory.github.io/LBM-Suite2p-Python/install.html) for more details.

This pipeline is fully installable with `pip`.

`conda` can still be used for the virual environment, but be mindful to only install packages with `conda install` when absolutely necessary.

We recommend cloning the repository, until a more established workflow is available to upload to PyPi.

```
git clone https://github.com/MillerBrainObservatory/LBM-Suite2p-Python.git
git clone https://github.com/Suite3D # TODO
cd LBM-Suite2p-Python

# make sure your virtual environment is active
pip install ".[all]"  # optional, contains ".[gui, notebook]"
```

## Issues
Widgets may throw "Invalid Rect" errors. This can be safely ignored until it is [resolved](https://github.com/pygfx/wgpu-py/issues/716#issuecomment-2880853089).

---

## Acknowledgements

Thank you to the developers of [scanreader](https://github.com/atlab/scanreader), which provides a clean interface to ScanImage metadata using only tifffile and numpy.

We vendor this repository because it is not published to an indexable Python package registry like PyPI.
