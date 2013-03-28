set term pdf color size 6,6
set xlabel "K"
set ylabel "r"
set ytics 0.1
set xtics 1
set size 1,1
#set autoscale
set key tmargin
plot "mean/rgb.dat"      using 1:2 title "RGB" with lines,\
     "mean/hsv.dat"      using 1:2 title "HSV" with lines, \
     "mean/hist.dat"     using 1:2 title "RGB Histograms" with lines, \
     "mean/hsv-hist.dat" using 1:2 title "HSV Histograms" with lines, \
     "mean/edge.dat"     using 1:2 title "Edge Strength" with lines, \
     "mean/steerable.dat" using 1:2 title "Steerable filters: 4 orientations" with lines,\
     "mean/gabor.dat" using 1:2 title "Gabor filters: 4 orientations" with lines,\
     "mean/gabor8.dat" using 1:2 title "Gabor filters: 8 orientations" with lines,\
     "mean/hog.dat" using 1:2 title "HOG (Discrete Derivatives): 15 orientations" with lines,\
     "mean/hog4.dat" using 1:2 title "HOG (Discrete Derivatives): 4 orientations" with lines,\
     "mean/hog8.dat" using 1:2 title "HOG (Discrete Derivatives): 8 orientations" with lines,\
     "mean/hog16.dat" using 1:2 title "HOG (Discrete Derivatives): 16 orientations" with lines
