class queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity-1
        self.q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size==self.capacity
    
    def isEmpty(self):
        return self.size == 0

    def enqueue(self,item):
        if self.isFull():
            print("queue is full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.q[self.rear]=item
        self.size = self.size+1
        print("item enqueued",item) 

    def dequeue(self):
        if self.isEmpty():
            print("queue empty , nothing to dequeue")
            return
        item = self.q[self.front]
        self.front = (self.front + 1)%(self.capacity)
        self.size = self.size-1
        print("item dequeued ",item)

    def f(self):
        print("front : ",self.q[self.front])

    def r(self):
        print("rear : ",self.q[self.rear])

if __name__=="__main__":
    Q = queue(10)
    for item in range(5):
        Q.enqueue(item)
    Q.f()
    Q.r()
    for item in range(3):
        Q.dequeue()
    Q.f()
    Q.r()