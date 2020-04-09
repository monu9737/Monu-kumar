from tkinter import *
import mysql.connector
screen=Tk()
screen.title("Registeration-form")
screen.geometry('500x400')

def DataRetrieve():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="user"
        )
    mycursor=mydb.cursor()
    table_name=str(data1.get())
    sql=("select * from {}".format(table_name))
    mycursor.execute(sql)
    result=mycursor.fetchall()

    out00=Label(frame,text="Name",width=10).grid(row=3,column=0)
    out01=Label(frame,text="Uid",width=10).grid(row=3,column=1)
    out03=Label(frame,text="Gender",width=10).grid(row=3,column=2)
    out04=Label(frame,text="Email",width=10).grid(row=3,column=3)
    out05=Label(frame,text="Phone",width=10).grid(row=3,column=4)
    out06=Label(frame,text="Password",width=10).grid(row=3,column=5)

    row_count=4
    for row in result:
        out11=Label(frame,text=row[0] ,width=10).grid(row=row_count,column=0)
        out12=Label(frame,text=row[1] ,width=10).grid(row=row_count,column=1)
        out13=Label(frame,text=row[2] ,width=10).grid(row=row_count,column=2)
        out14=Label(frame,text=row[3] ,width=10).grid(row=row_count,column=3)
        out15=Label(frame,text=row[4] ,width=10).grid(row=row_count,column=4)
        out16=Label(frame,text=row[5] ,width=10).grid(row=row_count,column=5)
        row_count+=1
    mydb.commit()
    print("Data Displayed ")

data1=StringVar()
frame=Frame(screen,width=500,height=400)
h1=Label(frame, text='Database', font=60,height=2,width=10).grid(row=0,column=1,pady=10,columnspan=6)
name=Label(frame, text='Table Name:',width=10).grid(row=1,column=2)
e1=Entry(frame, textvariable=data1 ,width=10).grid(row=1,column=3)
btn=Button(frame, text="Show Data", command=DataRetrieve()).grid(row=2,column=1,pady=20,columnspan=6)
frame.pack()
screen.mainloop()
