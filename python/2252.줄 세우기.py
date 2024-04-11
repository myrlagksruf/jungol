import sys
input = sys.stdin.readline
print = sys.stdout.write
from graphlib import TopologicalSorter

N, M = map(int, input().split())

graph = { str(key): set() for key in range(1, N + 1) }
for _ in range(M):
  a, b = input().rstrip().split()
  graph[b].add(a)

ts = TopologicalSorter(graph)

print(f"{' '.join(ts.static_order())}\n")