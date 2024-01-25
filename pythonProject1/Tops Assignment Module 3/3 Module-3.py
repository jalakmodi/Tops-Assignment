# #************List ma duplicate Velue Mate **********
a = [ 1, 2,3,4,3,4,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("List In : B ",b)

