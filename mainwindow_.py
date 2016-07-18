'''
Created on Jun 22, 2016

@author: gmaturan
'''

import calculator1 as cal
import intro_ as intro

def main():
    
    #introduction only last 10 seconds
    intro.intro_().flash_screen()
    cal.calculator1('Blood Sugar Level') 
    
#call main function
main()
