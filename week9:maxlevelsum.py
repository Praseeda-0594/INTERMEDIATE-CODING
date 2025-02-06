# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on. Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        queue = deque([root])

        while queue:
            level_sum = sum(node.val for node in queue)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            current_level += 1

        return max_level

def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root

def main():
    values = input("Enter the tree nodes in level-order (use None for null nodes, separated by spaces): ").split()

    for i in range(len(values)):
        if values[i].lower() == "none":
            values[i] = None
        else:
            values[i] = int(values[i])

    root = build_tree(values)
    solution = Solution()
    max_level = solution.maxLevelSum(root)

    print("Level with maximum sum:", max_level)

if __name__ == "__main__":
    main()
