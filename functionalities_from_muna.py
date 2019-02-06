# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:56:39 2019

@author: maria
"""



import sqlite3
import os
from PhoneBook_Project_functions import *
import requests
from math import sin, cos, sqrt, atan2, radians
from collections import defaultdict

def main_functionalities(environment):
    if check_db(environment):
        cursor, connection= get_cursor(environment)
        business_type=check_if_input_business_type_is_in_database(cursor)
        long1, lat1=get_input_postcode_and_coordinates_for_input_postcode()
        businesses_info_list=get_information_for_businesses_with_input_business_type(cursor,business_type)
        businesses_info_list_with_distance=distance(businesses_info_list,long1,lat1)
        result=convert_businesses_info_list_into_dictionary(businesses_info_list_with_distance )
        sorted_result=sort_result_by_distance(result)
    else:
        print("The path to this database is not available")
    return sorted_result
        
            
    
def check_db(environment):
    if os.path.exists("{}_phoneBookProject.db".format(environment)):
        return True
    else:
        return False

#This function does not need to be run in this file, it's only purpose is to test it
#with unit test to check if the connection exists. This connection_factory(environment) should have been already tested with unittest in a real work scenario.
def get_cursor(environment):
    cursor, connection = connection_factory(environment)
    return cursor, connection

            
def check_if_input_business_type_is_in_database(cursor):  
    
    while True:
        try:
            business_type=input("Please specify the business type:\n").title()
#            print("hello1",business_type,cursor)
#            print(type(cursor))
            if business_type.isdigit():
                raise character_error
            cursor.execute("SELECT business_category FROM businesses WHERE business_category=?", (business_type,))
            results = cursor.fetchall()
            for index in range(len(results)-1):
                
                if business_type in results[index]:
#                    print("Mariana is the best.")
                    return business_type
                else:
#                    print("Muna is the best!")
                    raise Exception
            
        except Exception as character_error:
            print("Please only use characters.")
        except Exception as e:
            print(e)
                 
                
              
def get_input_postcode_and_coordinates_for_input_postcode():
    while True:
        try:
            input_postcode=input("Please specify the postcode:\n")
            input_postcode=input_postcode.replace(" ","")
            endpoint_postcode="https://api.postcodes.io/postcodes/"
            postcode_response=requests.get(endpoint_postcode+input_postcode)
            data_postcode=postcode_response.json()
            if data_postcode['status'] ==200:
                lat1=data_postcode['result']['latitude']
                long1=data_postcode["result"]["longitude"]
#                print(long1, lat1)
                return long1, lat1
            else:
                raise postcode_not_valid
                
        except Exception as postcode_not_valid: 
            print("The postcode you provided is not valid!")

def get_information_for_businesses_with_input_business_type(cursor,business_type):
    
  
    cursor.execute("SELECT business_name, telephone_number, postcode FROM businesses WHERE business_category=?", (business_type,)) 
    results = cursor.fetchall()
    businesses_info_list=[]
#    print(results)
#    print(type(results))
    for row in results:
#        print(row)
        row=list(row)
#        print(type(row))
#        print(row)
        postcode=row[2]
#        print(postcode)
        coordinates=get_coordinates_for_postcode(postcode)
        coordinates=list(coordinates)
#        print(coordinates)
        row.extend(coordinates)
#        print(row)
        businesses_info_list.append(row)
#    print(businesses_info_list)
    return businesses_info_list

def get_coordinates_for_postcode(postcode):
    endpoint_postcode="https://api.postcodes.io/postcodes/"
    postcode_response=requests.get(endpoint_postcode+postcode)
    data_postcode=postcode_response.json()
    if data_postcode['status'] ==200:
        latitude=data_postcode['result']['latitude']
        longitude=data_postcode["result"]["longitude"]
#        print(longitude, latitude)
        return longitude, latitude
    else:
        print("The postcode you provided is not valid!!!!")
   
        
    
def distance(businesses_info_list,long1,lat1):
    
   
    for index in range(len(businesses_info_list)-1):
        long2=businesses_info_list[index][3]
        lat2=businesses_info_list[index][4]
        R = 6373.0 # approximate radius of earth in km
        
        dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a=abs(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        hdist = R * c
        hdist=int(hdist)
    #        print(hdist)
    #        print(businesses_info_list[index])
        
        businesses_info_list[index].append(hdist)
#        print(businesses_info_list[index])
#    print (businesses_info_list)
    
#    print("I'm here")
    return businesses_info_list


def convert_businesses_info_list_into_dictionary(businesses_info_list ):
    
    d = defaultdict(list)     
    for index in range(len(businesses_info_list)-1):
        list1= businesses_info_list[index]
#    print(list1)
        d[list1[0]] += list1[1:]
    #print(dict(d))
    d=dict(d)
    return d


def sort_result_by_distance(result):
   
    sorted_result = sorted(result.items(),key=lambda kv:kv[1][-1])
#    print(sorted_result)
    return sorted_result




#main_functionalities("mariana")




























    
    
    
            


















































































































































































#from PhoneBook_Project_functions2_from_Muna import *
#def getBusinesses(city=None, business_category=None, business_name=None):
#    cursor, connection = connection_factory("mariana")
#    if city != None:
#        query = "SELECT business_name FROM businesses WHERE adress_line_2=?"
#        cursor.execute(query,(city,))
#        results = cursor.fetchall()
#        for row in results:
#            print(row)
#    elif business_category != None:
#        query2 = "SELECT business_name FROM businesses WHERE business_category=?"
#        cursor.execute(query2,(business_category,))
#        results1 = cursor.fetchall()
#        for row in results1:
#            print(row)
#    elif business_name != None:
#        query2 = "SELECT * FROM businesses WHERE business_name=?"
#        cursor.execute(query2,(business_name,))
#        results1 = cursor.fetchall()
#        for row in results1:
#            print(row)
#getBusinesses("London", "Toys")  
#getBusinesses(business_category="Toys") 
#getBusinesses(business_name="Yodoo") 
            
#def searchBusinessType():
#    cursor, connection = connection_factory("mariana")
#    business_category = input("Business category: ")
#    country=input("Business location: ")
#    if business_category != None:
#        query = "SELECT * FROM businesses WHERE business_category=? AND adress_line_3=?"
#        cursor.execute(query,(business_category,country,))
#        results1 = cursor.fetchall() 
#        count=0
#        for row in results1:
#            count+=1
#            print(row)
#            if count >=50:
#                break
            
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