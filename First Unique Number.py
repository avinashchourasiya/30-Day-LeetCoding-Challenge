from collections import deque as q;
from collections import OrderedDict as dd

class FirstUnique:
    def __init__(self, nums):
        self.arr = nums
        self.d = dd();
        for index, number in enumerate(self.arr):
            if (number in self.d):
                self.d[number] += 1;
            else:
                self.d[number] = 1;
        # print(self.d)


    def showFirstUnique(self):
        print(self.d);



    def add(self, value):
         print(q);

f=FirstUnique([2,3,4,5,5,5,1]);
f.add(7);
f.showFirstUnique();

