class Student:

    '''
    We declare a class of students where we have the name and ID
    of each student
    '''
    
    def __init__(self, name, studentID):
        self.__name = name
        self.__studentID = studentID

    def getStudentName(self):
        return self.__name

    def getStudentID(self):
        return self.__studentID

    def setName(self, x):
        self.__name = x

    def setStudentID(self, y):
        self.__studentID = y

    def idVerification(self):
        if isinstance(self.__studentID, int): pass
        else: raise TypeError("Invalid student ID !")

    def lista(self):
        l = []
        l.append(self.__studentID)
        l.append(self.__name)
        return l
    

def test_Student():

    assert str(Student('Moldovan Alexandru-Vasile', 2172)) == '2172 Moldovan Alexandru-Vasile'
    assert str(Student('Moldovan Alexandru-Vasile', '2172')) == '2172 Moldovan Alexandru-Vasile'
