class StackLinkedList:
    class Node:
        def __init__(self, element, nnext=None):
            self.element = element
            self.nnext = nnext

    def __init__(self, max_size=10):
        self.head = None
        self.size = 0
        self.MaxSize = max_size

    def push(self, element):
        if not self.isFull():
            new_node = self.Node(element, self.head)
            self.head = new_node
            self.size += 1
            self.display()  
        else:
            print("Stack is full!")

    def pop(self):
        if not self.isEmpty():
            result = self.head.element
            self.head = self.head.nnext
            self.size -= 1
            return result
        else:
            print("Stack is empty!")
            return None

    def top(self):
        if not self.isEmpty():
            return self.head.element
        else:
            print("Stack is empty!")
            return None

    def isFull(self):
        return self.size >= self.MaxSize

    def isEmpty(self):
        return self.size == 0

    def display(self):
        current = self.head
        print("Stack elements:")
        while current:
            print(current.element, end=" -> ")
            current = current.nnext
        print("None")

stack = StackLinkedList()
stack.push(5)
stack.push(10)
stack.push(15)

# Pushing 
for i in range(1, 5):
    stack.push(i)

print("Top element :", stack.top())
print("Popped element:", stack.pop())
stack.display()
print("Top element after pop :", stack.top())
