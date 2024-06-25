import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cmp_to_key, partial
from collections import deque

N = int(input())

arr = [tuple(int(i) for i in input().split()) for _ in range(N)]

st = min(arr)

def ccw(st: tuple[int], p1: tuple[int], p2: tuple[int]) -> int:
  cross_product = (p1[0] - st[0]) * (p2[1] - st[1]) - (p2[0] - st[0]) * (p1[1] - st[1])
  if cross_product > 0:
    return 1
  elif cross_product < 0:
    return -1
  else:
    return 0
arr.sort()
arr.sort(key=cmp_to_key(partial(ccw, st)))
arr = [st, *[i for i in arr if i != st], st]
shell = deque()
for i in arr:
  if len(shell) < 2:
    shell.append(i)
    continue
  while len(shell) >= 2 and ccw(shell[-2], shell[-1], i) >= 0 :
    shell.pop()
  shell.append(i)
# print(f"{arr}\n")
# print(f"{shell}\n")
print(f"{len(shell) - 1}\n")
