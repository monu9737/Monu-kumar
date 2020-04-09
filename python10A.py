from tkinter import *
import mysql.connector
screen = Tk()
screen.title(" User Registration ")
screen.geometry('300x400')

def User_register():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="user"
    )
    mycursor = mydb.cursor()

    name = str(data1.get())
    uid = str(data2.get())
    gender = str(data3.get())
    email = str(data4.get())
    phone = str(data5.get())
    password = str(data6.get())

    sql = ("insert into students values(%s,%s,%s,%s,%s,%s)")
    val = (name, uid, gender, email, phone, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Data inserted ")
data1 = StringVar()
data2 = StringVar()
data3 = StringVar()
data4 = StringVar()
data5 = StringVar()
data6 = StringVar()

frame = Frame(scr, height=300, width=400)

h1 = Label(frame, text='Registeration', font=60, height=2, width=15).grid(row=0, column=1, pady=10)

name = Label(frame, text='Name:').grid(row=1, column=0)
e1 = Entry(frame, textvariable=data1).grid(row=1, column=1)

uid = Label(frame, text='UID:').grid(row=2, column=0)
e2 = Entry(frame, textvariable=data2).grid(row=2, column=1)

gender = Label(frame, text='Gender:').grid(row=3, column=0)
rd1 = Radiobutton(frame, text='Male', variable=data3, value="Male").grid(row=3, column=1)
rd2 = Radiobutton(frame, text='Female', variable=data3, value="Female").grid(row=4, column=1)

email = Label(frame, text='Email:').grid(row=5, column=0)
e4 = Entry(frame, textvariable=data4).grid(row=5, column=1)

phone = Label(frame, text='Phone:').grid(row=6, column=0)
e5 = Entry(frame, textvariable=data5).grid(row=6, column=1)

pswd = Label(frame, text='Password:').grid(row=7, column=0)
e6 = Entry(frame, textvariable=data6).grid(row=7, column=1)

btnaa = Button(frame, text="register", command=User_register()).grid(row=8, column=1)

frame.pack()
screen.mainloop()
