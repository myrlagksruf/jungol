import sys
input = sys.stdin.readline
print = sys.stdout.write

class TreeNode:
  def __init__(self, key, height=1, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right
    self.height = height

class AVLTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, node, key):
    if not node:
      return TreeNode(key)
    elif key < node.key:
      node.left = self._insert(node.left, key)
    else:
      node.right = self._insert(node.right, key)

    node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    return self.rebalance(node)

  def delete(self, key):
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):
    if not node:
      return node

    if key < node.key:
      node.left = self._delete(node.left, key)
    elif key > node.key:
      node.right = self._delete(node.right, key)
    else:
      if not node.left:
        return node.right
      elif not node.right:
        return node.left
      temp = self.find_min(node.right)
      node.key = temp.key
      node.right = self._delete(node.right, temp.key)

    if not node:
      return node

    node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    return self.rebalance(node)

  def find_min(self, node):
    while node.left is not None:
      node = node.left
    return node

  def rebalance(self, node):
    balance = self.get_balance(node)

    # Left Left
    if balance > 1 and self.get_balance(node.left) >= 0:
      return self.rotate_right(node)

    # Right Right
    if balance < -1 and self.get_balance(node.right) <= 0:
      return self.rotate_left(node)

    # Left Right
    if balance > 1 and self.get_balance(node.left) < 0:
      node.left = self.rotate_left(node.left)
      return self.rotate_right(node)

    # Right Left
    if balance < -1 and self.get_balance(node.right) > 0:
      node.right = self.rotate_right(node.right)
      return self.rotate_left(node)

    return node

  def rotate_left(self, z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def rotate_right(self, z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def get_height(self, node):
    if not node:
      return 0
    return node.height

  def get_balance(self, node):
    if not node:
      return 0
    return self.get_height(node.left) - self.get_height(node.right)

  def lower_bound(self, key):
    result = self._lower_bound(self.root, key)
    return result.key if result else None

  def _lower_bound(self, node, key):
    if not node:
      return None
    if node.key >= key:
      return self._lower_bound(node.left, key) or node
    return self._lower_bound(node.right, key)



avl = AVLTree()

N, K = map(int, input().split())
arr = []

for _ in range(N):
  arr.append([int(i) for i in input().split()[::-1]])

arr.sort(reverse=True)

for _ in range(K):
  avl.insert(int(input()))

result = 0

for v, m in arr:
  lower_m = avl.lower_bound(m)
  if not lower_m:
    continue
  avl.delete(lower_m)
  result += v

print(f"{result}\n")
