import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

arr = [int(input()) for _ in range(N)]

jump_node = [0] * N

for ind, i in enumerate(arr, 1):
  jump_node[i - 1] = ind - 1
  print(f"{i - 1} -> ? -> {ind - 1}\n")

def dfs(next_node:list[int], remain:set[int], depth:int):
  global jump_node
  if depth == N:
    return next_node
  if next_node[depth] != -1:
    return dfs(next_node, remain, depth + 1)
  for i in remain:
    if next_node[i] != -1 and next_node[i] != jump_node[depth]:
      continue
    next_node[depth] = i
    next_node[i] = jump_node[depth]
    remain.discard(i)
    remain.discard(depth)
    result = dfs(next_node, remain, depth + 1)
    if result:
      return result
    remain.add(depth)
    remain.add(i)
  return None


print(f"{dfs([-1] * N, set(range(N)), 0)}\n")