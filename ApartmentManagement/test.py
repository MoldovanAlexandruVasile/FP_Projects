import controler


def addTest():

    '''
    This functions tests the addItem function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.addItem(15, 'gas', 1000)
    assert len(controler.apartmentList) == 13
    assert len(controler.typeList) == 13
    assert len(controler.amountList) == 13
    controler.addItem('asd', 'gas', 1000)
    assert len(controler.apartmentList) == 13
    assert len(controler.typeList) == 13
    assert len(controler.amountList) == 13
    controler.addItem(15, 'gass', 1000)
    assert len(controler.apartmentList) == 13
    assert len(controler.typeList) == 13
    assert len(controler.amountList) == 13
    controler.addItem(15, 'gas', 'asd00')
    assert len(controler.apartmentList) == 13
    assert len(controler.typeList) == 13
    assert len(controler.amountList) == 13
    print("===============================")


def removeTest():

    '''
    This function tests all the remove functions
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.removeByApartment(15)
    assert len(controler.apartmentList) == 8
    assert len(controler.typeList) == 8
    assert len(controler.amountList) == 8
    controler.removeByApartment('gas')
    assert len(controler.apartmentList) == 8
    assert len(controler.typeList) == 8
    assert len(controler.amountList) == 8
    controler.removeByApartment(-15)
    assert len(controler.apartmentList) == 8
    assert len(controler.typeList) == 8
    assert len(controler.amountList) == 8
    print("===============================")
    

def replaceTest():

    ''' 
    This function test the replaceAmount function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.replaceAmount(15, 'gas', 1000)
    controler.replaceAmount('asd', 'gas', 1000)
    controler.replaceAmount(15,'gaas', 100)
    controler.replaceAmount(15,'gas', '10s0')
    print("===============================")



def listTest():

    '''
    This function test the showList function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.showList('',-15)
    controler.showList(-15,0)
    controler.showList('=',157)
    controler.showList('','gas')
    #controler.showList('',15)
    #controler.showList('',0)
    #controler.showList('>',100)
    #controler.showList('=', 156)
    #controler.showList('<',100)
    print("===============================")


def sumTest():

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.sum('-15')
    controler.sum('x')
    controler.sum('gas')
    print("===============================")


def maxTest():

    '''
    This function tests the max function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.max(-15,'')
    controler.max('gas','')
    controler.max('x','')
    #controler.max(15,'')


def sortTest():

    '''
    This function tests the sort function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.sort(-15)
    controler.sort('x')
    #controler.sort('apartment')
    #controler.sort('type')
    print("===============================")

def filterTest():

    '''
    This function tests the filter function
    '''

    assert len(controler.apartmentList) == 12
    assert len(controler.typeList) == 12
    assert len(controler.amountList) == 12
    controler.filter(0,'gas')
    assert len(controler.apartmentList) == 3
    assert len(controler.typeList) == 3
    assert len(controler.amountList) == 3
    controler.filter(100,'')
    assert len(controler.apartmentList) == 1
    assert len(controler.typeList) == 1
    assert len(controler.amountList) == 1

    
def test():

    controler.initList()
    addTest()
    controler.initList()
    removeTest()
    controler.initList()
    replaceTest()
    controler.initList()
    sumTest()
    maxTest()
    sortTest()
    filterTest()
