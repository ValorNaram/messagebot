#!/bin/bash
from User import *

"""
Representing a message sent via the (instant) messaging/communication service. This class is not thread save

message = Message("Hello World!")
print("Message content: " + message.text)
"""
class Message():
	def __init__(self, text, vendorMessage=None):
		self.text = text
		self.mentions = []
		self.roomid = None
		self.author = None
		self.vendorMessage = vendorMessage
