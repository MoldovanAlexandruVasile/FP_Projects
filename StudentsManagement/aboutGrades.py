class GradesController(object):

    def __init__(self, Students, Disciplines, Grades):

        self.__students = Students
        self.__disciplines = Disciplines
        self.__grades = Grades

    def sortAlphabetically(self):

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

        list = []

        for i in self.__students.getAll():
            k = 0.0
            avg = 0.0
            for j in self.__grades.getAll():
                if j.getStudentID() == i.getID():
                    avg += j.getGradeValue()
                    k += 1.0
            if avg != 0.0:
                list.append([float(avg / k), i.getName()])
            else:
                list.append([0.0, i.getName()])

        list.sort(reverse=True)
        return list

    def failing(self):

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

        list = []

        for i in self.__students.getAll():
            k = 0.0
            avg = 0.0
            for j in self.__grades.getAll():
                if j.getStudentID() == i.getID():
                    avg += j.getGradeValue()
                    k += 1.0
            if avg != 0.0:
                list.append([float(avg / k), i.getName()])

        list.sort(reverse=True)
        return list

    def oneGrade(self):

        list = []

        for i in self.__disciplines.getAll():
            k = 0.0
            avg = 0.0
            for j in self.__grades.getAll():
                if i.getID() == j.getDisciplineID():
                    avg += j.getGradeValue()
                    k += 1.0

            if k != 0.0:
                list.append([float(avg / k), i.getName()])

        list.sort(reverse=True)
        return list