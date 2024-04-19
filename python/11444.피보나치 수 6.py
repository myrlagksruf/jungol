import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache
from fractions import Fraction
N = 1000000007
n = int(input())

def gob(a:tuple[int], b:tuple[int]):
  return (a[0] * b[0] + 5 * a[1] * b[1]) % N, (a[0] * b[1] + a[1] * b[0]) % N

@cache
def nthgob(n:int):
  if n == 1:
    return (Fraction(1, 2), Fraction(1, 2))
  if n % 2 == 0:
    return gob(nthgob(n // 2), nthgob(n // 2))
  return gob(gob(nthgob(n // 2), nthgob(n // 2)), (Fraction(1, 2), Fraction(1, 2)))

print(f"{int(nthgob(n)[1] * 2) % N}\n")