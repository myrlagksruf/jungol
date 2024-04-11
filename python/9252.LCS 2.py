import sys
input = sys.stdin.readline
print = sys.stdout.write

L = input().rstrip()
R = input().rstrip()

mp = [[(0, '')] * (len(L) + 1) for _ in range(len(R) + 1)]

for ind, i in enumerate(R, 1):
  for ind2, j in enumerate(L, 1):
    if i == j:
      mp[ind][ind2] = (mp[ind - 1][ind2 - 1][0] + 1, mp[ind - 1][ind2 - 1][1] + j)
      continue
    mp[ind][ind2] = max(mp[ind - 1][ind2], mp[ind][ind2 - 1])

print('\n'.join(map(str, mp[-1][-1])))