import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product

N, M = map(int, input().split())

arr = {int(i) for i in input().split()}

for i in product(sorted(arr), repeat=M):
  print(" ".join(map(str, i)) + "\n")