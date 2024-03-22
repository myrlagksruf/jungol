import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])

pick = set()
don_pick = {}
ma = -10000000
way = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

def add_pick(n1, m1):
    global don_pick, pick
    pick.add((n1, m1))
    for dn, dm in way:
        n2 = n1 + dn
        m2 = m1 + dm
        if n2 < 0 or n2 >= n or m2 < 0 or m2 >= m:
            continue
        don_pick[(n2, m2)] = don_pick.get((n2, m2), 0) + 1

def remove_pick(n1, m1):
    global don_pick, pick
    pick.discard((n1, m1))
    for dn, dm in way:
        n2 = n1 + dn
        m2 = m1 + dm
        if n2 < 0 or n2 >= n or m2 < 0 or m2 >= m:
            continue
        don_pick[(n2, m2)] -= 1
        if don_pick[(n2, m2)] == 0:
            don_pick.pop((n2, m2))


def pick_map(depth = 0):
    global ma, arr
    if depth == k:
        ma = max(ma, sum(arr[i][j] for i, j in pick))
        return
    st = 0
    if len(pick) != 0:
        n1, m1 = max(pick)
        st = n1 * m + m1 + 1
    for i in range(st, n * m):
        n1 = i // m
        m1 = i % m
        if (n1, m1) in don_pick:
            continue
        add_pick(n1, m1)
        pick_map(depth + 1)
        remove_pick(n1, m1)

pick_map()

print(f"{ma}\n")