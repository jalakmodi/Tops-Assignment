from tkinter import *
import mysql.connector
from tkinter import messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="my school")
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    elif e_mobile.get().isalpha() or len(e_mobile.get())!=10 or e_id.get().isalpha():
        msg.showerror("error","Mobile Number And ID Is Only 10 Digit")
        return
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into jnclass(First_Name,Last_Name,Email,Mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,"end")
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")
def serch_data():
    e_fname.delete(0,"end")
    e_lname.delete(0, "end")
    e_email.delete(0, "end")
    e_mobile.delete(0, "end")
    if  e_id.get()=="":
        msg.showinfo("info Message","ST Id Fill Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query = "select * from jnclass where st_id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row :
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status", "Id Not Found")
        conn.close()
def update_data():
    if  e_id.get()=="" or e_fname.get() == "" or e_lname.get() == "" or e_email.get() == "" or e_mobile.get() == "":
        msg.showinfo("Insert Status", "All Fields Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "update jnclass set First_Name=%s,Last_Name=%s,Email=%s,Mobile=%s where st_id=%s"
        args = (e_fname.get(), e_lname.get(), e_email.get(), e_mobile.get(), e_id.get())
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        msg.showinfo("info","Your Data Has Been Updated")
        e_id.delete(0,"end")
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_email.delete(0, "end")
        e_mobile.delete(0, "end")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("info Message", "ST Id Fill Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from jnclass where st_id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0, "end")
        e_fname.delete(0, "end")
        e_lname.delete(0, "end")
        e_email.delete(0, "end")
        e_mobile.delete(0, "end")
        msg.showinfo("info Message", "Your Data Has Been Deleted")
root=Tk()
root.geometry("360x380+600+100")
root.title("Registration Form")
root.config(bg="Light Blue")
root.resizable(width=False,height=False)


lbl=Label(root,text=": Student Information Form :",font="airal 18 bold",anchor=CENTER)
lbl.place(x=21,y=10)

l_id=Label(root,text="St ID : ",font="airal 10 bold",bg="Light Blue")
l_id.place(x=22,y=60)
e_id=Entry(root,textvariable="",font=10,width=20,)
e_id.place(x=110,y=60)

l_fname=Label(root,text="First Name : ",font="airal 10 bold",bg="Light Blue")
l_fname.place(x=22,y=110)
e_fname=Entry(root,textvariable="",font=10,width=20,)
e_fname.place(x=110,y=110)

l_lname=Label(root,text="LastName: ",font="airal 10 bold",bg="Light Blue")
l_lname.place(x=22,y=160)
e_lname=Entry(root,textvariable="",font=10,width=20)
e_lname.place(x=110,y=160)

l_email=Label(root,text="Email Id : ",font="airal 10 bold",bg="Light Blue")
l_email.place(x=22,y=210)
e_email=Entry(root,textvariable="",font=10,width=20)
e_email.place(x=110,y=210)

l_mobile=Label(root,text="Mobile: ",font="airal 10 bold",bg="Light Blue")
l_mobile.place(x=22,y=260)
e_mobile=Entry(root,textvariable="",font=10,width=20)
e_mobile.place(x=110,y=260)

bt_submit=Button(root,text="Submit",font="airal 12 bold",bg="Blue",fg="Yellow",command=insert_data)
bt_submit.place(x=22,y=310)
bt_serch=Button(root,text="Serch",font="airal 12 bold",bg="Blue",fg="Yellow",command=serch_data)
bt_serch.place(x=95,y=310)
bt_update=Button(root,text="Update",font="airal 12 bold",bg="Blue",fg="Yellow",command=update_data)
bt_update.place(x=160,y=310)
bt_delete=Button(root,text="Delete",font="airal 12 bold",bg="Blue",fg="Yellow",command=delete_data)
bt_delete.place(x=235,y=310)

mainloop()
