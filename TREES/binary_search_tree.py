class BinaryNode:
    def __init__(self, elem, left: "BinaryNode" = None, right: "BinaryNode" = None):
        self.elem = elem
        self.left = left
        self.right = right


class BSNode(BinaryNode):
    def __init__(self, key, elem, left: BinaryNode = None, right: BinaryNode = None):
        self.key = key
        super().__init__(elem, left, right)


class BinarySearchTree:
    """
    Ordered binary tree, the key of each node is larger than the keys of all the
    nodes of the left subtree and it is smaller than all the keys of all nodes
    of the right subtree.
    """
    def __init__(self, root: BSNode = None):
        self._root = root

    def height(self):
        return self._height(self._root)
    
    def _height(self, node: BSNode) -> int:
        if node == None:
            return -1
        
        return 1 + max(self._height(node.left), self._height(node.right))

    def search(self, item):
        """Search for 'item' in BST. Return True if found."""
        return self._search(item, self._root)

    def _search(self, item, node: BSNode) -> bool:
        """
        Easier than binary search, data already organized in a decision tree
        manner.
        """
        if node is not None:
            if node.elem == item:
                return True
            elif node.elem > item:
                return self._search(item, node.left)
            else:
                return self._search(item, node.right)
            
        return False
    
    def insert_iterative(self, item) -> None:

        node = self._root
        parent = None

        while node:
            parent = node
            if node.elem == item:
                print(f"Insertion error item: {item} Already in BST")
                return 
            elif node.elem > item:
                node = node.left
            else:
                node = node.right
        
        if item > parent.elem:
            parent.right = BSNode(item, item)
        else:
            parent.left = BSNode(item, item)

    def insert(self, item) -> None:
        self._root = self._insert(self._root, item)

    def _insert(self, node: BSNode, item) -> BSNode:
        """
        Recursive Insertion Implementation.
        Nodes are re-assigned the same value until they become None, 
        then they are assigned a new node containing item.
        """
        if node is None:
            node = BSNode(item, item)

        elif node.elem == item:
            print(f"Insertion error item: {item} Already in BST")
        
        elif node.elem > item:
            node.left = self._insert(node.left, item)

        else:
            node.right = self._insert(node.right, item)
        
        return node
            
        



if __name__ == "__main__":
    depth_5_16 = BSNode(16, 16)

    depth_4_1 = BSNode(1, 1)
    depth_4_4 = BSNode(4, 4)
    depth_4_17 = BSNode(17, 17, depth_5_16)    

    depth_3_3 = BSNode(3, 3, depth_4_1, depth_4_4)
    depth_3_7 = BSNode(7, 7)
    depth_3_15 = BSNode(15, 15, None, depth_4_17)
    depth_3_30 = BSNode(30, 30)

    depth_2_5 = BSNode(5, 5, depth_3_3, depth_3_7)
    depth_2_20 = BSNode(20, 20, depth_3_15, depth_3_30)

    depth_1_10 = BSNode(10, 10, depth_2_5, depth_2_20)

    tree = BinarySearchTree(depth_1_10)

    print("Height: ", tree.height())

    item = 18
    print(f"Search {item} in Tree: ", tree.search(item))

    print("Search 8 in Tree: ", tree.search(8))
    tree.insert(8)
    print("Insert 8 in tree.")
    print("Search 8 in Tree: ", tree.search(8))


