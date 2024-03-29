import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [int(i) for i in input().split()]
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i] + dp[i - 1], arr[i])

print(f"{max(dp)}\n")
