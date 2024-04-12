import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]

first_r = (0, 0)
first_b = (0, 0)

for ind, i in enumerate(arr):
  for ind2, j in enumerate(i):
    if j == 'R':
      first_r = (ind, ind2)
      arr[ind][ind2] = '.'
    elif j == 'B':
      first_b = (ind, ind2)
      arr[ind][ind2] = '.'

# score, (Ry, Rx), (By, Bx)
h = deque([(0, first_r, first_b)])

way = [
  (1, 0),
  (-1, 0),
  (0, 1),
  (0, -1)
]

his = set([(first_r, first_b)])

def god(r, b, d):
  dx, dy = d
  move = (r[0], r[1], 'r')
  other = (b[0], b[1], 'b')
  dr = dx if dx != 0 else dy
  indr = 1 if dx != 0 else 0
  ed = M if dx != 0 else N
  if dr * (r[indr] - b[indr]) < 0:
    move, other = other, move
  flag = 0
  st = move[indr] + dr
  if dr < 0:
    ed = -1
  for i in range(st, ed, dr):
    if dx == 0:
      val = arr[i][move[1]]
    else:
      val = arr[move[0]][i]
    if val == '#':
      move = list(move)
      move[indr] = i - dr
      move = tuple(move)
      break
    elif val == 'O':
      if move[2] == 'b':
        return (move, other, 2)
      move = (-1, -1, 'r')
      flag = 1
      break
  else:
    move = list(move)
    move[indr] = ed - dr
    move = tuple(move)
  
  st = other[indr] + dr

  for i in range(st, ed, dr):
    if dx == 0:
      val = arr[i][other[1]]
      val2 = (i, other[1])
    else:
      val = arr[other[0]][i]
      val2 = (other[0], i)
    if val == '#' or val2 == (move[0], move[1]):
      other = list(other)
      other[indr] = i - dr
      other = tuple(other)
      break
    elif val == 'O':
      if other[2] == 'b':
        return (move, other, 2)
      return (move, other, 1)
  else:
    other = list(other)
    other[indr] = ed - dr
    other = tuple(other)
  
  r = (move[0], move[1])
  b = (other[0], other[1])
  if move[2] == 'b':
    r, b = b, r
  return (r, b, flag)
    
while len(h):
  score, r, b = h.popleft()
  if score == 10:
    continue
  for d in way:
    nr, nb, f = god(r, b, d)
    if f == 1:
      print(f"{score + 1}\n")
      exit()
    if f == 2 or (nr, nb) in his:
      continue
    his.add((nr, nb))
    h.append((score + 1, nr, nb))

print(f"-1\n")