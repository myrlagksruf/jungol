import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappush, heappop

N, M = map(int, input().split())

mp = [list(input().rstrip()) for _ in range(N)]

way = [(0, 1), (1, 0), (0, -1), (-1, 0)]

d = [(N + M + 1, 0, 0, 1)]
while len(d):
  _, y, x, p = heappop(d)
  if mp[y][x] == '0':
    continue
  mp[y][x] = '0'
  if (y, x) == (N - 1, M - 1):
    print(f"{p}\n")
    break
  for dx, dy in way:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= M or ny < 0 or ny >= N or mp[ny][nx] == '0':
      continue
    heappush(d, (p + 1 + N + M - ny - nx, ny, nx, p + 1))