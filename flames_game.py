name1_list=[]
name2_list=[]
flames=['f','l','a','m','e','s']
relationship={'f':"Friend",'l':"Love",'a':"Admirer",'m':"Marry",'e':"Enemy",'s':"Sibling"}
def common_char(name1_list,name2_list):
    for i in name1_list:
        if i in name2_list:
            name1_list.remove(i)
            name2_list.remove(i)
            common_char(name1_list,name2_list)
        
def iterate(flames,length_concat):
    a=0
    while(len(flames) != 1):
        a+=(length_concat-(len(flames)))
        a=a%(len(flames))
        flames.pop(a)
    
def display(relationship,b,name1,name2):
    print("the relationship between",'"',name1,'"'," and ",'"',name2,'"'," is derived as ",'"',relationship[b],'"'," by the “FLAMES” game.")
    
A=input("enter the first name : ")
B=input("enter the second name : ")
name1=A.lower()
name2=B.lower()
for i in name1:
    name1_list.append(i)
for j in name2:
    name2_list.append(j)

common_char(name1_list,name2_list)
concat_list=name1_list+name2_list
x=''
for i in concat_list:
    x+=i
print("the resultant string is : ",x)
length_concat=len(concat_list)-1
print("the length of the concated string is : ",length_concat+1)
iterate(flames,length_concat)
b=flames[0]
display(relationship,b,name1,name2)
    
        
