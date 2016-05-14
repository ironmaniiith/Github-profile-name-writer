import hashlib, os, sys, random
import collections, itertools, operator, inspect, re
import subprocess

class Helper:
	"""
		This class is for other helper functions used in main
	"""

	def __init__(self, wordsOfGod='I am the Ironman..!!'):
		self.wordsOfGod = wordsOfGod # :P :V

	def pathExists(self, a):
		"""
			Check if the path corresponding to a exists or not
			Return type: Boolean
		"""
		
		return os.path.exists(a)

	def calcMd5(self, text):
		"""
			Returns the md5 hash of the given text
			Return type: String
		"""
		
		return hashlib.md5(str(text)).hexdigest()

	def regCheck(self, text, regExp):
		"""
			Verify whether the given text matches the given regExp
			Return type: Boolean
		"""

		try:
			pattern = re.compile(regExp)
			if pattern.match(text):
				return True
		except Exception, e:
			pass
		return False

	def getFunctionName(self, obj, namespace):
		"""
			Returns the name of the function passed in the argument 'obj' declared in 'namespace'
			Return type: String

			Example:
				Suppose function is declared by the name 'func' { def func(): pass } then:  
					helper.getFunctionName(func, globals()) -> Returns 'func'
				
				namespace is the namespace in which the function is declared
		"""

		return [name for name in namespace if namespace[name] is obj]

	def getCommandOutput(self, command):
		"""
			Run the command using subprocess and returns the output
			Return type: String
		"""

		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		output = process.communicate()
		return output[0].strip()

	def typer(self, text, maxTime=None):
		"""
			Hey, this is my friend who helps me in typing, isn't the name itself self explanatory :P
		"""

		defaultTimeGap = 0.05
		if maxTime != None:
			newTime = maxTime/(len(text) * 0.1)
			if newTime < defaultTimeGap:
				defaultTimeGap = newTime
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush() # Flush it write now :P
			time.sleep(defaultTimeGap)
