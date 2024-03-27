import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = [int(i) for i in input().rstrip().split()]
cur = arr[-1]
curind = -1
for i in range(-2, -len(arr) - 1, -1):
  if cur < arr[i]:
    curind = i
    cur = arr[i]
    break
  cur = arr[i]
else:
  print("-1\n")
  exit()
ma = (-float("inf"), curind)

for i in range(curind, 0):
  if cur <= arr[i]:
    continue
  if ma[0] < arr[i]:
    ma = (arr[i], i)

arr[curind], arr[ma[1]] = ma[0], cur
arr[curind + 1:] = sorted(arr[curind + 1:], reverse=True)
print(f"{' '.join(map(str,arr))}\n")