import datetime, random, time, os, sys
from finalIndexing import *
from helper import Helper
from subprocess import Popen, PIPE

"""
	Refer to folder components for generating different patterns for alphabets and numbers.
"""

helper = Helper('I am the Ironman..!!')

GLOBALS = {
	'FORCE_PUSH' : True,
	'DEFAULT_DAYS_INCREMENT' : 7,
	'WRITER_FILE': 'writer.sh',
}

class User:
	"""
		Class storing the default user info
	"""

	def __init__(self):
		
		"""
			The next three lines are just for an example.
		"""
		self._userName = 'ironmaniiith' # Username used for logging into github account
		self._emailId = 'aalekhj2507@gmail.com' # Registered email id on github
		self._profileName = 'Aalekh Jain' # The name that needs to be written on the corresponding github profile

		self.__set_username__()
		self.__set_emailid__()
		self.__set_profile_name__()

	def getUserInfo(self, configInfo):
		
		"""
			Generalized functions that serve the following purpose for __username__, __email__, and __profile__

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

		# Returns an empty string if the above configs are not available
		return ''

	def __set_username__(self):
		"""
			set user's github username (self._userName)
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

class Date:
	"""
		Class storing default date info
	"""

	def __init__(self):
	
		self.setDefaultDate()
		print '\nEnter the Base Date in the format (YY-MM-DD).'
		print '<(For more details or to know how to find Base Date, refer README.md)>',
		self.setBaseDate()

	def setDefaultDate(self):
		"""
			Procedure for setting the default date:
				1. Find the date corresponding to exactly one year back.
				2. Add three weeks to that date and find the nearest Sunday after this day (ceiling function wrt Sunday :P ).
				3. Set the default base date as the date corresponding to one day less than this Sunday (according to the requirements, base date need to start from a Saturday)
		"""
		
		self.now = datetime.datetime.now()
		self.oldDate = self.now - datetime.timedelta(days=365-3*7)
		
		diffSunday = 6 - self.oldDate.weekday() # Difference with the nearest Sunday after this day

		self.defaultDate = self.oldDate + datetime.timedelta(days=diffSunday-1) # Base date need to start from Saturday, hence -1

		self.year = self.defaultDate.year
		self.month = self.defaultDate.month
		self.day = self.defaultDate.day

	def setBaseDate(self):
		print '\n<default: {0}>: '.format(self.defaultDate.strftime('%Y-%m-%d')),

		info = raw_input()
		if len(info):
			info = info.strip('-')
			try:
				self.year = int(info[0])
				self.month = int(info[1])
				self.day = int(info[2])
				datetime.datetime(year=self.year, month=self.month, day=self.day)
			except Exception:
				print 'Please enter a valid Base Date (leave blank for using Default Date)'
				self.setBaseDate()

	def getBaseDate(self):
		return {
			'year' : self.year,
			'month' : self.month,
			'day' : self.day
		}

date = Date()
base_date = date.getBaseDate()

# User Info
INFO = {
	'userName' : user._userName,
	'emailId' : user._emailId,
	'profileName': user._profileName,
	'no_of_commits' : 5,
}

allowedChars = [' '] # Add more in future

# TODO @@@@ Verify name here, also warn user for longer names that may not fit on profile
# CheckName()


# Get the info for number of commits here
info = raw_input('Number of commits per day:\n<default: 5>: ')
if len(info):
	try:
		info = int(info)
		INFO['no_of_commits'] = info
	except Exception:
		pass

startingDate = datetime.datetime(base_date['year'], base_date['month'], base_date['day'])

for alphabet in INFO['profileName']:
	time.sleep(0.1)

	if (not alphabet.isalnum()) and (alphabet not in allowedChars):
		print 'Tha character {0} is not yet released'.format(str(alphabet))
	elif alphabet != ' ':
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

			# Write the final constructed command in GLOBALS['WRITER_FILE']
			with open(GLOBALS['WRITER_FILE'], 'a') as f:
				f.write('for i in `seq 1 ' + str(INFO['no_of_commits']) + '`;do ' +  finalCommand + '; done' + '\n')
		startingDate += datetime.timedelta(days=increment*GLOBALS['DEFAULT_DAYS_INCREMENT'])
	else:
		print ' ',
		startingDate += datetime.timedelta(days=GLOBALS['DEFAULT_DAYS_INCREMENT'])

print '\nNow go and execute the file {0} in your repository\nHave Fun :D'.format(GLOBALS['WRITER_FILE'])