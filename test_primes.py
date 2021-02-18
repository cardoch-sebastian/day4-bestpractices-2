import cy_primes
import primes
import time

if __name__ == '__main__':
    s = time.time()
    for i in range(10):
        primes.primes(2000)
    e = time.time()
    print(f"Wall time: {e-s}")

    s = time.time()
    for i in range(10):
        cy_primes.primes(2000)
    e = time.time()
    print(f"Wall time: {e-s}")

