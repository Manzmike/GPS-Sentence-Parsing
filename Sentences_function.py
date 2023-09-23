#******************************************************************
# Program #8: Reading from serial port
#
# Programmer: Michael Lindsay
#
# Due Date: 05/25/2022
#
# EGRE 347, Spring 2022       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python example for reading information from serial port one byte at a time
#
# Input: command line argument of the desired serial port
#
# Output: Message Type,Message Data, Checksum
#
#******************************************************************


from enum import Enum
import sys

State = 1
GPS_tuple = []
CheckSum = ""
Type = ""
Real_CheckSum = 0
Temp = 0

	
class Work:
	def __init__(self):
		#self.__state = States(1)
		super().__init__
		self.GPS_tuple = []
		self.State = 0

	def Parser(self,byte):

		""" 
		Summary:
		Through this code my code essentially reads the data one bit at a time
		Through my code it is always checking for the dollar sign state from 
		there it checks the actual type of the function going bit by bit wheile saving 
		the in to the global. Following It checks/saves the data for * and doing the check sum
		FOllowing it only prints the data,type,and checksum if it is equal to the check sum


		Parameters:
		It is only passed the byte through the function as well as the self parameter
		btye(string/char): byte is the single byte each time 

		Returns:
		Nothing
		The fucntion will print but does not return a value

		
		"""


		global State
		global CheckSum
		global GPS_tuple
		global Type
		global Real_CheckSum
		global Temp


		
		if(State == 1) or (byte == "$"):
			GPS_tuple.clear()
			Type=""
			Real_CheckSum=0
			State =2;



		#State 1
		elif(State == 2):
			if(byte == "G"):
				State = 3
				Type=byte


				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]

				GPS_tuple.append(byte)
			elif(byte != "G"):
				State = 1


		#State 2
		elif(State == 3):
			if(byte == "P"):
				State = 4
				Type+=byte


				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]

				GPS_tuple.append(byte)

			elif(byte != "P"):
				State = 1


		#State 3
		elif(State == 4):

			if(byte == "G") or (byte == "R"):
				State += 1
				Type+=byte


				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]

				GPS_tuple.append(byte)

			else:
				State = 1

				


		#State 4
		elif(State == 5):
			if((byte == "G") or (byte == "S") or (byte == "M")):
				State += 1
				Type+=byte

				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]

				GPS_tuple.append(byte)
			else:
				State = 1




		elif(State == 6):
			if((byte == "A") or (byte == "V") or (byte == "C")):

				
				Type+=byte

				if (Type == "GPGGA") or (Type == "GPGSA") or (Type == "GPGSV") or (Type == "GPRMC"):
					State += 1
				else:
					State = 1
				


				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]

				GPS_tuple.append(byte)


			
			else:
				State = 1


		elif(State == 7):


			if(byte == "*"):
				State += 1


			else:
				
				GPS_tuple.append(byte)
				Real_CheckSum^=ord(byte)
				Temp = hex(Real_CheckSum) 
				Temp= Temp[2:]


		elif(State == 8):
			CheckSum=byte

			State+=1

		elif(State == 9):
			CheckSum+=byte


			if CheckSum == Temp.upper():
				print("Message type:%s"%Type)
				print("Message data:",end="")
				for item in GPS_tuple:
					print(str(item[0]),end = "")
				print("\nMessage checksum:%s\n"%Temp.upper())
		else:
			State = 1



