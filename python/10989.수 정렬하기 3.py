import sys
input = sys.stdin.buffer.readline
print = sys.stdout.write

N = int(input())
arr = [0] * 10001

for _ in range(N):
  arr[int(input())] += 1

for i in range(len(arr)):
  for _ in range(arr[i]):
    print(f"{i}\n")