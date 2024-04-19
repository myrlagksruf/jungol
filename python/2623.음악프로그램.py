import sys
input = sys.stdin.readline
print = sys.stdout.write
from graphlib import TopologicalSorter


N, M = map(int, input().split())
g = { str(key):set() for key in range(1, N + 1)}
for i in range(M):
  arr = input().rstrip().split()
  for j in range(1, int(arr[0])):
    g[arr[j + 1]].add(arr[j])

t = TopologicalSorter(g)
try:
  print('\n'.join(t.static_order()))
except:
  print("0")
print("\n")