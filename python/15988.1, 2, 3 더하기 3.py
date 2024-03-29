import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
N = 1000000009
arr = [0] * 1000001
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 1000001):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % N

for _ in range(n):
    print(f"{arr[int(input())]}\n")
