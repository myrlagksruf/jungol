import sys
input = sys.stdin.readline
print = sys.stdout.write
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 6)

# @lru_cache(maxsize=None)
# def dfs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return (dfs(n - 1) % 10007 + dfs(n - 2) % 10007) % 10007

# print(f"{dfs(int(input()))}\n")
a = 1
b = 2
c = 3
n = int(input())
if n == 1:
    print(f"{a}\n")
    exit()
elif n == 2:
    print(f"{b}\n")
    exit()

for i in range(n - 3):
    a, b, c = b, c, (b + c) % 10007

print(f"{c}\n")