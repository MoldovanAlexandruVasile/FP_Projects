import UI

def initList():

    '''
    This function it's initializing the list
    '''

    global apartmentList
    global typeList
    global amountList
    
    apartmentList = [15, 15, 10, 1, 2, 15, 20, 7, 18, 25, 30, 15]
    typeList = ['Gas', 'Heating', 'Electricity', 'Heating', 'Gas', 'Heating', 'Electricity', 'Water' ,'Gas', 'Water', 'Electricity', 'Other']
    amountList = [87, 156, 250, 102, 523, 59, 40, 405, 100, 231, 412, 97]

    global undoApartmentList
    global undoTypeList
    global undoAmountList

    undoApartmentList = []
    undoTypeList = []
    undoAmountList = []


def showList(y,x):

    '''
    This functions shows the wanted elements from the list
    Input: y - sgn
           x - the amount
    Output: A list
    '''

    if y != '':
        if validPositiveNumber(x) == True:
            print('\n')
            k = 0
            if y == '>':
                for i in range(len(amountList)):
                    if amountList[i] > x:
                        k = k + 1
                        UI.prettyPrint(apartmentList[i],typeList[i],amountList[i])   
            elif y == '<':
                for i in range(len(amountList)):
                    if amountList[i] < x:
                        k = k + 1
                        UI.prettyPrint(apartmentList[i],typeList[i],amountList[i]) 
            elif y == '=':
                for i in range(len(amountList)):
                    if amountList[i] == x:
                        k = k + 1
                        UI.prettyPrint(apartmentList[i],typeList[i],amountList[i]) 
            if k == 0: print('\n Invalid data !')
        else: print('\n Invalid data !')
    elif y == '':
        print('\n')
        if x == 0:
            for i in range(len(apartmentList)):
                UI.prettyPrint(apartmentList[i],typeList[i],amountList[i]) 
        elif existNumber(x, apartmentList) == True:
            for i in range(len(apartmentList)):
                if apartmentList[i] == x:
                    UI.prettyPrint(apartmentList[i],typeList[i],amountList[i])

                    
def existNumber(x, lista):
    
    '''
    This function tests if an item is already in the list or not
    Input: x - The element which existence it's tested
           lista - The list in which we'll test the existence of
                   x element
    Output: False if the item doesn't exist
            True if the item it's already in the list
    '''

    if validPositiveNumber(x) == True:
        x = int(x)
        sem = False
        i = 0
        while i < len(lista) and sem == False:
            if lista[i] == x: sem = True
            else: i = i + 1
        return sem


def existCategory(x, lista):

    '''
    This function tests if an item is already in the list or not
    Input: x - The element which existence it's tested
           lista - The list in which we'll test the existence of
                   x element
    Output: False if the item doesn't exist
            True if the item it's already in the list
    '''
        
    x = x.capitalize()
    if validCategory(x) == True:
        sem = False
        i = 0
        while i < len(lista) and sem == False:
            if lista[i] == x: sem = True
            else: i = i + 1
        return sem


def validCategory(x):

    '''
    This function verify if the introduced category is a valid one
    Input: x - the introduced data, which will be verifyed
    Output: True - If it's a valid category
            False - If it's an invalid category
    '''
    
    x = str(x)
    if x == 'water' or x == 'Water' or x == 'Heating' or x == 'heating' or x == 'electricity' or x == 'Electricity' or x == 'Gas' or x == 'gas' or x == 'Other' or x == 'other':
        return True
    else: return False

    
def validPositiveNumber(x):

    '''
    This function verify if the introduced number it's a positive one
    Input: x - The number
    Output: True - If the number it's positive
            False - otherwise
    '''
    
    try:
        x = int(x)
        if x > 0: return True
        else: return False
    except ValueError: return False


def addItem(ap, ty, am):
    
    '''
    This function adds a new item to the list
    Input: ap - the apartment number
           ty - the type
           am - the amount
    Output: --
    '''

    if validPositiveNumber(ap) == True:
        ty = ty.capitalize()
        if validCategory(ty) == True:
            if validPositiveNumber(am) == True:
                apartmentList.append(int(ap))
                typeList.append(ty)
                amountList.append(int(am))
                addToUndoList()
                print("\n Item added !")
            else: print('\n Invalid data !')
        else: print('\n Invalid data !')
    else: print('\n Invalid data !')
    

def removeByApartment(ap):
    
    '''
    This function removes an apartment from the list
    Input: ap - the apartment number
    Output: -
    '''

    if validPositiveNumber(ap) == True:
        ap = int(ap)
        if existNumber(ap,apartmentList) == True:
            i = 0
            k = 0
            while i < len(apartmentList):
                if apartmentList[i] == ap:
                    del apartmentList[i]
                    del typeList[i]
                    del amountList[i]
                    k = k + 1
                else: i = i + 1
            if k != 0:
                print("\n Item removed !")
                addToUndoList()
        else: print("\n The apartment does not exist !")
    else: print('\n Invalid data !')


def removeByType(ty):
    
    '''
    This function removes an item from the list
    Input: ty - the type
    Output: -
    '''

    if validCategory(ty) == True:
        ty = ty.capitalize()
        if existCategory(ty,typeList) == True:
            i = 0
            k = 0
            while i < len(typeList):
                if typeList[i] == ty:
                    del apartmentList[i]
                    del typeList[i]
                    del amountList[i]
                    k = k + 1
                else: i = i + 1
            if k != 0:
                print("\n Item removed !")
                addToUndoList()
        else: print("\n Category does not exist !")
    else: print('\n Invalid data !')
        

def removeInRow(start,end):

    '''
    This function removes from a given apartment number to another one
    Input: start - the apartment number from the deleting starts
           end - the apartment number where the deleting ends
    Output: -
    '''
    
    if validPositiveNumber(start) == True:
        if validPositiveNumber(end) == True:
            i = 0
            k = 0
            start = int(start)
            end = int(end)
            while i < len(apartmentList):
                if apartmentList[i] >= start and apartmentList[i] <= end:
                    del apartmentList[i]
                    del typeList[i]
                    del amountList[i]
                    k = k + 1
                else: i = i + 1
            if k != 0:
                print("\n Item removed !")
                addToUndoList()
        else: print('\n Invalid data !')
    else: print('\n Invalid data !')

    
def replaceAmount(ap,ty,am):

    '''
    This function replace the amount of an item from the list
    that has the necessary requirements
    Input: ap - apartment
           ty - type
           am - amount
    Output: -
    '''

    if validPositiveNumber(ap) == True:
        if existNumber(ap,apartmentList) == True:
            ty = ty.capitalize()
            if validCategory(ty) == True:
                if existCategory(ty,typeList) == True:
                    if validPositiveNumber(am) == True:
                        ap = int(ap)
                        i = int(0)
                        while i < len(apartmentList):
                            if apartmentList[i] == ap and typeList[i] == ty:
                                break
                            else: i = i + 1
                        if i >= len(apartmentList): print("\n Such a combination does not exist !")
                        else:
                            amountList[i] = int(am)
                            print("\n Amount replaced !")
                            addToUndoList()
                    else: print('\n Invalid data !')
                else: print("\n The category does not exist !")
            else: print("\n Invalid data !")
        else: print("\n The apartment number does not exist !")
    else: print('\n Invalid data !')


def sum(x):

    '''
    This function calculates the sum of a given type
    Input: x - the type
    Output: The sum of expenses of the x type
    '''
    
    s = 0
    if existCategory(x,typeList) == True:
        x = x.capitalize()
        for i in range(len(typeList)):
            if typeList[i] == x:
                s = s + amountList[i]
        print('\n The sum of type',x,'is: ',s)
    else: print("\n The category does not exist !")
    

def max(x,y):

    '''
    This function shows the maxumim amount for each type
    Input: x - the apartment
           y - a string that tolds the program what should return
    Output: The expenses of each type of the x apartment
    '''

    w, h, e, g, o = 0, 0, 0, 0, 0
    if existNumber(x, apartmentList) == True:
        for i in range(len(apartmentList)):
            if apartmentList[i] == x:
                if typeList[i] == 'Water':
                    if w < amountList[i]: w = amountList[i]
                elif typeList[i] == 'Heating':
                    if h < amountList[i]: h = amountList[i]
                elif typeList[i] == 'Electricity':
                    if e < amountList[i]: e = amountList[i]
                elif typeList[i] == 'Gas':
                    if g < amountList[i]: g = amountList[i]
                elif typeList[i] == 'Other':
                    if o < amountList[i]: o = amountList[i]
        if y == '':
            print('\n Maximum amounts of each type: ')
            print('\n Water = ',w)
            print('\n Heating = ',h)
            print('\n Electricity = ',e)
            print('\n Gas = ',g)
            print('\n Other = ',o)
        elif y != '':
            total = w + h + e + g + o 
            return total
    else:
        if validPositiveNumber(x) == True:
            print("\n The apartment does not exist !")


def sort(x):

    '''
    This function sorts the apartments or types by the expenses
    Input: x - a string which reflects what will be sort in this function
    Output: -
    '''
    
    if x == 'apartment':
        apl = []
        k = 0
        for i in range(len(apartmentList)):
            if existNumber(apartmentList[i], apl) == False:
                apl.append(apartmentList[i])
                k = k + 1
        aml = []
        for i in range(len(apl)):
            total = max(apl[i],'sum')
            aml.append(total)
        i = 0
        j = 1
        while i < len(aml) - 1:
            j = i + 1
            while j < len(aml):
                if aml[i] > aml[j]:
                    aml[i], aml[j] = aml[j], aml[i]
                    apl[i], apl[j] = apl[j], apl[i]
                j = j + 1
            i = i + 1
        for i in range(len(apl)):
            print('\n Apartment',apl[i], 'with amount',aml[i])
    elif x == 'type':
            tyl = []
            k = 0
            for i in range(len(typeList)):
                if existCategory(typeList[i], tyl) == False:
                    tyl.append(typeList[i])
                    k = k + 1
            aml = [0,0,0,0,0]
            for i in range(len(tyl)):
                for j in range(len(typeList)):
                    if tyl[i] == typeList[j]:
                        aml[i] = aml[i] + amountList[j]
            i = 0
            j = 1
            while i < len(tyl) - 1:
                j = i + 1
                while j < len(tyl):
                    if aml[i] > aml[j]:
                        aml[i], aml[j] = aml[j], aml[i]
                        tyl[i], tyl[j] = tyl[j], tyl[i]
                    j = j + 1
                i = i + 1
            for i in range(len(tyl)):
                print('\n Type "',tyl[i], '" with amount',aml[i])
    else: print('\n Invalid data !')


def filter(x,y):

    '''
    This function delets all the data without the input
    Input: x - amount
           y - type
    Output: - 
    '''
    
    if x != 0 and validPositiveNumber(x) == True:
        i = 0
        k = 0
        while i < len(amountList):
            if x <= amountList[i]:
                k = k + 1
                del apartmentList[i]
                del typeList[i]
                del amountList[i]
            else: i = i + 1
        if k != 0:
            print('\n Item removed !')
            addToUndoList()
    elif y != '' and validCategory(y) == True:
        i = 0
        k = 0
        y = y.capitalize()
        while i < len(typeList):
            if y != typeList[i]:
                k = k + 1
                del apartmentList[i]
                del typeList[i]
                del amountList[i]
            else: i = i + 1
        if k != 0:
            print('\n Item removed !')
            addToUndoList()
    else: print('\n Invalid data !')


def addToUndoList():

    '''
    This function stores every modification made of the list in another list.
    It will be made a list of lists
    '''
    
    lap = []
    lty = []
    lam = []
    for i in range(len(apartmentList)):
        lap.append(apartmentList[i])
        lty.append(typeList[i])
        lam.append(amountList[i])
    undoApartmentList.append(lap)
    undoTypeList.append(lty)
    undoAmountList.append(lam)


def undo():

    '''
    This function undo the precedent modification made to the list.
    Undos can be made until the list it's equal with the original one
    '''

    if len(undoApartmentList) > 1:
        del undoApartmentList[len(undoApartmentList)-1]
        del undoTypeList[len(undoTypeList)-1]
        del undoAmountList[len(undoAmountList)-1]
        global apartmentList
        global typeList
        global amountList
        apartmentList = []
        typeList = []
        amountList = []
        apartmentList = undoApartmentList[len(undoApartmentList)-1]
        typeList = undoTypeList[len(undoTypeList)-1]
        amountList = undoAmountList[len(undoAmountList)-1]
    else:
        print("\n You can't undo !")
        initList()
        addToUndoList()
    
    
def readCommand():

    '''
    This function reads the command
    Input: -
    Output: command - the command
            apartment - the apartment number
            type - Gas, Heating, Other, Electricity, Water
            amount - the price
            sgn - the sign (<,>,=)
    '''

    global command
    global command2
    global apartment
    global type
    global amount
    global length
    global sgn
    
    command = ''
    command2 = ''
    apartment = int(0)
    type = ''
    amount = int(0)
    length = int(0)
    sgn = ''
    
    read = input("\n Your command: ")

    list = read.split(' ')
    length = len(list)
    command = list[0]
    if length == 2:
        if list[1] == 'apartment' or list[1] == 'type':
            command2 = list[1]
        else:
            if validCategory(list[1]) == True:
                type = list[1]
            elif validPositiveNumber(list[1]) == True:
                apartment = int(list[1])
    elif length == 3:
        if list[1] == '>' or list[1] == '<' or list[1] == '=':
            sgn = list[1]
            if validPositiveNumber(list[2]) == True:
                amount = int(list[2])
        elif validPositiveNumber(list[1]) == True:
            apartment = int(list[1])
            if validCategory(list[2]) == True:
                type = list[2]
    elif length == 4:
        if validPositiveNumber(list[1]) == True:
            apartment = int(list[1])
        if validCategory(list[2]) == True:
            type = list[2]
        if list[2] == 'to': command2 = list[2]
        if validPositiveNumber(list[3]) == True:
            amount = int(list[3])
    elif length == 5:
        if validPositiveNumber(list[1]) == True:
            apartment = int(list[1])
        if validCategory(list[2]) == True:
            type = list[2]
        if validPositiveNumber(list[4]) == True:
            amount = int(list[4])
        command2 = list[3]
    elif length == 0 or length > 5:
        print("\n Invalid data !")
   
    
def mainMenu():
    
    '''
    This function it's printing out the main menu
    Input: -
    Output: The main menu
    '''

    print("\n For HELP type: help \n")
    
    initList()

    addToUndoList()
   
    readCommand()
    while command != 'exit':
            if command == 'add':
                addItem(apartment, type, amount)
            elif command == 'remove':
                if length == 2:
                    if apartment > 0:
                        removeByApartment(apartment)
                    else:
                        if type != '' and validCategory(type) == True:
                            removeByType(type)
                        else: print('\n Invalid data !')
                elif length == 4:
                    if command2 == 'to': removeInRow(apartment, amount)
                    else: print('\n Invalid data !')
            elif command == "replace":
                if command2 == 'with': replaceAmount(apartment, type, amount)
                else: print('\n Invalid data !')
            elif command == 'help': UI.help()
            elif command == 'list':
                if length == 1: showList('',0)
                elif length == 2:
                    if apartment != 0: showList('',apartment)
                    else: print("\n Invalid data !")
                elif length == 3: showList(sgn,amount)
            elif command == 'sum':
                if validCategory(type) == True: sum(type)
                else: print('\n Invalid data !')
            elif command == 'max':
                if apartment != 0: max(apartment,command2)
                else: print('\n Invalid data !')
            elif command == 'sort':
                sort(command2)
            elif command == 'filter':
                if apartment > 0:
                    filter(apartment,'')
                else:
                    if type != '' and validCategory(type) == True:
                        filter(0,type)
                    else: print('\n Invalid data !')
            elif command == 'undo': undo()
            elif command == 'exit': break
            else: print("\n Unknown command ! \n")
            print('\n \n ====================================================== \n')
            readCommand()
