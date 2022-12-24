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
			val = int(self.queue[0])
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
		print(self.index)
		print(self.queue)
		
	def isEmpty(self):
		#print(len(self.queue))
		if(len(self.queue)>0):
			return False
		else:
			return True

#######################################################################################################
### BITS TOWER CLASS
#######################################################################################################
class BITSTower:
	
	#Constructor to initialize days and discs for the BITS Tower
	def __init__(self):
		self.days = 0
		self.discs = []
		self.maxDiscSize = 0

	# Input File Validation and read the number of days and disc values to the BITSTower Object
	#  
	# Validate whether the given input file is valid. Following validations are done on the input file
	# 1. InputFile with name inputPS07.txt present in the source folder where the .py file is present
	# 2. InputFile "inputPS07.txt" contains only 2 Lines as expected without any leading / trailing spaces or empty returns
	# 3. Input Data Validation:
	#		a. Input File contains only input numbers and not characters
	#		b. The number of values in the Line#2 is exactly equal to the input on Line#1 
	# 		c. In the Input File, the Line#2 has only distinct values. Duplicate values considered as invalid input
	#		d. The Max disc size should not be greater than the N value given in Line#1
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
				#Check for duplicates in the discs size
				discSet = set(discs)
				if(len(discs)!= len(discSet)):
					raise Exception("Invalid Input Format")
				#check if the max disc size is greater than given input N
				maxVal = max(discs)
				if(max(discs) > self.days):
					raise Exception("Invalid Input Format")
			inputfile.close()
			return True
		except FileNotFoundError:
			print("Input File not found in the source folder")
			return False
		except Exception:
			return False
	
	#This method clears the contents of the output file before processing a valid input file.
	#If the input file is invalid, the previous output file will not be cleared.
	def clearOldOutputFiles(self):
		outputFile = open("outputPS07.txt",'w')
		outputFile.close()
			
	#This method writes the output to the output file "outputPS07.txt"
	def outputData(self, data, newLine = 0):
		#print("OUTPUT")
		#print(data)
		f = open("outputPS07.txt", "a")
		f.write(" ")
		f.write(str(data))
		if newLine == 1:
			f.write("\r")
		f.close()

	#This method is where the core processing is carried out as per the tower construction Logic
	def processDiscs(self):
		inputQueue = Queue() #Input Queue to Read the input discs one per day
		bufferQueue = Queue() #Buffer Queue to accomodate the queues that are not placed to output based on the construction Logic
		
		#Insert the values into a Queue Data Structure from the Input file - InputQueue
		i=0
		while(i<int(self.days)):
			val = int(self.discs[i])
			self.maxDiscSize = max(val, self.maxDiscSize)
			inputQueue.enqueue(val)
			i = i+1
			
		#Arranging the Discs one day at a time
		day = 0
		while not (inputQueue.isEmpty()): 
			queueVal = int(inputQueue.dequeue())
			#print("QUEUE VAL")
			#print(queueVal)
			day += 1
			#When the incoming disc size is the expected Disc size, write the disc to the output file and process if the buffer queue is not empty
			#in desired format "dayNumber > discSize" - Eg. "1 > 5"
			if(self.maxDiscSize==queueVal):	
				tower.outputData (day)
				tower.outputData ('>')
				tower.outputData(queueVal)
				self.maxDiscSize -= 1
				tower.processBufferData(bufferQueue)
				tower.outputData ('',1)
			#If the incoming disc size is not the expected disc size, enqueue the disc to bufferQueue for further processing the next day
			else:
				tower.outputData (day)
				tower.outputData ('>',1)
				bufferQueue.enqueue(queueVal)
		
		#inputQueue.printQueue()
		#bufferQueue.printQueue()
		
	#This method processes the buffer queue
	def processBufferData(self, bufferQueue):
		i=0
		while not(bufferQueue.isEmpty()):
			queueVal = int(bufferQueue.dequeue())
			#print("BufferQueueVal")
			#print(queueVal)
			#process the buffer queue and push to outuput if the popped value is equal to expected disc 
			if(self.maxDiscSize==queueVal):
				tower.outputData(queueVal)
				self.maxDiscSize -= 1
			#if not enqueue the value back to the buffer queue
			else:
				bufferQueue.enqueue(queueVal)
			i += 1
			#Break the loop once all the elements of the buffer queue are processed only once.
			if(i>bufferQueue.size()+1):
				break;
		#print("bufferSize")
		#print(bufferQueue.printQueue())

#Main Program Execution starts Here
tower = BITSTower()
if(tower.validateInputFile()):
	tower.clearOldOutputFiles()
	tower.processDiscs()
	#print ("Valid Input File")
	#print(tower.days)
	#print(tower.discs)
else:
	print("Input File is not in the expected format. Program Terminating.... \nExpected Format:\nTotal of two lines with  \n\tLine #1 Mentioning Number of days (n) \n\tLine #2 Having distinct n entries where n is the input given in line #1")
	quit()