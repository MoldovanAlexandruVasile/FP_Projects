class Statistics(object):

    def __init__(self, aboutGrades):

        self.__aboutGrades = aboutGrades

    def sortAlphabetically(self):

        s = ""
        for i in self.__aboutGrades.sortAlphabetically():
            s += "\n \t" + i
        return s

    def sortAverageGrade(self):

        s = "\n"
        for i in self.__aboutGrades.sortAverageGrade():
            s += "\t Grade: " + str(i[0]) + "      Name: " + str(i[1]) + '\n'
        return s

    def failing(self):

        s = '\n'
        for i in self.__aboutGrades.failing():
            s += "\t" + str(i[1]) + "      ID: " + str(i[0]) + '\n'
        return s

    def bestSchoolSituation(self):

        s = '\n'
        for i in self.__aboutGrades.bestSchoolSituation():
            s += "\t Name: " + str(i[1]) + "      Average grade: " + str(i[0]) + '\n'
        return s

    def oneGrade(self):

        s = '\n'
        for i in self.__aboutGrades.oneGrade():
            s += "\t" + str(i[1]) + '\n'
        return s