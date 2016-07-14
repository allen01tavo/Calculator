'''
Created on Jun 25, 2016

@author: gmaturan
'''

import Tkinter as tr
import texttable as tbl

class graph_:
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def graph(self):
        # Graph sugar level vs time
        # This section has not been implemented
        title = 'Sugar Level Vs. Time'
        output_txt = tbl.Texttable()
    
        output_txt.add_row(['Gus', 36]) 
        output_txt.add_row(['Xavier', 33])
    
        self.graph_window = tr.Tk()                     # creates a new window
        self.graph_window.minsize(400, 300)
        self.graph_window.title(title)
        self.frame_1 = tr.Frame(self.graph_window) # frame to enclose the button
        self.frame_2 = tr.Frame(self.graph_window)
    
        # Creates a close button
        self.close_btn = tr.Button(self.frame_1, \
                                    text = 'Close', command = self.close_window)
        self.output_lbl = tr.Label(self.frame_2, \
                                    text = output_txt.draw())

        self.close_btn.pack(side = 'left')
        self.output_lbl.pack(side = 'right')
        self.frame_1.pack(side = 'bottom')
        self.frame_2.pack(side = 'top')
        print(output_txt.draw())
        
    def daily_graph(self):
        # Implementation needed
        print('Implementation needed')
        
    def weekly_graph(self):
        # Implementation needed
        print('Implementation needed')
        
    def monlty_graph(self):
        # Implementation needed
        print('Implemenation needed')
        