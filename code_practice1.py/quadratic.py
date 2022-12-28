

# quadratic equation standard form ax**2 + bx + c == 0

a = 2
b = 3
c = 5

# quadratic formula

#-b + or - square(4*a*c)

#print(u"\u00B1") for plus or minus symbol

import cmath

q = (b ** 2) - (4 * a * c)

s1 = (-b-cmath.sqrt(q))/2 * a
s2 = (-b+cmath.sqrt(q))/2 * a
print(s1,s2)