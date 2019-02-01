# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:56:39 2019

@author: maria
"""

from PhoneBook_Project_functions2_from_Muna import *
def getBusinesses(city=None, business_category=None, business_name=None):
    cursor, connection = connection_factory("mariana")
    if city != None:
        query = "SELECT business_name FROM businesses WHERE adress_line_2=?"
        cursor.execute(query,(city,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    elif business_category != None:
        query2 = "SELECT business_name FROM businesses WHERE business_category=?"
        cursor.execute(query2,(business_category,))
        results1 = cursor.fetchall()
        for row in results1:
            print(row)
    elif business_name != None:
        query2 = "SELECT * FROM businesses WHERE business_name=?"
        cursor.execute(query2,(business_name,))
        results1 = cursor.fetchall()
        for row in results1:
            print(row)
#getBusinesses("London", "Toys")  
#getBusinesses(business_category="Toys") 
#getBusinesses(business_name="Yodoo") 
            
def searchBusinessType():
    cursor, connection = connection_factory("mariana")
    business_category = input("Business category: ")
    country=input("Business location: ")
    if business_category != None:
        query = "SELECT * FROM businesses WHERE business_category=? AND adress_line_3=?"
        cursor.execute(query,(business_category,country,))
        results1 = cursor.fetchall() 
        count=0
        for row in results1:
            count+=1
            print(row)
            if count >=50:
                break
            
#searchBusinessType()

#def searchBusinessTypex():
#    cursor, connection = connection_factory("mariana")
#    
#    country=input("Business location: ")
#    if country != None:
#        query = "SELECT * FROM businesses WHERE adress_line_3=?"
#        cursor.execute(query,(country,))
#        results1 = cursor.fetchall() 
#        count=0
#        for row in results1:
#            count+=1
#            print(row)
#            print("--------",count,"--------")
#            if count >=50:
#                break        
#        
#searchBusinessTypex()    