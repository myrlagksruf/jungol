import sys
input = sys.stdin.readline
print = sys.stdout.write
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

n = int(input())
result = []

for _ in range(n):
    m, n, x, y = map(int, input().split())
    # ma + nb = gcd를 만족하는
    # m1*a + n1*b = 1를 만족하는
    x -= 1
    y -= 1
    gcd, a, b = extended_gcd(m, n)
    m1 = m // gcd
    n1 = n // gcd
    x1 = x % m1
    y1 = y % n1
    mn = m1 * n1
    res = (x1 * n1 * b + y1 * m1 * a) % mn
    for _ in range(gcd):
        if x == res % m and y == res % n:
            result.append(str(res + 1))
            break
        res += mn
    else:
        result.append('-1')

print('\n'.join(result))
