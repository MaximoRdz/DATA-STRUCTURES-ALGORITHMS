from BST import BinarySearchTree, BSNode


class AVL(BinarySearchTree):
    def balance_factor(self, node: BSNode):
        """
        bf = height_R - height_L
        Height of leaf nodes is 1
        """
        if node is None:
            return 0

        return self._height(node.right) - self._height(node.left)

    def insert(self, item: object) -> None:
        self._root = self.__insert(self._root, item)

    def __insert(self, node: BSNode, item: object) -> BSNode:
        node = super()._insert(node, item)  # Usual BST insertion
        node = self.__balance(node)
        return node

    def remove(self, item: object) -> None:
        self._root = self.__remove(self._root, item)

    def __remove(self, node: BSNode, item: object) -> BSNode:
        node = super()._remove(node, item)
        node = self.__balance(node)
        return node

    def __balance(self, node: BSNode) -> BSNode:

        if abs(self.balance_factor(node)) <= 1:
            return node

        # First NOT BALANCED node.
        height_left = self._height(node.left)
        height_right = self._height(node.right)

        if height_left > height_right:  # Left-heavy branch: Left-(...) cases.
            height_left_left = self._height(node.left.left)
            height_left_right = self._height(node.left.right)

            if (
                height_left_left < height_left_right
            ):  # Child Right-heavy branch L-R case:
                node.left = self.__left_rotation(node.left)

            node = self.__right_rotation(node)

        else:  # Right-heavy branch: Right-(...) cases.
            height_right_left = self._height(node.right.left)
            height_right_right = self._height(node.right.right)

            if (
                height_right_right < height_right_left
            ):  # Child Left-heavy branch R-L case:
                node.right = self.__right_rotation(node.right)

            node = self.__left_rotation(node)

        return node

    def __left_rotation(self, node: BSNode) -> BSNode:
        """
                y               x
               / \      L      / \
             T1   x    -->    y   T3
                 / \         / \
                T2  T3     T1  T2    
        """
        x = node.right
        T2 = x.left
        x.left = node
        node.right = T2

        return x

    def __right_rotation(self, node: BSNode) -> BSNode:
        """
                y               x
               / \      R      / \
             T1   x    <--    y   T3
                 / \         / \
                T2  T3     T1  T2    
        """
        y = node.left
        T2 = y.right
        y.right = node
        node.left = T2

        return y


if __name__ == "__main__":
    tree = AVL()
    tree.insert(30)
    print(tree)
    tree.insert(35)
    print(tree)
    tree.insert(40)
    print(tree)
    tree.insert(20)
    print(tree)
    tree.insert(15)
    print(tree)
    tree.remove(15)
    print(tree)
    tree.remove(20)
    print(tree)
