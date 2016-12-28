from domain.classes import *

class Repository:

    '''s
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
                k = k + 1
                return i
        if k == 0: return 0

    def findName(self, item):

        '''
        Check for the position of an item
        '''

        k = 0
        for i in self._data:
            if item in i.getName():
                k = k + 1
                return i
        if k == 0: return 0

    def findIDWithName(self, name):

        '''
        Fidns the ID of an object with the name
        :param name: the object name
        :return: the object ID
        '''

        for i in self._data:
            if name == i.getName():
                return i.getID()

    def findNameWithID(self, ID):

        '''
        Finds the name of an object with the ID
        :param name: the object ID
        :return: the object name
        '''

        for i in self._data:
            if ID == i.getID():
                return i.getName()

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

        for i in self._data:
            if i.getID() == item:
                self._data.remove(i)

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
        
        return len(self._data)

    def listByID(self, item):

        '''
        Prints the items with the ID item
        '''

        for i in self._data:
            if item == i.getID(): print('     ID: ',i.getID(),'    Name: ',i.getName())

    def listByName(self, item):

        '''
        Prints the items with the name item
        '''

        for i in self._data:
            if item in i.getName(): print('     ID: ',i.getID(),'    Name: ',i.getName())

    def getAll(self):

        '''
        Returns the repository
        '''
        
        return self._data

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
    The class gradeRepository stores the data of Grade class
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

    def findByDisciplineID(self, ID):

        list = []
        for i in self._data:
            if ID == i.getDisciplineID():
                list.append(i.getStudentID())
        return list

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