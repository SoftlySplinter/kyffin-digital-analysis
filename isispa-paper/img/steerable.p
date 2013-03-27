set term pdf color size 5,2
set style data histogram
set style fill solid border -1
set xlabel "θ"
set ylabel "S"
set yrange [0:15]
unset key
plot "steerable.dat" using 2:xtic(1)
