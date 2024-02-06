aud=[]
eve=[]
i=1
num=(int(input("Enter Number : ")))
#while i < num+1 :
for i in range(1,num):
    if i % 2 == 0:
        print(" -",i,end="")
        aud.append(i)
        i=i+1
    elif i %2!=0:
        print(" +",i,end="")
        eve.append(i)
        i=i+1
print("\n",aud)
print(eve)

