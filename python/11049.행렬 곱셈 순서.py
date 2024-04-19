import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

arr = [[int(i) for i in input().split()] for _ in range(N)]
dp = [[0] * N for _ in range(N)]

def solution(st:int, ed:int):
  global dp
  if ed == st:
    return 0
  if ed - st == 1:
    return arr[ed][0] * arr[ed][1] * arr[st][0]
  if dp[st][ed] != 0:
    return dp[st][ed]
  mi = float('inf')
  for i in range(st, ed):
    mi = min(mi, solution(st, i) + solution(i + 1, ed) + arr[st][0] * arr[i][1] * arr[ed][1])
  dp[st][ed] = mi
  return mi

print(f"{solution(0, N - 1)}\n")