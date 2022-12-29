# queue implimentation using queue class

from collections import deque

queue = deque()

print(queue)

# inserting the elements in queue

queue.append('element 1')
queue.append('element 2')
queue.append('element 3')
print("The queue elements are:")
print(queue)

# deleting the elements from queue
queue.popleft()
queue.popleft()
queue.popleft()
print("The queue after removing the elements:")
print(queue)

