set term pdf color size 5,3
set style data histogram
set style fill solid border -1
set ylabel "Error"
set xlabel "Year"
set xtics nomirror rotate by -90
set yr [0:500000]
unset ytics
plot "gabor8-exemplar.dat" using 2:xtic(1) title "Nearest Statistical Exemplar", \
     "theoretical-gabor8.dat" using 2:xtic(1) title "Statistical Centroid"
