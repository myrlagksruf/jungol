import sys
input = sys.stdin.readline
print = sys.stdout.write

str1 = input().rstrip()
str2 = input().rstrip()

arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for ind1, i in enumerate(str1, start=1):
  for ind2, j in enumerate(str2, start=1):
    if i == j:
      arr[ind1][ind2] = arr[ind1 - 1][ind2 - 1] + 1
      continue
    arr[ind1][ind2] = max(arr[ind1 - 1][ind2], arr[ind1][ind2 - 1])

print(f"{max(arr[len(str1)])}\n")