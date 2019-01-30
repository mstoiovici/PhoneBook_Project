#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
import sqlite3
import requests

conn=sqlite3.connect("db/phoneBookProject2.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS location(postcode TEXT , latitude TEXT, longitude TEXT)")

def create_practice():
    
    c.execute("CREATE TABLE IF NOT EXISTS practice(postcode TEXT,latitude TEXT, longitude TEXT)")

def people_data_entry():
    for item in people_data:
        #print("first item: ",item)
        #print(type(item))
        #print("-------------------------------")
        #key_list=list(item.keys())
        values_list=list(item.values())
        #print(key_list)
        #print(values_list)
        c.execute("INSERT INTO people(first_name,last_name,adress_line_1,adress_line_2,adress_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
    
    

def business_data_entry():   
    for item in business_data:
        values_list=list(item.values())
        #print(values_list)
        c.execute("INSERT INTO businesses(business_name, adress_line_1,adress_line_2, adress_line_3,postcode, country,telephone_number,business_category) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
    
    

     

        

import json
def store_data_in_variables():
    global business_data
    global people_data
    with open('jeison/business.json') as business:
        business_data=json.load(business)
    with open('jeison/people.json') as people:
        people_data=json.load(people)
    #print("business_data: ",business_data)
    #print("people_data: ",people_data)
    return business_data,people_data


 
def populate_location_with_postcodes_from_businesses():
    c.execute("SELECT postcode FROM businesses ") 
    for row in c.fetchall():
        check_if_postcode_exists_in_location(row)
        if len(results)<1:
            retrieve_coordinates_and_insert_into_location()
        else:
            print("Results has a len larger than 1, or tha postcode already exists")
            
def populate_location_with_postcodes_from_people():
    c.execute("SELECT postcode FROM people ") 
    for row in c.fetchall():
        check_if_postcode_exists_in_location(row)
        if len(results)<1:
            retrieve_coordinates_and_insert_into_location()
        else:
            print("Results has a len larger than 1, or tha postcode already exists")
                

    
def check_if_postcode_exists_in_location(row):
    global current_postcode
    current_postcode= row[0] 
    current_postcode=current_postcode.replace(" ","")
    c.execute("SELECT postcode FROM practice WHERE postcode = ?", (current_postcode,))
    global results
    results=c.fetchall()
          
    

def retrieve_coordinates_and_insert_into_location():
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
    
    
    




             

    
