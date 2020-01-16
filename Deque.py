class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data  = [None]*k
        self.count = 0
        self.head  = 0
        self.tail  = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if (self.head == 0):
                self.head = len(self.data)-1
            else:
                self.head = self.head - 1
            self.data[self.head] = value
            self.count = self.count + 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            #print ('isFull tail', self.tail, self.count)
            self.data[self.tail] = value
            if (self.tail < len(self.data)-1):
                self.tail = self.tail + 1
            else:
                self.tail = 0
            self.count = self.count + 1
            return True
        else:
            #print (self.data)
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if (self.head < len(self.data)-1):
                self.head = self.head + 1
            else:
                self.head = 0
            self.count = self.count - 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if (self.tail == 0):
                self.tail = len(self.data)-1
            else:
                self.tail = self.tail -1
            self.count = self.count - 1
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.data[self.head]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.data[self.tail-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.count == len(self.data):
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
