class disciplineController:

    '''
    Modify the repository of disciplines
    '''

    def __init__(self, repo):

        self.__repo = repo

    def addDiscipline(self, discipline):

        '''
        Add a new discipline
        '''

        self.__repo.add(discipline)

    def removeDiscipline(self, index):

        '''
        Remove a discipline
        '''

        self.__repo.remove(index)

    def updateDiscipline(self, old, new):

        '''
        Update a discipline
        '''

        self.__repo.update(old, new)

    def getAll(self):
        
        """
        Returns the discipline repository
        """
        
        return self.__repo.getAll()
