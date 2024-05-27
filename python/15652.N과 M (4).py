import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations_with_replacement
n, m = map(int, input().split())
print('\n'.join(map(lambda v: ' '.join(map(str, v)), combinations_with_replacement(range(1, n + 1), m))))