import sys
input = sys.stdin.readline
print = sys.stdout.write

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]

a = L1[2] - L1[0]
b = L2[0] - L2[2]
c = L1[3] - L1[1]
d = L2[1] - L2[3]

rt1 = L2[0] - L1[0]
rt2 = L2[1] - L1[1]

det = a * d - b * c
if det == 0:
  xmeet = L2[0] >= min(L1[0], L1[2]) and L2[0] <= max(L1[0], L1[2]) or L1[0] >= min(L2[0], L2[2]) and L1[0] <= max(L2[0], L2[2]) or L2[2] >= min(L1[0], L1[2]) and L2[2] <= max(L1[0], L1[2]) or L1[2] >= min(L2[0], L2[2]) and L1[2] <= max(L2[0], L2[2])
  ymeet = L2[1] >= min(L1[1], L1[3]) and L2[1] <= max(L1[1], L1[3]) or L1[1] >= min(L2[1], L2[3]) and L1[1] <= max(L2[1], L2[3]) or L2[3] >= min(L1[1], L1[3]) and L2[3] <= max(L1[1], L1[3]) or L1[3] >= min(L2[1], L2[3]) and L1[3] <= max(L2[1], L2[3])
  if a * rt2 == c * rt1 and (ymeet and xmeet or L1[0] == L1[2] and ymeet or L1[1] == L1[3] and xmeet):
    print(f"1\n")
    exit()
  print(f"0\n")
  exit()

t1 = rt1 * d - rt2 * b
t2 = rt2 * a - rt1 * c
if t1 >= min(det, 0) and t1 <= max(det, 0) and t2 >= min(det, 0) and t2 <= max(det, 0):
  print(f"1\n")
else:
  print(f"0\n")