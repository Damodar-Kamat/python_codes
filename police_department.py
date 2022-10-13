#police department
class person:
    def __init__(self,name,age,crime):
        self.name=name
        self.age=age
        self.crime=crime
        
class missing(person):
    def __init__(self,p,date,reported):
        super().__init__(*p)
        self.date=date
        self.reported=reported
    
class absconding(person):
    def __init__(self,p,date,reward):
        super().__init__(*p)
        self.date=date
        self.reward=reward
        
prisoner=person('aaron',35,'robbery')
missing_prisoner=missing(('rohan',55,'murder'),'12-03-2020','15-03-2020')
absconding_prisoner=absconding(('mahesh',45,'bank robbery'),'18-05-2021',10000)

print("the prisoner's name is :",prisoner.name)
print("the missing prisoner name is :",missing_prisoner.name)
print("the missing date : ",missing_prisoner.date,",the reported date : ",missing_prisoner.reported)
print("the absconded prisoner name is :",absconding_prisoner.name)
print("the absconded date :",absconding_prisoner.date,",the reward is :",absconding_prisoner.reward)
