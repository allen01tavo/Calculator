''' written by: Gustavo A. Maturana
    written on: May 14, 2016
    filename: calculator1.py
'''

import tkinter as Tr
#import Tkiter as Tr

from tkinter import ttk

import database_ as db
import errors_ as ers


class calculator1:
    
    DB_NAME = 'patient'

    def __init__(self, title):
    
        # Create the main window Widget
        # Main application page
        self.dataCols = ('PATIENT ID', 'NAME', 'AGE', 'DATE OF BIRTH')
        
        self.root = Tr.Tk()                         # creates a main application window
        self.root.title(title)                      # application window title
        self.root.minsize(width=666, height=300)    # application window size
        self.frame_1 = Tr.Frame(self.root)
        self.frame_2 = Tr.Frame(self.root)
        self.frame_3 = Tr.Frame(self.root)
        self.frame_4 = Tr.Frame(self.root)
        
        self.btn_click = Tr.Button(self.frame_1, \
                                       text  = 'NEW PATIENT', command = self.new_patient_win)
        self.btn_close = Tr.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.quit)
        
        self.recordListColumn = ttk.Treeview(self.frame_4,columns = self.dataCols, show = 'headings')
        
        self.patientLbl = Tr.Label(self.frame_4, text = 'PATIENT LIST')
        self.recordListColumn.bind("<Double-Button-1>", self.OnClick)
        
        self.patientLbl.pack(side = 'top')
        self.recordListColumn.pack(side = 'top')
        
        self.btn_click.pack(side = 'bottom')
        self.btn_close.pack(side = 'right')

        # Creates database if it does not exist or open database to connect to it
        db.database_().databse()
        #inserting values into the record list
        for item in db.database_().db_print('patient.db'):
            self.recordListColumn.insert('', 'end', values=item)
            
        # the following lines add the name to the title to the columns
        for col in self.dataCols:
            self.recordListColumn.heading(col, text = col.title())
            
        self.frame_1.pack(side = 'top')
        self.frame_2.pack(side = 'bottom')
        self.frame_3.pack(side = 'bottom')
        self.frame_4.pack(side = 'bottom')
        
        Tr.mainloop()
    
    # General Message            
    def ok_message(self):
        
        self.lable_1 = Tr.Label(self.frame_1, \
                                    text = 'Thank you for pressing me!')
        self.lable_1.pack(side = 'right')
        self.graph_()               # calls out the graph function after button is pressed
        self.databse()           # calls out for the creation of the database
    
    # destroys main window
    def destroy_root(self):
        
        self.root.destroy()
    
    # This module creates a new patient
    def new_patient_win(self):
        
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
        
        # Creates a save and close button
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

        # setting up frames and buttons
        self.save_btn.pack(side = 'right')
        self.cancel_btn.pack(side = 'left')
        self.frame1.pack(side = 'bottom')
        self.frame2.pack(side = 'top')
        self.frame3.pack(side = 'top')
        self.frame4.pack(side = 'top')
        self.frame5.pack(side = 'top')
        self.frame6.pack(side = 'top')
        
        #focus the curser to the Patient ID entry
        self.keyEntry.focus()
        
    # This is section creates the edit window for the patient record
    def editPatient(self, key):
        # the patient name will be displayed on window title
        title = db.database_().get_record('patient.db', key)
        
        self.edit_patient_window = Tr.Tk()                     # creates a new window
        self.edit_patient_window.minsize(500, 400)
        self.edit_patient_window.title(title)
        self.frame1 = Tr.Frame(self.edit_patient_window, height = 100)
        self.frame2 = Tr.Frame(self.edit_patient_window, width = 100)
        self.frame3 = Tr.Frame(self.edit_patient_window, width = 100)
        self.frame4 = Tr.Frame(self.edit_patient_window, width = 100)
        self.frame5 = Tr.Frame(self.edit_patient_window)
        self.frame6 = Tr.Frame(self.edit_patient_window)
        self.frame7 = Tr.Frame(self.edit_patient_window)
        
        #store the value for the specific record that has been clicked
        record_ = db.database_().get_patient('patient.db', key)
        
        # Creates save, cancel and delete buttons
        self.edit_save_btn = Tr.Button(self.frame1, \
                                        text = 'SAVE EDIT', command = self.save_edit)
        self.edit_cancel_btn = Tr.Button(self.frame1, \
                                        text = 'CANCEL EDIT', command = self.cancel_edit)
        self.edit_delete_btn = Tr.Button(self.frame1, \
                                        text = 'DELETE', command = self.delete_patient)
        self.bsugarLevel_btn = Tr.Button(self.frame7, \
                                         text = 'Enter Blood Sugar level', command = self.blood_sugar_level)
        self.view_data_btn = Tr.Button(self.frame7, \
                                         text = 'View Data', command = self.cancel_edit)
        self.edit_keyLbl = Tr.Label(self.frame3, \
                                        text = 'PATIENT ID #:', width = 25, justify='left')
        self.edit_keyLbl.pack(side = 'left')
        self.edit_keyEntry = Tr.Label(self.frame3, \
                                        text = record_[0], width = 10,  )
        
        self.edit_nameLbl = Tr.Label(self.frame4, \
                                        text = 'NAME:         ', width = 15, justify='right')
        self.edit_nameLbl.pack(side = 'left')
        self.edit_nameEntry = Tr.Entry(self.frame4, \
                                        width = 20)
        self.edit_nameEntry.insert('end', record_[1])
        
        self.edit_ageLbl = Tr.Label(self.frame5, \
                                        text = 'AGE:                           ', width = 31, justify='right', fg = 'red')
        self.edit_ageLbl.pack(side = 'left')
        self.edit_ageEntry = Tr.Entry(self.frame5, \
                                        width = 4)
        self.edit_ageEntry.insert('end', record_[2])
        
        self.edit_bdayLbl = Tr.Label(self.frame6, \
                                        text = 'BIRTHDAY:', width = 15, justify='left')
        self.edit_bdayLbl.pack(side = 'left')
        self.edit_bdayEntry = Tr.Entry(self.frame6, \
                                        width = 20)
        self.edit_bdayEntry.insert('end', record_[3])
        
        self.edit_keyEntry.pack(side = 'right')
        self.edit_nameEntry.pack(side = 'right')
        self.edit_ageEntry.pack(side = 'right')
        self.edit_bdayEntry.pack(side = 'right')
        self.view_data_btn.pack(side = 'top')

        # Setup the buttons and frames
        self.edit_save_btn.pack(side = 'right')
        self.edit_cancel_btn.pack(side = 'left')
        self.edit_delete_btn.pack(side = 'left')
        self.bsugarLevel_btn.pack(side = 'top')
        self.frame1.pack(side = 'bottom')
        self.frame2.pack(side = 'top')
        self.frame3.pack(side = 'top')
        self.frame4.pack(side = 'top')
        self.frame5.pack(side = 'top')
        self.frame6.pack(side = 'top')
        self.frame7.pack(side = 'bottom')

    # The following function saves the records to the database
    # The function also checks that none of the Entries are empty or null   
    def save_record(self):
            
        if  self.keyEntry.get() == '' or  self.nameEntry.get() == '' or \
            self.ageEntry.get() == '' or self.bdayEntry.get() == '': 
            if self.nameEntry.get() == '':
                ers.errors_().general_error_messages('NAME')
                self.nameLbl.set('NAME:', fg = 'red')
            if self.ageEntry.get() == '':
                ers.errors_().general_error_messages('AGE')
            if self.bdayEntry.get() == '':
                ers.errors_().general_error_messages('BIRTHDAY') 
        else:
            id_ = int(self.keyEntry.get())
            name_ = self.nameEntry.get()
            age_ = int(self.ageEntry.get())
            bday_ = self.bdayEntry.get()
            db.database_().insert_record_patient('patient.db', (id_, name_, age_, bday_))
            self.clear_()
        
    # Clear all Entries and focus on nameEntry
    def clear_(self):
        
        self.keyEntry.delete(0, Tr.END)
        self.nameEntry.delete(0, Tr.END)
        self.ageEntry.delete(0, Tr.END)
        self.bdayEntry.delete(0, Tr.END)
        self.nameEntry.focus()
    
    # Cancels the new new_patient_win
    def cancel_(self):
        # Destroys the new_patient_window
        self.new_patient_window.destroy()
    
    # Deletes patient record    
    def delete_patient(self):
        
        name_ = self.edit_nameEntry.get()
        
        result = ers.errors_().delete_confirmation('test')
        
        if result == True:
            
            db.database_().remove_record('patient.db', name_)
            st = 'Patient name: ' + name_ + ' has been deleted'
            ers.errors_().delete_message(st)
            # Destroys the window
            self.edit_patient_window.destroy()    
        else:
            self.edit_nameEntry.focus()
    
    # Cancel the edit
    def cancel_edit(self):
        # Destroys the edit_patient_window
        self.edit_patient_window.destroy()
    
    def save_edit(self):
        # Saves the edit record
        print('Implementation needed')
        
    # OnClick opens a new window when a record in the patient list is clicked 
    def OnClick(self, event):
        
        selection = self.recordListColumn.focus()
        value = self.recordListColumn.item(selection).get('values')
        # Opens the edit patient window
        # and passes the patient id#
        self.editPatient(value[0])
        
    # Creates a separate table with the patient ID
    def blood_sugar_level(self):
        
        selection = self.recordListColumn.focus()
        value = self.recordListColumn.item(selection).get('values')
        # value[0] is the Patient ID. value[0] must be a string
        # Creates a new table for the specific patient
        db_name = 'patient' + str(value[0]) + '.db'
        db.database_().databse_patient(db_name)
            
                
#myGuid = calculator1('BLOOD SUGAR LEVEL')
    
