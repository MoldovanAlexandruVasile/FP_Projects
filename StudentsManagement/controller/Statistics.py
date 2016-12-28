from controller.statisticController import *

class Statistics:

    def __init__(self, aboutGrades):

        self.__aboutGrades = aboutGrades

    def sortAlphabetically(self):

        '''
        Creates a string of the list of students ordered alphabetically
        '''

        s = ""
        for i in self.__aboutGrades.sortAlphabetically():
            s += "\n \t" + i
        return s

    def sortAverageGrade(self):

        '''
        Creates a string of the list of students sorted by average grade
        ''' 

        s = "\n"
        for i in self.__aboutGrades.sortAverageGrade():
            s += "\t Grade: " + str(i[0]) + "      Name: " + str(i[1]) + '\n'
        return s

    def failing(self):

        '''
        Creates a string of the list of the students that are failing
        at a discipline
        '''

        s = '\n'
        for i in self.__aboutGrades.failing():
            s += "\t" + str(i[1]) + "      ID: " + str(i[0]) + '\n'
        return s

    def bestSchoolSituation(self):

        '''
        Creates a string of the list of students with the best school situation
        '''

        s = '\n'
        for i in self.__aboutGrades.bestSchoolSituation():
            s += "\t Name: " + str(i[1]) + "      Average grade: " + str(i[0]) + '\n'
        return s

    def oneGrade(self):

        '''
        Creates a string of the list of discipline where is at least one grade
        '''

        s = '\n'
        for i in self.__aboutGrades.oneGrade():
            s += "\t" + 'ID: ' + str(i[0]) + '    Discipline name: ' + str(i[1]) + '\n'
        return s