import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = [int(i) for i in input().split()]

dp = [0] * n

for i in range(n):
  dp[i] = nums[i]
  for j in range(i):
    if nums[j] >= nums[i]:
      continue
    dp[i] = max(dp[i], dp[j] + nums[i])

print(f"{max(dp)}\n")