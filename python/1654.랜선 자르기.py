import sys
input = sys.stdin.readline
print = sys.stdout.write

K, N = map(int, input().split())

arr = [int(input()) for _ in range(K)]

def check(x:int):
  return sum(i // x for i in arr)

mi, ma = 0, 2 ** 31 - 1
while mi < ma:
  mid = (mi + ma + 1) // 2
  result = check(mid)
  if result >= N:
    mi = mid
  else:
    ma = mid - 1

print(f"{mi}\n")