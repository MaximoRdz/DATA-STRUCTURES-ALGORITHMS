from collections import deque


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

    def __str__(self):
        q = deque()
        q.append(self._root)
        nodes = []
        while q:
            node = q.popleft()
            
            if node is not None:
                nodes.append(node.elem)
            
                q.append(node.left)
                q.append(node.right)
        
        return ", ".join(nodes)

    def height(self) -> int:
        return self._height(self._root)
    
    def _height(self, node: BSNode) -> int:
        if node == None:
            return -1
        
        return 1 + max(self._height(node.left), self._height(node.right))

    def search(self, item: object) -> bool:
        """Search for 'item' in BST. Return True if found."""
        return self._search(item, self._root)

    def _search(self, item: object, node: BSNode) -> bool:
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
    
    def insert_iterative(self, item: object) -> None:

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

    def insert(self, item: object) -> None:
        self._root = self._insert(self._root, item)

    def _insert(self, node: BSNode, item: object) -> BSNode:
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
    
    def _minimum_node(self, node: BSNode):
        """Iterativel find min function."""
        if node is None:
            return None
        
        min_node = node
        while min_node.left:
            min_node = min_node.left
        
        return min_node
        
    def remove(self, item: object) -> None:
        self._root = self._remove(self._root, item)

    def _remove(self, node: BSNode, item: object) -> BSNode:
        """
        Recursively search the node to remove.
        1) Remove Node is leaf: Simply remove connection with parent.
        2) Remove Node has one child: Parent node now must point to its grandchild.
        3) Remove Node has two children: To meet BST condition search for a successor
        such that, every key of the left subtree will be smaller than the successor
        and every key in the right subtree will be larger. Successor will be the smallest
        item in RIGHT subtree of 'Remove Node'.
        """
        if node is None:
            print(f"Item: {item} not found in TREE.")
            return

        if node.elem < item:
            node.right = self._remove(node.right, item)

        elif node.elem > item:
            node.left = self._remove(node.left, item)
        
        else:
            if node.left is None and node.right is None:
                # Returning None and because the recursive nature of calls of this function
                # makes parent node disconnected from this node. Since calls stack up and
                # when it falls None the tree cannot continue to this position.
                return None

            if node.left is None:
                # The node to remove has exactly one child so we pass this child directly to
                # the parent node making a bridge on the reference connection (python garbage
                # collector will get rid of this)
                return node.right
            
            elif node.right is None:
                return node.left
            
            else:
                # Node to remove has two children, successor -> smallest right subtree item
                successor = self._minimum_node(node.right)
                node.elem = successor.elem
                node.right = self._remove(node.right, successor.elem)
        
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

    print("Search 5 in Tree: ", tree.search(5))
    print(tree)
    print("Remove 5")
    tree.remove(5)
    print("Search 5 in Tree: ", tree.search(5))
    print(tree)






