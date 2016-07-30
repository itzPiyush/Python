#!/usr/bin/python

from random import randint

print '    ***********'
print '      WELCOME'
print '    ***********'
print 'Enter to "exit" the game.'
print '_________________________'
nam = raw_input("Enter your name: ")
var = True
score = 0

while var:
  num = raw_input("Enter the number b/w 0 - 10: ")
  if num == 'exit':
    var = False
    break
  num = int(num)
  #rand = randint(0,10)
  rand = 7
  print num	,'||',	rand
  if num > rand:  
    print "Guessed too high."
  elif num < rand:
    print "Guessed too low."
  else:  
    print "Exactly Right!"
    score += 1
  
print '_______________'
print '  SCORE BOARD'
print '---------------'
print nam,' Scored : ',score
print '________________'
