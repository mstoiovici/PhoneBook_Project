# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:56:04 2019

@author: maria
"""



import unittest
import sqlite3
from functionalities_file import *
#from PhoneBook_Project_functions2_from_Muna import *

class Test_Phonebook(unittest.TestCase):
    def test_dbs(self):
        self.assertTrue(check_db("mariana_phoneBookProject2.db"))
    def test_get_cursor(self):
        self.assertTrue(get_cursor("mariana"))
##        
        
if __name__=="__main__":
    unittest.main() 
    
