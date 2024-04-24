import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product
n, m = map(int, input().split())
print('\n'.join(map(lambda v: ' '.join(map(str, v)), product(range(1, n + 1), repeat=m))))