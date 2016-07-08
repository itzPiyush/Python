#!/usr/bin/python
class Demo:
  'This is the first class made in python'
  my_var = 10
  #The my_var is a class variable whose value is sharyed among all instances
  # of this class. Can be accessed as Demo.my_var

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Demo.my_var += 1
  #This methos is class constuctor or intialisation method that Python creates
  #  when you create a new instance of this class

  def display(self):
    print "Total EMployee %d" % Employee.my_var

  def displayEmp(self):
    print "Name: ", self.name, ", salary: ",self.salary 



#Creating first object of the Demo class
obj1 = Demo("Zara",2000)
#second object
obj2 = Demo("John",5000)

#Accessing object attributes
obj1.displayEmp()
obj2.displayEmp()
#Accessing class variables
print "Total Employee %d" % Demo.my_var
