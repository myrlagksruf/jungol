import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N, M = map(int, input().split())
qu = deque()
mp = []
ma = 0
way = [(0, 1), (1, 0), (-1, 0), (0, -1)]
good = 0
for i in range(M):
    temp = [int(k) for k in input().split()]
    for j in range(N):
        if temp[j] != 0:
            good += 1
        if temp[j] != 1:
            continue
        qu.append((i, j, 0))
    mp.append(temp)

while len(qu) and good != N * M:
    i, j, score = qu.popleft()
    for dx, dy in way:
        y = i + dy
        x = j + dx
        if x < 0 or x >= N or y < 0 or y >= M or mp[y][x] != 0:
            continue
        mp[y][x] = 1
        good += 1
        ma = max(ma, score + 1)
        qu.append((y, x, score + 1))

if good != N * M:
    print("-1\n")
else:
    print(f"{ma}\n")