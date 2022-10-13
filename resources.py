seminar={}
lab1={}
lab2={}
class resources:
    def __init__(self,resource,name,date):
        self.resource=resource
        if self.resource=='seminar_hall':
            self.date=date
            if self.date in seminar.values():
                print("seminar hall is already booked")
            else:
                self.name=name
                self.date=date
                seminar.update({self.name:self.date})
                for key,value in seminar.items():
                    print("the seminar hall is booked by :",key,",on :",value)
        elif self.resource=='lab1':
            self.date=date
            if self.date in lab1.values():
                print("lab1 is already booked")
            else:
                self.name=name
                self.date=date
                lab1.update({self.name:self.date})
                for key,value in lab1.items():
                    print("the lab1 is booked by :",key,",on :",value)
        elif self.resource=='lab2':
            self.date=date
            if self.date in lab2.values():
                print("lab2 is already booked")
            else:
                self.name=name
                self.date=date
                lab2.update({self.name:self.date})
                for key,value in lab2.items():
                    print("the lab2 is booked by :",key,",on :",value)
        else:
            print("no such resource available")
        
try:            
    obj1=resources('seminar_hall','a','12-05-2022')
    obj2=resources('seminar_hall','b','12-05-2022')
    obj3=resources('seminar_hall','c','13-05-2022')
    obj4=resources('lab1','d','15-05-2022')
    obj5=resources('lab1','e','15-05-2022')
    obj6=resources('lab1','f','16-05-2022')
    obj7=resources('lab2','i','15-05-2022')
    obj8=resources('lab2','j','15-05-2022')
    obj9=resources('lab2','k','16-05-2022')
    obj10=resources('lab2''k','16-05-2022')
except:
    print("THE SYNTAX OF THE OBJECT CREATED IS INCORRECT")
