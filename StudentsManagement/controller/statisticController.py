class statisticController:

    def __init__(self, student, discipline, grade):

        self.__students = student
        self.__disciplines = discipline
        self.__grades = grade

    def sortAlphabetically(self):

        '''
        Creates a list of students sorted alphabetically enroled at a given discipline.
        ''' 

        try:
            ID = int(input("\n \t \t Discipline ID: "))
            list = self.__grades.findByDisciplineID(ID)
            list2 = []
            for i in list:
                list2.append(self.__students.find(i).getName())
            list2.sort()
            return list2
        except ValueError: pass

    def sortAverageGrade(self):

        '''
        Creates a list of students sorted > by grade average
        '''

        list = []
        for i in self.__students.getAll():
            k = 0
            avg = 0
            for j in self.__grades.getAll():
                if j.getStudentID() == i.getID():
                    avg = avg + j.getGradeValue()
                    k = k + 1
            if avg != 0:
                list.append([float(avg / k), i.getName()])
            else:
                list.append([0.0, i.getName()])
        list.sort(reverse=True)
        return list

    def failing(self):

        '''
        Creates a list of lists. The lists from the lists are made of student ID
        and student name. This list will contain the students that are failing
        at a discipline
        ''' 

        list = []
        list2 = []
        for i in self.__grades.getAll():
            if i.getGradeValue() < 5:
                list.append(i.getStudentID())
        list = set(list)
        for i in list:
            ID = str(self.__students.find(i).getID())
            name = self.__students.find(i).getName()
            list2.append([ID, name]);
        return list2

    def bestSchoolSituation(self):

        '''
        Creates a list of lists. The lists from the lists are made of average grade
        and student name. This list will contain the students with best school
        situation
        '''

        list = []

        for i in self.__students.getAll():
            k = 0
            avg = 0
            for j in self.__grades.getAll():
                if j.getStudentID() == i.getID():
                    avg = avg + j.getGradeValue()
                    k = k + 1
            if avg >= 5:
                list.append([float(avg / k), i.getName()])
        list.sort(reverse=True)
        return list

    def oneGrade(self):

        '''
        Creates a list. The list is made of disciplines sorted alphabetically
        '''

        list = []
        for i in self.__disciplines.getAll():
            k = 0
            avg = 0
            for j in self.__grades.getAll():
                if i.getID() == j.getDisciplineID():
                    avg = avg + j.getGradeValue()
                    k = k + 1
            if k != 0:
                list.append([i.getID(),i.getName()])
        list.sort()
        return list