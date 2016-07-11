#!/usr/bin/python

#class A():	#old-style class
class A(object):	#new-style class
  pass
class B(A):
  pass

a = A()
b = B()
print (type(A), type(B))
print (type(a), type(b))
print B.mro()
