import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [int(i) for i in input().split()]
dp = [[0, 0] for _ in range(n)]
dp[0][0] = arr[0]

ma = arr[0]
for i in range(1, n):
    dp[i][0] = max(arr[i] + dp[i - 1][0], arr[i])
    dp[i][1] = max(arr[i] + dp[i - 1][1], dp[i - 1][0])
    ma = max(ma, dp[i][0], dp[i][1])

print(f"{ma}\n")
