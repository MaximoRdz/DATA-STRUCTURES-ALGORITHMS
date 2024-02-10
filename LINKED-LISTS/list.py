class SimpleNode:
    def __init__(
        self,
        elem: object,
        next: "SimpleNode" = None,
        prev: "SimpleNode" = None
    ):
        self.elem = elem
        self.prev = prev
        self.next = next


class LinkedList:
    """
    List / Array implementation using Linked Lists Data Structure
    Each element has one predecessor a one successor except first
    with no predecessor and last with no succesor.

    Linked list implementation based on two pointers, head points
    to first element tail points to last element.
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
        if self.is_empty():
            raise IndexError("Cannot Pop From Empty List")

        if len(self) == 1:
            elem = self._tail.elem
            self.__init__()
            return elem

        for i, node in enumerate(self):
            if i == len(self) - 2:
                result = node.next.elem
                node.next = None
                self._tail = node

        self._size -= 1

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

    def popleft(self) -> None:
        if self.is_empty():
            raise IndexError("Cannot Pop From Empty List")

        if len(self) == 1:
            elem = self._tail.elem
            self.__init__()
            return elem

        result = self._head.elem
        self._head = self._head.next
        self._head.prev = None

        self._size -= 1

        return result

    def index(self, item) -> int:
        """
        Return the index of 'item' first appeareance if it is not
        in the list returns -1
        """
        for i, node in enumerate(self):
            if node.elem == item:
                return i
        return -1

    def get_at(self, ind: int):
        if not (0 <= ind < len(self) - 1):
            print("Index Out Of Range returns None instead")
            return None

        for i, node in enumerate(self):
            if i == ind:
                return node.elem

    def insert(self, ind: int, item) -> None:
        """Insert a node at index ind."""
        if not (0 <= ind <= self._size):
            raise IndexError("Cannot Insert Out of List Index Range")

        if ind == 0:
            self.appendleft(item)
            return None

        if ind == len(self):
            self.append(item)
            return None

        node = self._head
        for i in range(ind - 1):
            node = node.next

        new_node = SimpleNode(item, node.next, node)
        node.next = new_node
        self._size += 1

    def remove(self, ind: int) -> None:
        if not (0 <= ind < self._size):
            raise IndexError("Index Out Of Range")

        if ind == 0:
            _ = self.popleft()

        if ind == len(self) - 1:
            _ = self.pop()

        node = self._head
        for _ in range(ind):
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

        self._size -= 1


if __name__ == "__main__":
    array = LinkedList()

    for i in range(5):
        array.append(i)

    print("Example: ", array)
    print("Pop: ", array.pop(), "Result: ", array)
    array.append(4)

    for i in range(1, 5):
        array.appendleft(-i)

    print("AppendLeft: ", array)
    print("PopLeft: ", array.popleft(), "Result: ", array)

    print("Index of -1: ", array.index(-1))
    print("Index of 'ex': ", array.index("ex"))

    print("Get at 2: ", array.get_at(2))
    print("Get at 200: ", array.get_at(200))

    print(array, "length: ", len(array))
    array.insert(0, "First")
    print("Insert at 0: ", array)
    array.insert(len(array), "Last")
    print("Insert at -1: ", array, "Length: ", len(array))
    array.insert(len(array) // 2, "Middle")
    print(f"Insert at {len(array)//2}: ", array)

    array.remove(2)
    print("Remove -2: ", array, "Length: ", len(array))
