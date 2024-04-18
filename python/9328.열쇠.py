import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

T = int(input())
not_visit_key:dict[str,set[tuple[int]]] = {}
can_visit_key:dict[str,set[tuple[int]]] = {}
mp:list[list[str]] = []
visited:list[list[bool]] = []
first:set[tuple[int]] = set()
key:set[str] = set()
way = [(0, 1), (1, 0), (-1, 0), (0, -1)]
h, w, r = 0, 0, 0
def bfs():
  global not_visit_key, can_visit_key, mp, visited, first, h, w, r
  d = deque(first)
  first.clear()
  while len(d):
    y, x = d.popleft()
    for dy, dx in way:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= w or ny < 0 or ny >= h or visited[ny][nx] or mp[ny][nx] == '*':
        continue
      val = mp[ny][nx]
      if val in key:
        valu = val.upper()
        can_visit_key[valu].discard((ny, nx))
        not_visit_key[valu].discard((ny, nx))
        mp[ny][nx] = '.'
        val = '.'
      if val in can_visit_key and (ny, nx) in can_visit_key[val]:
        continue
      if val == '$':
        r += 1
      if val.isalpha() and val.isupper():
        not_visit_key[val].discard((ny, nx))
        can_visit_key[val].add((ny, nx))
        continue
      elif val.isalpha():
        valu = val.upper()
        if len(can_visit_key[valu]) + len(not_visit_key[valu]) != 0:
          key.add(val)
      visited[ny][nx] = True
      mp[ny][nx] = '.'
      d.append((ny, nx))

def update_first():
  global not_visit_key, can_visit_key, mp, visited, first, h, w, r
  for i in key:
    v = i.upper()
    if v not in can_visit_key:
      can_visit_key[v] = set()
      not_visit_key[v] = set()
    for j in can_visit_key[v]:
      mp[j[0]][j[1]] = '.'
      visited[j[0]][j[1]] = True
      first.add(j)
    can_visit_key[v].clear()

for _ in range(T):
  h, w = map(int, input().split())
  r = 0
  not_visit_key.clear()
  can_visit_key.clear()
  mp.clear()
  visited.clear()
  first.clear()
  key.clear()
  for y in range(h):
    temp = []
    visit = []
    for x, i in enumerate(input().rstrip()):
      temp.append(i)
      if i == '*':
        visit.append(False)
        continue
      if (y == 0 or y == h - 1 or x == 0 or x == w - 1) and (i == '.' or i.islower() or i == '$'):
        visit.append(True)
        if i == '$':
          temp[x] = '.'
          r += 1
        first.add((y, x))
      else:
        visit.append(False)
      if i == '.' or i == '$':
        continue
      u = i.upper()
      if u not in can_visit_key:
        not_visit_key[u] = set()
        can_visit_key[u] = set()
      if (y == 0 or y == h - 1 or x == 0 or x == w - 1) and i.islower():
        key.add(i)
        temp[x] = '.'
      elif (y == 0 or y == h - 1 or x == 0 or x == w - 1) and i.isupper():
        can_visit_key[i].add((y, x))
      elif i.isupper():
        not_visit_key[i].add((y, x))
    mp.append(temp)
    visited.append(visit)
  key = key | set(input().rstrip())
  key.discard('0')
  update_first()
  while len(first):
    bfs()
    update_first()

  print(f"{r}\n")