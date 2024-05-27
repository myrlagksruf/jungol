import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
k = int(input())

def count_n(num:int):
  result = 0
  for i in range(1, min(n, num) + 1):
    result += min(num // i, n)
  return result

left = 0
right = n * n

while left < right:
  mid = (left + right) // 2
  if count_n(mid) < k:
    left = mid + 1
  else:
    right = mid

print(f"{left}\n")