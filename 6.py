#!/usr/bin/python
import random
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_'
mypw = ''
pw_len = 0
print 'How Strong you want your random password?'
print 'Press "1" for WEAK password'
print 'Press 2 for MEDIUM password'
print 'Press 3 for STRONG password'

num = input("Enter your choice: ")

#set password length according to choice made above
if num == 1:
  pw_len = 8
elif num == 2:
  pw_len = 10
elif num == 3:
  pw_len = 12
else:
  print 'Not a Valid Choice'
  sys.exit(0)
#computes password
for i in range(pw_len):
  next_ind = random.randrange(len(alphabet))
  mypw = mypw + alphabet[next_ind]

print ''
print 'Password Ready:	',mypw
print ''

#reference :  http://interactivepython.org/runestone/static/everyday/2013/01/3_password.html
