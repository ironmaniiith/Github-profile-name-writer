#1/usr/bin/python
import datetime
import random
import time
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

A = [-3, -2, -1, 0, 3, 5, 10, 12, 18, 19, 20, 21]
AIncrement = 5
B = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 18, 19, 20]
BIncrement = 5
C = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 21]
CIncrement = 5
D = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 18, 19, 20]
DIncrement = 5
E = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 21]
EIncrement = 5
F = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 17]
FIncrement = 5
G = [-4, -3, -2, -1, 0, 3, 7, 10, 12, 14, 17, 19, 21, 24, 26, 27, 28]
GIncrement = 6
H = [-4, -3, -2, -1, 0, 5, 12, 17, 18, 19, 20, 21]
HIncrement = 5
I = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 21, 24, 28]
IIncrement = 6
J = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 24]
JIncrement = 6
K = [-4, -3, -2, -1, 0, 5, 11, 13, 17, 21]
KIncrement = 5
L = [-4, -3, -2, -1, 0, 7, 14, 21]
LIncrement = 5
M = [-4, -3, -2, -1, 0, 4, 12, 18, 24, 25, 26, 27, 28]
MIncrement = 6
N = [-4, -3, -2, -1, 0, 4, 12, 20, 24, 25, 26, 27, 28]
NIncrement = 6
O = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 18, 19, 20, 21]
OIncrement = 5
P = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 18]
PIncrement = 5
Q = [-4, -3, -2, -1, 0, 3, 7, 10, 13, 14, 17, 21, 24, 25, 26, 27, 28, 35]
QIncrement = 7
R = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 13, 18, 21]
RIncrement = 5
S = [-4, -3, -2, 0, 3, 5, 7, 10, 12, 14, 17, 19, 20, 21]
SIncrement = 5
T = [-4, 3, 10, 11, 12, 13, 14, 17, 24]
TIncrement = 6
U = [-4, -3, -2, -1, 0, 7, 14, 17, 18, 19, 20, 21]
UIncrement = 5
V = [-4, -3, -2, 6, 14, 20, 24, 25, 26]
VIncrement = 6
W = [-4, -3, -2, -1, 0, 6, 12, 20, 24, 25, 26, 27, 28]
WIncrement = 6
X = [-4, 0, 4, 6, 12, 18, 20, 24, 28]
XIncrement = 6
Y = [-4, 4, 12, 13, 14, 18, 24]
YIncrement = 6
Z = [-4, 0, 3, 6, 7, 10, 12, 14, 17, 18, 21, 24, 28]
ZIncrement = 6

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
	word = word.upper()
	if word != ' ':
		increment = eval(word.upper() + 'Increment')
		print word
		myArray = eval(word)
		for i in myArray:
			first = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			second = 'git add .'
			third = 'git commit -m "blah blah" --amend --author="' + user + ' <' +email + '> " --date="' + (startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y") + '"'

			final = first + '; ' + second + '; ' + third + '; git push origin master --force'
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(num) + '`;do ' +  final+ '; done' + '\n')
		startingDate = startingDate + datetime.timedelta(days=increment*7)