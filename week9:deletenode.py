# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self.getMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node

def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root

def level_order_traversal(root):
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

def main():
    values = input("Enter the BST nodes in level-order (use None for null nodes, separated by spaces): ").split()

    for i in range(len(values)):
        if values[i].lower() == "none":
            values[i] = None
        else:
            values[i] = int(values[i])

    root = build_tree(values)

    key = int(input("Enter the node value to delete: "))

    solution = Solution()
    root = solution.deleteNode(root, key)

    print("BST after deletion (level-order):", level_order_traversal(root))

if __name__ == "__main__":
    main()
