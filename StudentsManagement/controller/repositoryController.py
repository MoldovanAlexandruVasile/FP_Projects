from repository.repository import *

class repositoryController:
    def __init__(self, repository):
        self.__repository = repository

    def add(self, item):
        self.__repository.add(item)

    def update(self, item):
        self.__repository.update(item)

    def remove(self, item):
        self.__repository.remove(item)

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