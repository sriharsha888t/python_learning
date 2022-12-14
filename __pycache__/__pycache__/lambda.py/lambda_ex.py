# using lambda function 
x=lambda a : a * a
print(x(20))

# using normal function
def new(a):
    return a*a
new(20)

# lambda using in user_defined function
def A(x):
    return(lambda y : x + y)
B=A(10)
print(type(B))
print(B(10))
C = A(1)
print(C(2))

# lambda for Algebra
# linear equations
s = lambda a :a*a
print(s(10))

d=lambda x,y:3*x+4*y
print(d(2,3))

# quadratic equation
# (a+b)^2
x=lambda a,b:(a+b)**2
y=x(2,2)
print(y)