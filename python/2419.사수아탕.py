import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache

n, m = map(int, input().split())
arr = [0]
first = 0
flag = 0
for _ in range(n):
  val = int(input())
  if val < 0:
    first += 1
  if val == 0:
    flag = m
    n -= 1
    continue
  arr.append(val)

arr.sort()

dp = [(0, 0)] * 180601

def get_result(st:int, ed:int, remain:int, ori_remain:int, isLeft:bool):
  if remain == 0:
    return 0
  result = []
  if st - 1 >= 0:
    ind = (st - 1) * 600 + ed * 2 + 1
    if dp[ind][1] != ori_remain:
      dp[ind] = (get_result(st - 1, ed, remain - 1, ori_remain, True), ori_remain)
    result.append(dp[ind][0] - remain * abs(arr[[ed, st][int(isLeft)]] - arr[st - 1]) + m)
  if ed + 1 < len(arr):
    ind = st * 600 + (ed + 1) * 2
    if dp[ind][1] != ori_remain:
      dp[ind] = (get_result(st, ed + 1, remain - 1, ori_remain, False), ori_remain)
    result.append(dp[ind][0] - remain * abs(arr[ed + 1] - arr[[ed, st][int(isLeft)]]) + m)
  return max(result)

result = 0

for i in range(1, n + 1):
  result = max(result, get_result(first, first, i, i, True))

print(f"{result + flag}\n")