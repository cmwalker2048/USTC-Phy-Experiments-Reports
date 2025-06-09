#!/bin/zsh

gnuplot -persist <<EOF

set xlabel 'U/V'
set ylabel 'I/$\mu A$'
set title 'I-U relationship of DC low pressure discharge'
#set title 'U-P relationship(Gas breakdown voltage under different pressure)'
#set xrange [-100:100]
#set yrange [-6:6]
set key top left
set key box
set key font "times.ttf,20,Bold"
#unset key
#set grid
#set term epslatex standalone lw 2 color 11
#set output"./pic4.tex"

#f1(x) = x**2/(2*0.511)
#f2(x) = sqrt(x**2+0.511**2)-0.511

f(x) = a*x + b
fit f(x) "./bm_2.dat" via a,b

#f(x) = a*x + b
#g(x) = c*x + d
#h(x) = e*x + f
#fit f(x) "./3_1.dat" via a,b
#fit g(x) "./3_2_2.dat" via c,d
#fit h(x) "./3_2_3.dat" via e,f

#plot "./1_1.dat" with linespoints
#plot "./1_2.dat" with linespoints
plot f(x) title "fitted data", \
     "./bm_2.dat" title "original data"

#set label 2 "$ I_{i01}$" at -10,2.2814
#set label 3 "$ I_{i02}$" at 0,-2.08568
#set label 1 "$ \frac{d\,V_{D}}{d\,I_{D}}$" at 0,0

#plot "./3.dat" title "original data" with points,\
#     f(x) title "fitted data 1",\
#     g(x) title "fitted data 2",\
#     h(x) title "fitted data 3"
#plot "./1_1.dat" title "P = 20pa" with linespoints,\
#     "./1_2.dat" title "P = 40pa" with linespoints

#plot "./data/neo/nn_1.txt" with lines linecolor 1 linewidth 2
set output

EOF