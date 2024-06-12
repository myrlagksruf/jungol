import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 6 + 1)

N = int(input())

arr = [set() for _ in range(N + 1)]
dp = [[-1, -1] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[1] = True

for _ in range(N - 1):
  a, b = map(int, input().split())
  arr[a].add(b)
  arr[b].add(a)


def dfs(x):
  if len(arr[x]) == 0:
    dp[x][0] = 0
    dp[x][1] = 1
    return
  dp[x][0] = 0
  dp[x][1] = 1
  for i in arr[x]:
    if visited[i]:continue
    visited[i] = True
    if dp[i][0] == -1:
      dfs(i)
    dp[x][0] += dp[i][1]
    dp[x][1] += min(dp[i])

dfs(1)

print(f"{min(dp[1])}\n")