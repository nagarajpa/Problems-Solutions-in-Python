class Node(object):
  '''
  Node object used to create Linked list
  '''
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    nstr = 'Data:' + str(self.data)
    nstr += '\n'
    if (self.next != None):
      nstr += 'Next Node data:' + str(self.next.data)
    else:
      nstr += 'No next Node'
    return nstr

  def get_next(self):
    return self.next


class LinkedList(object):
  '''
  Linked list object
  '''
  def __init__(self, head):
    self.head = head

  def __str__(self):
    lstr = ""
    tmp = self.head
    while tmp.next:
      lstr += str(tmp.data) + " -> "
      tmp = tmp.next

    lstr += str(tmp.data)
    return lstr

  def add(self, data):
    head = self.head
    while (head.next):
      head = head.next
    head.next = Node(data)
    head.next.next = None
    return

  @staticmethod
  def FromList(l : list):
    if l:
      head = Node(l[0])
    else:
      head = None
    node = head
    for x in range(1,len(l)):
      node.next = Node(l[x])
      node = node.next
    node.next = None
    return head

  @staticmethod
  def ToList(head: Node):
    l = []
    if head == None:
      return l
    else:
      while (head.next):
        l.append(head.data)
        head = head.next

      l.append(head.data)
    return l




if __name__ == '__main__':
  a = Node(10)
  b = Node(20)
  a.next = b
  print(a)
  print(b)

  ll = LinkedList(a)
  ll.add(30)
  l = [1,2,3]
  ll2 = LinkedList(LinkedList.FromList(l))
  print (ll)
  print (ll2)
  l1 = LinkedList.ToList(ll2.head)
  print ('###')
  print (l1)

