from collections import deque


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

    def size(self):
        return self._size(self._root)
    
    def _size(self, node: BinaryNode):
        if node is None:
            return 0
        
        return 1 + self._size(node.left) + self._size(node.right)
        
    def height(self):
        return self._height(self._root)
    
    def _height(self, node: BinaryNode):
        if node is None:
            return -1
        
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def inorder(self):
        traversal = []
        self._inorder(self._root, traversal)

        return traversal
    
    def _inorder(self, node: BinaryNode, traversal: list) -> None:
        "left root right"
        if node is not None:
            self._inorder(node.left, traversal)
            traversal.append(node.elem)
            self._inorder(node.right, traversal)

    def breadth_first(self):
        q = deque()
        q.append(self._root)

        traversal = []

        while q:
            node = q.popleft()
            if node is None:
                continue
            traversal.append(node.elem)
            q.append(node.left)
            q.append(node.right)
        
        return traversal


if __name__ == "__main__":
    #              10
    #         4        6
    #     3     5          7
    # 2           1    3       4
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

    print("Tree Length Recursive: ", tree.size())
    print("Tree Height: ", tree.height())
    print("Inorder: ", tree.inorder())
    print("Breadth First: ", tree.breadth_first())