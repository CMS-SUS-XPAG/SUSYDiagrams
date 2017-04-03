SUSYDiagrams
==============

LaTeX code and compilation script to produce Simplified Model diagrams for SUSY

  * [Producing diagrams](#producing-diagrams)
  * [Code setup](#code-setup)


#### Producing diagrams

Just run the `compile.py` script on any of .tex files with the LaTeX code for a diagram, e.g.

    ./compile.py TChiHH.tex

You can also compile all the diagrams in the current folder by running

    ./compile.py all

To create a new diagram just copy one of the provided .tex files, change the decays as you wish, and change
the name of the fmffile to match the new filename, e.g. if you create a `T2bb.tex` file, the fmffile
should be named `FeynmanT2bb`.

#### Code setup

Runnying the `compile.py` script require pythong, LaTeX, and the `feynmp-auto.sty` package.