class SimpleNode:
    def __init__(self, elem: object, next_node: "SimpleNode" = None):
        self.elem = elem
        self.next = next_node


class Queue:
    """
    Queue implementation based on Linked Lists and optimized
    with head and tail nodes.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0
    
    def append(self, item: object) -> None:
        node = SimpleNode(item)

        if self.size == 0:
            self._head = node
            self._tail = self._head
            self.size += 1
            return None

        self._tail.next = node
        self._tail = self._tail.next

        self.size += 1


    def popleft(self):
        if self.size == 0:
            raise IndexError("Cannot Pop Element From Empty Queue")
        
        item = self._head.elem
        self._head = self._head.next
        self.size -= 1

        return item

    def __str__(self):
        s = []
        node = self._head

        while True:
            s.append(str(node.elem))
            if node.next is None:
                break
            node = node.next

        return ", ".join(s)
        


if __name__ == "__main__":
    q = Queue()
    q.append(3)
    q.append(4)
    q.append(5)
    q.append(6)
    q.append(None)

    print(q)
