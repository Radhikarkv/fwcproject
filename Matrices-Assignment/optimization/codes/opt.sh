#!/bin/bash
cd /storage/9B93-1913/Download/optimassign
python3 opt.py
pdflatex optim.tex
termux-open optim.pdf
