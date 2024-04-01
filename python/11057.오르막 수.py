import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

N = 10007

arr = [[0] * 10 for _ in range(n)]

for i in range(10):
  arr[0][i] = 1

for i in range(1, n):
  for j in range(10):
    arr[i][j] = 0
    for k in range(0, j + 1):
      arr[i][j] = (arr[i][j] + arr[i - 1][k]) % N

print(f"{sum(arr[n - 1]) % N}\n")