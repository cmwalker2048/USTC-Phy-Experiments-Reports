#!/bin/zsh

gnuplot -persist <<EOF

set xlabel '$ p\cdot c$ (MeV)'
set ylabel '$ E_{k}$ (MeV)'
set title '$ E_{k},P$ relationship'
set xrange [0:2.2]
set key top left
set key box
#set key font "times.ttf,18,Bold"
#unset key
set term epslatex standalone lw 2 color 11
set output"pic.tex"

f1(x) = x**2/(2*0.511)
f2(x) = sqrt(x**2+0.511**2)-0.511

plot f1(x) title "Classic",\
     f2(x) title "Relativity",\
     "beta1.dat" title "theoretical Classic",\
     "beta2.dat" title "theoretical Relativity",\
     "beta3.dat" title "Experment"
#plot "./data/neo/nn_1.txt" with lines linecolor 1 linewidth 2
set output

EOF