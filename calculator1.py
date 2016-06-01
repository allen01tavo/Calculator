''' written by: Gustavo A. Maturana
    written on: May 14, 2016
    filename: calculator1.py
'''
import tkinter as Tr
import tkinter.messagebox

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
        self.frame_1 = tkinter.Frame(self.root)
        self.frame_2 = tkinter.Frame(self.root)
        
        self.btn_click = tkinter.Button(self.frame_1, \
                                       text  = 'Press Me', command = self.ok_message)
        self.btn_close = tkinter.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.destroy)

        self.btn_click.pack(side = 'left')
        self.btn_close.pack(side = 'left')
        self.databse()
        self.frame_1.pack()
        self.frame_2.pack(side = 'bottom')
        
        tkinter.mainloop()
        
        
    def databse(self):
        # Create a database to store blood sugar levels of patient
        # This needs some implementation 
        table = sql.connect('patient.db')
        cursor = table.cursor()
        self.testvalue = ''
        
        # CREATES TABLE IF DOES NOT EXIST
        table.execute('''CREATE TABLE IF NOT EXISTS PATIENT (
                           ID INT PRIMARY         KEY     NOT NULL,
                           NAME                   TEXT    NOT NULL,
                           AGE                    INT     NOT NULL,
                           BLOOD SUGAR LEVEL      INT     NOT NULL,
                           TIME                   INT     NOT NULL,
                           DATE                   TEXT    NOT NULL);''')

        self.root.title('Success')      # for testing only
        # print database
        values = cursor.fetchall()
        for row in values:
            self.testvalue += row + '\n'

        self.frame_3 = Tr.Frame(self.root)
        self.label_2 = tkinter.Label(self.frame_1, \
                                    text = self.testvalue)
        
        self.label_2.pack(side = 'right')
        
        
        table.close()
        
    def insert_data(self, table):
        #insert items into table
        for i in [('Gustavo Maturana', 36, 95, 80, 'May 6'),
                  ('Javier  Maturana', 33, 95, 100, 'May 7')]:
            table.execute('INSERT INTO PATIENT VALUES (?,?,?,?,?)', i)
            table.commit()
        for i in [('Gustavo Maturana', 36, 95, 80, 'May 6'),
                  ('Javier  Maturana', 33, 95, 100, 'May 7')]:
            table.execute('INSERT INTO PATIENT VALUES (?,?,?,?,?)', i)
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
        self.graph_window = Tr.Tk()                     # creates a new window
        self.graph_window.minsize(400, 300)
        self.graph_window.title(title)
        self.frame_1 = tkinter.Frame(self.graph_window) # frame to enclose the button
        
        # Creates a close button
        self.close_btn = Tr.Button(self.frame_1, \
                                       text  = 'Close', command = self.close_window)
    
        self.close_btn.pack(side = 'left')
        self.frame_1.pack(side = 'bottom')
        
        
    def close_window(self):
        
        self.graph_window.destroy()
        # after the graph is destroyed it cannot be recreated
        # needs to fix this par
        
        
myGuid = calculator1('BLOOD SUGAR LEVELS')
    