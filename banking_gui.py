from atexit import register
from cProfile import label
from ctypes.wintypes import PINT
from multiprocessing import connection
from tkinter import *
import tkinter
from turtle import right
from matplotlib.pyplot import connect, text
import math
import sqlite3

'''
#Database 
connected = sqlite3.connect('romeo_bank.db')
curs = connected.cursor()

#Database Table
curs.execute("""CREATE TABLE records (
        user_name text, 
        user_balance integer, 
        user_pin text
        )""")

#Commit changes and close connection
connected.commit()        
connected.close()
'''

#Root Page
root = Tk()
root.geometry("300x300")

bank_name = Label(root, text="Romeo's Banking App")
bank_name.place(x=30, y=0)


def registration():
    #Top Page
    top = Toplevel()
    top.geometry("300x300")
    global username
    global pin_number

    register_user = Label(top, text="Register")
    register_user.place(x=30, y=0)

    username_label = Label(top, text="Username")
    username_label.place(x=30, y=35)

    username = Entry(top, bd=10, border=5)
    username.place(x=100, y=35)

    opening_balance_label = Label(top, text="Balance")
    opening_balance_label.place(x=30, y=70)

    opening_balance = Entry(top, bd=10, border=5)
    opening_balance.place(x=100, y=70)

    pin_number_label = Label(top, text="Pin Number")
    pin_number_label.place(x=30, y=105)

    pin_number = Entry(top, bd=10, border=5)
    pin_number.place(x=100, y=105)

    def submit():
        #Database 
        connected = sqlite3.connect('romeo_bank.db')
        curs = connected.cursor()

        #Database Table
        curs.execute('INSERT INTO records VALUES (:u_name, :u_balance, :u_pin)',
                {
                    'u_name': username.get(),
                    'u_balance': opening_balance.get(),
                    'u_pin': pin_number.get()
                })

        #Commit changes and close connection
        connected.commit()        
        connected.close()

        username.delete(0, END)
        opening_balance.delete(0, END)
        pin_number.delete(0, END)

    def query():
        #Database
        connected = sqlite3.connect('romeo_bank.db')
        curs = connected.cursor()

        #Database Table
        curs.execute('SELECT *, oid FROM records')
        bank_records = curs.fetchall()
        print(bank_records)

        Output.insert(END, bank_records)

        connected.commit()
        connected.close()

    transaction_details = Button(top, bd=10, border=5, text="Enter Details", command=submit)
    transaction_details.place(x=100, y=140)

    query_details = Button(top, bd=10, border=5, text="Query Details", command=query)
    query_details.place(x=100, y=180)

    Output = Text(top, bd=10, height=5, width=20)
    Output.place(x=100, y=220)


register_btn = Button(root, text="Register", command=registration)
register_btn.place(x=30, y=35)

def login():
    top2 = Toplevel()
    top2.geometry("300x300")

    login_user = Label(top2, text="Login")
    login_user.place(x=30, y=0)

    login_username_label = Label(top2, text="Username")
    login_username_label.place(x=30, y=35)

    login_username = Entry(top2, bd=10, border=5)
    login_username.place(x=100, y=35)

    login_pin_number_label = Label(top2, text="Pin Number")
    login_pin_number_label.place(x=30, y=105)

    login_pin_number = Entry(top2, bd=10, border=5)
    login_pin_number.place(x=100, y=105)

    def validation():
        connected = sqlite3.connect('romeo_bank.db')
        curs = connected.cursor()
        curs.execute('SELECT *, oid FROM records')
        data = curs.fetchall()


        '''
        for w in data:
            p = w[2]
            print(p)

            try:
                if w[2] == login_pin_number.get() and w[0] == login_username.get():
                    y.append(login_pin_number.get())
                    y.append(login_username.get())
                    print("awe!")

                else:
                    print("Try again dude!")
                    

            except ValueError:
                print("Glow in the dark!")
        print(y)
        '''
        y = []
        z = []

        for x in data:
            #c = x[0]
            #b = x[2]
            try:
                if x[0] == login_username.get() and x[2] == login_pin_number.get():                
                    y.append(x[0])
                    z.append(x[2])
                    print("Logged in!")

            except ValueError:
                print("error!")
        
        '''
         p = y+z
        if p == []:
            print("Error!")
        elif y == login_username.get() and  z == login_pin_number.get():
            print("Success!")
        else:
            print("Error!")

        print(y+z)

        
        for x in y:
            try:
                if x == login_pin_number.get() and x == login_username.get():
                    print(x)
                    print("great!")
                    break

                elif x != login_pin_number.get() and x != login_username.get():
                    print(x)
                    break

                else:
                    print("bummer!")
                    break

            except ValueError:
                print("Glow in the dark!")
        
        username_entry = []
        password_entry = []

        
        for x in y:
            username_entry.append(x)            
            password_entry.append(x)
 
            try:
                if x == login_pin_number.get() and x == login_username.get():
                    print("This is it!!!")
                    print(y)
                    

                else:
                    print("Try again!!!")
                    print(x)
                
            
            except ValueError:
                print("Syntax Error!!!")
        print(y)

        print(username_entry)
        print(password_entry)
        '''


        

        

        connected.commit()
        connected.close()

    login_submit = Button(top2, text="Login Submit", command=validation)
    login_submit.place(x=100, y=160)

login_btn = Button(root, text="Login", command=login)
login_btn.place(x=30, y=70)

root.mainloop()
