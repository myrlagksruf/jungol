import sys
input = sys.stdin.readline
print = sys.stdout.write
from cmath import exp, pi

n = int(input())
val1 = [int(i) for i in input().split()]
val2 = [int(i) for i in input().split()]

def fft(a, inverse=False):
    n = len(a)
    if n == 1:
        return a
    w = exp(-2j * pi / n) if not inverse else exp(2j * pi / n)
    a0 = fft(a[::2], inverse)
    a1 = fft(a[1::2], inverse)
    p = [pow(w, k) for k in range(n // 2)]
    f = [0] * n
    for k in range(n // 2):
        f[k] = a0[k] + p[k] * a1[k]
        f[k + n // 2] = a0[k] - p[k] * a1[k]
        if inverse:  # If we are performing the inverse FFT, divide by 2
            f[k] /= 2
            f[k + n // 2] /= 2
    return f

def polynomial_multiply(p1, p2):
    # Extend the polynomials to the next power of two to accommodate the FFT process
    n = 1
    while n < max(len(p1), len(p2)):
        n *= 2
    n *= 2  # Double the size for polynomial multiplication
    p1.extend([0] * (n - len(p1)))
    p2.extend([0] * (n - len(p2)))

    # FFT
    fp1 = fft(p1)
    fp2 = fft(p2)

    # Point-wise multiplication
    fp = [fp1[i] * fp2[i] for i in range(n)]

    # Inverse FFT
    product = fft(fp, inverse=True)

    # Rounding the result for simplicity and removing negligible imaginary parts
    result = [round(p.real) for p in product]
    return result

# Polynomial multiplication
result = polynomial_multiply(val1, val2[::-1])
for i in range(n, len(result)):
  result[i % n] += result[i]
  result[i] = 0

print(f"{max(result)}\n")
