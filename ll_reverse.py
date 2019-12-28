class LinkedList(object):
  def __init__(self, head=None):
    self.head = head


  def __str__(self):
    lstr = ""
    tmp = self.head
    while tmp.next:
      lstr += str(tmp.data) + " -> "
      tmp = tmp.next

    lstr += str(tmp.data)
    return lstr


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

  def get_next(self):
    return self.next

def ll_reverse(l):
  head_o = l.head
  upd_next = None
  while head_o.next != None:
    #print(head_o.data)
    temp = head_o.next
    head_o.next = upd_next
    upd_next = head_o
    head_o   = temp
  head_o.next = upd_next
  #print(head_o.next)

  l.head = head_o
  return l




if __name__ == '__main__':
  head1 = Node(1)
  head1.next = Node(2)
  head1.next.next = Node(3)
  head1.next.next.next = Node(4)

  n = head1.next.next.next

  head2 = Node('a')
  head2.next = Node('b')
  head2.next.next = n

  n.next = Node(9)
  n.next.next = Node(6)
  n.next.next.next = Node(7)

  l1 = LinkedList(head1)
  l2 = LinkedList(head2)
  print('Original ll')
  print(l1)
  #print(l2)
  print('Reversed ll')
  print(ll_reverse(l1))

