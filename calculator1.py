''' written by: Gustavo A. Maturana
    written on: May 14, 2016
    filename: calculator1.py
'''
import Tkinter as Tr
import database_ as db
import errors_ as ers
from asyncio.locks import Event


#import mysql
#from mysql.connector import error_code

class calculator1:
    
    DB_NAME = 'patient'
    

    def __init__(self, title):
    
        # Create the main window Widget
        # Main application page
        
        self.root = Tr.Tk()                         # creates a main application window
        self.root.title(title)                      # application window title
        self.root.minsize(width=666, height=400)    # application window size
        self.frame_1 = Tr.Frame(self.root)
        self.frame_2 = Tr.Frame(self.root)
        self.frame_3 = Tr.Frame(self.root)
        self.frame_4 = Tr.Frame(self.root)
        
        
        self.btn_click = Tr.Button(self.frame_1, \
                                       text  = 'NEW PATIENT', command = self.new_patient_win)
        self.btn_close = Tr.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.quit)
        
        self.recordList = Tr.Listbox(self.frame_4, height=8, width= 50)
        
        self.patientLbl = Tr.Label(self.frame_4, text = 'PATIENT LIST')
        self.recordList.bind("<Double-Button-1>", self.OnDouble)
        self.recordList.pack(side = 'bottom')
        self.patientLbl.pack(side = 'top')
        
        self.btn_click.pack(side = 'bottom')
        self.btn_close.pack(side = 'right')

        # Creates database if it does not exist or open database to connect to it
        db.database_().databse()
        #inserting values into the record list
        self.recordList.tk_menuBar()
        cnt = 0
        for result in db.database_().db_print('patient.db'):
            self.recordList.insert(cnt,result)
            ++cnt
        self.frame_1.pack(side = 'top')
        self.frame_2.pack(side = 'bottom')
        self.frame_3.pack(side = 'bottom')
        self.frame_4.pack(side = 'bottom')
        
        
        Tr.mainloop()
                
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
    
    def new_patient_win(self):
        # This section creates a new patient
        title = 'NEW PATIENT'
        
        self.new_patient_window = Tr.Tk()                     # creates a new window
        self.new_patient_window.minsize(400, 300)
        self.new_patient_window.title(title)
        self.frame1 = Tr.Frame(self.new_patient_window, height = 100)
        self.frame2 = Tr.Frame(self.new_patient_window, width = 100)
        self.frame3 = Tr.Frame(self.new_patient_window, width = 100)
        self.frame4 = Tr.Frame(self.new_patient_window, width = 100)
        self.frame5 = Tr.Frame(self.new_patient_window)
        self.frame6 = Tr.Frame(self.new_patient_window)
        
        
        # Creates a close button
        self.save_btn = Tr.Button(self.frame1, \
                                        text = 'SAVE', command = self.save_record)
        self.cancel_btn = Tr.Button(self.frame1, \
                                        text = 'CANCEL', command = self.cancel_)
        
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
            
        db.database_().insert_record_patient('patient.db', (id_, name_, age_, bday_))
        self.clear_()
    
    def clear_(self):
        
        self.keyEntry.delete(0, Tr.END)
        self.nameEntry.delete(0, Tr.END)
        self.ageEntry.delete(0, Tr.END)
        self.bdayEntry.delete(0, Tr.END)
        self.nameEntry.focus()
    
    def cancel_(self):
        self.new_patient_window.destroy()
        
    def disable_button_(self):
        
        if self.keyEntry.get() == '' or self.nameEntry.get() == '' \
                or self.ageEntry.get() == '' or self.bdayEntry.get() == '':
            self.save_btn(sate = 'DISABLE')
        
        else:
            self.save_btn(sate = 'ENABLE')
    
    #functions generates a new window when there is a double click on patient
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print ("selection:", selection, ": '%s'" % value)
        self.new_patient_win()
    
            
        
        
#myGuid = calculator1('BLOOD SUGAR LEVEL')
    
