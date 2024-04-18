import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = [[int(i) for i in input().split()] for _ in range(N)]
way = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dori = deque()
w = []
for ind, i in enumerate(arr):
  for ind2, j in enumerate(i):
    if j == 2:
      dori.append((ind, ind2))
    elif j == 0:
      w.append((ind, ind2))
ma = 0
for p in combinations(w, r=3):
  brr = []
  d = deque(dori)
  count = 0
  for ind, i in enumerate(arr):
    brr.append([])
    for ind2, j in enumerate(i):
      if (ind, ind2) in p:
        brr[ind].append(1)
        continue
      if j == 0:
        count += 1
      brr[ind].append(j)
  while len(d):
    y, x = d.popleft()
    for dx, dy in way:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= M or ny < 0 or ny >= N or brr[ny][nx] != 0:
        continue
      count -= 1
      brr[ny][nx] = 2
      d.append((ny, nx))
  ma = max(ma, count)

print(f"{ma}\n")