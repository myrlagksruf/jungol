import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations
result = []
while True:
    n = input().rstrip().split()
    if n[0] == '0':
        break
    for i in combinations(n[1:], 6):
        result.append(' '.join(i))
    result.append('')

print('\n'.join(result))