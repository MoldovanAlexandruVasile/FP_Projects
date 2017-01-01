import pickle
from controller.repositoryController import *
from domain.classes import *

class studentsPickleFileRepository:

    def __init__(self,repository):
        self.__repository = repository

    def readFromStudentsFile(self):

        '''
        This function reads from a students pickle file the existing students
        '''

        f = open('StudentsPickle.pickle', "rb")
        try:
            for i in pickle.load(f):
                self.__repository.add(i)
            f.close()
        except EOFError: return []
        except IOError as e: print('\n',e)

    def writeToStudentsFile(self):

        '''
        This function writes in the students pickle file the added students in the program
        '''

        s = []
        f = open('StudentsPickle.pickle', "wb")
        for i in self.__repository._data:
            x = Student(int(i.getID()), str(i.getName()))
            s.append(x)
        pickle.dump(s, f)
        f.close()

    def deleteFromStudentsFile(self, item):

        '''
        This function removes a student from students pickle file
        :param item: is the ID of object we want to delete
        '''

        s = []
        f = open('StudentsPickle.pickle', "wb")
        for i in self.__repository._data:
            if i.getID() != item:
                x = Student(int(i.getID()), str(i.getName()))
                s.append(x)
        pickle.dump(s, f)
        f.close()