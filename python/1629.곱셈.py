import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache

A, B, C = map(int, input().split())

@cache
def gob(a:int, b:int):
  if b == 0:
    return 1
  if b % 2 == 1:
    return (gob(a, b // 2) * gob(a, b // 2) * a) % C
  return (gob(a, b // 2) * gob(a, b // 2)) % C

print(f"{gob(A, B)}\n")