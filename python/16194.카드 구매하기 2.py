import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [0] * (n + 1)
cards = [int(i) for i in input().split()]

for i in range(1, n + 1):
  arr[i] = cards[i - 1]
  for j in range(1, i):
    arr[i] = min(arr[i - j] + cards[j - 1], arr[i])

print(f"{arr[n]}\n")