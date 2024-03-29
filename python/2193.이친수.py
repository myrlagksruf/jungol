import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [[0] * 2 for _ in range(n)]
arr[0][0] = 0
arr[0][1] = 1

for i in range(1, n):
    arr[i][1] = arr[i - 1][0]
    arr[i][0] = sum(arr[i - 1])

print(f"{sum(arr[n - 1])}\n")