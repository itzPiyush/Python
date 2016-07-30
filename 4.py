#!/usr/bin/python

def fib(num):
	v1 = 0
	v2 = 1
	i = 0
	tot = 0

	while i < num:
		tot = tot + v2
		v2 = v1
		print tot
		v1 = tot
		i += 1

num = input("Enter the number of how many Fibonnaci numbers: ")
fib(num)
 
