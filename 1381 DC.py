from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.stack = deque()

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.appendleft(x)
            self.size += 1
        
    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        else:
            return -1
        
    def increment(self, k: int, val: int) -> None:
        if self.size > k:
            self.stack = 
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)