import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations
mo = 'aeiou'
n, m = map(int, input().split())
posible = set(input().rstrip().split())
realmo = { i for i in posible if i in mo }
posible -= realmo
result = []

for i in range(1, min(len(realmo) + 1, n - 1)):
    for j in combinations(realmo, i):
        for k in combinations(posible, n - i):
            result.append(''.join(sorted(k + j)))

print('\n'.join(sorted(result)))