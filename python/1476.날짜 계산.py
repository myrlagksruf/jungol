import sys
input = sys.stdin.readline
print = sys.stdout.write

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return 0
    return x % m

def chinese_remainder_theorem(remainders, moduli):
    s = 0
    prod = 1
    for modulus in moduli:
        prod *= modulus

    for remainder, modulus in zip(remainders, moduli):
        p = prod // modulus
        s += remainder * mod_inverse(p, modulus) * p
    return s % prod

e, s, m = map(int, input().rstrip().split())

print(f"{chinese_remainder_theorem((e - 1, s - 1, m - 1), (15, 28, 19)) + 1}\n")