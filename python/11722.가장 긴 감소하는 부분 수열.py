import sys
input = sys.stdin.readline
print = sys.stdout.write
from bisect import bisect_right

n = int(input())
arr = [int(i) for i in input().split()]
def lengthOfSIS(nums):
    tails = []
    for ind, num in enumerate(nums[::-1]):
        left = bisect_right(tails, (num, -ind), key=lambda v:(v[0], -v[1]))
        if left == len(tails):
            tails.append((num, ind))
        else:
            tails[left] = (num, ind)
    return len(tails)

print(f"{lengthOfSIS(arr)}\n")