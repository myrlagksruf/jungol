import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

nums = [int(i) for i in input().split()]
arr = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]

m = int(input())

def is_pal(a:int, b:int):
  global arr
  if a == b:
    return 1
  if b - a == 1:
    return int(nums[a - 1] == nums[b - 1])
  if nums[a - 1] != nums[b - 1]:
    arr[a][b] = 0
    return 0
  if arr[a][b] == -1:
    arr[a][b] = is_pal(a + 1, b - 1)
  return arr[a][b]

for _ in range(m):
  print(f"{is_pal(*map(int, input().split()))}\n")