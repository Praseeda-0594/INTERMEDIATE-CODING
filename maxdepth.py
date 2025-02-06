# Given the root of a binary tree, return its maximum depth.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def maxDepth(self, root):
      if not root:
          return 0
      l_depth = self.maxDepth(root.left)
      r_depth = self.maxDepth(root.right)
      return max(l_depth, r_depth) + 1

def build_tree(values, index=0):
  if index >= len(values) or values[index] is None:
      return None
  root = TreeNode(values[index])
  root.left = build_tree(values, 2 * index + 1)
  root.right = build_tree(values, 2 * index + 2)
  return root

def main():
  values = list(map(int, input("Enter the tree nodes in level-order (use None for null nodes): ").split()))
  root = build_tree(values)
  solution = Solution()
  print("Maximum depth of the tree:", solution.maxDepth(root))

if __name__ == "__main__":
  main()
