class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

def __main__():
    my_stack = Stack()
    my_stack.push(2)
    my_stack.push(4)
    my_stack.push(1)
    
    print(my_stack)
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack)

__main__()
