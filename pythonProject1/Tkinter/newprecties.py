# a=1
# while a<5:
#     print("this Is new ")
#     a=a+1
n=int(input("Enter Loop Number : "))
a=1
print("****Table of ",n,"****")
for i in range(1,11):
    t=n*i
    print(n," * ",a," = ",t)
    a=a+1
