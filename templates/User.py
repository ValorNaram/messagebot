#!/bin/python

"""
Representing a user of the (instant) messaging/communication service. This class is not thread save

user = User(mybot, 1234)
print("User ID:      " + str(user.id))
"""
class User():
	def __init__(self, instance, userid):
		self.userid = userid
		self.userlevel = -1
		self.username = None
		self.displayname = None
		self.instance = instance # shared data space of a running instance of the open source bot
	
	"""
	Save the user data to the database or update it
	"""
	def commit(self, cursor):
		pass
	
	"""
	Static method to do a check to verify if all necessary data are available for this class to work properly
	"""
	@staticmethod
	def check(cls, instance):
		pass
