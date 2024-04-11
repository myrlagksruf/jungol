import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

n = int(input())

arr = [[int(i) for i in input().split()] for _ in range(n)]

way = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def deep(arr:list[list[int]], ma):
#   for dx, dy in way:
#     brr = deque()
#     addbig = 
