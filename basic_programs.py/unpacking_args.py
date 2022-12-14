# unpacking the list normal call
print(list(range(3,6)))


# call with arguments unpacked from the list
args = [3,10]
print(list(range(*args)))


v = [0,21]
print(list(range(*v)))

