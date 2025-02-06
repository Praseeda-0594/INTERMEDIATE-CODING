# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result

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
    result = solution.levelOrder(root)

    print("Level Order Traversal:", result)

if __name__ == "__main__":
    main()
