import re
st = 'python123'
print(re.search('[^0-9]',st))   # it returns only one charcter which is not a digit

print(re.search('[^0-9][^0-9][^0-9][^0-9]',st))  # it returns 4 charecters which are not a digit 