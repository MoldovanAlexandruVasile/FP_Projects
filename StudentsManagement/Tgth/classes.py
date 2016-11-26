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




class Grade:

    '''
    We declare a class of grades where we have the discipline ID,
    student ID and the value of the grade
    '''
    
    def __init__(self, disciplineID, studentID, gradeValue):
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__gradeValue = gradeValue

    def getDisciplineID(self):
        return self.__disciplineID

    def getStudentID(self):
        return self.__studentID

    def getGradeValue(self):
        return self.__studentID

    def setDisciplineID(self, x):
        self.__disciplineID = x

    def setStudentID(self, y):
        self.__studentID = y

    def setGradeValue(self, z):
        self.__gradeValue = z

    def idVerification(self):
        if isinstance(self.__studentID, int): pass
        else: raise TypeError("Invalid student ID !")

    def __str__(self):
        s = ''
        r = str(self.__disciplineID) + ' ' + str(self.__studentID) + ' ' + str(self.__gradeValue)
        return r
    

def test_Grade():

    assert str(Grade(1, 11, 10)) == '1 11 10'
    assert str(Grade(24, 2, 7)) == '24 2 7'
    


def test_Discipline():

    assert str(Discipline('1', 'Matematica')) == '1 Matematica'
    assert str(Discipline(2, 'Romana')) == '2 Romana'


def test_Student():

    assert str(Student('Moldovan Alexandru-Vasile', 2172)) == '2172 Moldovan Alexandru-Vasile'
    assert str(Student('Moldovan Alexandru-Vasile', '2172')) == '2172 Moldovan Alexandru-Vasile'


