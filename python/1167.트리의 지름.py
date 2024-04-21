import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 5)

graph:dict[int,dict[int,int]] = {}
start_node = 0
for _ in range(int(input())):
  v, *arr, _ = map(int, input().split())
  start_node = v
  graph[v] = {}
  for i in range(0, len(arr), 2):
    graph[v][arr[i]] = arr[i + 1]

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