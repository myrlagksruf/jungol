import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = sorted([int(input()) for _ in range(n)])

dp = [{} for _ in range(n)]
inds = {}
for ind, i in enumerate(arr):
  inds[i] = ind

# dp[1][arr[1] - arr[0]] = 2
ma = 1
for i in range(1, n):
  for j in range(i):
    dp[i][arr[i] - arr[j]] = max(dp[i].get(arr[i] - arr[j], 2), dp[inds[arr[j]]].get(arr[i] - arr[j], 1) + 1)
    ma = max(ma, dp[i][arr[i] - arr[j]])

print(f"{ma}\n")