import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

n = int(input())

arr = deque(deque(int(i) for i in input().split()) for _ in range(n))

way = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def isout(ind:int):
  return ind < 0 or ind >= n

def make_brr_dx(arr:deque[deque[int]], dx:int):
  brr = deque()
  st = 0
  ma = 0
  if dx < 0:
    st = -1
  for i in range(n):
    temp = deque(j for j in arr[i] if j != 0)
    cur = deque()
    add = cur.append
    pop = temp.popleft
    if dx < 0:
      add = cur.appendleft
      pop = temp.pop
    while len(temp):
      if len(temp) < 2 or temp[st] != temp[st + dx]:
        val = pop()
      else:
        val = pop() + pop()
      ma = max(ma, val)
      add(val)
    for k in range(n - len(cur)):
      add(0)
    brr.append(cur)
  return brr, ma

def make_brr_dy(arr:deque[deque[int]], dy:int):
  brr = deque(deque([0] * n) for _ in range(n))
  st = 0
  ma = 0
  if dy < 0:
    st = -1
  for i in range(n):
    temp = deque(arr[j][i] for j in range(n) if arr[j][i] != 0)
    pop = temp.popleft
    if dy < 0:
      pop = temp.pop
    point = st
    while len(temp):
      if len(temp) < 2 or temp[st] != temp[st + dy]:
        val = pop()
      else:
        val = pop() + pop()
      ma = max(ma, val)
      brr[point][i] = val
      point += dy
  return brr, ma

  
def deep(arr:deque[deque[int]], depth:int, ma:int):
  if depth == 10:
    return ma
  for dx, dy in way:
    if dx == 0:
      brr, ma_temp = make_brr_dy(arr, dy)
      ma = max(ma, ma_temp)
      ma = max(ma, deep(brr, depth + 1, ma))
      continue
    brr, ma_temp = make_brr_dx(arr, dx)
    ma = max(ma, ma_temp)
    ma = max(ma, deep(brr, depth + 1, ma))
  return ma

print(f"{deep(arr, 0, 0)}\n")