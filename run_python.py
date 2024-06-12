import random
import time


def multiply_by_brute_force_with_indices(a, b, qar, qac, qbr, qbc, n):
    # initialize c with all 0's using list comprehension
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] = c[i][j] + a[qar+i][qac+k] * b[qbr+k][qbc+j]
    return c


def multiply_by_brute_force(a, b, n):
    # initialize c with all 0's using list comprehension
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c


def recur_fibo(n):
    # from https://www.programiz.com/python-programming/examples/fibonacci-recursion
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def run_fibonacci(n):
    # fibonacci recursive
    # from https://www.programiz.com/python-programming/examples/fibonacci-recursion
    t_s = time.time()
    for i in range(n + 1):
        recur_fibo(i)
    t_e = time.time()
    print("Fibonacci time (n=" + str(n) + ") in Python: " + str(t_e - t_s) + " seconds")


def run_brute_force_no_indices(r, a, b):
    t_s = time.time()
    multiply_by_brute_force(a, b, r)
    t_e = time.time()
    print("Raw brute force (" + str(r) + "x" + str(r) + ") in Python: " + str(t_e - t_s) + " seconds")


def run_brute_force_with_indices(r, a, b):
    t_s = time.time()
    multiply_by_brute_force_with_indices(a, b, 0, 0, 0, 0, r)
    t_e = time.time()
    print("Indexed brute force (" + str(r) + "x" + str(r) + ") in Python: " + str(t_e - t_s) + " seconds")


if __name__ == "__main__":
    n = 35
    r = 512
    # create 2 matrices to be multiplied
    a = [[random.random() for _ in range(r)] for _ in range(r)]
    b = [[random.random() for _ in range(r)] for _ in range(r)]
    # run algorithms
    run_fibonacci(n)
    run_brute_force_no_indices(r, a, b)
    run_brute_force_with_indices(r, a, b)
