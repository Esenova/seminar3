from linked_list import MyList, ListNode
from linked_class import Stack
from myclass import Uzbek_Plov


p1 = Uzbek_Plov('Plov 1')
p2 = Uzbek_Plov('Plov 2')
p3 = Uzbek_Plov('Plov 3')
p4 = Uzbek_Plov('Plov 4')

a_stack = Stack()

a_stack.push(Student_1)
a_stack.push(Student_2)
a_stack.push(Student_3)
a_stack.push(Student_4)

print("Size of the stack:", a_stack.length())
st = a_stack.pop()
print("POP: ", st.add_carrot())
print("Size of the stack:", a_stack.length())
st = a_stack.peek()
print("PEEK: ", st.add_carrot())
print("Size of the stack:", a_stack.length())

st = a_stack.pop()
print("POP: ", st.length())
