import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [[0] * 3 for _ in range(10001)]
for i in range(1, 4):
    for j in range(i):
        arr[i][j] = 1

for i in range(4, 10001):
    for j in range(3):
        arr[i][j] = 0
        for k in range(j + 1):
            arr[i][j] += arr[i - j - 1][k]

for _ in range(n):
    print(f"{sum(arr[int(input())])}\n")
