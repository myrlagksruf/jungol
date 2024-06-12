import sys
input = sys.stdin.readline
print = sys.stdout.write
from itertools import product
from collections import Counter

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

AB = [sum(i) for i in product(A, B)]
CD = [sum(i) for i in product(C, D)]
AB.sort()
CD.sort(reverse=True)

ab = 0
cd = 0
count = 0
ablen = len(AB)
cdlen = len(CD)
while ab < ablen and cd < cdlen:
  temp = AB[ab] + CD[cd]
  if temp < 0:
    ab += 1
    continue

  if temp > 0:
    cd += 1
    continue

  if temp == 0:
    abcount = 0
    cdcount = 0
    abori = ab
    cdori = cd
    while ab < ablen and AB[ab] + CD[cdori] == temp:
      ab += 1
      abcount += 1
    while cd < cdlen and AB[abori] + CD[cd] == temp:
      cd += 1
      cdcount += 1
    count += abcount * cdcount

print(f"{count}\n")