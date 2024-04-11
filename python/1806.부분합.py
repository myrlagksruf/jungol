import sys
input = sys.stdin.readline
print = sys.stdout.write

n, s = map(int, input().split())

arr = [int(i) for i in input().split()]

if sum(arr) < s:
  print(f"0\n")
  exit()

sm = 0
ed = 0
result = 100000

for st in range(n):
  if sm >= s:
    result = min(result, ed - st)
  while sm < s and ed < len(arr):
    sm += arr[ed]
    ed += 1
  if sm >= s:
    result = min(result, ed - st)
  sm -= arr[st]

print(f"{result}\n")