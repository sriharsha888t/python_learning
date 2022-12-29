# stack implimentation using Lifoqueue class in queue module
from queue import LifoQueue
import sys
# defining a stack using Lifoqueue
stack = LifoQueue(maxsize=4)

# qsize() shows the number of elements in queue
print(stack.qsize())

stack.put('1st element')
stack.put('2nd element')
stack.put('3rd element')
stack.put('4th element')
print(stack.__repr__())



print("full:",stack.full())
print("size:",stack.qsize())


# get() function pops the element LIFO order
print(stack.get())
print(stack.get())

stack.put("new element")
#qsize() returns how many elements are in queue
print(stack.qsize())
# empty() returns true if queue is full otherwise false
print(stack.empty())







