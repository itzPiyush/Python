#!/usr/bin/python

class Point:
  def __intit(self, x=0, y=0):
    self.x = x
    self.y = y
  def __del__(self):
    class_name = self.__class__.__name__
    print class_name, "Destroyed"

ptr1 = Point()
ptr2 = Point()
ptr3 = ptr1
print id(ptr1), id(ptr2), id(ptr3)  #prints id of the object

del ptr1
del ptr2
del ptr3

