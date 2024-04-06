import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappush, heappop

way = [
    (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1)
]

for _ in range(int(input())):
    I = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    h = [((abs(s1 - e1) + abs(s2 - e2)) // 3, s1, s2, 0)]
    his = [[0] * I for _ in range(I)]
    while len(h):
        _, s1, s2, score = heappop(h)
        if his[s2][s1] == 1:
            continue
        his[s2][s1] = 1
        if (s1, s2) == (e1, e2):
            print(f"{score}\n")
            break
        for dx, dy in way:
            x = s1 + dx
            y = s2 + dy
            if x < 0 or x >= I or y < 0 or y >= I or his[y][x] == 1:
                continue
            heappush(h, ((abs(x - e1) + abs(y - e2)) // 3 + score + 1, x, y, score + 1))