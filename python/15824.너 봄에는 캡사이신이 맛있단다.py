import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = sorted([int(i) for i in input().split()])
P = 1000000007
dp = [0] * 300001
def get_gob(r:int):
  global dp
  if r == 0:
    return 1
  if dp[r] != 0:
    return dp[r]
  if r % 2 == 0:
    dp[r] = get_gob(r // 2) * get_gob(r // 2) % P
  else:
    dp[r] = (get_gob(r // 2) * get_gob(r // 2) % P) * 2 % P
  return dp[r]

acc = 0
for i in range(N):
  acc += (arr[-1 - i] - arr[i]) * (get_gob(N - i - 1) - 1) % P
  acc %= P

print(f"{acc}\n")
