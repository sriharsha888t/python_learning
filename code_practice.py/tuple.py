if __name__ == '__main__':
    n = int(input())
    lst = map(int,input().split())
    lst = tuple(lst)
    print(hash(lst))



