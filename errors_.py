'''
Created on Jun 27, 2016

@author: gmaturan
'''

import tkinter as tk

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
            tk.messagebox.showinfo('Error 4:', 'To be implemented')
        if choice == 5:
            tk.messagebox.showinfo('Error 5:', 'UNABLE TO FETCH DATA')
    
    def hints(self, choice):
        
        if choice == 1:
            tk.messagebox.showinfo("Hint 1:", 'Enter a correct value')
        if choice == 2:
            tk.messagebox.showinfo("Hint 2:", 'Enter a numerical value')
            
            
#End of Class