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
for r in range(5):
    for c in range(5):
        if r==0 and c<5 or c==2 and r<5 or c==0 and r==3 or c==0 and r==4  :
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n******************************")

# ***************** A Later Print *******************
for r in range(6):
    for c in range(5):
        if c==0 and r<6 and r!=0 or (c==4 and r<6 and r!=0 ) or (r==0 and c<5  and c!=0 and c!=4) or (r==3 and c<5  and c!=0 and c!=4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n******************************")

# ***************** L Later Print *******************
for r in range(6):
    for c in range(5):
        if r<5 and c==0 or r==4:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n******************************")

# ***************** A Later Print *******************
for r in range(6):
    for c in range(5):
        if c==0 and r<6 and r!=0 or (c==4 and r<6 and r!=0 ) or (r==0 and c<5  and c!=0 and c!=4) or (r==3 and c<5  and c!=0 and c!=4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n******************************")


# ***************** k Later Print *******************
for r in range(6):
    for c in range(5):
        if c==0 and r<5 or r==2 and c==1 or r==1 and c==2 or r==0 and c==3 or  c==2 and r==3 or r==4 and c==4:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n******************************")
















