'''
Created on Jun 23, 2016
filename: database_.py

@author: gmaturan
'''

import sqlite3 as sql
import errors_ as ers


class database_:
    
    DB_NAME = 'patient.db'
    
    def __init__(self):
        
        '''
        '''
        
    def databse(self, db_name = DB_NAME):
        # Create a database to store blood sugar levels of patient
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        # CREATES TABLE IF DOES NOT EXIST
        cursor.execute('''CREATE TABLE IF NOT EXISTS PATIENT (
                           ID                     KEY     NOT NULL,
                           NAME                   TEXT    NOT NULL,
                           AGE                    INT     NOT NULL,
                           BIRTHDAY               TEXT    NOT NULL);''')
        table.commit()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS BLSUGGAR (
                           ID_KEY_PRIMARY         KEY     NOT NULL,
                           BLOOD SUGAR LEVEL      INT     NOT NULL,
                           TIME                   INT     NOT NULL,
                           DATE                   TEXT    NOT NULL);''')
        table.commit()
        
        # The two tables must be join in order to create a better database
        # This part needs implementation
        
        table.close()
        
    def databse_patient(self, db_name):
        # Create a database to store blood sugar levels of patient
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        # CREATES TABLE IF DOES NOT EXIST        
        cursor.execute('''CREATE TABLE IF NOT EXISTS BLSUGGAR (
                           ID_KEY_PRIMARY         KEY     NOT NULL,
                           BLOOD SUGAR LEVEL      INT     NOT NULL,
                           TIME                   INT     NOT NULL,
                           DATE                   TEXT    NOT NULL);''')
        table.commit()
        
        table.close()
        
    def insert_record_patient(self, db_name, record):
        #insert items into PATIENT table
        table = sql.connect(db_name)
        table.execute('INSERT INTO PATIENT VALUES (?,?,?,?)', record)
        table.commit()
        
    def insert_record_blsuggar(self, db_name, record):
        #insert items into BLSUGGAR table
        table = sql.connect(db_name)
        table.execute('INSERT FROM BLSUGGAR VALUES (?,?,?,?)', record)
        table.commit()
        
    def remove_record(self, db_name, record):
        # Deletes item from Database
        table = sql.connect(db_name)
        #table.execute('DELETE FROM PATIENT VALUES (?,?,?,?)', record)
        table.execute('DELETE FROM PATIENT WHERE NAME=?', (record,))
        table.commit()
        
    def remove_record_item(self, db_name, item):
        # Deletes item from Database
        table = sql.connect(db_name)
        table.execute('DELETE FROM PATIENT WHERE VALUES (?,?,?,?)', (item,))
        table.commit()
        
    def db_print(self, db_name):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        # Prepare SQL query to INSERT a record into the database.
        condition = "SELECT * FROM PATIENT \
               WHERE ID > '%d'" % (0)

        # Creates a list to store output values
        data = [] 
        
        try:
            # Execute the SQL command
            cursor.execute(condition)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                id_ = row[0]
                name = row[1]
                age = row[2]
                birthday = row[3]
                # Collects information an stores it into array
                #value = "%d,    %s,    %d,    %s" % (id_, name, age, birthday)
                value = ( id_, name, age, birthday)
                data.append(value)

        except:
            ers.errors_().error_messages(5)
            print('Error: cannot fetch data') 
        
        # disconnect from server
        table.close()
        return data
    
    # Navigation to the database possible   
    def db_navagation(self):
        
        print('Implementation needed')
        
    # Deletes item from Database
    def remove_item(self, itm):
        
        print('Implementation needed')
    
    def get_statement(self, text1, text2, text3, text4):
        #turn text boxes into text
        txt = '(' + text1 + ',' + text2 + ',' + text3 + ',' + text4 + ')'
        
        return txt
    
    # Retrieves the patient name
    def get_record(self, db_name, key):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM PATIENT \
               WHERE ID == '%d'" % (key)
        
        cursor.execute(condition)
        name_ = cursor.fetchone()
        # returns the patient name
        return name_[1]
    
    # Retrieves the patient record according matching a ID
    def get_patient(self, db_name, ID):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM PATIENT \
               WHERE ID == '%d'" % (ID)
        
        cursor.execute(condition)
        record_ = cursor.fetchone()
        
        return record_
        
    
