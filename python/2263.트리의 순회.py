import sys
input = sys.stdin.readline
print = sys.stdout.write
from typing import Self
sys.setrecursionlimit(10**6)

n = int(input())

class Node:
  left:Self|None
  right:Self|None
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

in_order = [int(i) for i in input().split()]
post_order = [int(i) for i in input().split()]
in_dict = {val: ind for ind, val in enumerate(in_order)}

def make_tree(in_start, in_end, post_start, post_end, result:list[str]):
  if in_start > in_end or post_start > post_end:
    return
  val = post_order[post_end]
  result.append(str(val))
  left = in_dict[val] - in_start
  right = in_end - in_dict[val]
  make_tree(in_start, in_start + left - 1, post_start, post_start + left - 1, result)
  make_tree(in_dict[val] + 1, in_end, post_end - right, post_end - 1, result)

result:list[str] = []
make_tree(0, n - 1, 0, n - 1, result)

print(' '.join(result))
