#!/usr/bin/env python 

import sys

def greet(name):
	print "Hello, ",name,"!"
	return;

greet(str(sys.argv[1]))
