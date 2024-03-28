import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 6)
arr = [0] * 1000001

n = int(input())

def get_min_val(n):
  if n == 1:
    return 0
  res = []
  if n % 2 == 0:
    if not arr[n // 2]:
      arr[n // 2] = get_min_val(n // 2)
    res.append(arr[n // 2] + 1)
  if n % 3 == 0:
    if not arr[n // 3]:
      arr[n // 3] = get_min_val(n // 3)
    res.append(arr[n // 3] + 1)
  if not arr[n - 1]:
    arr[n - 1] = get_min_val(n - 1)
  res.append(arr[n - 1] + 1)
  return min(res)

print(f"{get_min_val(n)}\n")