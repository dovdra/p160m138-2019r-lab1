#!/usr/bin/env python 

import sys

def greet(name):
	shout_count = 1
	if int(sys.argv[2]) != 1:
		shout_count = int(sys.argv[2])	

	sys.stdout.write("Hello, ")
	sys.stdout.write(name )

	for i in range(shout_count):
		sys.stdout.write("!")
	print ""
	return;

greet(str(sys.argv[1]))
