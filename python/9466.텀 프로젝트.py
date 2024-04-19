import sys
input = sys.stdin.readline
print = sys.stdout.write

sys.setrecursionlimit(10 ** 5)

arr:list[int] = []
# 0: unvisited, 1: visited, 2:not circle, 3: circle start, 4: circle end
circle:list[int] = []

def dfs(i:int):
  global arr, circle
  if circle[i] == 1:
    circle[i] = 3
    return
  if circle[i] != 0:
    return
  circle[i] = 1
  dfs(arr[i] - 1)
  if circle[arr[i] - 1] == 3:
    if circle[i] != 4:
      circle[i] = 3
    circle[arr[i] - 1] = 4
  else:
    circle[i] = 2


for _ in range(int(input())):
  input()
  arr = [int(i) for i in input().split()]
  circle = [0] * len(arr)
  for i in range(len(arr)):
    dfs(i)
  print(f"{sum(1 for i in circle if i == 2)}\n")