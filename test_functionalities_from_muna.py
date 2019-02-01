# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:56:04 2019

@author: maria
"""

import unittest
#from unitte
import sqlite3
from PhoneBook_Project_functions2_from_Muna import *

class Test_Phonebook(unittest.TestCase):
    def test_dbs(self):
        self.assertTrue(check_db("mariana_phoneBookProject2.db"))
    def test_connection(self):
        self.assertTrue(connection_factory("mariana"))
    def test_get_businesses(self):
        self(searchBusinessType()):
        

if __name__=="__main__":
    unittest.main() 