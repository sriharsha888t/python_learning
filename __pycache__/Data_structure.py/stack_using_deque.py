# stack implimentation using deque
  

# importing the deque class from the collections module
from collections import deque


# creating the stack
stack = deque()

print("The stack before inserting the values:")
print(stack)


# inserting the values
                                                # |              |
stack.append('1st value')                       # |  3rd value   |
stack.append('2nd value')                       # | 2nd value    |
stack.append('3rd value')                       # |  1st value   |
print("The stack after inserting the values:")  #  --------------
print(stack)

print("Deleting the elements from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())







