import sys
input = sys.stdin.readline
print = sys.stdout.write
from typing import Dict
RecursiveDict = Dict[str, 'RecursiveDict']


N = int(input())

di = {}

for _ in range(N):
  _, *arr = input().rstrip().split()
  cur = di
  for i in arr:
    cur[i] = cur.get(i, {})
    cur = cur[i]

def render(di:RecursiveDict, depth:int):
  for i in sorted(di.keys()):
    print(f"{'--' * depth}{i}\n")
    render(di[i], depth + 1)
  return

render(di, 0)