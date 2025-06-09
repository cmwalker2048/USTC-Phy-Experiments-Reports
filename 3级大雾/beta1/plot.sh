#!/bin/zsh

gnuplot -persist <<EOF

set xlabel 'N/d'
set ylabel '$ \log_{10}{\frac{I}{I_0}}$'
set title ''
unset key
set logscale y
#set term epslatex standalone lw 2 color 11
#set output"fig2.tex"

f(x) = a*x + b
fit f(x) "./t1.dat" via a,b

g(x) = c*x + d
fit g(x) "./t2.dat" via c,d

h(x) = e*x + f
fit h(x) "./t3.dat" via e,f

plot "./t1.dat" with linespoints linecolor 1 linewidth 2
#     f(x)
set output

EOF