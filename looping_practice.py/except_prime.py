import math                  # importing math module
def is_not_prime(n):         # function definition
   flag = False              # flag variable
   for i in range(2, int(math.sqrt(n)) + 1):  # range from 2 to 
        if n % i == 0:
            flag = True
        return flag

range_starts = 10
range_ends = 30
print("Non-prime numbers between",range_starts,"and", range_ends,"are:")
 
for number in filter(is_not_prime, range(range_starts, range_ends)):
    print(number)

