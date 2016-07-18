'''
Created on Jun 27, 2016

@author: gmaturan
'''


import tkinter as tk
from tkinter import messagebox
#import Tkinter as tk


class errors_:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def error_messages(self, choice):
        
        if choice == 1:
            tk.messagebox.showinfo('Error 1:', 'Please enter a blood sugar level value')
        if choice == 2:
            tk.messagebox.showinfo('Error 2:', 'Blood sugar level is too high')
        if choice == 3:
            tk.messagebox.showinfo('Error 3:', 'Blood sugar level is too low')
        if choice == 4:
            tk.messagebox.showinfo('Error 4:', 'There is not value')
        if choice == 5:
            tk.messagebox.showinfo('Error 5:', 'UNABLE TO FETCH DATA')
    
    def hints(self, choice):
        
        if choice == 1:
            tk.messagebox.showinfo("Hint 1:", 'Enter a correct value')
        if choice == 2:
            tk.messagebox.showinfo("Hint 2:", 'Enter a numerical value')
    
    # specific messages
    def general_error_messages(self, st):
        
        message = 'Please enter a value for: ' + st
        tk.messagebox.showinfo('Missing Information', message)
    
    # delete message
    def delete_message(self, st):
        message = 'Patient name: ' + st + ' has been deleted!'
        tk.messagebox.showinfo('Deletion Confirmation', message)
    
    def delete_confirmation(self, st):
        result = tk.messagebox.askyesno('Confirm Deletion', st)
        
        return result
            
#End of Class
