#from textwrap import wrap
#import textwrap

#def wrap(string, max_width):
 
 #   return textwrap.fill(string,max_width)
   



#print(dir(textwrap))

#def wrap(string, max_width):
 #     d = textwrap.wrap(string,max_width)
  #    return d
        
 

#if __name__ == '__main__':
 #   string, max_width = input("Enter the string:"), int(input("Enter the width:"))
  #  result = wrap(string, max_width)
   # print(result)





    
    
def wrap(s,m):
  s = s.strip()
  k = 0
  for i in range(m,len(s),m):
    print(s[k : i])
    k = i
    return s[k : ]

if __name__ == '__main__':
   string, max_width = input("input the string:"), int(input("width for string:"))
   result = wrap(string, max_width)
   print(result)