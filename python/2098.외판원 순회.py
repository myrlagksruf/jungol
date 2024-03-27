import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import lru_cache

n = int(input())
arr = {}

for i in range(n):
    arr[1 << i] = { (1 << j): int(val) for j, val in enumerate(input().split()) }

@lru_cache(maxsize=None)
def dfs(bit, last):
    if bit == 0:
        val = arr[last][1]
        if val == 0:
            return float("inf")
        return val
    loop_bit = bit
    ma = float("inf")
    while loop_bit:
        val = loop_bit & -loop_bit
        loop_bit &= (loop_bit - 1)
        if arr[last][val] == 0:
            continue
        ma = min(ma, dfs(bit & ~val, val) + arr[last][val])
    return ma
    
print(f"{dfs((1 << n) - 2, 1)}\n")