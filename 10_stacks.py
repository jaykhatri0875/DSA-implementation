# implementation of all stack functions

from traceback import print_tb


stack = []
print(stack)
stack.append(1)
stack.append(3)
print(stack)
stack.pop()
print(stack)
'''
class stack:
    sta = []
    top = 0
    def __init__(self,data):
        pass
    def push(self,item):
        self.sta.append(item)
        self.top += 1
    def pop(self):
        del self.sta[self.top]
        self.top -= 1
    
'''