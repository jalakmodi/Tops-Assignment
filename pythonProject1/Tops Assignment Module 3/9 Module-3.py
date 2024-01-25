
t=(1,2,1.1,2.2,[100,200,300],"tops",True,10,1,2)

print(t)
print(t.count(1))
print(t.index(10))
print(t[4])
t[4].append(400)
print(t)

for i in t:
    print(i)

print(10 in t)
