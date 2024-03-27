import sys
input = sys.stdin.readline
print = sys.stdout.write

N, S = map(int, input().split())
count = 0
s_nums = {(1 << ind): int(i) for ind, i in enumerate(input().split())}

for i in range(1, 1 << N):
    sum_nums = 0
    while i:
        val = i & -i
        sum_nums += s_nums[val]
        i &= i - 1
    if S == sum_nums:
        count += 1

print(f"{count}\n")