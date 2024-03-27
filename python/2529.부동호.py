import sys
input = sys.stdin.readline
print = sys.stdout.write
from string import digits

n = int(input())

arr = input().rstrip().split()
result = []

# from itertools import permutations, pairwise
# for i in permutations(digits, n + 1):
#   for j, k in zip(pairwise(i), arr):
#     if not (k == "<" and j[0] < j[1] or k == ">" and j[0] > j[1]):
#       break
#   else:
#     result.append(i)

# print(f"{''.join(max(result))}\n{''.join(min(result))}\n")

def get_n(remain:tuple[int], res:tuple[int], s:int, e:int):
  global result
  if len(res) == n:
    for i in range(s, e):
      result.append(res + (remain[i],))
    return
  for i in range(s, e):
    ss = 0
    ee = len(remain) - 1
    if arr[len(res)] == "<":
      ss = i
    else:
      ee = i
    get_n(remain[:i] + remain[i + 1:], res + (remain[i],), ss, ee)

get_n(digits, tuple(), 0, 10)

print(f"{''.join(max(result))}\n{''.join(min(result))}\n")