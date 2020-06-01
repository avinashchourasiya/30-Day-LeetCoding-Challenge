class MinStack:
    def __init__(self):
        self.stk = [];
        self.stk.clear();
        self.m = 0

    def push(self, x: int) -> None:
        if(len(self.stk)==0):
            self.stk.append([x, x]);
        else:
            self.stk.append([x,min(x,self.stk[len(self.stk)-1][1])]);


    def pop(self) -> None:
        self.stk.pop(-1);
        print(self.stk);

    def top(self) -> int:
        return (self.stk[len(self.stk) - 1][0]);
        print(self.stk);

    def getMin(self) -> int:
        return (self.stk[len(self.stk) - 1][1]);
        print(self.stk);


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin());
obj.pop()
print(obj.top());
print(obj.getMin());


