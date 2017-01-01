import pickle
from controller.repositoryController import *
from domain.classes import *

class gradesPickleFileRepository:

    def __init__(self,repository):
        self.__repository = repository

    def readFromGradesFile(self):

        '''
        This function reads from a students pickle file the existing students
        '''

        f = open('GradesPickle.pickle', "rb")
        try:
            for i in pickle.load(f):
                self.__repository.add(i)
            f.close()
        except EOFError: return []
        except IOError as e: print('\n', e)

    def writeToGradesFile(self):

        '''
        This function writes in the students pickle file the added students in the program
        '''

        s = []
        f = open('GradesPickle.pickle', "wb")
        for i in self.__repository._data:
            x = Grade(int(i.getDisciplineID()), int(i.getStudentID()), int(i.getGradeValue()))
            s.append(x)
        pickle.dump(s, f)
        f.close()

    def deleteFromGradesFile(self, item):

        '''
        This function removes a student from Students.txt
        :param item: is the ID of object we want to delete
        '''

        s = []
        f = open('GradesPickle.pickle', "wb")
        for i in self.__repository._data:
            if i.getStudentID() != item:
                x = Grade(int(i.getDisciplineID()), int(i.getStudentID()), int(i.getGradeValue()))
                s.append(x)
        pickle.dump(s, f)
        f.close()