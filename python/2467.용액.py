import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_left

n = int(input())

arr = sorted([int(i) for i in input().split()])

mini = (3000000000, 0, 0)

for ind, i in enumerate(arr):
  find_ind = bisect_left(arr, -i)
  if find_ind >= len(arr):
    find_ind = len(arr) - 1
    if ind == find_ind:
      break
  if ind == find_ind:
    find_ind += 1
  elif ind > find_ind:
    break
  check_arr = [mini, (abs(i + arr[find_ind]), i, arr[find_ind])]
  if find_ind - 1 > ind:
    check_arr.append((abs(i + arr[find_ind - 1]), i, arr[find_ind - 1]))
  if find_ind + 1 < len(arr) and find_ind + 1 != ind:
    check_arr.append((abs(i + arr[find_ind + 1]), i, arr[find_ind + 1]))
  mini = min(check_arr)

print(f"{' '.join(map(str, sorted(mini[1:])))}\n")