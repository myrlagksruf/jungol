import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappop, heappush

N, M, X = map(int, input().split())
arr = [{} for _ in range(N + 1)]
rarr = [{} for _ in range(N + 1)]
for _ in range(M):
  S, E, T = map(int, input().split())
  arr[S][E] = T
  rarr[E][S] = T

def find_dist(graph:list[dict[int, int]], start_node:int):
  d = [float('inf')] * (N + 1)
  d[start_node] = 0
  h = [(0, start_node)]

  while len(h):
    dist, cur_node = heappop(h)
    if dist > d[cur_node]:
      continue
    for next_node, val in graph[cur_node].items():
      temp_dist = dist + val
      if temp_dist < d[next_node]:
        d[next_node] = temp_dist
        heappush(h, (temp_dist, next_node))
  return d

d1 = find_dist(arr, X)
d2 = find_dist(rarr, X)

ma = 0
for i in range(1, N + 1):
  ma = max(ma, d1[i] + d2[i])

print(f"{ma}\n")