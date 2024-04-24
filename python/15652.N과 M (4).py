import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product, pairwise
n, m = map(int, input().split())
print(
    '\n'.join(
        ' '.join(map(str, v)) for v in product(range(1, n + 1), repeat=m) if all(i[0] <= i[1] for i in pairwise(v))
    )
)