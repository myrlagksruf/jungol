import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import permutations

N, M = map(int, input().split())

print('\n'.join(map(lambda v:' '.join(map(str,v)), sorted(set(permutations([int(i) for i in input().split()], M))))))