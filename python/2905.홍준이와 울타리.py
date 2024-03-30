import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

n, x = map(int, input().split())
ultas = [int(i) for i in input().split()]

mono = deque()

top = (0, -1)
area = 0
su = 0
roll = 0
mi = 0
premi = 0

for ind, val in enumerate(ultas):
    su += val
    while mono and ultas[mono[-1]] > val:
        mono.pop()

    mono.append(ind)

    if ind < x - 1:
        continue

    if ind - mono[0] >= x:
        mono.popleft()

    mi = ultas[mono[0]]

    if top[0] < mi or ind - top[1] >= x:
        print(f"{ind}\n")
        area += mi * x
        roll += 1
        if ind - top[1] < x:
            area -= (x - ind + top[1]) * top[0]
        top = (mi, ind)
        
    premi = mi

ind = len(ultas) - 1
if ind != top[1]:
    area += mi * x
    roll += 1
    if ind - top[1] < x:
        area -= (x - ind + top[1]) * top[0]

print(f"{su - area}\n{roll}\n")


