# queue implimentation using list

# defining queue
queue = []

# inserting the elements in queue
print(queue)              #              values    deque <<<<---   1   2    3  <<<----- enque                   
queue.append(1)           #                    
queue.append(2)           #               index                    0   1    2           
queue.append(3)           #                                         
print("Elements are Enqueue to queue:")
print(queue)


print("dequeue elements are:")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))


print("The queue after removing elements:")
print(queue)

