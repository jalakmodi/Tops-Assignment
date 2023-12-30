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