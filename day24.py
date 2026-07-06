#stack using array
class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0 
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print('Stack is empty. Cannot Pop')
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is Empty. Cannot peek")
            return None
    def size(self):
        return len(self.stack)
        
        
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)        
print("Stack:", stack.stack)  # Output: Stack: [1, 2, 3]

print("Peek:", stack.peek())  # Output: Peek: 3

print("Pop:", stack.pop())    # Output: Pop: 3
print("Stack:", stack.stack)  # Output: Stack: [1, 2]

print("Is Empty?", stack.is_empty())  # Output: Is Empty? False

print("Stack Size:", stack.size())     # Output: Stack Size: 2

#queue using array
class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)   
    
#stack using queue

from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        s = self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        n = self.q.queue[0]
        self.q.get()
        return n
    def top(self) -> int:
        return self.q.queue[0]

        

    def empty(self) -> bool:
        return self.q.empty()
    
#queue using stack
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return -1
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            print("Queue is empty, cannot peek.")
            return -1

        return self.output[-1]

        

    def empty(self) -> bool:
        return not self.input and not self.output

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
        


