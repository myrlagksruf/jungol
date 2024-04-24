import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import permutations
n, m = map(int, input().split())
arr = sorted([int(i) for i in input().rstrip().split()])
print('\n'.join(map(lambda v: ' '.join(map(str, v)), permutations(arr, m))))