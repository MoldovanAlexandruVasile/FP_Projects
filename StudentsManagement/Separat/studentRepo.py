from studentClass import *


class studentRepository:

    def __init__(self):

        '''
        Constructor for Student class
        '''

        self.__data = []

    def add(self, student):

        '''
        Add a new student to the repository
        student - student to be added
        '''

        self.__data.append(student)

    def remove(self, index):

        '''
        Remove a student from the repository
        '''

        k = 0
        for i in range(len(self.__data)):
            if self.__data[i] == index: k = k + 1 
        if k != 0: return self.__data.pop(index)
        else: raise repositoryException("\n \t No such student found.")

    def update(self, old, new):

        ''' 
        Replace an item in the repository
        old - the current item
        new - the new item
        '''
        
        l = []
        for i in range(len(self.__data)):
            if self.__data.get(i) != old:
                l.append(self.__data[i])
            else:
                l.addNode(new)
        self.__data = l

    def __len__(self):
        
        """
        The length of the list
        """
        
        return len(self.__data)

    def getAll(self):
        
        """
        Return all repository data
        """
        
        return self.__data


class RepositoryException(Exception):
    
    """
    Exception class for repository errors
    """
    
    def __init__(self, message):
        
        '''
        Constructor for repository exception class
        message - A string representing the exception message
        '''
        
        self.__message = message

    def __str__(self):
        return self.__message

    
