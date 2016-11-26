from repository import *
from classes import *

       
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
        string += "\n \t 8. Search."
        string += "\n \t 9. Redo."
        string += "\n \t 10. Undo."
        string += "\n \t 11. Print content"
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

        grade.add(Grade(1, 2172, 10))
        grade.add(Grade(2, 51, 8))
        grade.add(Grade(1, 315, 9))
        grade.add(Grade(3, 523, 6))
        grade.add(Grade(4, 102, 10))
        
        command = -1

        U = UI()

        while command != 0:

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
                x = U.readStudent()
                if student.find(x.getID()) != 0:
                    student.remove(x.getID())
                    grade.removeByStudent(x.getID())
                else: print("\n The student does not exist !")

            elif command == '4':
                x = U.readDiscipline()
                if discipline.find(x.getID()) != 0:
                    grade.removeByDiscipline(x.getID())
                    discipline.remove(x.getID())
                else: print("\n The discipline does not exist !")

            elif command == '5':
                x = U.readStudent()
                if student.find(x.getID()) != 0:
                    student.update(x)
                else: print("\n The student does not exist !")
                
            elif command == '6':
                x = U.readDiscipline()
                if discipline.find(x.getID()) != 0:
                    discipline.update(x)
                else: print("\n The discipline does not exist !")
                
            elif command == '7':
                x = U.readGrade()
                if student.find(x.getStudentID()) != 0 and discipline.find(x.getDisciplineID()) != 0:
                    grade.add(x)
                else: print("\n Invalid data !")

            elif command == '8': pass

            elif command == '9': pass

            elif command == '10': pass

            elif command == '11':
                print("\n \t  ~Student list~ \n")
                student.list()
                print("\n =============================================== \n")
                print("\n \t ~Discipline list~ \n")
                discipline.list()
                print("\n =============================================== \n")
                print("\n \t   ~Grade list~ \n")
                grade.list()
                print("\n =============================================== \n")

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
        except ValueError: print("\n Invalid data")
