
# MODULES

# TYPES OF IMPORT METHODS

# import math - math la irukure functions ah import pannum
# from math import pow, sin - math la enna venumo adhu matum select panni import panni use panikalam
# from math import * - math la irukure ella function um varum
# import math as m - alias- function name ah short ah customise panikalam
# import calendar as cl

# import math as m
# print(m.sqrt(22)) - square root
# print(m.pow(4,2)) - power
# print(m.ceil(23.1)) - decimal ku aprm .1 irundhalum increase panidum
# print(m.floor(23.9)) - decimal ku aprm enna irundhalum adhu remove panidum
# print(m.radians(60)) - degree ah radians ah mathum
# print(m.degrees(1.0471975511965976)) - radians ah degree ah mathum
# print(m.factorial(5))
# print(m.pi)
# lis = [2,3,4,8,9]
# print(m.prod(lis)) - list kulla irukuradhu elame multiply pannidum
# print(m.remainder(5,2)) - remainder eduthu kudukum

# from os import *

# print("current working directory", getcwd()) - dirctory oda current path ah katum

# try:
#     print("before---->",getcwd())
#     chdir('/Users')
#     chdir('Honest-Raj')
#     print('after---->',getcwd())
# except Exception as e:
#     print('error:',e)
# file path change pandradhuku use agum - forward backward panalam file name ah potu

# import os
# make directory - mkdir - pudhusa file create panum
# direct ah terminal la kuda potu create panalam
# print("dir--->",os.getcwd())
#os.mkdir('os testing')

# remove directory - file ah delete panidum
# os.rmdir('jerry')

# path la irukure file ah delete pandradhuku use agum
# direct ah file ah delete panna mudiyadhu so path ah join panitu dhan delete panna mudiyum
# path ah select panitu last la file name kudukanum
# finalpath = os.path.join(os.getcwd(), 'random.txt')
# print('final path', finalpath)
# os.remove(finalpath)

# ---------------------------------------------------------------------------------

# THREADING

# threading.thread - to create a new threading
# start - to start a new thread
# join - to end a thread
# is_alive function - to check the thread is alive
# threading.enumerate() function - to get all active threads


# MULTI THREADING

# Multi threading is a ability of a program or an operating system to enable more than one task at a time
# or without requiring multiple copies of a program running on a computer.

# Multi treading can also handle various request from the same user.

# Multi threading is a way of achieving multi tasking.

# In Multi threading, the concept of threads is used.
# Threads are the smallest units of execution within a program.

# ADVANTAGES OF THREADS:

# Improved performance
# Responsiveness
# Simplified programming





# import threading

# def func1(num):
#     for i in range(num):
#         print("ii----------",i)

# def func2(num1,num2):
#     for j in range(num1,num2):
#         print("---------jj--------",j)


# thread1 = threading.Thread(target=func1, args=(10,))
# thread2 = threading.Thread(target=func2, args=(10,23))


# thread1.start()
# thread2.start()

# print("This is testing")

# thread1.join()
# thread2.join()

# print("-------------------------------------")



# import tkinter as tk
# from tkinter.messagebox import showinfo, showerror

# window = tk.Tk()
# window.geometry("500x500")


# title  = tk.Label(window, text="This is user registration").pack()


# userName = tk.StringVar()
# age = tk.IntVar()
# email = tk.StringVar()


# usernameField = tk.Entry(window, textvariable=userName ).pack()
# ageField = tk.Entry(window, textvariable=age ).pack()
# emailField = tk.Entry(window, textvariable=email).pack()

# users = []
# def buttonClick():
#     try:
#         dict = {}
#         dict['username'] = userName.get()
#         dict['email'] = email.get()
        
#         dict['age'] = age.get()
#         users.append(dict)
#         showinfo(
#                 title="Success Message",
#                 message=f"User added successfully {userName.get()}"
#         )
#         print(users)
        
#     except Exception as e:
#         showerror(
#             title="Something error happend",
#             message=f"Error : {e}"
#         )
# button = tk.Button(window, text="Add User", command=buttonClick).pack()


# window.mainloop()




import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import sqlite3
import os
print(os.getcwd())


db_connection = sqlite3.connect("Python Database.db")


window = tk.Tk()
window.geometry("500x500")


title  = tk.Label(window, text="This is user registration").pack()


userName = tk.StringVar()
age = tk.IntVar()
email = tk.StringVar()


usernameField = tk.Entry(window, textvariable=userName ).pack()
ageField = tk.Entry(window, textvariable=age ).pack()
emailField = tk.Entry(window, textvariable=email).pack()


def buttonClick():
    try:
        cursorconnect = db_connection.cursor()
        cursorconnect.execute('Insert into Users("Name","Age","Email") Values (?,?,?)',(userName.get(),age.get(),email.get()))
        data = list(cursorconnect.execute('select * from Users'))
        print("data",data)
        db_connection.commit()
        showinfo(
            title = "",
            message = "User details added successfully"

        )
 

    except Exception as e:
        showerror(
            title="Something error happend",
            message=f"Error : {e}"
        )
button = tk.Button(window, text="Add User", command=buttonClick).pack()


window.mainloop()













#--------------------------------------------------------

# SQL Database - Structured Query Language

# Data will be stored in table structure
# Accessing Using Queries
# SQL -
# SQLlite - Mini version and less storage
# Postgresql - Big level database

# NO SQL Database - Non Structured Query Language

# Accessing Using some Functions
# Data will be stored as collection
#     {
#         "name" = "Suresh",
#         "age" = 23,
#         "email"= "suresh@gmail.com"

#     }
# Mongodb