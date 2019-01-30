#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""


import sqlite3, json
import requests

conn=sqlite3.connect("Mariana_phoneBookProject.db")
c=conn.cursor()


def get_database_with_three_populated_tables():
    """
    This function has one input, the name of the database and no outputs. This function calls other sub-functions which:
        - creates the database
        - creates the tables
        - stores the data from the json files into a variable
        - populates the businesses table with data from the json file
        - populates the people table with data from the json file
        - populates the location table with postcodes from the businesses table, alongside 
          retrieving and adding the longitude and latitude for those postocodes
        - populates the location table with postcodes from the people table, alongside 
          retrieving and adding the longitude and latitude for those postocodes
    """
    
    create_table()
    data=store_data_in_variables()
    business_data_entry(data[0])
    people_data_entry(data[1])
    populate_location_with_postcodes_from_businesses()
    populate_location_with_postcodes_from_people()


  



def create_table():
    """
    This function takes one argument, database_cursor and has no output.
    It creates three tables in the database called businesses, people and location.
    """
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS location(postcode TEXT , latitude TEXT, longitude TEXT)")
   
def store_data_in_variables():
    """
    This function has no arguments and returns a tuple of json data.
    """
    with open('business.json') as business:
        business_data=json.load(business)
    with open('people.json') as people:
        people_data=json.load(people)
    #print("business_data: ",business_data)
    #print("people_data: ",people_data)
    return business_data,people_data


def business_data_entry(business_data):   
    """
    This function takes two arguments: data from a json file and an argument containing the cursor and connection to the database.
    It inserts this data into a table called businesses.
    """
    for item in business_data:
        values_list=list(item.values())
        #print(values_list)
        c.execute("INSERT INTO businesses(business_name, adress_line_1,adress_line_2, adress_line_3,postcode, country,telephone_number,business_category) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()

def people_data_entry(people_data):
    """
    This function takes two arguments: data from a json file and an argument containing the cursor and connection to the database.
    It inserts this data into a table called people.
    """
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
    
    


def populate_location_with_postcodes_from_businesses():
    """
    This function has one argument cursor_connection and has no output. It checks if the postcodes from 
    businesses table are already in the location table and if not, it retrieves the coordinates and inserts
    both into the location table.
    """
    c.execute("SELECT postcode FROM businesses ") 
    for row in c.fetchall():
        results=check_if_postcode_exists_in_location(row)
        if len(results[0])<1:
            retrieve_coordinates_and_insert_into_location(results[1])
        else:
            print("Results has a len larger than 1, businesses")
            
def populate_location_with_postcodes_from_people():
    """
    This function has one argument cursor_connection and has no output. It checks if the postcodes from 
    people table are already in the location table and if not, it retrieves the coordinates and inserts
    both into the location table.
    """
    c.execute("SELECT postcode FROM people ") 
    for row in c.fetchall():
        results = check_if_postcode_exists_in_location(row)
        if len(results[0])<1:
            retrieve_coordinates_and_insert_into_location(results[1])
        else:
            print("Results has a len larger than 1, or people")
                

    
def check_if_postcode_exists_in_location(row):
    """
    This function has 2 arguments row and database_cursor, it has one output, a tuple containing results and a postcode.???????????????????????????????????????????????????????????????????????????????????how to describe results?
    
    """
    postcode= row[0] 
    postcode=postcode.replace(" ","")
    c.execute("SELECT postcode FROM location WHERE postcode = ?", (postcode,))
    results=c.fetchall()
#    print(results)
    return results, postcode  
    

def retrieve_coordinates_and_insert_into_location(postcode):
    """
    This function takes 2 arguments: a postcode and cursor_connection and returns  a tuple containing longitude and latitude.
    """
    endpoint_postcode="https://api.postcodes.io/postcodes/"
    postcode_response=requests.get(endpoint_postcode+postcode)
    data_postcode=postcode_response.json()
    if data_postcode['status'] ==200:         
        latitude=data_postcode['result']['latitude']
        longitude=data_postcode["result"]["longitude"]
        c.execute("INSERT INTO location(postcode,latitude,longitude) VALUES(?,?,?)", (postcode,latitude,longitude))
        conn.commit()
        return longitude, latitude
    else:
        print("Your postcode status is not 200!")
    
    
    
def read_from_db_all(apple):
    c.execute('SELECT * FROM businesses WHERE business_category=? ', (apple,))
    for row in c.fetchall():
        print(row)

def read_from_db2():
    c.execute('SELECT*FROM stuffToBuild WHERE value=8 and unix>1534855733 and unix<1547033137')
    for row in c.fetchall():
        print(row[0])


read_from_db_all("Computers")

    
