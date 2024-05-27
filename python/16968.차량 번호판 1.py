from itertools import product, pairwise
from string import ascii_lowercase, digits

i = input().rstrip()

def solution(cd:str):
  prod:list[str] = []
  ans = 0

  for i in cd:
    if i == 'c':
      prod.append(ascii_lowercase)
    else:
      prod.append(digits)

  for i in product(*prod):
    for j in pairwise(i):
      if j[0] == j[1]:
        break
    else:
      ans += 1

  return ans

print(solution(i))