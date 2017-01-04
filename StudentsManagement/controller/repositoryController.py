from repository.repository import *
from controller.undoController import *

class repositoryController:
    def __init__(self, repository, undoController, grades):
        self.__repository = repository
        self.__undoController = undoController
        self.__grades = grades

    def add(self, item):

        '''
        This function adds the new object to the repository
        Also prepares the undo and redo functions
        :param item: object which we want to add
        '''

        self.__repository.add(item)
        redo = FunctionCall(self.add, item)
        undo = FunctionCall(self.remove, item.getID())
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def update(self, item):

        '''
        This funcion updates an object
        Also prepares the undo and redo functions
        :param item: object we want to update
        '''

        previous = self.__repository.find(item.getID())
        self.__repository.update(item)
        redo = FunctionCall(self.update, item)
        undo = FunctionCall(self.update, previous)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def remove(self, item):

        '''
        This function removes an object from the repo
        Also prepares undo and redo functions
        :param item: The object ID
        '''

        previous = self.__repository.find(item)
        list = self.__grades.getStudentGrades(item)
        self.__repository.remove(item)
        redo = FunctionCall(self.remove, item)
        undo = FunctionCall(self.add, previous)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)
        for i in list:
            redo = FunctionCall(self.__grades.removeByStudent, i)
            undo = FunctionCall(self.__grades.add, i)
            operation = Operation(redo, undo)
            self.__undoController.recordOperation(operation)

    def find(self, item):

        '''
        Check the position of the item
        :param item: The ID of the item we are looking for
        :return: The position of the item
        '''

        return self.__repository.find(item)

    def findName(self,item):

        '''
        Check the position of the item
        :param item: The name of the item we are looking for
        :return: The position of the item
        '''

        return self.__repository.findName(item)

    def findIDWithName(self, item):

        '''
        This function finds the ID of object, with objects name
        :param item: The name
        :return: The ID of the object
        '''

        return self.__repository.findIDWithName(item)

    def findNameWithID(self, item):

        '''
        This function finds the name of object, with objects ID
        :param item: The ID
        :return: The name of the object
        '''

        return self.__repository.findNameWithID(item)

    def listByID(self, item):

        '''
        This function searches for an object with ID item
        :param item: The ID
        :return: The object
        '''

        return self.__repository.listByID(item)

    def listByName(self, item):

        '''
        This function searches for an object with name item
        :param item: The name
        :return: The objects
        '''

        return self.__repository.listByName(item)

    def getAll(self):

        '''
        :return: The repository
        '''

        return self.__repository.getAll()

    def __str__(self):
        return str(self.__repository)

    def __len__(self):
        return len(self.__repository)


class gradeRepositoryController:

    def __init__(self, repository, student, discipline, undoController):
        self.__repository = repository
        self.__student = student
        self.__discipline = discipline
        self.__undoController = undoController

    def add(self, item):

        '''
        This function adds the new object to the repository of grades
        Also prepares the undo and redo functions
        :param item: object which we want to add
        '''

        self.__repository.add(item)
        redo = FunctionCall(self.add, item)
        undo = FunctionCall(self.removeLast, item.getStudentID())
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def find(self, item):
        '''
        Check the position of the item
        :param item: The ID of the item we are looking for
        :return: The position of the item
        '''

        return self.__repository.find(item)

    def removeLast(self, item):

        '''
        This function removes the las element of the repository
        :param item: The ID of object
        '''

        self.__repository.removeLast(item)

    def removeByStudent(self, ID):

        '''
        This function removes from the reposoitory by students ID
        :param item: ID
        '''

        self.__repository.removeByStudent(ID)

    def removeByDiscipline(self, ID):

        '''
        This function removes from the reposoitory by disciplines ID
        :param item: ID
        '''

        self.__repository.removeByDiscipline(ID)

    def findByDisciplineID(self, ID):

        '''
        This function find all the students enroled at the discipline with ID ID
        :param ID: ID of the discipline
        :return: a string with the students
        '''

        return self.__repository.findByDisciplineID(ID)

    def getAll(self):
        return self.__repository.getAll()

    def __str__(self):
        return str(self.__repository)

    def __len__(self):
        return len(self.__repository)