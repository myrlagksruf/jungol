import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = []

for _ in range(N):
    arr.append([int(i) for i in input().split()])

def get_max(arr):
    dp = [0] * (len(arr) + 1)
    for ind, (t, p) in enumerate(arr):
        next_day = ind + t
        if next_day < len(dp):
            dp[next_day] = max(dp[next_day], dp[ind] + p)
        dp[ind + 1] = max(dp[ind + 1], dp[ind])
    return dp[-1]
    
print(f"{get_max(arr)}\n")