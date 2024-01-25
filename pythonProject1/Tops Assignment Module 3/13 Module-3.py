#**************Find Repet Item In tupel***************
t=(10,20,30,40,40,10,50)
t1=()
for i in t:
    if t.count(i) > 1:
        print(i)
