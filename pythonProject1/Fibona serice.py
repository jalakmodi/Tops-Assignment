n=int(input('Enter The Number is :- '))
a,b=0,1
print(a,end=' ')
while b<=n:
    print(b,end=' ')
    a,b=b,a+b

n=int(input("Enter Your Number : - "))
if n<0:
    print(f'Your Number {n} is Negative')
else:
    print(f'Your Number {n} is Positive')