# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:20:33 2019

@author: maria
"""

import unittest
from functionalities import *

from PhoneBook_Project_functions import *


class TestFunctionalities(unittest.TestCase):  
    def test_check_if_db_exists(self):
        self.assertTrue(check_if_db_exists("mariana_phoneBookProject2.db"))    
    def test_getCursor(self):
        self.assertTrue(getCursor("mariana"))


if __name__=="__main__":
    unittest.main()
