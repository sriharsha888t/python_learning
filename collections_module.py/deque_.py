from collections import deque

queue = deque(['name','age','dob'])

print(queue)

# defining the deque 
q = deque([2,3,4,5])

print(q)

# appending the value into right side of the deque
q.append(10)

print(q)


# appending the value into left side of the deque
q.appendleft(12)

print(q)


# pop() removes the element from the right side of the deque
q.pop()
print(q)

# popleft() removes the element from the left side of the deque
q.popleft()
print(q)


# accessing the deque elements

q1 = deque([9,8,7,6,4,8,3,4,9])
# finding the element using index
print(q1.index(4,5,8))  # (element,i-start,i-index) 

# inserting the value into specific index position

q1.insert(1,10)

print(q1)
# count(element) returns the occurence of the element
print(q1.count(4))

# remove() method removes the specific element from the deque

q1.remove(4)

print(q1)


# extending the deque with iterable

q2 = deque([20,30,40,50])

l = [9,8,7,6]
# extending the values at right side of the deque
q2.extend(l)
print(q2)

l2 = [11,22,33,44]
# extending the values at left side of the deque
q2.extendleft(l2)
print(q2)

# rotate(number specified)  used to rotate the deque
#q2.rotate(4)
print(q2)


q2.reverse()
print(q2)