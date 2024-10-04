import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

n = int(input())
arr = deque(int(input()) for _ in range(n))

res:list[str] = []
d = deque()
for i in range(1, n + 1):
  d.append(i)
  res.append("+")
  while len(d) and len(arr) and d[-1] == arr[0]:
    arr.popleft()
    d.pop()
    res.append("-")

if len(arr) or len(d):
  print("NO")
  exit()

print("\n".join(res))