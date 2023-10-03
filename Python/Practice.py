#Binary Search Tree
"""class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySeachTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None
    
    def insert(self, value):
        new_node = Node(value)
        if self.is_empty:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                if value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
            return None
                
    def delete(self, value):
        if self.is_empty:
            return None
        if value < self.root.value:
            self.root.left = self.delete(self.root.left, value)
        elif value > self.root.value:
            self.root.right = self.delete(self.root.right, value)
        else:
            if self.root.left is None:
                return self.root.right
            elif self.root.right is None:
                return self.root.left
            else:
                successor = self.minV(self.root.right)
                self.root.value = successor.value
                self.root.right = self.delete(self.root.right, successor.value)
    
    def minV(self):
        current = self.root
        if current.left is not None:
            current = current.left
        return current
    
    def inOrder_DFS(self):
        if self.is_empty:
            return None
        left_traversal = self.inOrder_DFS(self.root.left)
        right_traversal = self.inOrder_DFS(self.root.right)
        return left_traversal + [self.root] + right_traversal
    
bst = BinarySeachTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(13)
bst.insert(18)
print(bst.inOrder_DFS())"""

