class BinaryNode:
    def __init__(
            self,
            elem: object,
            left: "BinaryNode" = None,
            right: "BinaryNode" = None
            ) -> None:
        
        self.elem = elem
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: BinaryNode = None) -> None:
        self._root = root

    def __len__(self):
        """
        Size of a Tree (number of nodes). Iterative Implementation
        PreOrder traversal.
        """
        if self._root is None:
            return 0
        
        stack = []
        stack.append(self._root)

        size = 1

        while stack:
            node = stack.pop()

            left = node.left
            right = node.right

            if left is not None:
                size += 1
                stack.append(left)
            
            if right is not None:
                size += 1
                stack.append(right)
        
        return size
    
    def size(self):
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """
        Recursive node counting
        """
        if node is None:
            return 0
        
        return 1 + self._size(node.left) + self._size(node.right)
    
    def height(self):
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        "Longest path from a node to a leaf."
        if node is None:
            return -1
        
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def preorder(self) -> None:
        print("\nPreorder Traversal Recursive:")
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        """
        Prints the preorder traversal of the tree (recursive implementation)
        first visited marked or (root, left, right).
        """
        if node is not None:
            print(node.elem, end=" ")       
            self._preorder(node.left)
            self._preorder(node.right)
        
    def inorder(self) -> None:
        print("\nInorder Traversal Recursive:")
        self._inorder(self._root)
        print()
    
    def _inorder(self, node: BinaryNode) -> None:
        "second visited or (left, root, right)"
        if node is not None:    
            self._inorder(node.left)
            print(node.elem, end=" ")  
            self._inorder(node.right)

    def postorder(self) -> None:
        print("\nPostorder Traversal Recursive:")
        self._postorder(self._root)
        print()
    
    def _postorder(self, node: BinaryNode) -> None:
        "third/last visited or (left, right, root)"
        if node is not None:    
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=" ")  

    def pre_order_traversal(self):
        """Pre Order traversal by default."""
        if self._root is None:
            raise IndexError("Empty Tree Cannot Be Traversed.")

        node = self._root
        path = []
        
        stack = []
        stack.append(node)

        while stack:
            node = stack.pop()
            path.append(node.elem)

            left = node.left
            right = node.right

            if right is not None:
                stack.append(right)
            
            if left is not None:
                stack.append(left)
        
        return path
    

if __name__ == "__main__":
    #             10
    #         4       6
    #     3   5           7
    # 2           1   3       4
    leaf_2 = BinaryNode(2)
    leaf_1 = BinaryNode(1)
    leaf_3 = BinaryNode(3)
    leaf_4 = BinaryNode(4)

    inner_3 = BinaryNode(3, leaf_2)
    inner_5 = BinaryNode(5, None, leaf_1)
    inner_7 = BinaryNode(7, leaf_3, leaf_4)

    sec_4 = BinaryNode(4, inner_3, inner_5)
    sec_6 = BinaryNode(6, None, inner_7)

    root = BinaryNode(10, sec_4, sec_6)

    tree = BinaryTree(root)

    print("Tree Length: ", len(tree))
    print("Tree Length Recursive: ", tree.size())
    print("Tree Height: ", tree.height())

    print("PreOrder Stack: ", tree.pre_order_traversal())
    tree.preorder()
    tree.inorder()
    tree.postorder()




