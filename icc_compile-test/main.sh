icc main.c -O3 -lm -mkl
time ./a.out
rm a.out

# gnuplot <<EOF
# load "main.plt"
# EOF
