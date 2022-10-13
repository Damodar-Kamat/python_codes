#debit card or credit card

def issuer(user_card):
    issuer_info=["Airline","Some master card accounts since 2017","American express and Diners club","Visa","Mastercard","Discover","Petroleum","Telecommunications","Government"]
    a = int(user_card[0])
    b = issuer_info[a]
    return b

def bank(user_card):
    bank_info = user_card[4:8]
    return bank_info

def verification(user_card):  
    verify = user_card[0:14]  
    verification1 = list(verify)
    verification1_rev = verify[::-1] 
    verification1_double = [int(x)+int(x) for x in verification1_rev[1:14:2]] 
    verification1_double_rev = []
    sum = 0
    for i in verification1_double:
        if i>9:
            c = verification1_double.index(i)
            d = c%10 
            c = d//10 
            c = c+d
            verification1_double[c] = i     
            verification1_double_rev = verification1_double[::-1]
    j=0
    for val in range(0,14,2):
        verification1[val] = verification1_double_rev[j]
        j+=1
    verify = [int(x) for x in verify ]
    for val in verify:               
        sum = sum+val
    print("check sum: ",sum)
    if sum%10 == 0:                             
        valid = True
    else:
        valid = False
    return valid



user_card=input("Enter your 16 digit card number : ")
if len(user_card)>16 or len(user_card)<16:
    print("invalid card number!!")
else:
    print("your card number is : ",user_card)
    print("issuer info : ",issuer(user_card))
    print("Bank info : ",bank(user_card))
    user_validity = verification(user_card)
    if user_validity:
        print("user card is valid")
    else:
        print("user card is invalid")