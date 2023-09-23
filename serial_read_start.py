#******************************************************************
# Program #: Reading from serial port
#
# Programmer: Robert Klenke
#
# Due Date: NA
#
# EGRE 347, Spring 2022       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python example for reading information from serial port one byte at a time
#
# Input: command line argument of the desired serial port
#
# Output: none
#
#******************************************************************

from Sentences_function import Work

import sys


# Open the terminal for reading

Data = Work()





count = 0
if len(sys.argv) < 2:
  print("Usage: <prog_name> <pty terminal path>")
  sys.exit()

try:
  pty = open(sys.argv[1], "r")
except FileNotFoundError:
  msg = "Terminal: " + sys.argv[1] + " does not exist"
  print(msg)
  sys.exit()

print(sys.argv[1])
print("port successfully opened\n")



while True:
	byte = pty.read(1)

	#print("byte=",byte)
	Work().Parser(byte)
	


	

