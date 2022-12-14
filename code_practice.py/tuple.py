if __name__ == '__main__':
    n = int(input('enter how many elments:'))
    lst = map(int,input('enter elements:').split())
    t = tuple(lst)
    print(hash(t))



