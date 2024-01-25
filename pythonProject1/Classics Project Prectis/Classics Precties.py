# This Code For If
# a= int(input('Enter Number '))
# b=int(input('Enter Number '))
# c=a+b
# print('Addition  : ',c)
# c=a-b
# print('Subtr  : ',c)
# c=a*b
# print('Multypl  : ',c)

# a=float(input("Enter Number A : "))
# b=float(input("Enter Number B : "))
# if a>b:
#     print("A Is" ,a," is Max")
# else:
#     print("B Is" ,b, "is Max")

# a=float(input("Enter Number A : "))
# b=float(input("Enter Number B : "))
# c=float(input("Enter Number C : "))
#
# if a>b:
#     if a>c:
#         print(a,' Is Max')
#     else:
#         print(c," IS Max")
# elif b>c:
#     print(b, "Is Max")
# else:
#     print(c, "Is Max")

# This Code For Lader For Loop
# rno=int(input("Enter Roll Number"))
# sname=(input("Enter Name"))
# s1=int(input("Enter Mark S1"))
# s2=int(input("Enter Mark s2"))
# s3=int(input("Enter Roll Number"))
# total=s1+s2+s3
# per=total/3
#
# if per >= 70:
#     print(" Distinction")
# elif per >= 60:
#     print(" Fist Class")
# elif per >= 50:
#     print(" Second Class")
# elif per >= 40:
#     print(" Pass Class")
# else:
#     print("Fail")

# This Code For Loop

# for i in range(10):
#     print(i)
# print("**********************")
#
# for i in range(3,10):
#     print(i)
# print("**********************")
#
# for i in range(1,10,3):
#     print(i)
# print("**********************")


# for i in range(10):
#     print(" *"*i)
#
# for i in range(10):
#     print(" "*(9-i),"*"*i)
#
# for i in range(1,10):
#         print(" " * (9 - i), " *" * i)
# *****************J Later Print*******************
# for r in range(5):
#     for c in range(5):
#         if r==0 and c<5 or c==2 and r<5 or c==0 and r==3 or c==0 and r==4  :
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# print("\n******************************")
#
# # ***************** A Later Print *******************
# for r in range(6):
#     for c in range(5):
#         if c==0 and r<6 and r!=0 or (c==4 and r<6 and r!=0 ) or (r==0 and c<5  and c!=0 and c!=4) or (r==3 and c<5  and c!=0 and c!=4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# print("\n******************************")
#
# # ***************** L Later Print *******************
# for r in range(6):
#     for c in range(5):
#         if r<5 and c==0 or r==4:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# print("\n******************************")
#
# # ***************** A Later Print *******************
# for r in range(6):
#     for c in range(5):
#         if c==0 and r<6 and r!=0 or (c==4 and r<6 and r!=0 ) or (r==0 and c<5  and c!=0 and c!=4) or (r==3 and c<5  and c!=0 and c!=4):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# print("\n******************************")
#
#
# # ***************** k Later Print *******************
# for r in range(6):
#     for c in range(5):
#         if c==0 and r<5 or r==2 and c==1 or r==1 and c==2 or r==0 and c==3 or  c==2 and r==3 or r==4 and c==4:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# print("\n******************************")
#
# for l in "Tops Technology":
#     if l=="p" or l=='s':
#         break
#
# print ("Current Letter: ", l)

# # ***************** Numer Pyramid  *******************
# for i in range(1,9):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
# n= "Home Automation"
# print(n[0:5])
# print(n[-14:-1])
# print(n[-14:-1:2])
# print(n[::-3])

#Date **** 02-01-24 **********

# j=1
# for i in range(65,75):
#     print(chr(i)*j)
#     j=j+1



# n=int(input("Enter Number : "))
# while n>0:
#     print("Tops Technology")
#     n=n-1


# n=int(input('Enter The Number is :- '))
# a,b=0,1
# print(a,end=' ')
# while b<=n:
#     print(b,end=' ')
#     a,b=b,a+b


# a,b=0,1
# n=int(input('Enter The Number is :- '))
# print(a)
# while b <= n:
#     print(b)
#     a,b = b,a+b

#***********Prime Number ***********

# n=int(input("Enter Number"))
# if n%2!=0:
#     for i in range(3,int(n/2)+1,2):
#         if n%i==0:
#             print(n, "This Is not Prime")
#     else:
#             print(n,"is Prime")
# else:
#     print(n, " not Prime")

# n=int(input("Enter N: "))
# i = 1
# while i<= n:
#     print(i)
#     i=i+1
# n=int(input("Enter N: "))
# i=1
# while i<n:
#     print(i*i)
#     i =i+1

# print("Number Pattern ")
# row = 5
# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")

# s1=input("Enter String : ")
# u=l=c=s=n=sc=0
# for i in s1:
#     if i.isupper():
#         u=u+1
#     elif i.islower():
#         l=l+1
#     elif i.isalpha():
#         c=c+1
#     elif i.isnumeric():
#         n=n+1
#     elif i.isspace():
#         s=s+1
#     else:
#         sc=sc+1
#
# print("Total Uper Case : ",u)
# print("Total Lower Case : ",l)
# print("Total Alphabets : ",c)
# print("Total Numer : ",n)
# print("Total Uper Case : ",sc)

# Intializing the lists
# List1 = [4,28,6,99,100,25,18,10,40,73]
# list2 = [25, 40,73,4,80,63,99,6]
# new_list1 = [] #empty list
# for i in List1:
# 	if i not in list2:
# 		new_list1.append(i)
#
# print("elements of list 1 that are not present in list 2 ",new_list1)
# new_list2 = [] #empty list
# for i in list2:
# 	if i not in List1:
# 		new_list2.append(i)
# print("\nlements of list 2 that are not present in list 1 ",new_list2)
# print("\nelements of New_list 1 is ",new_list1)

# l = [10, 20, 30, 40]
# a = l.pop(10)
# print("\n", a)

# word = "PYTHON IS COOL"
# print(word[2:12])
# print(word[:6])
# print(word[4:13:2])
# print(word[5:11])
#
# print(word[:12])
#
# print(word[-7:-2])
#
# print(word[-9:8])
#
# print(word[::-1])

#**************Stack*********************
#
# from _collections import  deque
# l=deque([])
# l.append(10)
# print(list(l))
# l.append(20)
# print(list(l))
# l.append(30)
# print(list(l))
# l.append(40)
# print(list(l))
# l.append(50)
# print(list(l))
#
# #*************popleft Thi delete Karva Mate
# l.popleft()
# print(list(l))
# l.popleft()
# print(list(l))
# l.popleft()
# print(list(l))
# l.popleft()
# print(list(l))
# l.popleft()
# print(list(l))

#*************popleft Thi delete Karva Mate
# d={101:"Jalak",102:"Jigar",103:"Jay",104:"Sunil"}
# d2={}
# print(d)
# print(d[102])
# print(d.get(104))
# print(d.items())
# print(d.keys())
# print(d.values())
# #print(d.pop(103))
# print(d)
# print(d.popitem())
# d2.update({101:"jhvjh"})
# print(d2)
#
#
# print("Key  &  Value")
# for i in d:
#     print(i,d[i])

# d={}
# n=int(input("Enter N : "))
# for i in range(2,n+1):
#     d[i]=i*i
# print(d)

#************List ma Max Velue Mate **********
# a = [ 1, 2,  3.50, 5, 6 ]
# p=(max(a))
# print(p)
# #************List ma Min Velue mate **********
# a = [ 1, 2,  3.50, 5, 6 ]
# p=(min(a))
# print(p)
#
# #************List ma length Velue Mate **********
# a = [ 1, 2,  3.50, 5, 6]
# p=(len(a))
# print(p)

# #************List ma duplicate Velue Mate **********
# a = [ 1, 2,3,4,3, 4,5]
# b=[]
# for i in a:
#     #print(i)
#     if i not in b:
#         b.append(i)
#         #print(b)
# print("List Data In : B ",b)
#
# #************List ma duplicate  Velue Mate **********
# a = [1,2,3,4,5,6]
# b = [7,8,9,1,2,3,4]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print("\n The common element is:",c)

#************List ma Total Sum Velue Mate **********
# a = []
# n= int(input(" Enter N: "))
# sum=0
# for i in range(1,n):
#     a.append(i)
#     sum=sum+i
# print(sum)
# print(a)


# s= ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print("1  ",s[7:9])
# print("2  ",s[-3:-1])
# print("3  ",s[:3])
# print("4  ",s[-1:])
# print("5  ",s[14:-12])
# print("6  ",s[1:-1])
# print("7  ",s[0:5:2])
# print("8  ",s[::-1])
# print("9  ",s[5:2:-1])
# print("10  ",s[14:2:-3])

# l = ["apple", "banana", "cherry"]
# l.insert(3,["orange",10])
# print(l)

#************List ma Velue Che ke nai te Check Karva Mate **********
# n=input("Enter Your N : ")
#
# l = ["apple", "banana", "cherry"]
# if n in l:
#     print(f"{n} Is Available In List")
# else:
#     print(f"{n} Is Not Available In List")

#************List ma Velue Che ke nai te Check Karva Mate **********

# l1 = ["apple", "banana", "cherry"]
# l2=["apple", "banana", "cherry",10,20,30]
# l3=[]
# for a in l1:
#     for b in l2:
#         if a == b:
#             l3.append(l2)
# print(l3)
#************Tuple libarary Ma Use Thata  **********
# l=(20,80,90,20,30,10,5)
# s1="jalak"
#
# m=max(l)
# n=min(l)
# o=len(l)
# r=sum(l)
# s=sorted(l)
# t=l.count(20)
# u=l.index(5)
# v=tuple(s1)
#
# print(m)
# print(n)
# print("length of tuple : ",len(l))
# print(r)
# print(s)
# print(t)
# print(u)
# print(v)

# ************List ma Velue Che ke nai te Check Karva Mate **********
#
# n1= int(input('''Enter Below Choise
# 	[4, 55, 64, 32, 16, 32]
# 			 N : '''))
#
# fruits = [4, 55, 64, 32, 16, 32]
# if n1 in list(fruits):
#     x = fruits.index(n1)
#     print(n1, " is in index number", x)
# else:
#     print(n1, " is Not in index List")

# l1 = ["apple", "banana", "cherry", 10, 20, 30]
# l2 = ["apple", "banana", "cherry"]
# l3 = [a for a in l1 if a not in l2]
# print(l3)


# import random
# l=[]
# lucky=[]
# for i in range(1,101):
#     l.append(i)
#
# for i in range(10):
#     num=random.choice(l)
#     lucky.append(num)
#     l.remove(num)
# print(l)
# print(lucky)


#****************File Ne W+ Mode Ma use Karva Mate****** ***********11-01-1-24*****************
# file=open("tops1.txt","w")
# file.write("This Is Demo Class")
# file.close()
#
# file=open("tops1.txt","r")
# print(file.read())
# file.close()
#
# file=open("tops1.txt","a")
# file.write("\n This Is Demo Class1")
# file.close()

#****************File Ne W+ Mode Ma use Karva Mate******************
# file=open("tops2.txt","w+")
# file.write("\n This Is Demo Class with W+")
# file.seek(0)
# print(file.read())
# file.close()
# print("File Written Successfully")
# print("*******************************************")



#********************** UPS Argument **************** 23-01-24 *****************

#fuction With No Argument & No return Value.
#
# def printline():
#     print("*"*60)
#
# printline()
# print("Welcome To Jalak Modi")
# printline()
#
# #fuction With Argument But No return Value.
#
# def add(a,b):
#     print("addition : ", a+b)
#
# printline()
# x=int(input("Enter Velue :"))
# y=int(input("Enter Velue :"))
# add(x,y)
# printline()
#
# #fuction With Argument & return Value.
# def sub(a,b):
#     return a-b
#
# def test (a,b,c,d):
#     print("A : ",a,"B : ",b,"C : ",c,"D :",d)
# test(10,20,30,40)
#
# def test(a,b,c,*d,**e):
#     print("A",a,"B",b,"C",c,"D",d,"E",e)
#
# test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)
# ************oop Na Function Create Karva mate ****** ***********25-01-2.24*****************
# class Student:
#     def getData(self,fname,lname):
#        print("getData called")
#        self.f=fname
#        self.l=lname
#     def putData(self):
#         print("putData called")
#         print("First Name : ",self.f)
#         print("Last Name : ",self.l)
#
# s1=Student()
# s1.getData("Jalak", "Modi")
# s1.putData()






