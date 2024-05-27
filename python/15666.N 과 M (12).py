import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations_with_replacement

N, M = map(int, input().split())

arr = {int(i) for i in input().split()}

for i in combinations_with_replacement(sorted(arr), M):
  print(" ".join(map(str, i)) + "\n")