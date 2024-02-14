

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
    def __init__(self, root: "BinaryNode" = None) -> None:
        self._root = root

    def __len__(self):
        "Size of a Tree (number of nodes)."
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
    
    def in_order_traversal(self):
        """In Order traversal by default."""
        if self._root is None:
            raise IndexError("Empty Tree Cannot Be Traversed.")

        node = self._root
        path = []
        
        stack = []
        stack.append(node)

        visited = set()

        while stack:
            node = stack.pop()

            if node in visited:
                path.append(node.elem)
            else:
                stack.append(node)

            visited.add(node)

            left = node.left
            right = node.right

            if right is not None:
                stack.append(right)
            
            if left is not None:
                stack.append(left)
        
        return path




    def __str__(self, mode="") -> str:
        pass


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

    print(tree.in_order_traversal())


