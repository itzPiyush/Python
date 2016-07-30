#!/usr/bin/python
from collections import defaultdict
from random import randint
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#uncomment to use randomly generated lists
#a = random.sample(range(10), randint(5,15))
#b = random.sample(range(10), randint(5,15))

a.sort()
b.sort()

print "List a: ",a
print "List b: ",b

#creating dictinonary for list a
temp = {}
temp = defaultdict(lambda: 0 ,temp)
for i in range(0, a.__len__()):
  res = temp[a[i]]
  temp[a[i]] = res+1


new_list = []
ind = 0
#matching elements from dictionary having key = 1 with list b
for i in range(0, temp.__len__()):
  if temp[a[i]] == 1:
    for j in range(0, b.__len__()):
      if temp[a[i]] == b[j]:
	new_list.append(a[i])


print "Output ",new_list

