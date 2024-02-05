

class Stack:
    "LIFO stack implementation"

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        return False if self.items else True
    
    def __str__(self) -> str:
        return str(self.items)
    
    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def pop(self):
        if self.is_empty():
            print("Error empty Stack")
            return None
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
    

def balance(sentence):
    "Check if the brackets of sentence are balanced"

    stack = Stack()
    
    for c in sentence:
        if c == "(":
            stack.push("(")
        if c == ")":
            if stack.is_empty():
                return False
            
            _ = stack.pop()
    
    return stack.is_empty()


def balance_extended(sentence):
    "Check if (), [], {} are correctly balanced in sentence"
    matching_open = {")": "(",
                     "}": "{",
                     "]": "["}
    stack = Stack()
    for c in sentence:
        if c in "([{":
            stack.push(c)
        if c in ")]}":
            if stack.is_empty():
                return False
            nc = stack.pop()
            if nc != matching_open[c]:
                return False
    
    return stack.is_empty()




if __name__ == "__main__":
    ex1 = "()(((())))()()()"
    print(ex1, balance(ex1))

    ex2 = "(()()"
    print(ex2, balance(ex2))

    print(ex1, balance_extended(ex1))

    ex3 = "[{[()]}]"
    print(ex3, balance_extended(ex3))

    ex4 = "[{([()]}]"
    print(ex4, balance_extended(ex4))



