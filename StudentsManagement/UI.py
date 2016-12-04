from repository import *
from classes import *
from aboutGrades import *
from Statistics import *

       
class UI:
    
    def __init__(self): pass

    def printMenu(self):
        
        string = "\n \t        ~MENU~"
        string += "\n \t 1. Add a new student."
        string += "\n \t 2. Add a new discipline"
        string += "\n \t 3. Remove a student."
        string += "\n \t 4. Remove a discipline."
        string += "\n \t 5. Update a student."
        string += "\n \t 6. Update a discipline."
        string += "\n \t 7. Add a grade."
        string += "\n \t 8. Search a student by ID."
        string += "\n \t 9. Search a student by name."
        string += "\n \t 10. Search a discipline by ID."
        string += "\n \t 11. Search a discipline by name."
        string += "\n \t 12. Sort students enroled at a discipline alphabetically."
        string += "\n \t 13. Sort students by descending order of average grade."
        string += "\n \t 14. Students failing at a discipline."
        string += "\n \t 15. Students with the best school situation."
        string += "\n \t 16. Disciplines with at least one grade."
        string += "\n \t 17. Redo."
        string += "\n \t 18. Undo."
        string += "\n \t 19. Print content."
        string += "\n \t 0. Exit."
        print(string)

    def mainMenu(self):

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

        
        command = -1

        U = UI()

        while command != 0:

            x = GradesController(student, discipline, grade)
            statistics = Statistics(x)

            U.printMenu()
            
            command = input("\n Your command: ")

            if command == '0': break

            elif command == '1':
                x = U.readStudent()
                try:
                    if student.find(x.getID()) == 0: student.add(x)
                    else: print("\n Student already exists !")
                except: pass

            elif command == '2':
                x = U.readDiscipline()
                try:
                    if discipline.find(x.getID()) == 0: discipline.add(x)
                    else: print("\n Discipline already exists !")
                except: pass

            elif command == '3':           
                x = U.readStudentID()
                if student.find(x.getID()) != 0:
                    student.remove(x.getID())
                    grade.removeByStudent(x.getID())
                else: print("\n The student does not exist !")

            elif command == '4':
                x = U.readDisciplineID()
                if discipline.find(x.getID()) != 0:
                    grade.removeByDiscipline(x.getID())
                    discipline.remove(x.getID())
                else: print("\n The discipline does not exist !")

            elif command == '5':
                x = U.readStudent()
                if student.find(x.getID()) != 0: student.update(x)
                else: print("\n The student does not exist !")
                
            elif command == '6':
                x = U.readDiscipline()
                if discipline.find(x.getID()) != 0: discipline.update(x)
                else: print("\n The discipline does not exist !")
                
            elif command == '7':
                x = U.readGrade()
                if student.find(x.getStudentID()) != 0 and discipline.find(x.getDisciplineID()) != 0:
                    grade.add(x)
                else: print("\n Invalid data !")

            elif command == '8':
                x = U.readStudentID()
                if student.find(x.getID()) != 0: student.listByID(x.getID())
                else: print("\n Invalid data !")

            elif command == '9':
                x = U.readStudentName()
                if student.findName(x.getName()) != 0: student.listByName(x.getName())
                else: print("\n Invalid data !")

            elif command == '10':
                x = U.readDisciplineID()
                if discipline.find(x.getID()) != 0: discipline.listByID(x.getID())
                else: print("\n Invalid data !")

            elif command == '11':
                x = U.readDisciplineName()
                if discipline.findName(x.getName()) != 0: discipline.listByName(x.getName())
                else: print("\n Invalid data !")


            elif command == '12': print(statistics.sortAlphabetically())

            elif command == '13': print(statistics.sortAverageGrade())

            elif command == '14': print(statistics.failing())

            elif command == '15': print(statistics.bestSchoolSituation())

            elif command == '16': print(statistics.oneGrade())

            elif command == '17': pass

            elif command == '18': pass

            elif command == '19':
                print("\n \t      ~Student list~ \n")
                print(str(student))
                print("\n ==================================================== \n")
                print("\n \t     ~Discipline list~ \n")
                print(str(discipline))
                print("\n ==================================================== \n")
                print("\n \t       ~Grade list~ \n")
                print(str(grade))
                print("\n ==================================================== \n")

            else: print("\n Invalid data !")

    def readStudent(self):

        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Student ID: "))
            name = input("\n \t Student name: ")
            return Student(ID, name)
        except ValueError: print("\n Invalid data !")
        
    def readDiscipline(self):

        '''
        Reads a discipline
        '''

        try:
            ID = int(input("\n \t Discipline ID: "))
            name = input("\n \t Discipline name: ")
            return Discipline(ID, name)
        except ValueError: print("\n Invalid data !")

    def readGrade(self):

        '''
        Reads a grade of a discipline and student
        '''

        try:
            dID = int(input("\n \t Discipline ID: "))
            sID = int(input("\n \t Student ID: "))
            grade = int(input("\n \t Grade: "))
            if grade < 1 or grade > 10: raise ValueError
            return Grade(dID, sID, grade)
        except ValueError: print("\n Invalid data !")

    def readStudentID(self):

        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Student ID: "))
            return Student(ID, '')
        except ValueError: print("\n Invalid data !")

    def readStudentName(self):

        '''
        Reads a discipline
        '''

        name = input("\n \t Student name: ")
        return Student(0, name)

    def readDisciplineID(self):

        '''
        Reads a student
        '''

        try:
            ID = int(input("\n \t Discipline ID: "))
            return Discipline(ID, '')
        except ValueError: print("\n Invalid data !")

    def readDisciplineName(self):

        '''
        Reads a discipline
        '''

        name = input("\n \t Discipline name: ")
        return Discipline(0, name)
