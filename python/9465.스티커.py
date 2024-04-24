import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

def solution(n:int):
  arr1 = [int(i) for i in input().split()]
  arr2 = [int(i) for i in input().split()]
  dp = [[0] * 3 for _ in range(n)]
  dp[0][1] = arr1[0]
  dp[0][2] = arr2[0]
  for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + arr1[i]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + arr2[i]
  return max(dp[n - 1])
  

for _ in range(T):
  print(f"{solution(int(input()))}\n")