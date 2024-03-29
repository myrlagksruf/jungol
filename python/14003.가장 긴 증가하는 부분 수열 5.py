import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_left

n = int(input())
arr = [int(i) for i in input().split()]
def lengthOfLIS(nums):
    tails = []
    logs = [0] * len(nums)
    for ind, num in enumerate(nums):
        left = bisect_left(tails, (num, -ind), key=lambda v: (v[0], -v[1]))
        if left == len(tails):
            tails.append((num, ind))
        else:
            tails[left] = (num, ind)
        if left > 0:
            logs[ind] = left
    return logs

logs1 = lengthOfLIS(arr)
logs2 = lengthOfLIS(arr[::-1])
ma = 0
for i, j in zip(logs1, logs2[::-1]):
    ma = max(ma, i + j)

print(f"{ma + 1}\n")