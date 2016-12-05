import unittest
from classes import *
from repository import *


class MyTestCase(unittest.TestCase):

    def testClass(self):

        x = Student(1, 'Alex')
        assert x.getID() == 1
        assert x.getName() == 'Alex'

        x = Discipline(2, 'Matematica')
        assert x.getID() == 2
        assert x.getName() == 'Matematica'

        x = Grade(1, 2172, 10)
        assert x.getDisciplineID() == 1
        assert x.getStudentID() == 2172
        assert x.getGradeValue() == 10

    def testOperations(self):

        student = Repository()
        discipline = Repository()
        grade = gradeRepository()

        student.add(Student(2172, 'Moldovan Alexandru Vasile'))
        student.add(Student(2150, 'Antal Victor'))
        student.add(Student(3512, 'Moldovanu Tudor'))
        student.add(Student(812, 'Muresan Paul'))
        student.add(Student(150, 'Pruneanu Rares'))
        student.add(Student(523, 'Brinzuca Ioana Diana'))
        student.add(Student(102, 'Pilca Alina Mihaela'))
        student.add(Student(315, 'Parnut Ioan Simion'))
        student.add(Student(3514, 'Soaita Andreea'))
        student.add(Student(51, 'Soaita Diana Maria'))

        discipline.add(Discipline(1, 'Matematica'))
        discipline.add(Discipline(2, 'Informatica'))
        discipline.add(Discipline(3, 'Fundamentele Programarii'))
        discipline.add(Discipline(4, 'Assembly'))
        discipline.add(Discipline(5, 'Sport'))

        grade.add(Grade(1, 2172, 10))
        grade.add(Grade(1, 102, 10))
        grade.add(Grade(2, 51, 3))
        grade.add(Grade(1, 315, 2))
        grade.add(Grade(3, 523, 6))
        grade.add(Grade(4, 102, 10))
        grade.add(Grade(2, 2172, 10))
        grade.add(Grade(1, 523, 4))

        assert len(student) == 10
        assert len(discipline) == 5
        assert len(grade) == 8

        #Add
        student.add(Student(1, "George"))
        assert len(student) == 11
        discipline.add(Discipline(6, "Chimie"))
        assert  len(discipline) == 6
        grade.add(Grade(1, 2172, 10))
        assert len(grade) == 9

        #Remove
        x = Student(2172, 'Moldovan Alexandru Vasile')
        student.remove(x.getID())
        grade.removeByStudent(x.getID())
        assert len(student) == 10
        assert len(discipline) == 6
        assert len(grade) == 6

        #Update
        x = Student(2172, 'Moldovan Alexandru')
        assert student.find(x.getID()) == 0
        x = Student(51, 'Soaita Diana')
        student.update(x)
        assert x.getID() == 51
        assert x.getName() == 'Soaita Diana'

if __name__ == '__main__':
    unittest.main()