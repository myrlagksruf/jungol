import sys
input = sys.stdin.readline
print = sys.stdout.write

sys.setrecursionlimit(10 ** 5)

graph:dict[int,dict[int,int]] = {}
start_node = 0
for _ in range(int(input()) - 1):
  v1, v2, dist = map(int, input().split())
  start_node = v1
  if v1 not in graph:
    graph[v1] = {}
  if v2 not in graph:
    graph[v2] = {}
  graph[v1][v2] = dist
  graph[v2][v1] = dist

def get_distance(graph:dict[int,dict[int,int]], start_node:int):
  visited:set[int] = set()
  def dfs(node):
    visited.add(node)
    total = (0, node)
    for next_node, dist in graph[node].items():
      if next_node in visited:
        continue
      total_dist, end_node = dfs(next_node)
      total = max(total, (total_dist + dist, end_node))
    return total
  return dfs(start_node)

_, node = get_distance(graph, start_node)
dist, _ = get_distance(graph, node)

print(f"{dist}\n")