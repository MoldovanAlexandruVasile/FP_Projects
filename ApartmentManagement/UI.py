def help():

    '''
    This function prints all the comands of the program
    '''
    
    print("\n \n \t All the commands:")
    print("\n add <apartment> <type> <amount>")
    print("\n remove <apartment>")
    print("\n remove <start apartment> to <end apartment>")
    print("\n remove <type>")
    print("\n replace <apartment <type> with <amount>")
    print("\n help")
    print("\n list")
    print("\n list <apartment>")
    print("\n list [</=/>] <amount>")
    print("\n sum <type>")
    print("\n max <apartment>")
    print("\n sort apartment")
    print("\n sort type")
    print("\n filter <type>")
    print("\n filter <amount>")
    print("\n undo")
    print("\n exit \n")


def prettyPrint(x,y,z):

    '''
    This function prints out the data in columns
    Input: x - apartment number
           y - type
           z - amount
    Output: x,y,z - printed each data in his column
    '''
    
    lung = len('electricity') - len(y)
    s = ''
    j = 0
    while j <= lung + 3:
        s = s + ' '
        j = j + 1
    print(repr(x).rjust(2),'   ', repr(y).rjust(3), s, end = ' ')
    print(z)
