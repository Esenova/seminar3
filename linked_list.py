from mylistiterator import MyListIterator


class MyList:
	def __init__(self):
		self.head = None
		self.size = 0

	def __len__(self):
		return self.size

	def __contains__(self,target):
		myNode = self.head
		while (myNode is not None) and \
		(myNode.data!=target):
			myNode = myNode.next

		return myNode is not None

	def add(self, item):
		assert item != None
		item.next = self.head
		self.head = item
		self.size += 1 
     
	def remove(self, target):
		preNode = None
		myNode = self.head
		while (myNode is not None) and (myNode.data != target):
			preNode = myNode
			myNode = myNode.next

		if myNode is not None:
			self.size -= 1 
			if myNode is self.head:
				self.head = myNode.next
			else:
				preNode.next = myNode.next

	def __iter__(self):
		return MyListIterator(self.head)
		

class ListNode:
	def __init__(self, data=None):
		self.data = data 
		self.next = None
		
	def get_data(self):
		return self.data