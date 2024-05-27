import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import reduce

N, K = map(int, input().split())
P = 1000000007

def mod_inverse(a:int):
  return pow(a, P - 2, P)

def nCr(n:int, k:int):
  N_mod = reduce(lambda a, v: a * v % P, range(n - k + 1, n + 1), 1)

  K_mod = reduce(lambda a, v: a * v % P, range(1, k + 1), 1)

  K_inv = mod_inverse(K_mod)

  return (N_mod * K_inv) % P


print(f"{nCr(N, K)}\n")