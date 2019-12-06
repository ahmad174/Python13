from tkinter import *
import sqlite3 as db


conn = db.connect('Mydatabase.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS DATA 
             (
                EmployeeName TEXT,
                EmployeeGender  TEXT,
                EmployeeNationality TEXT,
                EmployeeDateofBirth TEXT,
                EmployeeAddress TEXT,
                EmployeeDepartment TEXT,
                EmployeeSalary real)
             ''')


cur.close()
conn.commit()
conn.close()


def put():
    conn = db.connect('Mydatabase.db')
    cur = conn.cursor()
    cur.execute("insert into DATA values('%s','%s','%s','%s','%s','%s','%s')"%(EmployeeName.get(),EmployeeGender.get(),EmployeeNationality.get(),EmployeeDateofBirth.get(),EmployeeAddress.get(),EmployeeDepartment.get(),EmployeeSalary.get()) )
    cur.close()
    conn.commit()
    conn.close()
    status.set("Data added successfully.")


def fetchdata():
    conn = db.connect('Mydatabase.db')
    cur = conn.cursor()
    cur.execute("Select * from DATA ")
    list1=cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    output = ''
    for x in list1:
        output = output +  x[0] + " " + x[1] + " " + x[2] + " " + x[3] + " " + x[4] + " " + x[5] + " " + str(x[6])  + "\n"
    return(output)


master = Tk()

#EmployeeNumber = StringVar()
EmployeeName = StringVar()
EmployeeGender = StringVar()
EmployeeNationality = StringVar()
EmployeeDateofBirth = StringVar()
EmployeeAddress = StringVar()
EmployeeDepartment = StringVar()
EmployeeSalary = StringVar()
status = StringVar()



#Label(master, text="EmployeeNumber:").grid(row=0,column=0)
Label(master, text="EmployeeName").grid(row=1,column=0)
Label(master, text="EmployeeGender").grid(row=2,column=0)
Label(master, text="EmployeeNationality").grid(row=3,column=0)
Label(master, text="EmployeeDateofBirth").grid(row=4,column=0)
Label(master, text="EmployeeAddress").grid(row=5,column=0)
Label(master, text="EmployeeDepartment:").grid(row=6,column=0)
Label(master, text="EmployeeSalary").grid(row=7,column=0)
Label(master, text="", textvariable = status).grid(row=8,column=1)

#Entry(master , textvariable = EmployeeNumber).grid(row=0,column=1)
Entry(master , textvariable = EmployeeName).grid(row=1,column=1)
Entry(master , textvariable = EmployeeGender).grid(row=2,column=1)
Entry(master , textvariable = EmployeeNationality).grid(row=3,column=1)
Entry(master , textvariable = EmployeeDateofBirth).grid(row=4,column=1)
Entry(master , textvariable = EmployeeAddress).grid(row=5,column=1)
Entry(master , textvariable = EmployeeDepartment).grid(row=6,column=1)
Entry(master , textvariable = EmployeeSalary).grid(row=7,column=1)


text =Text(master,height=100,width=80)
text.grid(row=11 , columnspan=2)

Button(master, text="Submit" , command=put).grid(row=9,column=0)
Button(master, text="Fetch" , command=lambda: (text.delete(1.0,END),text.insert(END,fetchdata()))).grid(row=9,column=1)


mainloop()