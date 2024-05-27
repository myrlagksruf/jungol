import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import combinations
from functools import reduce

n = int(input())
k = int(n ** 0.5) + 1
s = set(range(2, k))
for i in range(k):
  if i not in s:
    continue
  for j in range(i * 2, k, i):
    s.discard(j)

allval:set[int] = set()
tn = n
for i in s:
  if i > tn:
    break
  if tn % i != 0:
    continue
  while tn % i == 0:
    tn //= i
  allval.add(i)
  if tn == 1:
    break

if tn != 1:
  allval.add(tn)

way = 1
result = 0
for i in range(1, len(allval) + 1):
  for j in combinations(allval, i):
    result += reduce(lambda a, v: a // v, j, n) * way
  way *= -1

print(f"{n - result}\n")