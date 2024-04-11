import sys
input = sys.stdin.readline
print = sys.stdout.write
from graphlib import TopologicalSorter

T = int(input())

result = []
for _ in range(T):
  N, K = map(int, input().split())
  buildings = [int(i) for i in input().split()]
  rgraph = { key:set() for key in range(1, N + 1) }
  for _ in range(K):
    a, b = map(int, input().split())
    rgraph[b].add(a)
  ts = TopologicalSorter(rgraph)
  scores = [0] * (N + 1)
  for i in ts.static_order():
    ma = buildings[i - 1]
    for j in rgraph[i]:
      ma = max(ma, buildings[i - 1] + buildings[j - 1])
    buildings[i - 1] = ma
  result.append(str(buildings[int(input()) - 1]))

print("\n".join(result))