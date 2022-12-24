#######################################################################################################
### QUEUE IMPLEMENTATION
#######################################################################################################
class Queue:  
	#Constructor initialize the Queue List
	def __init__(self):
		self.index = 0 
		self.queue = list()  
		
	#Insert object at the rear of the queue, where the rear is identified by the index
	def enqueue(self,val):      
		self.queue.insert(self.index,val)
		self.index = self.index+1
        
	#Remove and return the first object in the queue; Returns Error Message if the queue is empty
	def dequeue(self):
		try:
			val = self.queue[0]
			self.queue.pop(0)
			self.index = self.index-1
			return val
		except Exception:
			print("Queue is Empty")
			
	#Returns the front most element in the Queue, but will not remove like dequeue Operation
	def front(self):
		try:
			val = self.queue[0]
			return val
		except Exception:
			print("Queue is Empty")
			
	#Returns the current size of the Queue
	def size(self):
		return self.index

	#Prints the Queue Length and the Queue Elements
	def printQueue(self):
		print(q.index)
		print(q.queue)

#######################################################################################################
### BITS TOWER CLASS
#######################################################################################################
class BITSTower:
	
	#Constructor to initialize days and discs for the BITS Tower
	def __init__(self):
		self.days = 0
		self.discs = []

	# Input File Validation and read the number of days and disc values to the BITSTower Object
	#  
	# Validate whether the given input file is valid. Following validations are done on the input file
	# 1. InputFile with name inputPS07.txt present in the source folder where the .py file is present
	# 2. InputFile "inputPS07.txt" contains only 2 Lines as expected without any leading / trailing spaces or empty returns
	# 3. Input Data Validation:
	#		a. Input File contains only input numbers and not characters
	#		b. The number of values in the Line#2 is exactly equal to the input on Line#1 
	# 		c. In the Input File, the Line#2 has only distinct values. Duplicate values considered as invalid input
	def validateInputFile(self):
		#Try and open inputPS07.txt input file. If the file is not present in the same path as this file, we get an exception and 
		#code execution will be stopped.
		try:
			with open("inputPS07.txt", "r") as inputfile:
				lines = [line.rstrip('\n') for line in inputfile]
			fileLength = len(lines)
			#Check there are only 2 lines in the input file
			if(fileLength!=2):
				return False			
			else:
				#Check the line 1 contains only numbers and no alphabets / special characters
				if(lines[0].isdigit()):
					numberOfDays = lines[0]
					self.days = numberOfDays
				else:
					raise Exception("Invalid Input Format")
				discs = lines[1].split()
				#Check all the entries in line 2 are valid numbers
				if not all(disc.isdigit() for disc in discs):
					raise Exception("Invalid Input Format")
				self.discs = discs
				#Check the numbers of discs is equal to the number of days
				if(int(numberOfDays)!=len(discs)):
					raise Exception("Invalid Input Format")
			inputfile.close()
			return True
		except FileNotFoundError:
			print("Input File not found in the source folder")
			return False
		except Exception:
			print("Input File is not in the expected format \n Expected Format: Total of two lines with  \nLine #1 Mentioning Number of days (n) \nLine #2 Having distinct n entries where n is the input given in line #1")
			return False

#Main Program Execution starts Here
tower = BITSTower()
if(tower.validateInputFile()):
	print ("Valid Input File")
	print(tower.days)
	print(tower.discs)