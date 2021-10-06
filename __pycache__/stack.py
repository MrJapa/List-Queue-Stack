class Stack:

    def __init__(self):
        self.stack = list()                         ## Instance - fortæller at stack er en list
        self.maxSize = 5                            ## Sætter en maks størrelse på listen
        self.top = 0                                ## Sætter top til 0
    
    def push(self,data):
        if self.top>=self.maxSize:                  ## Hvis toppen er større end nul, så er stacken fuld
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
    
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
       
    
    def size(self):
        return self.top

s = Stack()
print(f"Size of stack: {s.size()}\n")

print(f"Pushed 1: {s.push(1)}")
print(f"Pushed 2: {s.push(2)}")
print(f"Pushed 3: {s.push(3)}")
print(f"Pushed 4: {s.push(4)}")
print(f"Pushed 5: {s.push(5)}\n")

print(f"Size of stack: {s.size()}\n")   

print(f"Popped: {s.pop()}")
print(f"Popped: {s.pop()}")
print(f"Popped: {s.pop()}")
print(f"Popped: {s.pop()}")
print(f"Popped: {s.pop()}\n")

print(f"Size of stack: {s.size()}")  