import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [0] * (n + 1)

for i in range(2, n + 1):
  arr[i] = arr[i - 1] + 1
  if i % 2 == 0:
    arr[i] = min(arr[i // 2] + 1, arr[i])
  if i % 3 == 0:
    arr[i] = min(arr[i // 3] + 1, arr[i])

cur = n
res = [str(cur)]
while cur != 1:
  x = arr[cur]
  if cur % 2 == 0 and arr[cur // 2] == x - 1:
    cur //= 2
  elif cur % 3 == 0 and arr[cur // 3] == x - 1:
    cur //= 3
  else:
    cur -= 1
  res.append(str(cur))

print(f"{arr[n]}\n")
print(f"{' '.join(res)}\n")