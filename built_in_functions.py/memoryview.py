# a random byte array
randomByteArray = bytearray('ABC','utf-8')
mv = memoryview(randomByteArray)
# access the memory view at zero index
print(mv[0:3])  

# it can create byte from memory view
print(bytes(mv[0:3]))

# it can list from memory view
print(list(mv[0:3]))
