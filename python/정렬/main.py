import sys
input = sys.stdin.readline
print = sys.stdout.write
from sort import quick_sort
from random import randrange

n = int(sys.argv[1])
r = int(sys.argv[1])
reverse = False
if len(sys.argv) > 2:
  r = int(sys.argv[2])
if len(sys.argv) > 3:
  reverse = sys.argv[3] == "r"

arr = [randrange(r) for _ in range(n)]
print(f"{arr}\n")

print(f"{quick_sort(arr, reverse=reverse)}\n")
