import sys
input = sys.stdin.readline
print = sys.stdout.write
from random import randint

class BTN:
  value:int
  def __init__(self, value:int):
    self.value = value
    self.left:BTN|None = None
    self.right:BTN|None = None

def insert(root: BTN, value: int) -> BTN:
    """이진 트리에 값을 삽입하는 함수."""
    if root is None:
        return BTN(value)
    else:
        if value < root.value:
            if root.left is None:
                root.left = BTN(value)
            else:
                insert(root.left, value)
        else:
            if root.right is None:
                root.right = BTN(value)
            else:
                insert(root.right, value)
    return root

def generate_random_tree(n: int) -> BTN:
    """랜덤한 값을 가진 이진 트리를 생성하는 함수."""
    root = BTN(randint(1, 100))
    for _ in range(n - 1):
        insert(root, randint(1, 100))
    return root

def preorder(node:BTN):
  if not node: return None
  print(f"{node.value}\n")
  preorder(node.left)
  preorder(node.right)

def inorder(node:BTN):
  if not node: return None
  inorder(node.left)
  print(f"{node.value}\n")
  inorder(node.right)

def postorder(node:BTN):
  if not node: return None
  postorder(node.left)
  postorder(node.right)
  print(f"{node.value}\n")

preorder(generate_random_tree(20))