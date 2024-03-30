import sys
input = sys.stdin.readline
print = sys.stdout.write

s = [1]
not_self = set()

for i in range(2, 10001):
    if s[-1] < i and i not in not_self:
        s.append(i)
    cur = i
    while cur < 10001:
        temp = cur
        while temp != 0:
            cur += temp % 10
            temp //= 10
        if cur in not_self:
            break
        not_self.add(cur)

print('\n'.join(map(str, s)))