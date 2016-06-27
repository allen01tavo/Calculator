'''
Created on Jun 27, 2016

@author: gmaturan
'''

import tkinter as tk

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def error_messages(self, choice):
        
        if choice == 1:
            tk.messagebox.showinfo('Error 1', 'Please enter a blood sugar level value')
        if choice == 2:
            tk.messagebox.showinfo('Error 2', 'Blood sugar level is too high')
        if choice == 3:
            tk.messagebox.showinfo('Error 3', 'Blood sugar level is too low')
        if choice == 4:
            tk.messagebox.showinfo('Error 4', 'To be implemented')
        if choice == 5:
            tk.messagebox.showinfo('Error: unable to fecth data')