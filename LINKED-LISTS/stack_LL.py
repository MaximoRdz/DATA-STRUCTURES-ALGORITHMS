class SimpleNode:
    def __init__(self, e: object, next_node: "SimpleNode" = None) -> None:
        self.elem = e
        self.next = next_node
    

class Stack:
    """Stack implementation based on Linked Lists."""
    def __init__(self):
        self.size = 0
        self.head = None

    def pop(self):
        if self.size == 0:
            print("Empty Stack.")
            return None
        
        result = self.head.elem
        self.size -= 1
        
        self.head = self.head.next

        return result
        
    def push(self, item):
        new_node = SimpleNode(item, self.head)
        self.head = new_node
        self.size += 1
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        message = ""
        item = self.head.elem
        next_item = self.head.next
        while next_item is not None:
            message += " " + str(item)
            item, next_item = next_item.elem, next_item.next 
        return message
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    print(stack)

