import sys
input = sys.stdin.readline
print = sys.stdout.write

s, n = input().rstrip().split()
s = int(s)
nrr = [int(i) for i in n]
arr = [
  [' - ', '| |', '   ', '| |', ' - '],
  ['   ', '  |', '   ', '  |', '   '],
  [' - ', '  |', ' - ', '|  ', ' - '],
  [' - ', '  |', ' - ', '  |', ' - '],
  ['   ', '| |', ' - ', '  |', '   '],
  [' - ', '|  ', ' - ', '  |', ' - '],
  [' - ', '|  ', ' - ', '| |', ' - '],
  [' - ', '  |', '   ', '  |', '   '],
  [' - ', '| |', ' - ', '| |', ' - '],
  [' - ', '| |', ' - ', '  |', ' - '],
]
cur = -1

strarr = []

for i in range(2 * s + 3):
  if i % (s + 1) == 0:
    cur += 1
  temp = []
  for j in nrr:
    temp.append(f"{arr[j][cur][0]}{arr[j][cur][1] * s}{arr[j][cur][2]}")
  strarr.append(' '.join(temp))
  if i % (s + 1) == 0:
    cur += 1

print('\n'.join(strarr))