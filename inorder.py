# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []  # Create an empty list
    
    def inorder(node):
        if not node:
            return  # Base case
        
        inorder(node.left)  # Traverse left
        result.append(node.val)  # Visit root
        inorder(node.right)  # Traverse right

    inorder(root)  # Start recursion
    return result


# Tree Structure:
#       1
#        \
#         2
#        /
#       3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Call Function and Print Result
result = inorderTraversal(root)
print(result)  # Output: [1, 3, 2]  (Inorder: Left → Root → Right)
