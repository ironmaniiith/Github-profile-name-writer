import sys

"""
	First Line  : Enter the alphabet, number or special character.
	Second Line : Now enter the dimensions of the rectangle (n and m) that the above text will take.
	Next Lines	: Next enter the representation of the text of the given dimension...
	Following example will make it clear:
	
	Brace yourself, examples are coming :P
=======================================
	5
	5 5
	*****
	*
	*****
	    *
	*****
=======================================
	T
	5 5
	*****
	  *  
	  *  
	  *  
	  *  
=======================================

"""

text = raw_input()
numbers = raw_input()
numbers = map(int, numbers.split(' '))
n = numbers[0]
m = numbers[1]
arr = []

for x in xrange(0, n):
	test = raw_input()
	arr.append(test)
arr.reverse()
ans = []


# Index the arrays according to github dates
for i,line in enumerate(arr):
	index = -i
	for j,alpha in enumerate(line):
		if alpha == '*':
			ans.append(j*7 + index)
ans.sort()

print "arr" + text + " = " + str(ans)
print "increment" + text + " = " + str(m+1)
