#!/bin/bash

NAME = "<command name>" # the name of the command (human readable)
DESCRIPTION = "<command description>" # the description of that the command exactly does
VERSION = "1.0"
plugins = [] # a list of plugins this command requires to be installed on the message bot
aliases = [] # a list of command aliases which trigger the execution of this code. E.g. for a ban command use aliases like ["fban", "fblock", "fdisallow"] to allow the user to send "fban", "fblock" or "fdisallow" to trigger the same action "banning a specified user"


def command(command, issuer)
	pass
