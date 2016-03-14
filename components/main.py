#!/usr/bin/python
import datetime, random, time, os, sys
from finalIndexing import *
from helper import Helper
from subprocess import Popen, PIPE

"""
	Refer to folder components for generating different patterns for alphabets and numbers.
"""

helper = Helper()

GLOBALS = {
	'FORCE_PUSH' : True,
	'DEFAULT_DAYS_INCREMENT' : 7,
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
		# 'ironmaniiith'

	def __set_emailid__(self):
		"""
			set user's github emailId (self.__emailId)
			Return type: NoneType
		"""
		print 'Enter your registered github emailId: ',
		
		info = self.getUserInfo('email')
		if len(info):
			self._emailId = info
			print '\n<default: {0}>: '.format(info),

		info = raw_input()
		if len(info):
			self._emailId = info
		# 'aalekhj2507@gmail.com'

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
			self.__set_profile_name__()
		# 'Aalekh Jain'

user = User()

# ============================== TODO, add date class too which will contain the base date information

# User Info
INFO = {
	'userName' : user._userName,
	'emailId' : user._emailId,
	'profileName': user._profileName,
	'BASE_DATE' : {
		'year': 1970,
		'month': 1,
		'day': 1
	},
	'no_of_commits' : 5,
}

allowedChars = [' '] # Add more in future

print '\nEnter the Base Date.'
print '<(For more details or to know how to find Base Date, refer README.md)>'

# TODO @@@@ Error handling to be done here
base_date = INFO['BASE_DATE']

# Ask for the base date information here
# Also add feature for default date

base_date['year'] = int(raw_input('Enter year: '))
base_date['month'] = int(raw_input('Enter month: '))
base_date['day'] = int(raw_input('Enter day: '))

# TODO @@@@ Verify name here, also warn user for longer names that may not fit on profile
# CheckName()

INFO['no_of_commits'] = int(raw_input('How many commits do you want per day:\n<(more commits means darker color on the profile)>: '))
startingDate = datetime.datetime(base_date['year'], base_date['month'], base_date['day'])

for alphabet in INFO['profileName']:
	time.sleep(0.1)
	if alphabet != ' ':
		myArray = eval('arr' + alphabet.upper())
		increment = eval('increment' + alphabet.upper())

		# Print the current alphabet for user
		print alphabet,
		sys.stdout.flush()

		for i in myArray:
			components = [None]*3
			components[0] = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			components[1] = 'git add .'
			components[2] = 'git commit -m "blah blah" --amend --author="{0} <{1}> " --date="{2}"'.format(
								INFO['userName'],
								INFO['emailId'],
								(startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y")
							)
			finalCommand = ';'.join(components)

			if GLOBALS['FORCE_PUSH'] == True:
				finalCommand += '; git push origin master --force'

			# Write the final constructed command in runThis.sh
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(INFO['no_of_commits']) + '`;do ' +  finalCommand + '; done' + '\n')
		startingDate += datetime.timedelta(days=increment*GLOBALS['DEFAULT_DAYS_INCREMENT'])
	else:
		print ' ',
		startingDate += datetime.timedelta(days=GLOBALS['DEFAULT_DAYS_INCREMENT'])

print '\nNow go and execute the file runThis.sh in your repository\nHave Fun :D'