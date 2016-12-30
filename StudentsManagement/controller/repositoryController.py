from repository.repository import *
from controller.undoController import *

class repositoryController:
    def __init__(self, repository, undoController, grades):
        self.__repository = repository
        self.__undoController = undoController
        self.__grades = grades

    def add(self, item):
        self.__repository.add(item)
        redo = FunctionCall(self.add, item)
        undo = FunctionCall(self.remove, item.getID())
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
        self.__repository.remove(item)
        list = self.__grades.getStudentGrades(item)
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

    def __init__(self, repository, student, discipline, undoController):
        self.__repository = repository
        self.__student = student
        self.__discipline = discipline
        self.__undo = undoController

    def add(self, item):
        self.__repository.add(item)
        redo = FunctionCall(self.add, item)
        undo = FunctionCall(self.removeByStudent, item.getStudentID())
        operation = Operation(redo, undo)
        self.__undo.recordOperation(operation)

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