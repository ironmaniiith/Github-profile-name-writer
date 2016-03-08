#!/usr/bin/python
import datetime, random, time, os
from finalIndexing import *
from helper import *
from subprocess import Popen, PIPE

"""
Refer to folder components for generating different patterns.
"""

GLOBALS = {
	'FORCE_PUSH' = True,
}
#### To make helper script and to define Helper class in it

class User():
	"""
		Class storing the default user info
	"""

	def __init__(self):
		self.__userName = 'ironmaniiith'
		self.__emailId = 'aalekhj2507@gmail.com'
		self.__profileName = 'Aalekh Jain'
		self.__name__()
		self.__email__()
		self.__profile__()

	def getUserInfo(self, infoType):
		"""
			Extract the information from git config
		"""

		command = 'git config{0}user.{1}'
		globalUserConfig = command.format(' --global ', infoType)
		output = helper.getCommandOutput(globalUserConfig)

		if len(output):
			return output.strip()

		# If global config is not set, try for local config

		localUserConfig = command.format(' ', infoType)
		output = helper.getCommandOutput(localUserConfig)
		if len(output):
			return output.strip()
		return ''

	def __name__(self):
		"""
			set the value for self._username
			Return type: NoneType
		"""
		print 'Enter your github username: ',

		info = self.getUserInfo('name')
		if len(info):
			self.__userName = info
			print '\n<default: {0}>: '.format(info)

		info = raw_input()
		if len(info.strip()):
			self.__userName = info

		# return 'Aalekh Jain'

	def __email__(self):
		"""
			set user's github emailId
			Return type: NoneType
		"""
		print 'Enter your github emailId: '
		
		info = self.getUserInfo('email')
		if len(info):
			self.__emailId = info
			print '\n<default: {0}>: '.format(info)

		info = raw_input()
		if len(info):
			self.__emailId = info

	def __profile__(self):
		"""
			set user's profile name
			Return type: NoneType
		"""
		print 'Enter the name that you want to write on your profile: '
		
		info = raw_input()
		if len(info) : # TODO: check here for a valid profile name
			self.__profileName = info
		else:
			print '<InvalidName Error>'
			self.__profile__()

user = User()

# ============================== TODO, add date class too which will contain the base date information

# Default info
INFO = {
	# Fetch the default information from git config
	'user.name': user.__userName,
	'user.email': user.__emailId,
	'year': '1970', # TODO  -  Put
	'month': '1', # TODO   --- Default
	'day': '1', # TODO      -  Here
	'name': raw_input("Please enter your name: "),
	'no_of_commits': 5
}

allowedChar = [' '] # Add more in future
user = raw_input('Enter your github username: ')
email = raw_input('Enter your registered github email id: ')
print 'Enter the base date.'
time.sleep(1)
print '<(for more details or to know how to find base date, refer README.md)>'
time.sleep(1)

# TODO @@@@ Error handling to be done here
# Ask for the base date information here
year = int(raw_input('Enter year: '))
month = int(raw_input('Enter month: '))
day = int(raw_input('Enter day: '))
name = raw_input("Enter the name to write on profile: ")
# TODO @@@@ Verify name here, also warn user for longer names that may not fit on profile
# CheckName()

num = int(raw_input('How many commits do you want per day\n<(more commits means darker color on the profile)>: '))
startingDate = datetime.datetime(year, month, day)

for alphabet in name:
	if alphabet != ' ':
		myArray = eval('arr' + alphabet.upper())
		increment = eval('increment' + alphabet.upper())
		print alphabet
		for arr in myArray:
			components = [None]*3
			components[0] = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			components[1] = 'git add .'
			components[2] = 'git commit -m "blah blah" --amend --author="{0} <{1}> " --date="{2}"'.format(user, email, (startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y"))
			finalString = components.join('')
			final = ';'.join(components)
			if GLOBALS['FORCE_PUSH'] == True:
				final += '; git push origin master --force'
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(num) + '`;do ' +  final+ '; done' + '\n')
		startingDate = startingDate + datetime.timedelta(days=increment*7)
	else:
		print ''
		startingDate = startingDate + datetime.timedelta(days=7)
print 'Go and execute the file runThis.sh in your repository, enjoy :D'