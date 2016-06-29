''' written by: Gustavo A. Maturana
    written on: May 14, 2016
    filename: calculator1.py
'''
import tkinter as Tr
import tkinter.messagebox


import database_ as db

import texttable as tbl
import sqlite3 as sql
from test.sortperf import tabulate


#import mysql
#from mysql.connector import error_code

class calculator1:
    
    DB_NAME = 'patient'

    def __init__(self, title):
    
        # Create the main window Widget
        # Main application page
        
        self.root = Tr.Tk()                         # creates a main application window
        self.root.title(title)                      # application window title
        self.root.minsize(width=666, height=666)    # application window size
        self.frame_1 = tkinter.Frame(self.root)
        self.frame_2 = tkinter.Frame(self.root)
        self.frame_3 = tkinter.Frame(self.root)
        
        
        self.btn_click = tkinter.Button(self.frame_1, \
                                       text  = 'Press Me', command = self.ok_message)
        self.btn_close = tkinter.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.destroy)
        self.keyLabel = Tr.Entry(self.frame_1, \
                                        width = 4)
        self.nameLabel = Tr.Entry(self.frame_1, \
                                        width = 10)
        self.ageLabel = Tr.Entry(self.frame_1, \
                                        width = 4)
        self.blooSugarLabel = Tr.Entry(self.frame_1, \
                                        width = 10)
        
        self.recordList = Tr.Listbox(self.frame_1, height=4, width= 50)

        self.recordList.pack(side = 'bottom')
        
        self.btn_click.pack(side = 'left')
        self.btn_close.pack(side = 'left')
        self.keyLabel.pack(side = 'left')
        self.nameLabel.pack(side = 'left')
        self.ageLabel.pack(side = 'left')
        self.blooSugarLabel.pack(side = 'left')
        self.keyLabel.pack(side = 'left')
        #self.databse()
        db.database_().databse()
        #inserting values into the record list
        self.recordList.tk_menuBar()
        cnt = 0
        for result in db.database_().db_print('patient.db'):
            self.recordList.insert(cnt,result)
            ++cnt
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack(side = 'top')
        
        tkinter.mainloop()
        
        
    def databse(self):
        # Create a database to store blood sugar levels of patient
        # This needs some implementation 
        table = sql.connect('patient.db')
        cursor = table.cursor()
        #cursor.execute('CREATE DATABASE patient')
        self.testvalue = ''
        
        # CREATES TABLE IF DOES NOT EXIST
        cursor.execute('''CREATE TABLE IF NOT EXISTS PATIENT (
                           ID INT PRIMARY         KEY    NOT NULL,
                           NAME                   TEXT    NOT NULL,
                           AGE                    INT     NOT NULL,
                           BLOOD SUGAR LEVEL      INT     NOT NULL,
                           TIME                   INT     NOT NULL,
                           DATE                   TEXT    NOT NULL);''')

        # print database
        values = cursor.fetchall()
        for row in values:
            self.testvalue += row + '\n'

        self.frame_3 = Tr.Frame(self.root)
        self.label_2 = tkinter.Label(self.frame_1, \
                                    text = self.testvalue)
        
        self.label_2.pack(side = 'right')
        #self.insert_data(table)
        
        
        table.close()
        
    def insert_data(self, table):
        #insert items into table
        for i in [(1,'Gustavo Maturana', 36, 'May 6'),
                  (2,'Javier  Maturana', 33, 'May 7')]:
            table.execute('INSERT INTO PATIENT VALUES (?,?,?,?)', i)
            table.commit()
        for i in [(3,'Gustavo Maturana', 36, 'May 6'),
                  (4,'Javier  Maturana', 33, 'May 7')]:
            table.execute('INSERT INTO PATIENT VALUES (?,?,?,?)', i)
            table.commit()
        
    def db_print(self):
        # prints information stored in the database
        print('Implementation needed')
                
    def ok_message(self):
        # General Message
        self.lable_1 = tkinter.Label(self.frame_1, \
                                    text = 'Thank you for pressing me!')
        self.lable_1.pack(side = 'right')
        self.graph_()               # calls out the graph function after button is pressed
        self.databse()           # calls out for the creation of the database
    
    def destroy_root(self):
        # destroys main window
        self.root.destroy()
    
    def error_message(self, choice):
        # Error message codes
        if choice == 1:
            tkinter.messagebox.showinfo('Error 1', 'Please enter a blood sugar level value')
        if choice == 2:
            tkinter.messagebox.showinfo('Error 2', 'Blood sugar level is too high')
        if choice == 3:
            tkinter.messagebox.showinfo('Error 3', 'Blood sugar level is too low')
        if choice == 4:
            tkinter.messagebox.showinfo('Error 4', 'To be implemented')
    
    def graph_(self):
        # Graph sugar level vs time
        # This section has not been implemented
        title = 'Sugar Level Vs. Time'
        output_txt = tbl.Texttable()
        
        output_txt.add_row(['Gus', 36]) 
        output_txt.add_row(['Xavier', 33])
        
        self.graph_window = Tr.Tk()                     # creates a new window
        self.graph_window.minsize(400, 300)
        self.graph_window.title(title)
        self.frame_1 = tkinter.Frame(self.graph_window) # frame to enclose the button
        self.frame_2 = tkinter.Frame(self.graph_window)
        
        # Creates a close button
        self.close_btn = Tr.Button(self.frame_1, \
                                        text = 'Close', command = self.close_window)
        self.output_lbl = Tr.Label(self.frame_2, \
                                        text = output_txt.draw())
    
        self.close_btn.pack(side = 'left')
        self.output_lbl.pack(side = 'right')
        self.frame_1.pack(side = 'bottom')
        self.frame_2.pack(side = 'top')
        print(output_txt.draw())
        
        
    def close_window(self):
        
        self.graph_window.destroy()
        # after the graph is destroyed it cannot be recreated
        # needs to fix this par
        
        
#myGuid = calculator1('BLOOD SUGAR LEVEL')
    