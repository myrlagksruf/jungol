import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = [tuple(int(i) for i in input().split()) for _ in range(n)]
arr.append(arr[0])

temp = [0, 0]
for i in range(n):
  temp[0] += arr[i][0] * arr[i + 1][1]
  temp[1] += arr[i + 1][0] * arr[i][1]

print(f"{abs(temp[0] - temp[1]) / 2:.1f}\n")