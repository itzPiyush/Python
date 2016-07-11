#!/usr/bin/python

class Victor:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def __str__(self):
    return 'Vector (%d, %d)' % (self.a, self.b)

  #Operator overloading
  def __add__(self,other):
    return Victor(self.a + other.a, self.b - other.b)

v1 = Victor(2,10)
v2 = Victor(5,-2)

print v1 + v2

