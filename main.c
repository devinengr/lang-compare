#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// https://stackoverflow.com/questions/10192903/time-in-milliseconds-in-c
// https://www.programiz.com/python-programming/examples/fibonacci-recursion

#define ROWS 512
#define COLS 512

void matrix_multiply_brute_force(int a[ROWS][COLS], int b[ROWS][COLS], int c[ROWS][COLS], int tpn) {
    for (int i = 0; i < tpn; i++) {
        for (int j = 0; j < tpn; j++) {
            c[i][j] = 0;
            for (int k = 0; k < tpn; k++) {
                c[i][j] = c[i][j] + a[i][k] * b[k][j];
            }
        }
    }
}

int recur_fibo(int n) {
    if (n <= 1) {
        return n;
    }
    return (recur_fibo(n-1) + recur_fibo(n-2));
}

float cur_time() {
    return clock() / (CLOCKS_PER_SEC / 1000);
}

void run_fibonacci(int n) {
    // run the recursive fibonacci algorithm on each n from 0-n
    clock_t t_s = cur_time();
    for (int i = 0; i <= n; i++) {
        recur_fibo(i);
    }
    clock_t t_e = cur_time();
    // print results
    printf("Fibonacci time (n=%d) in C: %f seconds\n", n, (t_e - t_s) / 1000.0);
}

void run_brute_force() {
    // create 3 matrices (2 to be multiplied, 1 to store results)
    static int a[ROWS][COLS];
    static int b[ROWS][COLS];
    static int c[ROWS][COLS];
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            a[i][j] = rand() % 10;
            b[i][j] = rand() % 10;
        }
    }
    // multiply the matrices
    float t_s = cur_time();
    matrix_multiply_brute_force(a, b, c, ROWS);
    float t_e = cur_time();
    // print results
    printf("Brute-force matrix multiplication time (%dx%d) in C: %f seconds", ROWS, ROWS, (t_e - t_s) / 1000.0);
}

int main() {
    int n = 35;
    run_fibonacci(n);
    run_brute_force();
    return 0;
}
