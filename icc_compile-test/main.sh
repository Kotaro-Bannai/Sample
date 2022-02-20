icc main.c -O3 -lm -qmkl
time ./a.out
rm a.out

# gnuplot <<EOF
# load "main.plt"
# EOF
