#!/usr/bin/python
 #Parent class
class Parent:
  parentAttr = 100;
  def __init__(self):
    print "Calling parent constructor"

  def parentMethod(self):
    print 'Calline parent method'

  def setAttr(self, attr):
    Parent.parentAttr = attr

  def getAttr(self):
    print "Parent attribute : ", Parent.parentAttr

#Child class inheriting Parent
class Child(Parent):
  def __init__(self):
    Parent()	#explicit call to Parent Constructor
    print "Calling child constructor"

  def childMethod(self):
    print 'calling child method'

  def setAttr(self, attr):
    print "inside child", attr
    Parent.parentAttr = attr
# overiding Parent method
  def parentMethod(self):
    print "Changing Parent method from child's class"

c = Child()
c.childMethod()
c.parentMethod()
c.getAttr()
c.setAttr(200)
c.getAttr()
c.parentMethod()

#pre=Parent()
#print pre
Child()
