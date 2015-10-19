#1/usr/bin/python
import datetime
import random
import time
from finalIndexing import *

# A = [0,-1,-2,-3,3,5,10,12,18,19,20,21];
# L = [0,-1,-2,-3,-4,7,14,21]
# E = [0,-1,-2,-3,-4,7,14,21,3,10,17,5,12]
# K = [0,-1,-2,-3,-4,17,11,5,13,21]
# H = [0,-1,-2,-3,-4,5,12,21,20,19,18,17]
# J = [0,7,14,-4,3,10,17,24,11,12,13]
# I = J[:]
# I.extend([21,28])
# N = [0,-1,-2,-3,-4,4,12,20,24,25,26,27,28]

# aIncrement = 5
# lIncrement = 5
# eIncrement = 5
# kIncrement = 5
# hIncrement = 5
# jIncrement = 6
# iIncrement = 6
# nIncrement = 6

##########
# If you want to generate some different patterns then this, then the folder components is for you. :D
###########


user = raw_input("Enter the github username:- ")
email = raw_input("Enter the registered github email id:- ")
print "Now you need to enter the date from which you want to start writing your name"
time.sleep(2)
print "For more details or to know how to find date, refer README.md"
time.sleep(2)
year = int(raw_input("Enter the year:- "))
mon = int(raw_input("Enter the month:- "))
day = int(raw_input("Enter the day:- "))
name=raw_input("Enter the name (currently supports only name and space):- ")
num = int(raw_input("How many commits do you want..:- "))
startingDate = datetime.datetime(year, mon, day)

for word in name:
	if word.isdigit():
		text = "arr" + str(word)
	else:
		text = "arr" + word.upper()

	if text != ' ':
		increment = eval('increment' + word)
		print word
		myArray = eval(text)
		for i in myArray:
			first = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			second = 'git add .'
			third = 'git commit -m "blah blah" --amend --author="' + user + ' <' +email + '> " --date="' + (startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y") + '"'

			final = first + '; ' + second + '; ' + third + '; git push origin master --force'
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(num) + '`;do ' +  final+ '; done' + '\n')
		startingDate = startingDate + datetime.timedelta(days=increment*7)
	else:
		startingDate = startingDate + datetime.timedelta(days=1)
print "Go and execute the file runThis.sh in your repository"