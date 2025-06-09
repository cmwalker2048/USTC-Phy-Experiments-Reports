#!/bin/zsh

gnuplot -persist <<EOF

set xlabel 'B/mT'
set ylabel '$ I/\mu A$'
set title 'I-B relationship when B keeps going down'
unset key
#set term epslatex standalone lw 2 color 11
#set output"f2.tex"
plot "./data1.dat" with linespoints linecolor 1 linewidth 1,\
     "./data2.dat" with linespoints linecolor 1 linewidth 1
set output

EOF