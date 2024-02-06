import mysql.connector

con=mysql.connector.connect(host="localhost",user="jalak",password="Admin@123",database="tkinterdata")
mycursou=con.cursor()
#mycursou.execute("create table Employeeinfo(Emp_ID int,Emp_Name varchar(100),Designation VARCHAR (100),Salary DECIMAL (15,2))")
#mycursou.execute("insert into Employeeinfo(Emp_Name,Designation,Salary) values('Jalak Modi','Programer','50000')")
insertdata="insert into employeeinfo(Emp_Name,Designation,Salary) values(%s,%s,%s)"
record=[
    ("Sunnu Modi","Manager",85000),
    ("Janvi Modi","Programmer",80000),
    ("Suraj Modi","Assistant",75000)]
mycursou.executemany(insertdata,record)
con.commit()