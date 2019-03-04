from linked_list import MyList, ListNode

class Stack:
	def __init__(self):
		self.my_stack = MyList()
        
    def empty(self):
		if self.length() == 0:
			return True
		return False
		
	def length(self):
		return self.my_stack.__len__()
    
    def peek(self):
		if self.empty():
            print("Stack is empty")
		    return None
        else:
			return self.my_stack.head.get_data()
		
	def pop(self):
		if self.empty():
			print("Stack is empty")
            return None
        else:
            obj_data = self.my_stack.head.get_data()
			self.my_stack.remove(self.my_stack.head.get_data())
			return obj_data
			
		
	def push(self, obj):
		obj =  ListNode(obj)
		self.my_stack.add(obj)
