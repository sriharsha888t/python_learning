def split_and_join(line):
    splitted_string = line.split()

    delimiter = '-'
    return delimiter.join(splitted_string)
    
    # write your code here

if __name__ == '__main__':
    line = input("enter the sring:")
    result = split_and_join(line)
    print(result)