#!/bin/bash

"""
Representing a room in the (instant) messaging/communication service. This class is not thread save
"""
class Room():
	def __init__(self, roomid, roomtype, vendorRoom=None):
		self.roomid = roomid
		self.roomtype = roomtype
		self.vendorRoom = vendorRoom
		self.name = None
		self.description = None
