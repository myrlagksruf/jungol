import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, M, V = map(int, input().split())

mp = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  mp[a].append(b)
  mp[b].append(a)

def dfsbfs(mp, st, isdfs):
  d = deque([st])
  v = [0] * len(mp)
  f = d.popleft
  if isdfs:
    f = d.pop
  his = []
  while len(d):
    val = f()
    if v[val] == 1:
      continue
    his.append(str(val))
    v[val] = 1
    for i in sorted(mp[val], reverse=isdfs):
      if v[i]:
        continue
      d.append(i)
  return ' '.join(his)

print(f"{dfsbfs(mp, V, True)}\n")
print(f"{dfsbfs(mp, V, False)}\n")