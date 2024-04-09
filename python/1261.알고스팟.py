import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappush, heappop

N, M = map(int, input().split())

mp = [[int(i) for i in input().rstrip()] for _ in range(M)]

h = [(0, 0, 0, 0)]
his = {(0, 0): 0}
way = [(0, 1), (1, 0), (-1, 0), (0, -1)]

while len(h):
  heap_score, s, x, y = heappop(h)
  if (x, y) == (N - 1, M - 1):
    print(f"{s // 1000}\n")
    break
  if his[(x, y)] < heap_score:
    continue
  for dx, dy in way:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    ss = abs(N + M - nx - ny) + mp[ny][nx] * 1000 + s + 1
    if ((nx, ny) not in his or his[(nx, ny)] > ss):
      his[(nx, ny)] = ss
      heappush(h, (ss, s + mp[ny][nx] * 1000, nx, ny))