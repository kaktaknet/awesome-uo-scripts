from __future__ import division
import os, sys, os.path, string

import time

def touch(file):
	os.utime(file,None)
	
def main():
	touchall("scripts")
	
def touchall(folder):
	os.chdir(folder)
	files=os.listdir(".")
	for file in files:
		if file[-3:]=='.py':
			touch(file)
		elif os.path.isdir(file):
			touchall(file)
	os.chdir("..")
			
if __name__ == '__main__': main()