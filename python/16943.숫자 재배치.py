import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import permutations

A, B = map(int, input().rstrip().split())

X = sorted(list(str(A)), reverse=True)
for i in permutations(X):
  if i[0] == '0':
    continue
  temp = int(''.join(i))
  if temp < B:
    print(f"{temp}\n")
    exit()

print("-1\n")