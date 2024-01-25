n=int(input("Enter N : "))
l=[]
l2=[]
for i in range(1,n+1):
    l.append(i)
for j in (l[:5]):
    s=j*j
    l2.append(s)
for k in (l[-5:]):
    s=k*k
    l2.append(s)
print(l)
print("\nFirst Five And last Five Element Squre Is : ",l2)




