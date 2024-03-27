import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import lru_cache

N, S = map(int, input().split())
count = 0
s_nums = {(1 << ind): int(i) for ind, i in enumerate(input().split())}

@lru_cache(maxsize=None)
def get_val(i):
    if i in s_nums:
        return s_nums[i]
    val = i & -i
    i &= i - 1
    return get_val(i) + s_nums[val]

for i in range(1, 1 << N):
    val = get_val(i)
    if val == S:
        count += 1

print(f"{count}\n")