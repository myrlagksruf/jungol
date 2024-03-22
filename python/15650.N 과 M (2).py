import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations
n, m = map(int, input().split())
print('\n'.join(map(lambda v: ' '.join(map(str, v)), combinations(range(1, n + 1), m))))