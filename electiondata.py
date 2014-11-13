import csv

class ElectionResults:
  
	def __init__(self, filename):
		self.filename = filename

	def load(self):
		self.file = open(self.filename, 'r')
		self.all_lines = self.file.readlines()

	def states(self):
		all_names = []
		for line in self.all_lines:
			columns = line.split(',')
			all_names.append(columns[1])
		return all_names[1:]

	def state_count(self):
		return len(self.states())
	
	def obamaVotes(self):
		total = 0
		for line in self.all_lines:
			columns = line.split(',')
			if columns[3] != "Obama vote":
				total += int(columns[3])
		return total

	def romneyVotes(self):
		total = 0
		for line in self.all_lines:
			columns = line.split(',')
			if columns[5] != "Romney vote":
				total += int(columns[5])
		return total
		
					
	def compare_bystate(self):
		obamaStates = []
		romneyStates = []
		for line in self.all_lines:

			columns = line.split(',')

			if columns[3] != "Obama vote":
				obama = int(columns[3])
				romney = int(columns[5])
				if obama > romney:
					obamaStates.append(columns[1])
				else:
					romneyStates.append(columns[1])
		print "Obama has more votes in "+str(len(obamaStates))+" states:", obamaStates
		print "Romney has more votes in "+str(len(romneyStates))+" states:", romneyStates