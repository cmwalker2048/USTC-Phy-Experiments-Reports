#!/bin/zsh

gnuplot -persist <<EOF

set xlabel 'Wavelenth($\lambda$/nm)'
set ylabel '$\frac{I_0}{I}$ (a.u.)'
set title 'Normalized Absorption Spectrum Curve of Ruby Crystal'
unset key
set term epslatex standalone lw 2 color 11
set output"n_2.tex"
plot "./data/neo/nn_1.txt" with lines linecolor 1 linewidth 2
set output

EOF