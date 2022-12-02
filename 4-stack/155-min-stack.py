class MinStack:

    def __init__(self):
        self.storestack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.storestack.append(val)        
        if not len(self.minstack) or val <= self.minstack[-1]:
            self.minstack.append(val)


    def pop(self) -> None:
        ret = self.storestack.pop()
        if ret == self.minstack[-1]:
            self.minstack.pop()
        return ret

    def top(self) -> int:
        return self.storestack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        