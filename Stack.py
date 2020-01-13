#Stack:
#    push(x): O(1)
#    pop(): O(1)
#    size(): O(1)
#    top(): O(1)  # top of the stack without popping it
#    str(): O(n)

class Stack(object):
  def __init__(self, size):
    self.count = 0
    self.data  = [None]*size

  def __str__(self):
    return self.str()

  def str(self):
    str1 = ''
    for x in range(self.count):
      str1 += str(self.data[x])
      str1 += '<-'
    return str1

  def push(self, val):
    if (self.count == len(self.data)):
      raise Exception ('Push attempted when Stack is Full')
    else:
      self.data[self.count] = val
      self.count = self.count+1

  def pop(self):
    if (self.IsEmpty()):
      raise Exception ('Pop attempted when Stack is Empty')
    else:
      val,self.data[self.count-1] = self.data[self.count-1], None
      self.count = self.count-1
      return val

  def peek(self):
    return self.data[self.count-1]

  def size(self):
    return self.count

  def IsEmpty(self):
    return self.data[0] == None

if __name__ == "__main__":
  s = Stack(8)
  print ('Is Stack empty?:', s.IsEmpty())
  s.push(10)
  s.push(20)
  s.push(30)
  s.push(40)
  s.push(50)
  s.push(60)
  s.push(70)
  print ('Is Stack empty?:', s.IsEmpty())
  print ('Stack S:', s)
  print ('Size of stack:', s.count)
  v = s.pop()
  print ('popped elelement:', v)
  print ('After pop:', s)
  print ('Peek:', s.peek())
