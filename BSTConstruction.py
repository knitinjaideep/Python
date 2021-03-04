class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	#Average: O(logn) time | O(logn) space
	#Worst: O(n) | O(n)

	def insert(self,newValue):
		if newValue < self.value:
			if self.left is not None:
				self.left.insert(newValue)
			else:
				self.left = BST(value)
		else:
			if self.right is not None:
				self.right.insert(newValue)
			else:
				self.right = BST(value)
		return self
	