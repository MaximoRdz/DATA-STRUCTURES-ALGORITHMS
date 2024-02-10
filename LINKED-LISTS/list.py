class SimpleNode:
    def __init__(
        self, elem: object, next: "SimpleNode" = None, prev: "SimpleNode" = None
    ):
        self.elem = elem
        self.prev = prev
        self.next = next


class LinkedList:
    """
    List / Array implementation using Linked Lists Data Structure
    Each element has one predecessor a one successor except first
    with no predecessor and last with no succesor.

    Linked list implementation based on two pointers, head points to first element
    tail points to last element.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def __iter__(self):
        node = self._head
        i = 0
        while True:
            yield node
            node = node.next
            if node is None:
                return None
            i += 1
            if i == self._size:
                break

    def __str__(self):
        if self._size == 0:
            return "[]"
        s = "[" + ", ".join(str(node.elem) for node in self) + "]"
        return s
    
    def is_empty(self):
        return self._size == 0

    def append(self, item: object) -> None:
        node = SimpleNode(item)

        if self.is_empty():
            self._head = node
            self._tail = node
            self._size += 1
            return None
        
        node.prev = self._tail
        self._tail.next = node
        self._tail = node

        self._size += 1

    def pop(self) -> object:
        if not len(self):
            raise IndexError("Cannot Pop From Empty List")
        
        if len(self) == 1:
            elem = self._tail.elem
            self.__init__()
            return elem
        
        for i, node in enumerate(self):
            if i == len(self)-2:
                result = node.next.elem
                node.next = None
                self._tail = node
        
        return result
    
    def appendleft(self, item: object) -> None:
        node = SimpleNode(item)

        if self.is_empty():
            self._head = node
            self._tail = node
            self._size += 1
            return None
        
        node.next = self._head
        self._head.prev = node
        self._head = node

        self._size += 1


if __name__ == "__main__":
    array = LinkedList()
    for i in range(5):
        array.append(i)
    print("Example: ", array)
    print("Pop: ", array.pop(), "Result: ", array)

    for i in range(1, 5):
        array.appendleft(-i)
    print("AppendLeft: ", array)
