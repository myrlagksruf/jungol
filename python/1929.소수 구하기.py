import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
print = sys.stdout.write
s = set(range(2, 1000001))
for i in range(2, 1000001):
    if i not in s:
        continue
    for j in range(i * 2, 1000001, i):
        s.discard(j)
arr = sorted(s)
m, n = map(int, input().split())
m = bisect_left(arr, m)
n = bisect_right(arr, n)
printArr = []
for i in range(m, n):
    printArr.append(str(arr[i]))

print('\n'.join(printArr))