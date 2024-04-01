import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
dp = [0] * n
pdp = [0] * n
tris = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
  pdp[0] = dp[0]
  dp[0] += tris[i][0]
  for j in range(1, i):
    pdp[j] = dp[j]
    dp[j] = max(pdp[j - 1], pdp[j]) + tris[i][j]
  dp[i] = pdp[i - 1] + tris[i][i]

print(f"{max(dp)}\n")