import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product

N = 1000000009

c = int(input())

arr = [[0] * 2 for _ in range(100001)]

arr[1][1] = 1
arr[2][0] = 1
arr[2][1] = 1
arr[3][0] = 2
arr[3][1] = 2

for i, j in product(range(4, 100001), range(2)):
    arr[i][j] = (arr[i - 1][1 - j] + arr[i - 2][1 - j] + arr[i - 3][1 - j]) % N

for _ in range(c):
    n = int(input())
    print(f"{arr[n][1]} {arr[n][0]}\n")