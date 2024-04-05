import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

v = [0] * (N + 1)

answer = 0

for i in range(1, N + 1):
  if v[i] == 1:
    continue
  answer += 1
  d = deque([i])
  while len(d):
    val = d.popleft()
    for j in arr[val]:
      if v[j] == 1:
        continue
      v[j] = 1
      d.append(j)

print(f"{answer}\n")