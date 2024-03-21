import sys
from itertools import product
input = sys.stdin.readline
print = sys.stdout.write

def mul_mat(ro, tus):
    li = []
    for i, j in tus:
        tu1 = ro[0][0] * i + ro[0][1] * j
        tu2 = ro[1][0] * i + ro[1][1] * j
        li.append((tu1, tu2))
    return li

def rotate_block(li):
    ro = [[0, -1], [1, 0]]
    result = [li]
    for _ in range(3):
        result.append(mul_mat(ro, result[-1]))
    return result

arr = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    # 기억자
    *rotate_block([(0, 0), (1, 0), (2, 0), (2, 1)]),
    # 반대 기억자
    *rotate_block([(0, 0), (1, 0), (2, 0), (2, -1)]),
    # 번개
    *rotate_block([(0, 0), (1, 0), (1, 1), (2, 1)]),
    # 역번개
    *rotate_block([(0, 0), (1, 0), (1, -1), (2, -1)]),
    # 십자가
    *rotate_block([(0, 0), (0, 1), (0, 2), (1, 1)])
]

n, m = map(int, input().split())
arr_map = []
for _ in range(n):
    arr_map.append([int(i) for i in input().split()])

ma = 0
for i, j, d_blocks in product(range(n), range(m), arr):
    blocks = [(i + dx, j + dy) for dx, dy in d_blocks]
    if any(map(lambda v: v[0] < 0 or v[0] >= n or v[1] < 0 or v[1] >= m, blocks)):
        continue
    ma = max(ma, sum(map(lambda v:arr_map[v[0]][v[1]], blocks)))
print(f"{ma}\n")