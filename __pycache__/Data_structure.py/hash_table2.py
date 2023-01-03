def hash_function(text):
    return sum(ord(character) for character in text)

print(hash_function('harsha'))

print(ord('a'))

print(repr(3.14))

def hash_function1(key):
    return sum(ord(character)for character in repr(key))

print(hash_function1('3.14'))