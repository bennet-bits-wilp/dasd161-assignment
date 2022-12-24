#######################################################################################################
# QUEUE IMPLEMENTATION
#######################################################################################################
class Queue:
    # Constructor initialize the Queue List
    def __init__(self):
        self.index = 0
        self.queue = list()

    # Insert object at the rear of the queue, where the rear is identified by the index
    def enqueue(self, val):
        self.queue.insert(self.index, val)
        self.index = self.index + 1

    # Remove and return the first object in the queue; Returns Error Message if the queue is empty
    def dequeue(self):
        try:
            val = int(self.queue[0])
            self.queue.pop(0)
            self.index = self.index - 1
            return val
        except Exception:
            print("Queue is Empty")

    # Returns the front most element in the Queue, but will not remove like dequeue Operation
    def front(self):
        try:
            val = self.queue[0]
            return val
        except Exception:
            print("Queue is Empty")

    # Returns the current size of the Queue
    def size(self):
        return self.index

    # Prints the Queue Length and the Queue Elements
    def print_queue(self):
        print(self.index)
        print(self.queue)

    def is_empty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True


# Functions
# This method clears the contents of the output file before processing a valid input file.
# If the input file is invalid, the previous output file will not be cleared.
def clear_old_output_files():
    output_file = open("outputPS07.txt", 'w')
    output_file.close()


# This method writes the output to the output file "outputPS07.txt"
def output_data(data, new_line=0):
    f = open("outputPS07.txt", "a")
    f.write(" " + str(data))
    if new_line == 1:
        f.write("\r")
        f.close()


#######################################################################################################
# BITS TOWER CLASS
#######################################################################################################


class BITSTower:
    # Constructor to initialize days and discs for the BITS Tower
    def __init__(self):
        self.days = 0
        self.discs = []
        self.maxDiscSize = 0

    # Input File Validation and read the number of days and disc values to the BITSTower Object
    #
    # Validate whether the given input file is valid. Following validations are done on the input file
    # 1. InputFile with name inputPS07.txt present in the source folder where the .py file is present
    # 2. InputFile "inputPS07.txt" contains only 2 Lines without any leading / trailing spaces or empty returns
    # 3. Input Data Validation:
    #   a. Input File contains only input numbers and not characters
    #   b. The number of values in the Line#2 is exactly equal to the input on Line#1
    #   c. In the Input File, the Line#2 has only distinct values. Duplicate values considered as invalid input
    #   d. The Max disc size should not be greater than the N value given in Line#1
    def validate_input_file(self):
        # Try and open inputPS07.txt input file. If the file is not present in the same path as this file,
        # we get an exception and code execution will be stopped.
        try:
            with open("inputPS07.txt", "r") as input_file:
                lines = [line.rstrip('\n') for line in input_file]
            file_length = len(lines)
            # Check there are only 2 lines in the input file
            if file_length != 2:
                return False
            else:
                # Check the line 1 contains only numbers and no alphabets / special characters
                if lines[0].isdigit():
                    number_of_days = lines[0]
                    self.days = number_of_days
                else:
                    raise Exception("Invalid Input Format")
                discs = lines[1].split()
                # Check all the entries in line 2 are valid numbers
                if not all(disc.isdigit() for disc in discs):
                    print("Only numbers are allowed in the input")
                    raise Exception("Invalid Input Format")
                self.discs = discs
                # Check the numbers of discs is equal to the number of days
                if int(number_of_days) != len(discs):
                    print("Number of days does not match the number of discs")
                    raise Exception("Invalid Input Format")
                # Check for duplicates in the discs size
                disc_set = set(discs)
                if len(discs) != len(disc_set):
                    print("Disc sizes are not distinct. There are duplicates!")
                    raise Exception("Invalid Input Format")
                # check if the max disc size is greater than given input N
                max_val = max([eval(i) for i in discs])
                if max_val > int(self.days):
                    print("Max disc size is greater than N")
                    raise Exception("Invalid Input Format")
            return True
        except FileNotFoundError:
            print("Input file inputPS07.txt not found in the source folder")
            return False
        except Exception:
            return False
        finally:
            input_file.close()

    # This method is where the core processing is carried out as per the tower construction Logic
    def process_discs(self):
        # Input Queue to Read the input discs one per day
        input_queue = Queue()
        # Buffer Queue to accommodate the queues that are not placed to output based on the construction Logic
        buffer_queue = Queue()

        # Insert the values into a Queue Data Structure from the Input file - InputQueue
        i = 0
        while i < int(self.days):
            val = int(self.discs[i])
            self.maxDiscSize = max(val, self.maxDiscSize)
            input_queue.enqueue(val)
            i = i + 1

        # Arranging the Discs one day at a time
        day = 0
        while not (input_queue.is_empty()):
            queue_val = int(input_queue.dequeue())
            day += 1
            # When the incoming disc size is the expected Disc size, write the disc to the output file and process
            # if the buffer queue is not empty in desired format "dayNumber > discSize" - Eg. "1 > 5"
            if self.maxDiscSize == queue_val:
                output_data(str(day) + ' > ' + str(queue_val))
                self.maxDiscSize -= 1
                self.process_buffer_data(buffer_queue)
                output_data('', 1)
            # If the incoming disc size is not the expected disc size, enqueue the disc to bufferQueue for
            # further processing the next day
            else:
                output_data(str(day) + ' >', 1)
                buffer_queue.enqueue(queue_val)
        # inputQueue.printQueue()
        # bufferQueue.printQueue()

    # This method processes the buffer queue
    def process_buffer_data(self, buffer_queue):
        i = 0
        while not (buffer_queue.is_empty()):
            queue_val = int(buffer_queue.dequeue())
            # process the buffer queue and push to output if the popped value is equal to expected disc
            if self.maxDiscSize == queue_val:
                output_data(queue_val)
                self.maxDiscSize -= 1
                i = 0
            # if not enqueue the value back to the buffer queue
            else:
                buffer_queue.enqueue(queue_val)
                i += 1
            # Break the loop once all the elements of the buffer queue are processed only once.
            if i > buffer_queue.size() + 1:
                break


# Main Program Execution starts Here
tower = BITSTower()
if tower.validate_input_file():
    clear_old_output_files()
    tower.process_discs()
else:
    print("Input File is not in the expected format. Program Terminating.... \n"
          "Expected Format:\n"
          "Total of two lines with\n"
          "\tLine #1 Mentioning Number of days (n) \n"
          "\tLine #2 Having distinct n entries where n is the input given in line #1")
    quit()
