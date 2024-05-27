import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations
from collections import Counter

N, M = map(int, input().split())
counter = Counter(int(i) for i in input().split())
arr = [key for key, val in counter.items() for _ in range(min(M, val))]
arr.sort()
dup_check:set[tuple[int]] = set()
for i in combinations(arr, M):
  if i in dup_check:
    continue
  dup_check.add(i)
  print(' '.join(map(str, i)) + '\n')