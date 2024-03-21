import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
count = 0
cur = 1
pre = 1
x = 10
while True:
    if n < x:
        count += (n - pre + 1) * cur
        break
    count += (x - pre) * cur
    pre *= 10
    x *= 10
    cur += 1
    
print(f"{count}\n")