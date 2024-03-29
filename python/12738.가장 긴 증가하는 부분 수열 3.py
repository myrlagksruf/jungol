import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_right

n = int(input())
arr = [int(i) for i in input().split()]
def lengthOfLIS(nums):
    tails = []
    for num in nums:
        left = bisect_right(tails, num)
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)

print(f"{lengthOfLIS(arr)}\n")