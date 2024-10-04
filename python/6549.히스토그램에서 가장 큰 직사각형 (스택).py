import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

def solve(h:list[int]):
  ma = 0
  d = deque()
  def update(ind:int, i:int = 0):
    nonlocal ma
    prepre = ind
    while len(d):
      preind, val = d[-1]
      if val == i:
        break
      if val < i:
        d.append((prepre, i))
        break
      ma = max(ma, (ind - preind) * val)
      d.pop()
      prepre = preind
      if len(d) == 0:
        d.append((prepre, i))
        break
  
  for ind, i in enumerate(h):
    if len(d) == 0:
      d.append((ind, i))
      continue
    update(ind, i)
  update(len(h))
  return ma


while True:
  n, *h = map(int, input().split())
  if n == 0:
    break
  print(f"{solve(h)}\n")