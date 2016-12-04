class Student:

    '''
    We declare a class of students where we have the name and ID
    of each student
    '''
    
    def __init__(self, studentID, name):
        '''
        Initialise a student with name and ID
        '''

        self.__studentID = studentID
        self.__name = name

    def getID(self):

        '''
        Getter: returns the ID of the student
        '''

        return self.__studentID

    def getName(self):

        '''
        Getter: returns the name of the student
        '''
        
        return self.__name

    def __str__(self):

        '''
        Returns a string with student ID and his name
        '''

        return "Student ID: " + str(self.__studentID) + "    Student name: " + str(self.__name)


class Discipline:

    '''
    We declare a class of disciplines where we have the discipline ID and
    name
    '''
    
    def __init__(self, disciplineID, name):

        '''
        Initialise the discipline with an ID and name
        '''
        
        self.__disciplineID = disciplineID
        self.__name = name

    def getID(self):

        '''
        Getter: returns the discipline ID
        '''
        
        return self.__disciplineID

    def getName(self):

        '''
        Getter: returns the name of the discipline
        '''
        
        return self.__name

    def __str__(self):

        '''
        Returns a string with discipline ID and discipline name
        '''

        return "Discipline ID: " + str(self.__disciplineID) + "    Discipline name: " + str(self.__name)


class Grade:

    '''
    We declare a class of grades where we have the discipline ID,
    student ID and the value of the grade
    '''
    
    def __init__(self, disciplineID, studentID, gradeValue):

        '''
        Initialise the grade with discipline ID, student Id and grade value
        '''
        
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__gradeValue = gradeValue

    def getDisciplineID(self):

        '''
        Getter: returns the discipline ID
        '''
        return self.__disciplineID

    def getStudentID(self):

        '''
        Getter: returns the student ID
        '''
        
        return self.__studentID

    def getGradeValue(self):

        '''
        Getter: returns the grade value
        '''
        
        return self.__gradeValue

    def __str__(self):

        '''
        Returns a string with discipline ID, student ID and grade value
        '''

        return "Discipline ID: " + str(self.__disciplineID) + "    Student ID: " + str(self.__studentID) + "    Grade value: " + str(self.__gradeValue)