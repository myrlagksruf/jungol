import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product

n = int(input())

rgbs = []
costs = [[0] * 3 for _ in range(n)]

for _ in range(n):
  rgbs.append([int(i) for i in input().split()])

costs[0] = [*rgbs[0]]

ss = [
  [1, 2], [0, 2], [0, 1]
]

for i, j in product(range(1, n), range(3)):
  costs[i][j] = rgbs[i][j] + min(costs[i - 1][k] for k in ss[j])

print(f"{min(costs[n - 1])}\n")