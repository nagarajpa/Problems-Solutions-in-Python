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

def findMerge_N2(l1, l2):
  '''
  l1, l2: Linked list
  TODO: Implement
    return Node 'n' where l1 and l2 merge, None if they dont merge
  '''
  temp1 = l1.head
  temp2 = l2.head
  merge_node = None
  while temp1 != None:
    while temp2 != None:
      #print ('temp2',temp2.data)
      if (temp1 == temp2):
        return temp1
      temp2 = temp2.get_next()
    temp1 = temp1.get_next()
    temp2 = l2.head
    #print('temp1',temp1.data)
  return None


def findMerge_N(l1, l2):
  temp = l1.head
  map1 = {}
  while temp != None:
    map1[str(temp)] = 1
    temp =  temp.get_next()
  temp1 = l2.head
  while temp1 != None:
    if str(temp1) in map1:
      return temp1
    temp1 = temp1.get_next()

  return None

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

  print(l1)
  print(l2)
  print(findMerge_N(l1,l2).data)
  assert( findMerge_N2(l1, l2) == n)
  assert( findMerge_N(l1, l2) == n)

