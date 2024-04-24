import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N)]
arr = [[int(i) for i in input().split()] for _ in range(N)]

if arr[0][0] <= K:
  dp[0][arr[0][0]] = arr[0][1]

for ind in range(1, N):
  for i in range(arr[ind][0], K + 1):
    dp[ind][i] = max(dp[ind - 1][i], dp[ind - 1][i - arr[ind][0]] + arr[ind][1])
  for i in range(min(arr[ind][0], K + 1)):
    dp[ind][i] = dp[ind - 1][i]

print(f"{max(dp[N - 1])}\n")