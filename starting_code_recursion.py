# Step 1: Define a Node in the Binary Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: Define the Binary Tree with a Recursive Search Function
class BinaryTree:
    def __init__(self):
        self.root = None

    # Recursive function to check if a value exists in the tree
    def contains(self, node, target):
        if not node:
            return False
        if node.value==target:
            return True
        return self.contains(node.left,target) or self.contains(node.right,target)

# Step 3: Create a Binary Tree and Insert Nodes
tree = BinaryTree()
tree.root = TreeNode('D')
tree.root.left = TreeNode('B')
tree.root.right = TreeNode('F')
tree.root.left.left = TreeNode('A')
tree.root.left.right = TreeNode('C')
tree.root.right.left = TreeNode('E')
tree.root.right.right = TreeNode('H')

# Step 4: Test the Function with Different Values
print(tree.contains(tree.root, 'D'))  # True
print(tree.contains(tree.root, 'H'))  # True
print(tree.contains(tree.root, 'F'))  # True
print(tree.contains(tree.root, 'Q'))  # False
