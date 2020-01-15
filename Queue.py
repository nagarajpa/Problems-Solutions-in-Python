#Queue using Lists:
#     enqueue(x): O(1)
#     dequeue(): O(1)
#     peek(): O(1)  # front of the queue without removing
#     size: O(1)
#     str(): O(n)
class Queue(object):
  def __init__(self, size):
    self.count = 0
    self.data  = [None]*size
    self.head  = 0
    self.tail  = 0

  def __str__(self):
    return self.str()

  def str(self):
    str1 = ''
    for x in range(self.head,self.tail):
      str1 += str(self.data[x])
      str1 += '<-'
    return str1

  def push(self, val):
    if (self.count == len(self.data)):
      raise Exception ('Push attempted when Queue is Full')
    else:
      self.data[self.tail] = val
      self.count = self.count+1
      if (self.tail < len(self.data) - 1):
        self.tail  = self.tail + 1
      else:
        self.tail  = 0

  def pop(self):
    if (self.IsEmpty()):
      raise Exception ('Pop attempted when Queue is Empty')
    else:
      val,self.data[self.head] = self.data[self.head], None
      self.count = self.count-1
      if (self.head < len(self.data) - 1):
        self.head  = self.head + 1
      else:
        self.head  = 0
      return val

  def peek(self):
    if (self.IsEmpty()):
      return None
    else:
      return self.data[self.head]

  def size(self):
    return self.count

  def IsEmpty(self):
    return self.count == 0

if __name__ == "__main__":
  s = Queue(4)
  print ('Is Queue empty?:', s.IsEmpty())
  s.push(10)
  s.push(20)
  s.push(30)
  s.push(40)
  #s.push(50)
  #s.push(60)
  #s.push(70)
  s.pop()
  s.pop()
  s.pop()
  print ('Peek:', s.peek())
  print ('Is Queue empty?:', s.IsEmpty())
  print ('Queue S:', s)
  print ('Size of queue:', s.count)
  v = s.pop()
  print ('popped elelement:', v)
  print ('After pop:', s)
  print ('Peek:', s.peek())
  s.push(50)
  s.push(60)
  print ('Queue S:', s)
  print ('Size of queue:', s.count)
  v = s.pop()
  print ('popped elelement:', v)
  v = s.pop()
  print ('popped elelement:', v)

  print ('Size of queue:', s.count)
  print ('Peek:', s.peek())
