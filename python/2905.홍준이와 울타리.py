import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

n, x = map(int, input().split())
ultas = [int(i) for i in input().split()]

mono = deque()

area = 0
su = 0
mi = 0
tops = (0, -1)
reals = [tops]
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

    
    if (tops[0] > mi or tops[1] - reals[-1][1] >= x) and reals[-1] != tops:
        reals.append(tops)
        
    if reals[-1][0] < mi:
        reals.append((mi, ind))
    tops = (mi, ind)

if reals[-1][1] != tops[1]:
    reals.append(tops)

for i in range(1, len(reals)):
    premi, preind = reals[i - 1]
    mi, ind = reals[i]
    area += mi * x
    if ind - preind < x:
        area -= (x - ind + preind) * min(premi, mi)
    top = (mi, ind)

# print(f"{reals}\n")
print(f"{su - area}\n{len(reals) - 1}\n")