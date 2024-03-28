import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product

n = int(input())
arr = [[[0] * 10 for _ in range(4)] for _ in range(n)]
arr[0][1][0] = 0
arr[0][2][9] = 1

for i in range(1, 9):
    arr[0][0][i] = 1

for i, j in product(range(1, n), range(4)):
    arr[i][j | 1][0] += arr[i - 1][j][1]
    arr[i][j | 2][9] += arr[i - 1][j][8]
    for k in range(1, 9):
        arr[i][j][k] += arr[i - 1][j][k - 1] + arr[i - 1][j][k + 1]

print(f"{sum(arr[n - 1][3]) % 1000000000}\n")