import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappop, heappush

n = int(input())

arr = [tuple(sorted(int(i) for i in input().split())) for _ in range(n)]

d = int(input())
possible = [(i[0], i[0] + d) for i in arr]

arr.sort(reverse=True, key=lambda v:v[1])

possible.sort()
h:list[int] = []
ma = 0
for sp, ep in possible:
  while len(arr):
    s, e = arr[-1]
    if e > ep:
      break
    arr.pop()
    if s >= sp and e <= ep:
      heappush(h, s)

  while len(h):
    if h[0] < sp:
      heappop(h)
      continue
    break
  if ma < len(h):
    ma = max(ma, len(h))

print(f"{ma}\n")
