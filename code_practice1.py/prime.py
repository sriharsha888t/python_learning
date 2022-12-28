from math import sqrt
n = 71

prime_flag = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
       if (n % i == 0):
        prime_flag = 1
        break

    if (prime_flag == 0):
        print("Is a prime number.")

    else:
      print("Not a prime number.")
else:
    print("Not a prime number.")
