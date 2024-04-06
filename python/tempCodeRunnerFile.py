import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, K = map(int, input().split())

d = deque([(N, 0)])

while True:
    n, s = d.popleft()
    if n == K:
        print(f"{s}\n")
        break
    d.append((n + 1, s + 1))
    d.append((n - 1, s + 1))
    if n < 100000:
        d.append((n * 2, s + 1))