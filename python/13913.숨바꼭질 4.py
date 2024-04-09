import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, K = map(int, input().split())

di = [-10] * 200000
di[N] = 0

def dfs(n, k):
  global di
  if n >= k:
    for i in range(k, n):
      di[i] = n - i
    return n - k
  if k == 1:
    di[k] = 1
    return 1
  if k % 2 == 1:
    if di[k] == -10:
      di[k] = min(dfs(n, k + 1), dfs(n, k - 1)) + 1
    return di[k]
  if di[k] == -10:
    val2 = dfs(n, k // 2) + 1
    if k - n < val2:
      for i in range(n, k + 1):
        di[i] = i - n
      return di[k]
    di[k] = val2
  return di[k]

dfs(N, K)
cur = K
d = deque([str(K)])
while cur != N:
  score = di[cur]
  arr = [(di[cur + 1], cur + 1)]
  if cur > 0:
    arr.append((di[cur - 1], cur - 1))
  if cur % 2 == 0 and cur != 0:
    arr.append((di[cur // 2], cur // 2))
  for sc, nc in arr:
    if sc + 1 != score:
      continue
    cur = nc
    d.appendleft(str(cur))
    break

print(f"{len(d) - 1}\n")
print(f"{' '.join(d)}\n")