#!/usr/bin/python

#function takes input
def inp():
  a = []
  var = True
  print("Enter 99 to exit")
  print'-----------------'
  while var:
    num = input("Enter the no. :")
    if num == 99:
      var = False
      break
    a.append(num)
  return a

#function remove duplicates
def rem_dub(li):
  s = set(li)
  s2 = set()
  l2 = []
  for i in range(0, li.__len__()):
    for j in range(i+1, li.__len__()):
      if li[i] == li[j] and i != j:
        s2.add(li[i])
  li2 = list(s2)
  print ''
  print "Entered list: ", li
  print "Duplicates found: ", li2
  print ''
  print '---------------------'
  print "Desired Output: ",s-s2
  print '---------------------'
  print ' '

#input function
li = inp()
rem_dub(li)
