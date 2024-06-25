import sys
input = sys.stdin.readline
print = sys.stdout.write
P = 10007 
st = input().rstrip()
l = len(st)
dp = [[0] * l for _ in range(l)]

def solve(s:int, e:int):
  if s == e:
    return 1
  if s > e:
    return 0
  if dp[s][e] != 0:
    return dp[s][e]
  res = (solve(s + 1, e) + solve(s, e - 1) - solve(s + 1, e - 1)) % P
  if st[s] == st[e]:
    res = (res + solve(s + 1, e - 1) + 1) % P
  dp[s][e] = res
  return dp[s][e]
print(f"{solve(0, l - 1)}\n")