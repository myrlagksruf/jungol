import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
N = int(input())

d = deque([(0, 1, 0)])
his = set()
while len(d):
  s, n, c = d.popleft()
  if n == N:
    print(f"{s}\n")
    break
  if n > 1 and (n - 1, c) not in his:
    his.add((n, c))
    d.append((s + 1, n - 1, c))
  if n < 2000:
    if (n, n) not in his:
      his.add((n, n))
      d.append((s + 1, n, n))
    if (n + c, c) not in his:
      his.add((n + c, c))
      d.append((s + 1, n + c, c))