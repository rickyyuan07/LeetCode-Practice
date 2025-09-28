class MyCircularQueue:

    def __init__(self, k: int):
        self.cqueue = [-1] * k
        self.n = k
        self.len = 0
        self.head, self.tail = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.cqueue[self.tail] = value
        self.len += 1
        self.tail = (self.tail + 1) % self.n
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self.cqueue[self.head] = -1
        self.head = (self.head + 1) % self.n
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cqueue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cqueue[(self.tail-1+self.n) % self.n]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()