import sys
input = sys.stdin.readline
print = sys.stdout.write
from math import comb
P = 10007
N = int(input())

combmap = [[0] * 53 for _ in range(53)]

def getcomb(n:int, r:int):
  global combmap
  if combmap[n][r] != 0:
    return combmap[n][r]
  if n == r or r == 0:
    return 1
  else:
    combmap[n][r] = comb(n, r)
    return combmap[n][r]

count = N // 4
acc = 0
way = 1
for i in range(1, count + 1):
  acc += getcomb(13, i) * getcomb(52 - i * 4, N - i * 4) * way
  way = -way

print(f"{acc % P}\n")