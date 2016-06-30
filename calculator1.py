''' written by: Gustavo A. Maturana
    written on: May 14, 2016
    filename: calculator1.py
'''
import tkinter as Tr
import database_ as db

import texttable as tbl
import sqlite3 as sql



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
        self.frame_1 = Tr.Frame(self.root)
        self.frame_2 = Tr.Frame(self.root)

        self.frame_7 = Tr.Frame(self.root)
        self.frame_8 = Tr.Frame(self.root)
        
        
        self.btn_click = Tr.Button(self.frame_1, \
                                       text  = 'NEW PATIENT', command = self.new_patient)
        self.btn_close = Tr.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.destroy)
        

        
        self.recordList = Tr.Listbox(self.frame_8, height=4, width= 50)
        self.patientLbl = Tr.Label(self.frame_8, text = 'PATIENT LIST')

        self.recordList.pack(side = 'bottom')
        self.patientLbl.pack(side = 'top')
        
        self.btn_click.pack(side = 'bottom')
        self.btn_close.pack(side = 'right')

        #self.databse()
        db.database_().databse()
        #inserting values into the record list
        self.recordList.tk_menuBar()
        cnt = 0
        for result in db.database_().db_print('patient.db'):
            self.recordList.insert(cnt,result)
            ++cnt
        self.frame_1.pack(side = 'top')
        self.frame_2.pack(side = 'bottom')
        self.frame_7.pack(side = 'bottom')
        self.frame_8.pack(side = 'bottom')
        
        Tr.mainloop()
        
        
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
        self.label_2 = Tr.Label(self.frame_1, \
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
        self.lable_1 = Tr.Label(self.frame_1, \
                                    text = 'Thank you for pressing me!')
        self.lable_1.pack(side = 'right')
        self.graph_()               # calls out the graph function after button is pressed
        self.databse()           # calls out for the creation of the database
    
    def destroy_root(self):
        # destroys main window
        self.root.destroy()
                
    def close_window(self):
        
        self.graph_window.destroy()
        # after the graph is destroyed it cannot be recreated
        # needs to fix this par
    
    def new_patient(self):
        # This section creates a new patient
        title = 'NEW PATIENT'
        
        self.new_patient_window = Tr.Tk()                     # creates a new window
        self.new_patient_window.minsize(400, 300)
        self.new_patient_window.title(title)
        self.frame1 = Tr.Frame(self.new_patient_window)
        self.frame2 = Tr.Frame(self.new_patient_window)
        self.frame3 = Tr.Frame(self.new_patient_window)
        self.frame4 = Tr.Frame(self.new_patient_window)
        self.frame5 = Tr.Frame(self.new_patient_window)
        self.frame6 = Tr.Frame(self.new_patient_window)
        
        
        # Creates a close button
        self.save_btn = Tr.Button(self.frame1, \
                                        text = 'SAVE', command = self.save_record)
        self.cancel_btn = Tr.Button(self.frame1, \
                                        text = 'CANCEL', command = self.close_window)
        
        self.keyLbl = Tr.Label(self.frame3, \
                                        text = 'ENTRY #:     ')
        self.keyLbl.pack(side = 'left')
        self.keyEntry = Tr.Entry(self.frame3, \
                                        width = 4)
        
        
        self.nameLbl = Tr.Label(self.frame4, \
                                        text = 'NAME:        ')
        self.nameLbl.pack(side = 'left')
        self.nameEntry = Tr.Entry(self.frame4, \
                                        width = 10)
        
        self.ageLbl = Tr.Label(self.frame5, \
                                        text = 'AGE:        ')
        self.ageLbl.pack(side = 'left')
        self.ageEntry = Tr.Entry(self.frame5, \
                                        width = 4)
        
        self.bdayLbl = Tr.Label(self.frame6, \
                                        text = 'Birtdhay:    ')
        self.bdayLbl.pack(side = 'left')
        self.bdayEntry = Tr.Entry(self.frame6, \
                                        width = 10)
        
        self.keyEntry.pack(side = 'right')
        self.nameEntry.pack(side = 'right')
        self.ageEntry.pack(side = 'right')
        self.bdayEntry.pack(side = 'right')

    
        self.save_btn.pack(side = 'right')
        self.cancel_btn.pack(side = 'left')
        self.frame1.pack(side = 'bottom')
        self.frame2.pack(side = 'top')
        self.frame3.pack(side = 'top')
        self.frame4.pack(side = 'top')
        self.frame5.pack(side = 'top')
        self.frame6.pack(side = 'top')
        
    def save_record(self):
        # saves record into database
        id_ = int(self.keyEntry.get())
        name_ = self.nameEntry.get()
        age_ = int(self.ageEntry.get())
        bday_ = self.bdayEntry.get()
        
        #record_ = '('+id_ + ',' + name_ + ',' + age_ + ',' + blSugar_ + ')'
        table = sql.connect('patient.db')
        cursor = table.cursor()
        cursor.execute('INSERT INTO PATIENT VALUES (?,?,?,?)', (id_, name_, age_,bday_))
        table.commit()
        
        
        
#myGuid = calculator1('BLOOD SUGAR LEVEL')
    