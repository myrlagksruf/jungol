import sys
input = sys.stdin.readline
print = sys.stdout.write
from math import gcd
from random import randint
# n = int(randint(2, 4611686018427388003))
n = int(input())
first = 1000000
s = set(range(2, first))
N = int(first ** 0.5)
for i in range(N + 1):
  if i not in s:
    continue
  for j in range(i * 2, first, i):
    s.discard(j)

s = sorted(s)

def pollard(n:int, t = 1):
  if n % 2 == 0:
    return 2
  if n == 25:
    return 5
  x = t
  y = x
  if n in s:
    return n
  for _ in range(100000):
    x = (x * x + 1) % n
    y = (y * y + 1) % n
    y = (y * y + 1) % n
    if x == y:
      break
    d = gcd(abs(x - y), n)
    if d == 1:
      continue
    return d
  return 1

result = []
tarr = [1, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24]
bigFlag = False
cur = n
t = 0
while cur != 1 and t != 20:
  flag = False
  val = pollard(cur, tarr[t])
  if val == cur:
    result.append(cur)
    cur = 1
    break
  if val == 1:
    t += 1
    continue
  cur //= val
  t = 0
  for i in s:
    if val == 1:
      flag = True
      break
    if i * i > val:
      result.append(val)
      flag = True
      break
    while val % i == 0:
      val //= i
      result.append(i)
    
  if not flag:
    for i in s:
      if cur == 1:
        bigFlag = True
        break
      if i * i > cur:
        result.append(cur)
        bigFlag = True
        break
      while cur % i == 0:
        cur //= i
        result.append(i)
    else:
      result.append(cur)
      bigFlag = True
  if bigFlag:
    break

if cur != 1:
  result.append(cur)

result.sort()

print('\n'.join(map(str, result)))
