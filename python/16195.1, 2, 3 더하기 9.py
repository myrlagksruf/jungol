import sys
input = sys.stdin.readline
print = sys.stdout.write
from math import ceil

N = 1000000009

c = int(input())

arr = [[0] * 1001 for _ in range(1001)]
brr = [[0] * 1001 for _ in range(1001)]

arr[1][1] = 1
arr[2][1] = 1
arr[2][2] = 1
arr[3][1] = 1
arr[3][2] = 2
arr[3][3] = 1

brr[1][1] = 1
brr[2][1] = 1
brr[2][2] = 2
brr[3][1] = 1
brr[3][2] = 3
brr[3][3] = 4

for i in range(4, 1001):
    for j in range(ceil(i / 3), i + 1):
        arr[i][j] = (arr[i - 1][j - 1] + arr[i - 2][j - 1] + arr[i - 3][j - 1]) % N
        brr[i][j] = (brr[i][j - 1] + arr[i][j]) % N

for _ in range(c):
    n, m = map(int, input().split())
    print(f"{brr[n][m]}\n")