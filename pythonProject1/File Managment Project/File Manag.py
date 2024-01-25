# file=open("tops1.txt","w")
# file.write("This Is Demo Class")
# file.close()
#
# file=open("tops1.txt","r")
# print(file.read())
# file.close()
#
# file=open("tops1.txt","a")
# file.write("\n This Is Demo Class1")
# file.close()

#****************File Ne W+ Mode Ma use Karva Mate
file=open("tops2.txt","w+")
file.write("\n This Is Demo Class with W+")
file.seek(0)
print(file.read())
file.close()
print("File Written Successfully")
print("*******************************************")






