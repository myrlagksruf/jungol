import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N = int(input())
W = int(input())
arr = [tuple(int(i) for i in input().split()) for _ in range(W)]

dp = [[(0, 0)] * 1001 for _ in range(1001)]

def get_distance(ind:int, pol:int, police:int):
  if pol == 0:
    return abs(arr[ind - 1][0] - (1 if police == 1 else N)) + abs(arr[ind - 1][1] - (1 if police == 1 else N))
  return abs(arr[ind - 1][0] - arr[pol - 1][0]) + abs(arr[ind - 1][1] - arr[pol - 1][1])

def get_police(x1:int, x2:int):
  if x1 == W or x2 == W:
    dp[x1][x2] = (0, 1) if x1 > x2 else (0, 2)
    return 0
  if dp[x1][x2] != (0, 0):
    return dp[x1][x2][0]
  next_event = max(x1, x2) + 1
  val1 = get_police(next_event, x2) + get_distance(next_event, x1, 1)
  val2 = get_police(x1, next_event) + get_distance(next_event, x2, 2)
  dpval = min((val1, 1), (val2, 2))
  dp[x1][x2] = dpval
  return dp[x1][x2][0]

print(f"{get_police(0, 0)}\n")
cur = [0, 0]
while True:
  _, car = dp[cur[0]][cur[1]]
  print(f"{car}\n")
  next_event = max(cur[0], cur[1]) + 1
  cur[0 if car == 1 else 1] = next_event
  if next_event == W:
    break