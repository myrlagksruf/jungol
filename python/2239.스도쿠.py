import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = [[int(i) for i in input().rstrip()] for _ in range(9)]
COL = [set(range(1, 10)) - set(arr[i]) for i in range(9)]
ROW = [set(range(1, 10)) - set(j[i] for j in arr) for i in range(9)]
SQUARE = [[set(range(1, 10)) - set(arr[y][x] for x in range(j * 3, j * 3 + 3) for y in range(i * 3, i * 3 + 3)) for j in range(3)] for i in range(3)]

def nextij(i, j):
  return i + int((j + 1) == 9), (j + 1) % 9

def solve(i, j):
  global arr, COL, ROW, SQUARE
  if i == 9 and j == 0:
    return True
  if arr[i][j] != 0:
    return solve(*nextij(i, j))
  s = sorted(COL[i] & ROW[j] & SQUARE[i // 3][j // 3])
  cand:list[set[int]] = [COL[i], ROW[j], SQUARE[i // 3][j // 3]]
  for val in s:
    for t in cand:
      t.discard(val)
    arr[i][j] = val
    if solve(*nextij(i, j)):
      return True
    arr[i][j] = 0
    for t in cand:
      t.add(val)
  return False

solve(0, 0)

print('\n'.join(''.join(map(str, i)) for i in arr))