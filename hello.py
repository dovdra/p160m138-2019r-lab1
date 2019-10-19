#!/usr/bin/env python 

import sys

def greet(greeted_name):
	print "Hello, ",greeted_name,"!"
	return;

greet(str(sys.argv[1]))
