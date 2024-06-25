import sys
input = sys.stdin.readline
print = sys.stdout.write

T = input().rstrip()
P = input().rstrip()

def getPi(p:str):
  pi = [0] * len(p)
  j = 0
  for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
      j = pi[j - 1]
    if p[i] == p[j]:
      j += 1
    pi[i] = j
  return pi

pi = getPi(P)

res:list[int] = []
j = 0
for ind, i in enumerate(T):
  while j > 0 and i != P[j]:
    j = pi[j - 1]
  if i == P[j]:
    if j == len(P) - 1:
      res.append(ind - len(P) + 2)
      j = pi[j]
    else:
      j += 1

print(f"{len(res)}\n")
print("\n".join(map(str, res)))