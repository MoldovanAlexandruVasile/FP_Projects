from controller.Controller import *
from domain.classes import *

class studentsFileRepository:

    def __init__(self, repository):
        self.__repository = repository

    def readFromStudentsFile(self):

        '''
        This function reads from Students.txt file the existing students
        '''

        try:
            studentFile = open("Students.txt", "r")
            line = studentFile.readline().strip()
            while line != "":
                lx = line.split(',')
                self.__repository.add(Student(int(lx[0]), str(lx[1])))
                line = studentFile.readline().strip()
            studentFile.close()
        except IOError: pass

    def writeToStudentsFile(self):

        '''
        This function writes in Students.txt the added students in the program
        '''

        studentFile = open("Students.txt", "w")
        try:
            for i in self.__repository._data:
                s = str(i.getID()) + ',' + str(i.getName()) + '\n'
                studentFile.write(s)
            studentFile.close()
        except Exception as e: print('\t \n', e)

    def deleteFromStudentsFile(self,item):

        '''
        This function removes a student from Students.txt
        :param item: is the ID of object we want to delete
        '''

        studentFile = open("Students.txt", "w")
        try:
            for i in self.__repository._data:
                if item != i.getID():
                    s = str(i.getID()) + ',' + str(i.getName()) + '\n'
                    studentFile.write(s)
            studentFile.close()
        except Exception as e: print('\t \n', e)