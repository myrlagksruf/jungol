import sys
input = sys.stdin.readline
print = sys.stdout.write

N = 1000000009
n = int(input())

arr = [0] * 50001
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 50001):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % N

for _ in range(n):
    v = int(input())
    if v == 1:
        print(f"1\n")
        continue
    elif v == 2:
        print(f"2\n")
        continue
    elif v == 3:
        print(f"2\n")
        continue
    print(f"{(arr[v // 2] + arr[v // 2 - 1]) % N}\n")
