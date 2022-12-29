from queue import Queue

# defining the queue

q = Queue(maxsize=10)

# inserting the elements to the queue

q.put("1st element")
q.put("2nd element")
q.put("3rd element")
print(q.qsize())
print(q.full())

print("The q elements are:")
print(q)

# deleting elements from the queue

q.get()
q.get()
q.get()
print(q.qsize())
print(q.empty())
print(q)