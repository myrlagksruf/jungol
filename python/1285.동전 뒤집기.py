import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
result = 0
initCountArr:list[int] = []

for _ in range(n):
  result <<= n
  st = input().rstrip()
  s = sum(1 << ind if i == 'H' else 0 for ind, i in enumerate(st))
  initCountArr.append(n - 2 * st.count('H'))
  result += s

initCountArr = initCountArr[::-1]
colArr = [sum(1 << (n * i + j) for i in range(n)) for j in range(n)]
rowArr = [((1 << n) - 1) << i * n for i in range(n)]
nthDict = { (1 << key):key for key in range(n)}

def count_bits_kernighan(n):
  count = 0
  while n:
    n &= n - 1  # Remove the lowest set bit
    count += 1
  return count

def swapCol(n:int, i:int):
  res = n ^ colArr[i]
  return res

def swapRow(n:int, i:int):
  res = n ^ rowArr[i]
  return res

def deep(depth:int, result:int, count:int):
  if depth == n:
    cc = count
    for i in range(n):
      rowcount = count_bits_kernighan(result & colArr[i])
      if n - rowcount * 2 > 0:
        cc += n - rowcount * 2
    return cc
  
  next_result = swapRow(result, depth)
  return max(
    deep(depth + 1, next_result, count + initCountArr[depth]),
    deep(depth + 1, result, count)
  )

ma = deep(0, result, count_bits_kernighan(result))

print(f"{n * n - ma}\n")
