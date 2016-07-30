#!/usr/bin/python

#function to find max
def findMax(a,b,c):
  res = a if a > c and a > b else b if b > a and b > c else c
  print "Max: " , res

#calling function
a = 32
b = 31
c = 100
findMax(a,b,c)
