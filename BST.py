class Tree:
  
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
    
	def printtree(self):
		print(self.data)
		if self.left:
			print("left",end=" ")
			self.left.printtree()
		if self.right:
			print("right",end=" ")
			self.right.printtree()
      
	def insert(self, data):
		if self.data:
			if data <=self.data:
				if self.left is None:
					self.left = Tree(data)
				else:
					self.left.insert(data)
			else:
				if self.right is None:
					self.right = Tree(data)
				else:
					self.right.insert(data)


n=int(input("No. of Elements: "))
print("Enter Elements")
root=Tree(int(input()))
for ii in range(n-1):
	root.insert(int(input()))
root.printtree()
