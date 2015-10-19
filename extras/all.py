#1/usr/bin/python
import datetime
import random
A = [-3, -2, -1, 0, 3, 5, 10, 12, 18, 19, 20, 21]
B = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 18, 19, 20]
C = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 21]
D = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 21, 25, 26, 27]
E = [-4, -3, -2, -1, 0, 3, 5, 7, 10, 12, 14, 17, 21]
F = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 17]
G = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 19, 21, 24, 26, 27, 28]
H = [-4, -3, -2, -1, 0, 5, 12, 17, 18, 19, 20, 21]
I = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 21, 24, 28]
J = [-4, 0, 3, 7, 10, 11, 12, 13, 14, 17, 24]
K = [-4, -3, -2, -1, 0, 5, 11, 13, 17, 21]
L = [-4, -3, -2, -1, 0, 7, 14, 21]
M = [-4, -3, -2, -1, 0, 4, 12, 18, 24, 25, 26, 27, 28]
N = [-4, -3, -2, -1, 0, 4, 12, 20, 24, 25, 26, 27, 28]
O = [-4, -3, -2, -1, 0, 3, 7, 10, 14, 17, 18, 19, 20, 21]
P = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 18]
Q = [-4, -3, -2, -1, 0, 3, 7, 10, 13, 14, 17, 21, 24, 25, 26, 27, 28, 35]
R = [-4, -3, -2, -1, 0, 3, 5, 10, 12, 13, 18, 21]
S = [-4, -3, -2, 0, 3, 5, 7, 10, 12, 14, 17, 19, 20, 21]
T = [-4, 3, 10, 11, 12, 13, 14, 17, 24]
U = [-4, -3, -2, -1, 0, 7, 14, 17, 18, 19, 20, 21]
V = [-4, -3, -2, 6, 14, 20, 24, 25, 26]
W = [-4, -3, -2, -1, 0, 6, 12, 20, 24, 25, 26, 27, 28]
X = [-4, 0, 4, 6, 12, 18, 20, 24, 28]
Y = [-4, 4, 12, 13, 14, 18, 24]
Z = [-4, 0, 3, 6, 7, 10, 12, 14, 17, 18, 21, 24, 28]

user = raw_input("Enter the github username:- ")
email = raw_input("Enter the registered github email id:- ")
year = int(raw_input("Enter the year:- "))
mon = int(raw_input("Enter the month:- "))
day = int(raw_input("Enter the day:- "))
name=raw_input("Enter the name (currently supports only name and space):- ")
num = int(raw_input("How many commits do you want..:- "))
startingDate = datetime.datetime(year, mon, day)
for word in name:
	word = word.upper()
	if word != ' ':
		increment = eval(word.lower() + 'Increment')
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
	else:
		startingDate = startingDate + datetime.timedelta(days=7)