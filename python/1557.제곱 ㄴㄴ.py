import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

s = set(range(2, 50000))

for i in range(2, 224):
  if i not in s:
    continue
  for j in range(i * 2, 50000, i):
    s.discard(j)
sorted_s = sorted(s)
ss = [-2] * 50000
for i in s:
  ss[i] = 1

for i in s:
  cur = i * i
  for j in range(cur, 50000, cur):
    ss[j] = 0


def get_mb(num:int):
  cur = num
  count = 1
  for i in sorted_s:
    if cur < i * i:
      return count
    if cur % i == 0:
      cur //= i
      count *= -1

def get_num(num:int):
  cur = num
  for i in range(2, 50000):
    x = i * i
    if x > num:
      break
    if ss[i] == -2:
      ss[i] = get_mb(i)
    cur -= num // x * ss[i] 
  return cur


left = 0
right = 3000000000

while left != right:
  mid = (left + right) // 2
  val = get_num(mid)
  if val >= n:
    right = mid
  else:
    left = mid + 1

print(f"{left}\n")