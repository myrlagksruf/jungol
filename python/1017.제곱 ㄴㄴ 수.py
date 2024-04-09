import sys
input = sys.stdin.readline
print = sys.stdout.write

def solution(mi:int, ma:int):
  ma2 = int(ma ** 0.5)
  jegob = { i for i in range(mi, ma + 1)}
  for i in range(2, min(1000001, ma2 + 1)):
    i2 = i * i
    for j in range(mi // i2 * i2, ma + 1, i2):
      jegob.discard(j)
  return len(jegob)

mi, ma = [int(v) for v in input().split()]
print(solution(mi, ma))