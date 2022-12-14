def rev_word(word):
    return word[ : : -1]
    

print(rev_word('harsha'))

words = ['apple','banana','mango','pinapple']
print(sorted(words,key=rev_word))