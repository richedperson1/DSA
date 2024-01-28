class MinStack:

    """
    The above code defines a class that implements a stack data structure with additional functionality
    to keep track of the minimum element in the stack.
    """
    def __init__(self):
        self.stack = []
        self.mini  = []
        
    def push(self, val: int) -> None:
        index = len(self.mini)
        self.stack.append((val,index))
        if len(self.mini)==0:
            self.mini.append((val,index))
            return
        if self.mini[-1][0]>=val:
            self.mini.append((val,index))

    def pop(self) -> None:
        last_num,index = self.stack.pop()
        if index<=self.mini[-1][-1]:
            self.mini.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.mini[-1][0]
