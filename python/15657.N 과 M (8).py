import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product, pairwise
n, m = map(int, input().split())
arr = sorted([int(i) for i in input().rstrip().split()])
print(
    '\n'.join(
        ' '.join(map(str, v)) for v in product(arr, repeat=m) if all(i[0] <= i[1] for i in pairwise(v))
    )
)