import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [[0] * 10 for _ in range(n + 1)]
arr[1][0] = 0

for i in range(1, 10):
    arr[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        arr[i][j] = 0
        if j - 1 >= 0:
            arr[i][j] = (arr[i][j] + arr[i - 1][j - 1]) % 1000000000
        if j + 1 <= 9:
            arr[i][j] = (arr[i][j] + arr[i - 1][j + 1]) % 1000000000

print(f"{sum(arr[n]) % 1000000000}\n")