import sys
input = sys.stdin.readline
print = sys.stdout.write

from itertools import combinations

n = int(input())
A = []
for _ in range(n):
  A.append(input())
A=[[int(j) for j in i.split()] for i in A]

sum_all = 0
for i in A:
  sum_all += sum(i)

arr = []
for i, j in zip(A, zip(*A)):
  arr.append(sum(i) + sum(j))

ma = min(abs(sum_all - sum(i)) for i in combinations(arr, n // 2))
for j in range(1, n // 2):
  ma = min(ma, min(abs(sum_all - sum(i)) for i in combinations(arr, j)))

print(f"{ma}\n")