import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache
sys.setrecursionlimit(10 ** 6)

n = int(input())
N = 1000000009

@cache
def dp(n, last):
  if n < 4:
    if last == n:
      if n == 1 or n == 2:
        return 1
    if n == 3:
      return 1
    return 0
  su = 0
  for i in range(1, 4):
    if i == last:
      continue
    su += dp(n - last, i) % N
  return su % N

result = []
for _ in range(n):
  su = 0
  k = int(input())
  for j in range(1, 4):
    su += dp(k, j) % N
  result.append(str(su % N))

print("\n".join(result))
print("\n")