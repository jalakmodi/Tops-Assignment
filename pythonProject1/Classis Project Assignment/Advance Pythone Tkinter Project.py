from tkinter import *
import mysql.connector
from tkinter import messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_test"
        )
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get() =="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile,gender) values(%s,%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),var.get())
        cursor.execute(query,args)
        conn.commit()   
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        var.set("")
        msg.showinfo("Insert Status","Data Inserted Successfully")
print(insert_data)
root=Tk()
root.geometry("330x370")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)
var=StringVar()
def select():
    s=var.get()
    print(s)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

l_gen=Label(root,text="Gender")
l_gen.place(x=50,y=285)
var.set("Male")
e_gen1=Radiobutton(root,text="Male",variable=var,value="Male",command=select)
e_gen1.place(x=150,y=285)
e_gen2=Radiobutton(root,text="FeMale",variable=var,value="Female",command=select)
e_gen2.place(x=230,y=285)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",11),command=insert_data)
insert.place(x=20,y=320)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",11))
search.place(x=87,y=320)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",11))
update.place(x=162,y=320)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",11))
delete.place(x=235,y=320)



mainloop()

