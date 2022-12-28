password = input("Enter the password:")

lower_case = False        
upper_case = False          
digit = False               # flag variables declarations   
valid_length = False
special_char = False

if len(password) > 8 and len(password) < 16:   # checking the length of the password 
    valid_length = True   # flag chenged to the true if condition is true

    for i in password:           #  iterating the characters in a password
        if(i.islower()):           # characters are in lower flag changed to true
            lower_case = True
        
        if(i.isupper()):          # condtion to check uppercase letters
            upper_case = True

        if(i.isdigit()):        # condition to check digits
            digit = True

        if i == '@' or i == "#" or i == "$" or i =="%" or i == "^" or i == "&" or i == "*" :
            special_char = True     # condtion for special characters

if valid_length == True and special_char == True and upper_case == True and lower_case == True and digit == True :
    print("Password is valid")          # if all flag variables are in true case than password is valid .
else:
    print("Invalid Password")   # otherwise password is invalid


