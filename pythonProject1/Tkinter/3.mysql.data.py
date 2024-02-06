import mysql.connector

con=mysql.connector.connect(host="localhost",user="jalak",password="Admin@123",database="My School")
mycursou=con.cursor()
mycursou.execute("create table Employeeinfo(Emp_ID int,Emp_Name varchar(100),Designation VARCHAR (100),Salary DECIMAL (15,2))")



