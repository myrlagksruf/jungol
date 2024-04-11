import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_left

n = int(input())

arr = sorted([int(i) for i in input().split()])

mini = (3000000000, 0, 0, 0)
for ori_ind, val in enumerate(arr):
  for ind in range(ori_ind + 1, len(arr)):
    val2 = arr[ind]
    find_ind = bisect_left(arr, -val - val2, lo=ind + 1)
    if find_ind >= len(arr):
      find_ind = len(arr) - 1
      if ind == find_ind:
        break
    check_arr = [mini, (abs(val2 + arr[find_ind] + val), val2, val, arr[find_ind])]
    if find_ind - 1 > ind:
      check_arr.append((abs(val2 + arr[find_ind - 1] + val), val2, val, arr[find_ind - 1]))
    if find_ind + 1 < len(arr) and find_ind + 1 != ind:
      check_arr.append((abs(val2 + arr[find_ind + 1] + val), val2, val, arr[find_ind + 1]))
    mini = min(check_arr)

print(f"{' '.join(map(str, sorted(mini[1:])))}\n")