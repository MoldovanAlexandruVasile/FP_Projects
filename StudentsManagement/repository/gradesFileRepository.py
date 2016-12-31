from controller.repositoryController import *
from domain.classes import *

class gradesFileRepository:

    def __init__(self, repository):
        self.__repository = repository

    def readFromGradesFile(self):

        '''
        This function reads from Grades.txt file the existing grades
        '''

        try:
            gradeFile = open("Grades.txt", 'r')
            line = gradeFile.readline().strip()
            while line != "":
                lx = line.split(',')
                self.__repository.add(Grade(int(lx[0]), int(lx[1]), int(lx[2])))
                line = gradeFile.readline().strip()
            gradeFile.close()
        except IOError: pass

    def writeToGradesFile(self):

        '''
        This function writes in Grades.txt the added grades in the program
        '''

        gradeFile = open("Grades.txt", "w")
        try:
            for i in self.__repository._data:
                s = str(i.getDisciplineID()) + ', ' + str(i.getStudentID()) + ', ' + str(i.getGradeValue()) + '\n'
                gradeFile.write(s)
            gradeFile.close()
        except Exception as e: print('\t \n', e)

    def deleteFromGradesFile(self,item):

        '''
        This function removes the grades of a Student from Grades.txt
        :param item: is the ID of object we want to delete
        '''

        gradeFile = open("Grades.txt", "w")
        try:
            for i in self.__repository._data:
                if i.getStudentID() != item:
                    s = str(i.getDisciplineID()) + ', ' + str(i.getStudentID()) + ', ' + str(i.getGradeValue()) + '\n'
                    gradeFile.write(s)
            gradeFile.close()
        except Exception as e: print('\t \n', e)