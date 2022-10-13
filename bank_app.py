#import sqlalchemy
#import pandas as pa
import pymysql
import datetime



conn = pymysql.connect(host='localhost',user='root',password = "",db="BANK")
cur = conn.cursor()
#cur.execute("CREATE DATABASE BANK")
#cur.execute("CREATE TABLE cust_details (NAME VARCHAR(50), ADDRESS VARCHAR(50), PH_NO int(10),USERNAME varchar(25),PASSWORD varchar(25))")
#cur.execute("CREATE TABLE transaction (SL_NO INT(3),DATE_TIME varchar(25), DEPOSIT int(10), WITHDRAWAL int(10),BALANCE int(10)) ")
class deposit_class:
    def deposit(self,x):
        self.amount=int(input("enter the amount you want to deposit : "))
        cur.execute("SELECT BALANCE FROM transaction WHERE SL_NO=(SELECT max(SL_NO) FROM transaction)")
        rows = cur.fetchall()
        for row in rows:
            balance=int(row[0])
        balance+=self.amount
        cur.execute("SELECT SL_NO FROM transaction WHERE SL_NO=(SELECT max(SL_NO) FROM transaction)")
        rows = cur.fetchall()
        for row in rows:
            sl_no=int(row[0])+1
        self.ch=cur.execute("INSERT INTO transaction(SL_NO,DATE_TIME,DEPOSIT,WITHDRAWAL,BALANCE) VALUES(%s,%s,%s,%s,%s)",(sl_no,x,self.amount,'0',balance))
        print("Balance is : ",balance)
        conn.commit()
       
class withdraw_class:
    def withdraw(self,x):
        self.amount=int(input("enter the amount you want to withdraw : "))
        cur.execute("SELECT BALANCE FROM transaction WHERE SL_NO=(SELECT max(SL_NO) FROM transaction)")
        rows = cur.fetchall()
        for row in rows:
            balance=int(row[0])
        if balance>self.amount:
            balance-=self.amount
            cur.execute("SELECT SL_NO FROM transaction WHERE SL_NO=(SELECT max(SL_NO) FROM transaction)")
            rows = cur.fetchall()
            for row in rows:
                sl_no=int(row[0])+1
            self.ch=cur.execute("INSERT INTO transaction(SL_NO,DATE_TIME,DEPOSIT,WITHDRAWAL,BALANCE) VALUES(%s,%s,%s,%s,%s)",(sl_no,x,'0',self.amount,balance))
            print("Balance is : ",balance)
            conn.commit()
        else:
            print("insufficient balance!!")
class check_balance:
    def check(self):
        cur.execute("SELECT BALANCE FROM transaction WHERE SL_NO=(SELECT max(SL_NO) FROM transaction)")
        rows = cur.fetchall()
        for row in rows:
            balance=int(row[0])
        print("THE BALANCE IS : ",balance)

class passbook_class:
    def passbook(self):
        self.s_date=input("enter start date in format : ")
        self.e_date=input("enter end date in format : ")
        cur.execute("SELECT * FROM transaction")
        rows = cur.fetchall()
        print("-------------PASSBOOK---------------")
        print("SL_NO\tDATE\t\tDEPOSIT\tWITHDRAWAL\tBALANCE")
        for row in rows:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t\t",row[4],"\n")


print("enter the details")
user1=input("enter the username : ")
pass1=input("enter the password : ")
check="SELECT USERNAME,PASSWORD FROM cust_details WHERE USERNAME= %s and PASSWORD = %s"
choice=cur.execute(check,(user1,pass1))
if choice >0:
    ch=0
    print("----------LOGGED IN SUCCESSFULLY------------")
    while(ch!=5):
        print("----------TRANSACTIONS AVAILABLE------------")
        print("\n1.Deposit amount\n2.Withdrawal\n3.Check Balance\n4.Print passbook\n5.Exit\n")
        ch=int(input("enter your choice : "))
        if ch==1:
            x = datetime.datetime.now().date()
            p1=deposit_class()
            p1.deposit(x)
        if ch==2:
            x = datetime.datetime.now().date()
            p2=withdraw_class()
            p2.withdraw(x)
        if ch==3:
            p3=check_balance()
            p3.check()
        if ch==4:
            p4=passbook_class()
            p4.passbook()
        if ch==5:
            break
else:
    print("wrong username or password")
        
conn.close()
    

