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
        
#    def test_get_business_type(self):
#        
#        self.business_type=get_business_type()
#        if  self.business_type !=None:
#            return True
#        else:
#            return False
        
    def test_check_if_input_business_type_is_in_database(self):
        self.cursor,self.connection=get_cursor("mariana")
        
        if self.cursor !=None :
       
            self.checked_input=check_if_input_business_type_is_in_database(self.cursor)
            if self.checked_input !=None:
                return True
            else:
                return False
        else:
            
            return "no cursor"
        
        
        
    def test_get_input_postcode_and_coordinates_for_input_postcode(self):
        self.input_postcode=get_input_postcode_and_coordinates_for_input_postcode()
        if self.input_postcode != None:
            return True
        else:
            return False
        
    def test_get_information_for_businesses_with_input_business_type(self):
        self.cursor,self.connection=get_cursor("mariana")
        if self.cursor !=None :
            self.information_for_businesses=get_information_for_businesses_with_input_business_type(self.cursor,"toys")        
            if self.information_for_businesses !=None:
                return True
            else:
                return False
    def test_get_coordinates_for_postcode(self):
        self.coordinates=get_coordinates_for_postcode("se109jp")
        if self.coordinates !=None:
            return True
        else:
            return False
        
    def test_distance(self):
        self.cursor,self.connection=get_cursor("mariana")
        if self.cursor !=None :
        
            self.business_info_list=get_information_for_businesses_with_input_business_type(self.cursor,"toys")   
            self.coordinates=get_coordinates_for_postcode("se109jp")
            self.business_info_with_distance=distance(self.business_info_list,self.coordinates[0],self.coordinates[1])
            if self.business_info_with_distance != None:
                return True
            else:
                return False
            
    def test_convert_businesses_info_list_into_dictionary(self ):
        self.cursor,self.connection=get_cursor("mariana")
        if self.cursor !=None :
            self.business_info_list=get_information_for_businesses_with_input_business_type(self.cursor,"toys")
            self.businesses_info_list_into_dictionary=convert_businesses_info_list_into_dictionary(self.business_info_list)
            if self.businesses_info_list_into_dictionary !=None :
                return True
            else:
                return False
            
    def test_sort_result_by_distance(self):
        self.cursor,self.connection=get_cursor("mariana")
        if self.cursor !=None :
            self.business_info_list=get_information_for_businesses_with_input_business_type(self.cursor,"toys")
            self.businesses_info_list_into_dictionary=convert_businesses_info_list_into_dictionary(self.business_info_list)
            self.sorted_result=sort_result_by_distance(self.businesses_info_list_into_dictionary)
            if self.sorted_result !=None:
                return True
            else:
                return False
        
    
    def runTests(self):
        print(self.test_check_db())
        print(self.test_get_cursor())
        print (self.test_check_if_input_business_type_is_in_database())
        print(self.test_get_input_postcode_and_coordinates_for_input_postcode())
        print(self.test_get_information_for_businesses_with_input_business_type())
        print(self.test_get_coordinates_for_postcode())
        print(self.test_distance())
        print(self.test_convert_businesses_info_list_into_dictionary())
        print(self.test_sort_result_by_distance())
        

if __name__== "__main__":
    test_integration = TestEngine()
    test_integration.runTests()