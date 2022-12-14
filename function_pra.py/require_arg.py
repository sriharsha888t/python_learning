#  function with required argument arguments
def function(a,b):
    print("a value is:",a)
    print("b value is:",b)

# passing outof order elements
function(10,20)

# passing only one argument

try:
    function(100)
except:
    print("function needs two arguments")
