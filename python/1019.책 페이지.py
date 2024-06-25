import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache

N = int(input())
  
@cache
def get_num(num_str:str, with_zero = False):
  st = 0 if with_zero else 1
  num = int(num_str)
  count = len(num_str)
  if num < 10 and count < 2:
    arr = [0] * 10
    for i in range(st, num + 1):
      arr[i] = 1
    return arr
  val = 10 ** (count - 1)
  if with_zero:
    arr = [0] * 10
  else:
    arr = get_num(str(val - 1))
  for i in range(st, 10):
    if val * i > num:
      break
    plus = min(val, num - val * i + 1)
    arr[i] += plus
    for ind, j in enumerate(get_num(str(plus - 1).rjust(count - 1, '0'), True)):
      arr[ind] += j
  return arr

print(f"{' '.join(map(str, get_num(str(N))))}\n")