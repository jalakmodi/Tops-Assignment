# import mysql.connector
#
# con=mysql.connector.connect(host="localhost",user="jalak",password="Admin@123",database="tkinterdata")
# mycursou=con.cursor()
# mycursou.execute("select * from employeeinfo")
# showResult = mycursou.fetchall()
# for row in showResult:
#     print(row)

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("275x175")

var=IntVar()
def select():
    s=var.get()
    if s==1:
        print("Male")
    else:
        print("Female")

R1=Radiobutton(root,text="Male",variable=var,value=1,command=select)
R1.place(x=10,y=20)
R2=Radiobutton(root,text="FeMale",variable=var,value=2,command=select)
R2.place(x=70,y=20)


mainloop()

