from functools import lru_cache
import sys
input = sys.stdin.readline
print = sys.stdout.write

@lru_cache(maxsize=None)
def get123(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return get123(n - 1) + get123(n - 2) + get123(n - 3)
T = int(input())
for _ in range(T):
    print(f"{get123(int(input()))}\n")
    