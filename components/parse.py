#!/usr/bin/python
import sys
alphabet = raw_input()
numbers = raw_input()
n = int(numbers.split(' ')[0])
m = int(numbers.split(' ')[1])
arr = []
for x in xrange(0,n):
	test = raw_input()
	# test = test.split(' ')
	arr.append(test)
arr.reverse()
ans = []
# print arr
for i,line in enumerate(arr):
	index = -i
	for j,alpha in enumerate(line):
		if alpha == '*':
			ans.append(j*7 + index)
ans.sort()
print alphabet + " = " + str(ans)
print alphabet + "Increment = " + str(m+1)