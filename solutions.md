# Solutions to exercises

## Problem 1

(a)

```(bash)
primes.primes(2000)
Wall time: 1.744352102279663
cy_primes.primes(2000)
Wall time: 0.011397838592529297
```

(b-d) After executing `rbf.py` and creating a Cpython version of the code, I get the following results:

```(bash)
Python:  4.305681228637695
Scipy:  0.0501708984375
Cython:  3.1969821453094482
```

The execution time is reduced by a factor of 80 by using Scipy. In comparison the wall time using python and cpython roughly a one second improvement. The line_profiler give the following resutls:

```(bash)
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def rbf_network(X, beta, theta):
     8                                           
     9         1          6.0      6.0      0.0      N = X.shape[0]
    10         1          1.0      1.0      0.0      D = X.shape[1]
    11         1          3.0      3.0      0.0      Y = np.zeros(N)
    12                                           
    13      1001        426.0      0.4      0.0      for i in range(N):
    14   1001000     409340.0      0.4      3.3          for j in range(N):
    15   1000000     417218.0      0.4      3.3              r = 0
    16   6000000    2509468.0      0.4     20.0              for d in range(D):
    17   5000000    6831390.0      1.4     54.4                  r += (X[j, d] - X[i, d]) ** 2
    18   1000000     556229.0      0.6      4.4              r = r**0.5
    19   1000000    1836777.0      1.8     14.6              Y[i] += beta[j] * exp(-(r * theta)**2)
    20                                           
    21         1          1.0      1.0      0.0      return Y
```

Subtracting element in array X squared (line 17) takes the longest time to execute. The performance for executing the nested loops and the element-wise operation are not improved by compiling the code in C.
