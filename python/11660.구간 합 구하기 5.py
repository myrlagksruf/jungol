import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
  for y, j in enumerate(map(int, input().split()), start=1):
    arr[y][x] = j + arr[y - 1][x] + arr[y][x - 1] - arr[y - 1][x - 1]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(f"{arr[y2][x2] - arr[y1 - 1][x2] - arr[y2][x1 - 1] + arr[y1 - 1][x1 - 1]}\n")