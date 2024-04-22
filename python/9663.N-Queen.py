import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

def dfs(li:list[int], se:set[int]):
  if len(li) == n:
    return 1
  total = 0
  for i in range(n):
    if i in se:
      continue
    for x, j in enumerate(li):
      if abs(x - len(li)) == abs(i - j):
        break
    else:
      li.append(i)
      se.add(i)
      total += dfs(li, se)
      se.discard(i)
      li.pop()
  return total
# print(f"{[0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]}")
print(f"{dfs([], set())}\n")