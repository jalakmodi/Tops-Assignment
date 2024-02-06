import tkinter as tk
from tkinter import *

root=tk.Tk()
root.geometry("300x300")
root.title("RedioButton")
root.resizable(width=False,height=False)

def send():
    r = var.get()
    a=var0.get()
    b=var1.get()
    c=var2.get()
    print(r)
    file=open("Radio.txt","a")
    file.write("\n This Radio Is "+r)
    file.close()

var=StringVar()


var.set("Radio1")
R1=Radiobutton(root,text="Radio1",variable=var,value="Radio1",relief="raised",command=send)
R1.pack()
R2=Radiobutton(root,text="Radio2",variable=var,value="Radio2",relief="sunken",command=send)
R2.pack()
R3=Radiobutton(root,text="Radio3",variable=var,value="Radio3",relief="solid",command=send)
R3.pack()

var0=IntVar()
var1=StringVar()
var2=StringVar()
# var0="Radio4"
# var1="Radio5"
# var2="Radio6"

R4=Checkbutton(root,text="Radio4",variable=var0,relief="raised",command=send)#value="Radio4",
R4.pack()
R5=Checkbutton(root,text="Radio5",variable=var1,relief="sunken",command=send)#value="Radio5",
R5.pack()
R6=Checkbutton(root,text="Radio6",variable=var2,relief="solid",command=send)#value="Radio6",
R6.pack()

root.mainloop()
