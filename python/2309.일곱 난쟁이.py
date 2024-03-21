import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

candidate = []
for _ in range(9):
    candidate.append(int(input()))

for i in combinations(candidate, 7):
    if sum(i) != 100:
        continue
    print('\n'.join(map(str,sorted(i))))
    break