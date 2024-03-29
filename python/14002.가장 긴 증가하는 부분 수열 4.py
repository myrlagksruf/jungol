import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_left

n = int(input())
arr = [int(i) for i in input().split()]
def lengthOfLIS(nums):
    tails = []
    prevs = [-1] * len(nums)
    for ind, num in enumerate(nums):
        left = bisect_left(tails, (num, -ind), key=lambda v: (v[0], -v[1]))
        if left == len(tails):
            tails.append((num, ind))
        else:
            tails[left] = (num, ind)
        if left > 0:
            prevs[ind] = tails[left - 1][1]
    return tails, prevs

tails, prevs = lengthOfLIS(arr)

result = [str(tails[-1][0])]
cur_ind = tails[-1][1]
while True:
    prev_ind = prevs[cur_ind]
    if prev_ind == -1:
        break
    result.append(str(arr[prev_ind]))
    cur_ind = prev_ind

print(f"{len(tails)}\n")
print(f"{' '.join(result[::-1])}\n")