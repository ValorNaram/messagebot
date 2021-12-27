from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

"""
Message sent to a group this bot is in
"""
def groupMessage(client, message):
	pass

"""
Message sent privately to bot
"""
def privateMessage(client, message):
	pass

"""
A previously sent message got updated. This applies both messages sent to groups and private
"""
def messageUpdated(client, message):
	pass

def userJoins(client, info):
	pass

def userLeaves(client, info):
	pass

def fileTransfer(client, transfer):
	pass

def sticker(client, sticker):
	pass

def systemMessage(client, message):
	pass

def serverError(client, error):
	pass

def unimplementedEvent(client, ev):
	pass
