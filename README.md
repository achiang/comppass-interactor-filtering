Installation
============

Download and install the [Anaconda Python 3.6 distribution](https://www.anaconda.com/download/).

Using `conda`, install the following packages:

```
conda install -c conda-forge jupyterlab
conda install -c conda-forge ipywidgets
conda install -c conda-forge nodejs
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

Running
=======
Copy all input files into the same directory as this repo, and then start
Jupyter Lab:

```
jupyter lab
```

Using the file navigator in your browser's tab, navigate to this repo, and
launch the `CompPASS_Interactor_Filtering.ipynb` notebook.


Maintenance
-----------
Be sure to update your conda environment after every `git pull`. Jupyter Lab
is under heavy development, and you'll want to be sure to stay up to date
with any bug fixes.


```
conda update --all
```

You may need to additionally refresh jupyter-widgets; re-run the command
in the `Installation` section.


License
=======
© 2018 Alex Chiang <proteomics@chizang.net>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
