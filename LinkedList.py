########################################################
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
########################################################


########################################################
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

  def reverseBetween(self, m, n):
    head = self.head
    if (m == n):
        return head
    if head.next == None:
        return head
    temp_head = head
    short_head = head
    short_tail = head.next
    for x in range(n):
        if (x == m-2):
            short_head = temp_head
        if (x == n-1):
            short_tail = temp_head
        temp_head = temp_head.next
    upd_head_node = short_head
    upd_tail_node = short_tail
    if (m != 1):
        tmp_node = upd_head_node.next
        upd_head_node.next = short_tail
        upd_head_node = tmp_node
        upd_head_node_next = upd_head_node.next
        upd_head_node.next = short_tail.next
    else:
        tmp_node = upd_head_node.next
        upd_head_node.next = short_tail.next
        upd_head_node_next = tmp_node
    i = 0
    while upd_head_node_next != short_tail:
        tmp_node = upd_head_node_next.next
        upd_head_node_next.next  = upd_head_node
        upd_head_node      = upd_head_node_next
        upd_head_node_next = tmp_node
    upd_head_node_next.next = upd_head_node
    if (m == 1):
        head = short_tail
    return head

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
########################################################

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
  a = Node(10)
  b = Node(20)
  a.next = b
  print(a)
  print(b)

  ll = LinkedList(a)
  ll.add(30)
  l = [1,2,3,4,5,6]
  ll2 = LinkedList(LinkedList.FromList(l))
  print (ll)
  print (ll2)
  l1 = LinkedList.ToList(ll2.head)
  assert (LinkedList.ToList((ll2.reverseBetween(2,4))) == [1,4,3,2,5,6])
  #print (LinkedList(ll2.reverseBetween(2,4)))
  #print (LinkedList(ll2.reverseBetween(2,4)))

