import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 5)

N = int(input())

graph = [set() for _ in range(N + 1)]

for _ in range(N - 1):
  a, b = map(int, input().split())
  graph[a].add(b)
  graph[b].add(a)

parent = [''] * (N + 1)
parent[1] = '0'
def dfs(par:int, node:int):
  global parent, graph
  parent[node] = str(par)
  for i in graph[node]:
    if parent[i] != '':
      continue
    dfs(node, i)

dfs(0, 1)

print('\n'.join(parent[2:]))