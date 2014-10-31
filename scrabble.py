import string

class scrabbleSolver:
	frequencies = []
	sowpods = []
	boardwords=[]
	freqname="frequencies.txt"

	def load(self):
		self.loadSowpods()
		self.loadFrequencies()
#load dictionary
	def loadSowpods(self):
		f=open("sowpods.txt","r")
		f.readline()
		f.readline()
		self.sowpods=[line.strip() for line in f]
		f.close()
		#SORT BY LENGTH
		self.sowpods.sort(key=len)

#save the letter frequencies a-z as another file
	def saveFrequencies(self):
		if self.sowpods==[]:
			print("Please load the sowpods file using loadSowpods()")
		frequencies=[] #local variable
		for line in self.sowpods:
			code=''.join([str(line.count(i)) for i in string.ascii_lowercase])
			frequencies.append(code)
		f=open(self.freqname,"w")
		NULL=[f.writelines(line+"\n") for line in frequencies]
		f.close()

#load frequency data from file
	def loadFrequencies(self):
		try:
			f=open(self.freqname,"r")
			self.frequencies=[line.strip() for line in f] #global variable
			self.frequencies=[[int(i) for i in line] for line in self.frequencies] 
			#make strings into arrays of integers
			f.close
		except: print("file not found or unreadable. try saveFrequencies()")

	def solveForRack(self,rack,blanks=0):#number of blanks in rack
		if self.frequencies==[]:
			print("Please load the frequency file using loadFrequencies()")
			return None
		if self.sowpods==[]:
			print("Please load the sowpods file using loadSowpods()")
			return None
		solutions=[]
		rackfreq=[rack.count(i) for i in string.ascii_lowercase]
		#for each frequencies code compare the frequency of each letter with that of the rack letters
		for freq in range(len(self.frequencies)):
			free=0 #number of letters in word that are not in the rack
			for char in range(26):
				free+=max(self.frequencies[freq][char]-int(rackfreq[char]),0)
			# Add the associated word rather than its index
			# Maybe add a ranking later
			if (free<=blanks):
				solutions.append(self.sowpods[freq])#)
			
		return solutions

	def solveForLetters(self,rack):
	#slightly faster
		if self.frequencies==[]:
			print("Please load the frequency file using loadFrequencies()")
			return None
		if self.sowpods==[]:
			print("Please load the sowpods file using loadSowpods()")
			return None
		solutions=[]
		rackfreq=[rack.count(i) for i in string.ascii_lowercase]
		#for each frequencies code compare the frequency of each letter with that of the rack letters
		for freq in range(len(self.frequencies)):
			accept=True #number of letters in word that are not in the rack
			for char in range(26):
				if(self.frequencies[freq][char]>int(rackfreq[char])):
					accept=False
			# Add the associated word rather than its index
			# Maybe add a ranking later
			if (accept):
				solutions.append(self.sowpods[freq])#)
		return solutions

	def solveForWords(self,rack,words,blanks=0):#adds letters to existing words to make new words
		filteredsoln=[] #solutions after filtering out
		for word in words:
			soln=[] 
			if(blanks>0):			
				soln = self.solveForRack(rack+word,blanks)
			else:
				soln = self.solveForLetters(rack+word)
			for s in soln:
			#check if the word is actually there. it could be a permutation
				if(word in s): 
					filteredsoln.append(s)
		return filteredsoln

	def solveAcrossWords(rack,words,blanks=0):
#finds words to cross over existing words. for example a board word is horizontal and it finds a vertical using one letter in the other word.

		return 0
	def rankWords(self):
		return 0
	def addWords(self,word):
		self.boardwords.append(word)
	def clearWords(self,word):
		self.boardwords=[]

scrab=scrabbleSolver()
scrab.load()

