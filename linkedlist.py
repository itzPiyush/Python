#!/usr/bin/python

class Node(object):
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def get_data(self):
    return self.data
  
  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head

  def insert(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
 
  def print_list(self):
    current = self.head
    count=0;
    while current:
      count += 1
      print  current.data
      current = current.get_next()
    print 'Total nodes: ',count

#example code
l = LinkedList()
l.insert('a')
l.insert('b')
l.insert(1)
l.insert(2)
l.insert(3)

l.search('a')
l.print_list()

