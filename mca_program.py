class mca_program:
    def __init__(self):
        self.tot_sem=int(input("enter the total sem :"))
        self.univ=input("enter the university :")
        
class course(mca_program):
    def course_details(self):
        self.c_name=input("enter your name : ")
        self.c_id=input("enter your ID : ")
        self.sem=int(input("enter your sem : "))
    
class faculty(course):
    def faculty_details(self):
        self.f_name=input("enter faculty name : ")
        self.f_id=input("enter the faculty ID : ")
        self.section=input("enter the section : ")
        self.tot_course=int(input("enter the total course(<=2) :"))
        
class display(faculty):
    def output(self):
        print("------the output------")
        print("the total sem is :",self.tot_sem)
        print("the name of the university is :",self.univ)
        print("the name of the candidate :",self.c_name)
        print("the ID of the candidate is :",self.c_id)
        print("the sem of the candidate :",self.sem)
        print("the name of the faculty is :",self.f_name)
        print("the ID of the faculty is :",self.f_id)
        print("the section of the faculty :",self.section)
        if self.tot_course<=2:
            print("the total course of the faculty :",self.tot_course)
        else:
            print("THE COURSE OF THE FACULTY SHOULD BE <=2")

stud=display()
stud.course_details()
stud.faculty_details()
stud.output()


        