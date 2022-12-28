def mutate_string(string, position, character):
    list_object = list(string)
    list_object[position] = character
    string =''.join(list_object)
    return string



if __name__ == '__main__':
    s = input("enter the string:")
    i, c = input("position and element:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)







