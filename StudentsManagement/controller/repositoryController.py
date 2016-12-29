from repository.repository import *
from controller.undoController import *

class repositoryController:
    def __init__(self, repository, undoController, gradesRepository):
        self.__repository = repository
        self.__undoController = undoController
        self.__gradesRepository = gradesRepository

    def add(self, item):
        self.__repository.add(item)
        redo = FunctionCall(self.add, item)
        undo = FunctionCall(self.remove, item)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def update(self, item):
        previous = self.__repository.find(item)
        self.__repository.update(item)
        redo = FunctionCall(self.update, item)
        undo = FunctionCall(self.update, previous)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)

    def remove(self, item):
        previous = self.__repository.find(item)
        list = self.__gradesRepository.getStudentGrades(item)
        self.__gradesRepository.removeByStudent(item)
        redo = FunctionCall(self.remove, item)
        undo = FunctionCall(self.add, previous)
        operation = Operation(redo, undo)
        self.__undoController.recordOperation(operation)
        for i in list:
            redo = FunctionCall(self.__gradesRepository.remove, i)
            undo = FunctionCall(self.__gradesRepository.add, i)
            operation = Operation(redo, undo)
            self.__undoController.recordOperation(operation)

    def find(self, item):
        return self.__repository.find(item)

    def findName(self,item):
        return self.__repository.findName(item)

    def findIDWithName(self, item):
        return self.__repository.findIDWithName(item)

    def findNameWithID(self, item):
        return self.__repository.findNameWithID(item)

    def listByID(self, item):
        self.__repository.listByID(item)

    def listByName(self, item):
        self.__repository.listByName(item)

    def getAll(self):
        return self.__repository.getAll()

    def __str__(self):
        return str(self.__repository)

    def __len__(self):
        return len(self.__repository)


class gradeRepositoryController:

    def __init__(self, repository):
        self.__repository = repository

    def add(self, item):
        self.__repository.add(item)

    def find(self, item):
        return self.__repository.find(item)

    def removeByStudent(self, item):
        self.__repository.removeByStudent(item)

    def removeByDiscipline(self, ID):
        self.__repository.removeByDiscipline(ID)

    def findByDisciplineID(self, ID):
        return self.__repository.findByDisciplineID(ID)

    def getAll(self):
        return self.__repository.getAll()

    def __str__(self):
        return str(self.__repository)

    def __len__(self):
        return len(self.__repository)