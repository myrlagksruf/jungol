import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == 'push':
        d.append(cmd[1])
    elif cmd[0] == 'pop':
        val = -1
        if d: val = d.popleft()
        print(f"{val}\n")
    elif cmd[0] == 'size':
        print(f"{len(d)}\n")
    elif cmd[0] == 'empty':
        print(f"{int(len(d) == 0)}\n")
    elif cmd[0] == 'front':
        val = -1
        if d: val = d[0]
        print(f"{val}\n")
    elif cmd[0] == 'back':
        val = -1
        if d: val = d[-1]
        print(f"{val}\n")
