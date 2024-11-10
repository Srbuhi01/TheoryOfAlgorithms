class Stack:
    def __init__(self):
        self._listt = []  
        self.MaxSize = 10

    def push(self, element):
        if not self.isFull():
            self._listt.append(element)
            return self._listt  
        else:
            print("Stack is full!")
            return None

    def pop(self):
        if not self.isEmpty():
            return self._listt.pop()
        else:
            print("Stack is empty!")
            return None

    def top(self):
        if not self.isEmpty():
            return self._listt[-1]
        else:
            print("Stack is empty!")
            return None

    def isFull(self):
        if len(self._listt) >= self.MaxSize:
            return True
        return False

    def isEmpty(self):
        return len(self._listt) == 0
    
Sclass = Stack()

Sclass.push(5)
Sclass.push(10)
Sclass.push(15)

for i in range(1, 5):
    Sclass.push(i)
