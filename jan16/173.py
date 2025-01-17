from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.values = 0
        self.left = left
        self.right = right 

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.traverse(root)
        self.idx = -1
    
    def next(self) -> int:
        self.idx += 1
        return self.values[self.idx]
    
    def hasNext(self) -> bool:
        return self.idx < len(self.values) - 1

    def traverse(self, root: Optional[TreeNode]):
        if root == None:
            return 
        self.traverse(root.left)
        self.values.append(root.val)
        self.traverse(root.right)

# Time Complexity: O(n), initializing our class will take O(n) time because we are traversing through the tree, 
# but next() and hasNext() will only take O(1) time

# Space Complexity: O(n), because we are storing all values of bst in a array
