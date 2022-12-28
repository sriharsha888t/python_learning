def is_palindrome(s):
    if  s == s[::-1]:
        print("palindrome.")
    else:
        print("Not a palindrome.")
    

string = input("Input the string to check palindrome or not:")

is_palindrome(string)


