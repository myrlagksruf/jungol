import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappop, heappush

V, E = map(int, input().split())

K = int(input())

d = [float('inf')] * (V + 1)
d[K] = 0

graph:list[dict[int, int]] = [{} for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u][v] = min(graph[u].get(v, float('inf')), w)

h = [(0, K)]

while len(h):
  score, cur_node = heappop(h)
  if score > d[cur_node]:
    continue
  for next_node, weight in graph[cur_node].items():
    val = score + weight
    if d[next_node] > val:
      d[next_node] = val
      heappush(h, (val, next_node))

print('\n'.join(str(d[i]) if d[i] != float('inf') else 'INF' for i in range(1, len(d))))
