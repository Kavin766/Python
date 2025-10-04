class First:
	name = "Hello"		# class variable
	
	def addnum(self):
		self.a=34		#object variable
		self.b=56
		self.c=a+b
		print(" Result :" , self.c)

	def display(self):
		print(" Res " , self.c)

obj = First()
obj.addnum()
obj.display()
