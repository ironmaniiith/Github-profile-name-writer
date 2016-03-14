#!/usr/bin/python
import datetime, random, time, os
from finalIndexing import *
from helper import Helper
from subprocess import Popen, PIPE

"""
Refer to folder components for generating different patterns.
"""

helper = Helper()
GLOBALS = {
	'FORCE_PUSH' : True,
}
#### To make helper script and to define Helper class in it

class User():
	"""
		Class storing the default user info
	"""

	def __init__(self):
		"""
			The next three lines are for just an example.
		"""
		self._userName = 'ironmaniiith' # Username used for logging into github account
		self._emailId = 'aalekhj2507@gmail.com' # Registered email id on github
		self._profileName = 'Aalekh Jain' # The name that needs to be written on the github profile with above userName and emailId

		self.__set_username__()
		self.__set_emailid__()
		self.__set_profile_name__()

	def getUserInfo(self, configInfo):
		"""
			Generalized functions that server the purpose the following puspose for __username__, __email__, and __profile__

			# Extract and returns user information from:
				1. Global config file.
				2. Local config file.
				3. System config file.
			If all of the above fails, returns an empty string.

			Return type: String
		"""

		# Extract the information from global git config
		command = 'git config {0} user.{1}'
		configLocations = ['--global', '--local', '--system']

		for location in configLocations:
			userConfig = command.format(location, configInfo)
			output = helper.getCommandOutput(userConfig)
			if len(output):
				return output.strip()

		# Returns an empty string if both local and global config are not available
		return ''

	def __set_username__(self):
		"""
			set user's github username (self.__userName)
			Return type: NoneType
		"""
		print 'Enter your github username: ',

		info = self.getUserInfo('name')
		if len(info):
			self._userName = info
			print '\n<default: {0}>: '.format(info),

		info = raw_input()
		if len(info.strip()):
			self._userName = info

		# return 'Aalekh Jain'

	def __set_emailid__(self):
		"""
			set user's github emailId (self.__emailId)
			Return type: NoneType
		"""
		print 'Enter your github emailId: ',
		
		info = self.getUserInfo('email')
		if len(info):
			self._emailId = info
			print '\n<default: {0}>: '.format(info),

		info = raw_input()
		if len(info):
			self._emailId = info

	def __set_profile_name__(self):
		"""
			set user's profile name
			Return type: NoneType
		"""
		print 'Enter the name that you want to write on your profile: '
		
		info = raw_input()
		if len(info) : # TODO: check here for a valid profile name
			self._profileName = info
		else:
			print '<InvalidName Error>'
			self.__profile__()

user = User()

# ============================== TODO, add date class too which will contain the base date information

# Default info
INFO = {
	# Fetch the default information from git config
	'user.name': user._userName,
	'user.email': user._emailId,
	'year': '1970', # TODO  -  Put
	'month': '1', # TODO   --- Default
	'day': '1', # TODO      -  Here
	'name': user._profileName,
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