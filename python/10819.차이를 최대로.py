import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = sorted(map(int,input().split()))

vma = arr[-1]
vmi = arr[0]
s = vma - vmi
cmi = 1
cma = len(arr) - 2

while cma >= cmi:
  if cma == cmi:
    val = arr[cma]
    s += max(vma - val, val - vmi)
    break
  valma = arr[cma]
  valmi = arr[cmi]
  s += vma - valmi + valma - vmi
  cmi += 1
  cma -= 1
  vma = valma
  vmi = valmi

print(f"{s}\n")