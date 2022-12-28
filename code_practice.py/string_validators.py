if __name__ == '__main__':
    s = input("Enter string:")
    print(any(map(str.isalnum,s)))  
    print(any(map(str.isalpha,s)))   
    print(any(map(str.isdigit,s)))   
    print(any(map(str.islower,s)))
    print(any(map(str.isupper,s)))

 # any() returns true if any element of iterable is true.
 # map() is applying the given function to each element of the iterable.
 # str() converts specified value into string.