from classes import *

class Repository:

    '''
    The class Repository stores the data of Student and Discipline class
    '''

    def __init__(self):

        '''
        Constructor for Student class
        '''

        self._data = []

    def find(self, item):

        '''
        Check for the position of an item
        '''

        k = 0
        for i in self._data:
            if item == i.getID():
                return i
                k = k + 1
        if k == 0: return 0

    def add(self, item):

        '''
        Add a new student to the repository
        item - student and discipline to be added
        '''

        self._data.append(item)

    def remove(self, item):

        '''
        Remove a student from the repository
        item - the item which will be removed
        '''

        itm = self.find(item)
        self._data.remove(itm)

    def update(self, item):

        ''' 
        Replace an item in the repository
        item - the object which will be updated
        '''
        
        itm = self.find(item.getID())
        pos = self._data.index(itm)
        self._data.remove(itm)
        self._data.insert(pos, item)

    def __len__(self):
        
        """
        The length of the list
        """
        
        return len(self.__data)

    def list(self):

        '''
        Prints the repository
        '''
        
        for i in self._data:
            print('\n     ',i.getID(),' ',i.getName())
    
    def getAll(self):

        '''
        Returns the repository
        '''
        
        return self._data;

    def __str__(self):

        '''
        Transforms the list in a string
        '''
        
        s = ''
        for i in self._data:
            s += str(i) + "\n"
        return s


class gradeRepository():

    '''
    The class graeRepository stores the data of Grade class
    '''

    def __init__(self):

        self._data = []

    def add(self, item):

        '''
        Adds a new item to the repository
        '''

        self._data.append(item)

    def find(self, item):

        '''
        Check for the position of an item
        '''

        for i in self._data:
            if item == i.getID(): return i

    def removeByStudent(self, ID):

        '''
        Removes an item by a student ID
        '''

        for i in self._data:
            if ID == i.getStudentID():
                self._data.remove(i)

    def removeByDiscipline(self, ID):

        '''
        Removes an item by a discipline ID
        '''

        for i in self._data:
            if ID == i.getDisciplineID():
                self._data.remove(i)
                    
    def list(self):

        '''
        Prints the repository
        '''
        
        for i in self._data:
            print('\n     ',i.getDisciplineID(),' ',i.getStudentID(),' ',i.getGradeValue())
    
    def getAll(self):

        '''
        Returns the repository
        '''
        
        return self._data;

    def __len__(self):

        """
        The length of the list
        """
        
        return len(self._data)

    def __str__(self):

        '''
        Transforms the list in a string
        '''
        
        s = ''
        for i in self._data:
            s += str(i) + "\n"
        return s
