import sys
input = sys.stdin.readline
print = sys.stdout.write
N, K = map(int, input().split())

def dfs(n, k):
    if n >= k:
        return n - k
    if k == 1:
        return 1
    if k % 2 == 1:
        return min(dfs(n, k + 1), dfs(n, k - 1)) + 1
    return min(k - n, dfs(n, k // 2))

print(f"{dfs(N, K)}\n")

