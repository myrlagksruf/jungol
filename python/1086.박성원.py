import sys
input = sys.stdin.readline
print = sys.stdout.write
from functools import cache
from fractions import Fraction

N = int(input())
arr = [int(input()) for _ in range(N)]
strlenarr = [len(str(i)) for i in arr]
K = int(input())

di = { 1 << i:i for i in range(16) }
carr = []
acc = 1
for i in range(760):
  carr.append(acc)
  acc = acc * 10 % K
@cache
def get_num(x:int, k:int) -> dict[int, int]:
  temp = x
  al:list[int] = []
  count = 0
  while temp:
    f = temp & (-temp)
    temp -= f
    count += strlenarr[di[f]]
    al.append(di[f])
  if len(al) == 1:
    return {arr[al[0]] % k: 1}
  res:dict[int, int] = {}
  for i in al:
    c = count - strlenarr[i]
    val = arr[i] * carr[c] % k
    li = get_num(x - (1 << i), k)
    for key, value in li.items():
      newkey = (key + val) % k
      res[newkey] = (res.get(newkey, 0) + value)
  return res

ja = 0
mo = 0
for key, val in get_num((1 << len(arr)) - 1, K).items():
  if key == 0:
    ja += val
  mo += val

result = str(Fraction(ja, mo))
if result == '0':
  result = '0/1'
elif result == '1':
  result = '1/1'

print(f"{result}\n")