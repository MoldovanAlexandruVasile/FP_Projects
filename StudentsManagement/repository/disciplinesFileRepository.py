from controller.Controller import *
from domain.classes import *

class disciplinesFileRepository:

    def __init__(self, repository):
        self.__repository = repository

    def readFromDisciplinesFile(self):

        '''
        This function reads from Disciplines.txt file the existing disciplines
        '''

        try:
            disciplineFile = open("Disciplines.txt", 'r')
            line = disciplineFile.readline().strip()
            while line != "":
                lx = line.split(',')
                self.__repository.add(Discipline(int(lx[0]), str(lx[1])))
                line = disciplineFile.readline().strip()
            disciplineFile.close()
        except IOError: pass

    def writeToDisciplinesFile(self):

        '''
        This function writes in Disciplines.txt the added discipline in the program
        '''

        disciplineFile = open("Disciplines.txt", "w")
        try:
            for i in self.__repository._data:
                s = str(i.getID()) + ',' + str(i.getName()) + '\n'
                disciplineFile.write(s)
            disciplineFile.close()
        except Exception as e: print('\t \n', e)

    def deleteFromDisciplinesFile(self,item):

        '''
        This function removes a discipline from Disciplines.txt
        :param item: is the ID of object we want to delete
        '''

        disciplineFile = open("Disciplines.txt", "w")
        try:
            for i in self.__repository._data:
                if item != i.getID():
                    s = str(i.getID()) + ',' + str(i.getName()) + '\n'
                    disciplineFile.write(s)
            disciplineFile.close()
        except Exception as e: print('\t \n', e)