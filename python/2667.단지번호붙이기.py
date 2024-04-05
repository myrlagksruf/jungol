import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N = int(input())

mp = [list(input().rstrip()) for _ in range(N)]
visit_num = 0 
for i in mp:
  visit_num += i.count('0')

way = [(0, 1), (1, 0), (0, -1), (-1, 0)]

result = []
for i in range(N * N):
  y = i // N
  x = i % N
  if mp[y][x] == '0':
    continue
  val = 1
  mp[y][x] = '0'
  d = deque([(y, x)])
  while len(d):
    y, x = d.popleft()
    for dx, dy in way:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= N or ny < 0 or ny >= N or mp[ny][nx] == '0':
        continue
      mp[ny][nx] = '0'
      val += 1
      d.append((ny, nx))
  result.append(val)
  visit_num += val
  if visit_num == N * N:
    break

print(f"{len(result)}\n")
print('\n'.join(map(str,sorted(result))))