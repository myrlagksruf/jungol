import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import lru_cache

N, M = map(int, input().split())

arr = {}
wall = set([1, 1 << M, 1 << 2 * M, 1 << 3 * M])
for i in range(N):
  for ind, j in enumerate(list(input().rstrip())):
    arr[1 << (i * M + ind)] = int(j)

al = (1 << N * M) - 1

@lru_cache(maxsize=None)
def dfs(bit):
  if bit == 0:
    return 0
  temp = bit
  val = temp & -temp
  temp &= ~val
  ma = dfs(temp) + arr[val]

  arr_val = arr[val]
  M_temp = temp
  for i in range(1, M):
    cur = val << i
    if temp & cur == 0 or cur in wall:
      break
    arr_val = 10 * arr_val + arr[cur]
    M_temp &= ~cur
    ma = max(ma, dfs(M_temp) + arr_val)
  
  arr_val = arr[val]
  N_temp = temp
  for i in range(1, N):
    cur = val << (i * M)
    if temp & cur == 0:
      break
    arr_val = 10 * arr_val + arr[cur]
    N_temp &= ~cur
    ma = max(ma, dfs(N_temp) + arr_val)

  return ma

print(f"{dfs(al)}\n")