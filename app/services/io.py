class log:
	file = 0
	def __init__(self, filename):
		self.file = open(filename,'w')
	def bWrite(self,text):
		if self.file != 0 and type(text) is str:
			self.file.write(text)
		else:
			self.file.write(str(text))
			
