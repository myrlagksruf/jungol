import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import accumulate

n = int(input())
dup_check = set(range(-10, 11))
sign = input().rstrip()
di = {}
cnt = 0
for i in range(n):
  for j in range(i, n):
    di[(i, j)] = sign[cnt]
    cnt += 1
arr = []
def guess(num, tu):
  # global dup_check
  if num == n:
    return tu
  s = 1
  e = 11
  step = 1
  if di[(num, num)] == '-':
    s = -1
    e = -11
    step = -1
  elif di[(num, num)] == '0':
    # if 0 not in dup_check:
    #   return None
    # dup_check.discard(0)
    return guess(num + 1, tu + (0,))
  arr = []
  sum_arr = sum(tu)
  count = 0
  for j in tu:
    arr.append(sum_arr - count)
    count += j
  for i in range(s, e, step):
    # if i not in dup_check:
    #   continue
    for j in range(num):
      if not (arr[j] + i > 0 and di[(j, num)] == '+' or \
        arr[j] + i < 0 and di[(j, num)] == '-' or \
        arr[j] + i == 0 and di[((j, num))] == '0'):
        break
    else:
      # dup_check.discard(i)
      res = guess(num + 1, tu + (i,))
      # dup_check.add(i)
      if res:
        return res
  return None
  
print(f"{' '.join(map(str, guess(0, tuple())))}\n")