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
    

