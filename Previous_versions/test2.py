# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:49:39 2019

@author: maria
"""
#from functions.PhoneBook_Project_functions2 import *
import sqlite3

conn=sqlite3.connect("phoneBookProjectx.db")
c=conn.cursor()




#create_table()
#store_data_in_variables()
#people_data_entry()
#business_data_entry()

#create_practice()
import requests

def play1():
    c.execute("SELECT postcode FROM businesses ")
    count=0
    for row in c.fetchall():
        count+=1
        print("This is count: ",count)
        current_postcode= row[0] 
        current_postcode=current_postcode.replace(" ","")
        print("Current postcode is: ",current_postcode)
        c.execute("SELECT postcode FROM practice WHERE postcode = ?", (current_postcode,))
        results=c.fetchall()
        print("results is: ",results)
        print(type(results))
        if len(results)<1:
            #print(type(postcode))
            print("Current_postcode is: ",current_postcode)
            #print(postcode)
            endpoint_postcode="https://api.postcodes.io/postcodes/"
            test_postcode_url=(endpoint_postcode+current_postcode)
            print(test_postcode_url)
            postcode_response=requests.get(endpoint_postcode+current_postcode)
            data_postcode=postcode_response.json()
            print(data_postcode['status'])
            global latitude
            global longitude
            #print(type(data_postcode))
            if data_postcode['status'] ==200:         
                latitude=data_postcode['result']['latitude']
                print(latitude)
                longitude=data_postcode["result"]["longitude"]
                print(longitude)
                #check_postcode_exists_and_if_not_populate_practice(current_postcode,latitude,longitude)
                print("insert into practice table our current_postcode ",current_postcode," and latitude ",latitude," and longitude ",longitude)
                c.execute("INSERT INTO practice(postcode,latitude,longitude) VALUES(?,?,?)", (current_postcode,latitude,longitude))
                conn.commit()
            else:
                print("Your postcode status is not 200!")
        else:
            print("Results has a len larger than 1, or tha postcode already exists")
            
def play2():                               ############this is the final version before separating it into smaller function
    c.execute("SELECT postcode FROM businesses ")
    
    count=0
    for row in c.fetchall():
        count+=1
        current_postcode= row[0] 
        current_postcode=current_postcode.replace(" ","")
        c.execute("SELECT postcode FROM practice WHERE postcode = ?", (current_postcode,))
        results=c.fetchall()
        if len(results)<1:
            endpoint_postcode="https://api.postcodes.io/postcodes/"
            postcode_response=requests.get(endpoint_postcode+current_postcode)
            data_postcode=postcode_response.json()
            global latitude
            global longitude
            if data_postcode['status'] ==200:         
                latitude=data_postcode['result']['latitude']
                longitude=data_postcode["result"]["longitude"]
                c.execute("INSERT INTO practice(postcode,latitude,longitude) VALUES(?,?,?)", (current_postcode,latitude,longitude))
                conn.commit()
            else:
                print("Your postcode status is not 200!")
        else:
            print("Results has a len larger than 1, or tha postcode already exists")
            

                   
play1()
#populate_location_with_postcodes_from_people()
#populate_location_with_postcodes_from_businesses()
            
