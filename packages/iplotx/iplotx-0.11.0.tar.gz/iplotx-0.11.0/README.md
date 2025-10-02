![Github Actions](https://github.com/fabilab/iplotx/actions/workflows/test.yml/badge.svg)
![PyPI - Version](https://img.shields.io/pypi/v/iplotx)
![RTD](https://readthedocs.org/projects/iplotx/badge/?version=latest)
[![Coverage Status](https://coveralls.io/repos/github/fabilab/iplotx/badge.svg?branch=main)](https://coveralls.io/github/fabilab/iplotx?branch=main)
![pylint](assets/pylint.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16599333.svg)](https://doi.org/10.5281/zenodo.16599333)


# iplotx
[![Banner](docs/source/_static/banner.png)](https://iplotx.readthedocs.io/en/latest/gallery/index.html).

Visualise networks and trees in Python, with style.

Supports:
- **networks**:
  - [networkx](https://networkx.org/)
  - [igraph](igraph.readthedocs.io/)
  - [minimal network data structure](https://iplotx.readthedocs.io/en/latest/gallery/plot_simplenetworkdataprovider.html#sphx-glr-gallery-plot-simplenetworkdataprovider-py) (for educational purposes)
- **trees**:
  - [ETE4](https://etetoolkit.github.io/ete/)
  - [cogent3](https://cogent3.org/)
  - [Biopython](https://biopython.org/)
  - [scikit-bio](https://scikit.bio)
  - [minimal tree data structure](https://iplotx.readthedocs.io/en/latest/gallery/tree/plot_simpletreedataprovider.html#sphx-glr-gallery-tree-plot-simpletreedataprovider-py) (for educational purposes)

In addition to the above, *any* network or tree analysis library can register an [entry point](https://iplotx.readthedocs.io/en/latest/providers.html#creating-a-custom-data-provider) to gain compatibility with `iplotx` with no intervention from our side.

## Installation
```bash
pip install iplotx
```

## Quick Start
```python
import networkx as nx
import matplotlib.pyplot as plt
import iplotx as ipx

g = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
layout = nx.layout.circular_layout(g)
fig, ax = plt.subplots(figsize=(3, 3))
ipx.plot(g, ax=ax, layout=layout)
```

![Quick start image](docs/source/_static/graph_basic.png)

## Documentation
See [readthedocs](https://iplotx.readthedocs.io/en/latest/) for the full documentation.

## Gallery
See [gallery](https://iplotx.readthedocs.io/en/latest/gallery/index.html).

## Features
- Plot networks from multiple libraries including networkx and igraph, using matplotlib as a backend. ✅
- Plot trees from multiple libraries such as cogent3, ETE4, skbio, and biopython. ✅
- Flexible yet easy styling, including an internal library of styles ✅
- Interactive plotting, e.g. zooming and panning after the plot is created. ✅
- Store the plot to disk thanks to the many matplotlib backends (SVG, PNG, PDF, etc.). ✅
- Efficient plotting of large graphs using matplotlib's collection functionality. ✅
- Edit plotting elements after the plot is created, e.g. changing node colors, labels, etc. ✅
- Animations, e.g. showing the evolution of a network over time. ✅
- Mouse and keyboard interaction, e.g. hovering over nodes/edges to get information about them. ✅
- Node clustering and covers, e.g. showing communities in a network. ✅
- Choice of tree layouts and orientations. ✅
- Tree-specific options: cascades, subtree styling, split edges, etc. ✅
- (WIP) Support uni- and bi-directional communication between graph object and plot object.🏗️

## Authors
Fabio Zanini (https://fabilab.org)
