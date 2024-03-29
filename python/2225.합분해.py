import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product
from math import comb

N =  1000000000
n, k = map(int, input().split())

# arr = [[0] * (k + 1) for _ in range(n + 1)]

# arr[0][1] = 1

# for i in range(1, n + 1):
#     arr[i][1] = 1
#     for j, t in product(range(2, k + 1), range(i)):
#         arr[i][j] = (arr[i][j] % N + arr[i - t][j - 1] % N) % N

# print(f"{sum(arr[n]) % N}\n")

print(f"{comb(n + k - 1, n) % N}\n")