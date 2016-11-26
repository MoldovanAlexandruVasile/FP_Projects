class Discipline:

    '''
    We declare a class of disciplines where we have the discipline ID and
    name
    '''
    
    def __init__(self, disciplineID, name):
        self.__disciplineID = disciplineID
        self.__name = name

    def getDisciplineID(self):
        return self.__disciplineID

    def getStudentName(self):
        return self.__name

    def setDisciplineID(self, x):
        self.__disciplineID = x

    def setName(self, y):
        self.__name = y

    def idVerification(self):
        if isinstance(self.__disciplineID, int): pass
        else: raise TypeError("Invalid discipline ID !")

    def lista(self):
        l = []
        l.append(self.__disciplineID)
        l.append(self.__name)
        return l

def test_Discipline():

    assert str(Discipline('1', 'Matematica')) == '1 Matematica'
    assert str(Discipline(2, 'Romana')) == '2 Romana'
