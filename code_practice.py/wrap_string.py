def wrap(s,m):
   s = s.strip()
   k = 0
   for i in range(m,len(s),m):
    print(s[ k : i])
    k = i
   return s[k : ]

if __name__ == '__main__':
    string, max_width = input("input the string:"), int(input("enter max_width:"))
result = wrap(string, max_width)
print(result)