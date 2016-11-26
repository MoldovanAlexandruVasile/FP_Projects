class studentController:

    '''
    Modify the repository of students
    '''

    def __init__(self, repo):

        self.__repo = repo

    def addStudent(self, student):

        '''
        Add a new student
        '''
        
        self.__repo.add(student)

    def removeStudent(self, index):

        '''
        Remove a student
        '''

        self.__repo.remove(index)

    def updateStudent(self, old, new):

        '''
        Update a student
        '''

        self.__repo.update(old, new)

    def getAll(self):
        
        """
        Returns the student repository
        """
        
        return self.__repo.getAll()
