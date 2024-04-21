import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappop, heappush

N, M = map(int, input().split())

mp = [input().rstrip() for _ in range(N)]

# score, dist, y, x, can_wall
h:list[tuple[int]] = [(0, 1, 0, 0, 1)]

way = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = {(0, 0, 1):0}

while len(h):
  sc, dist, y, x, can_wall = heappop(h)
  if (y, x) == (N - 1, M - 1):
    print(f"{dist}\n")
    exit()
  if visited[(y, x, can_wall)] < sc:
    continue
  for dy, dx in way:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
      continue
    score = dist + N + M - ny - nx - 1
    if mp[ny][nx] == '0' and ((ny, nx, can_wall) not in visited or visited[(ny, nx, can_wall)] > score):
      visited[(ny, nx, can_wall)] = score
      h.append((score, dist + 1, ny, nx, can_wall))
    if can_wall and mp[ny][nx] == '1' and ((ny, nx, 0) not in visited or visited[(ny, nx, 0)] > score):
      visited[(ny, nx, 0)] = score
      h.append((score, dist + 1, ny, nx, 0))
print("-1\n")