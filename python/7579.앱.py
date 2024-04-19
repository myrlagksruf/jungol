import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

m = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

dp = [[0] * 10001 for _ in range(N)]
dp[0][c[0]] = m[0]
for i in range(1, N):
  dp[i][c[i]] = m[i]
  for j in range(10001):
    dp[i][j] = max(dp[i - 1][j], dp[i][j])
    if j < c[i]:
      continue
    dp[i][j] = max(dp[i][j], dp[i - 1][j - c[i]] + m[i])

for i in range(10001):
  if dp[N - 1][i] < M:
    continue
  print(f"{i}\n")
  break