#hangman game

def letter_guess(count):
    while count>0:
        user2=input("guess a letter : ")
        if user2 not in list1:
            print(user2,"is not in word")
            count-=1
            print("you are left with",count,"chances")
        else:
            print(user2,"is in word")
            list1.remove(user2)
            a=len(list1)
            if a==0:
                break
            
    if count==0:
        print("you have lost the game!!")
        print("!!HANGMAN!!")
        print("the word given by",user1_name,"is",user1)
    elif a==0:
        print("you won the game!!")
          
list1=[]
user1_name=input("enter your name : ")
user1=input("enter the word : ")
for i in range(0,len(user1)):
    list1.append(user1[i])
    
count=6
letter_guess(count)

        