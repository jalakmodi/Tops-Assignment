d={102:"Jalak",345:"Jigar",876:"Jay",908:"Sunil",676:"Harnish"}

print(d)
print(d[876])
print(d.get(908))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(345))
print(d)
print(d.popitem())
print(d)
d1={123:"Jigar",456:"Harnish"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])

d={}
n=int(input("Enter N : "))

for i in range(1,n+1):
    d[i]=i*i
print(d)


d[222]="Jigar"
d[111]="Jalak"
print(d)