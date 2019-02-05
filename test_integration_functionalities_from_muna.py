# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:47:31 2019

@author: maria
"""

from functionalities_from_muna import *
import os
import requests

class TestEngine():
    def test_check_db(self):
        self.check = check_db("mariana")
        if self.check:
            return True
        else:
            return False
        
    def test_get_cursor(self):
        self.cursor=get_cursor("mariana")
        if self.cursor !=None :
            return True
        else:
            return False
        
    def test_get_business_type(self):
        
        self.business_type=get_business_type()
        if  self.business_type !=None:
            return True
        else:
            return False
        
    def test_check_if_input_business_type_is_in_database(self):
        self.cursor=get_cursor("mariana")
        if self.cursor !=None :
       
            self.checked_input=check_if_input_business_type_is_in_database(self.cursor)
            if self.checked_input !=None:
                return True
            else:
                return False
        else:
            
            return "no cursor"
               
        
    def runTests(self):
        print(self.test_check_db())
        print(self.test_get_cursor())
        print (self.test_get_business_type())
        print (self.test_check_if_input_business_type_is_in_database())
        
        

if __name__== "__main__":
    test_integration = TestEngine()
    test_integration.runTests()