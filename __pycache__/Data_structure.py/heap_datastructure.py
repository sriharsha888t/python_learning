import heapq

l = [1,2,4,8,10,12]

heapq.heapify(l)

print("created heap is:",l)
# heappush() used to insert the value to the heap
print("modified heap after push is:",end=' ')
heapq.heappush(l,30)
print(l)


#heapq.heappush(l,32)
#print(l)



# heappop(heap) is used to remove smallest element
print("after pop operation:",end=" ")
print(heapq.heappop(l))


# heappushpop(heap,ele) used to perform the delete and insert operations
l2 = [90,80,70,60]

heapq.heapify(l2)
print("After pop item using heappushpop:",end=' ')
print(heapq.heappushpop(l2,90))


# heapreplace(heap,ele) used to replace the element
print("After replacing the element using heapreplace:",end=' ')
print(heapq.heapreplace(l2,60))


# finding largest and smallest elements from the list
l3 = [3,12,4,12,15,56,78,12]

heapq.heapify(l3)
print("The 3 largest elements from the l3 is:")
print(heapq.nlargest(3,l3))

print("The 2 smallest elements from the l3 is: ")
print(heapq.nsmallest(2,l3))




