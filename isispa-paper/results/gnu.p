set term pdf color size 6,6
set xlabel "K"
set ylabel "r"
set ytics 0.1
set xtics 1
set size 1,1
#set autoscale
set key tmargin
plot "mean/rgb.dat"      using 1:2 title "RGB Colour-Space Analysis" with lines,\
     "mean/hsv.dat"      using 1:2 title "HSV Colour-Space Analysis" with lines, \
     "mean/hist.dat"     using 1:2 title "RGB Histogram Analysis" with lines, \
     "mean/hsv-hist.dat" using 1:2 title "HSV Histogram Analysis" with lines, \
     "mean/edge.dat"     using 1:2 title "Edge Strength Analysis" with lines, \
     "mean/hog.dat"      using 1:2 title "Histogram of Oritenated Gradients Analysis" with lines
