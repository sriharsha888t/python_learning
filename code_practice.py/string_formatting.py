#print(bin(2))
#print(hex(2))
#print(oct(2))
    

def print_format(n):
    for i in range(1,n+1):
        binlen = len(str(bin(n)))
        octf = oct(i).split('o')
        hexf = hex(i).split('x')
        binf = bin(i).split('b')
        print(i , octf[1] , hexf[1].upper(),binf[1])


if __name__ == '__main__':
    n = int(input("Enter the range of decimal numbers:"))
    print_format(n)

