import pickle
from controller.Controller import *
from domain.classes import *

class disciplinesPickleFileRepository:

    def __init__(self,repository):
        self.__repository = repository

    def readFromDisciplinesFile(self):

        '''
        This function reads from a disciplines pickle file the existing students
        '''

        f = open('DisciplinesPickle.pickle', "rb")
        try:
            for i in pickle.load(f):
                self.__repository.add(i)
            f.close()
        except EOFError: return []
        except IOError as e: print('\n', e)

    def writeToDisciplinesFile(self):

        '''
        This function writes in the disciplines pickle file the added students in the program
        '''

        s = []
        f = open('DisciplinesPickle.pickle', "wb")
        for i in self.__repository._data:
            x = Discipline(int(i.getID()), str(i.getName()))
            s.append(x)
        pickle.dump(s, f)
        f.close()

    def deleteFromDisciplinesFile(self, item):

        '''
        This function removes a disciplines from discipline pickle file
        :param item: is the ID of object we want to delete
        '''

        s = []
        f = open('DisciplinesPickle.pickle', "wb")
        for i in self.__repository._data:
            if i.getID() != item:
                x = Discipline(int(i.getID()), str(i.getName()))
                s.append(x)
        pickle.dump(s, f)
        f.close()