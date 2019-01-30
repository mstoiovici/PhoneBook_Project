#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
import sqlite3, json
import requests

def main(environment):
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
    cursor_connection=connection_factory(environment)
    create_table(cursor_connection[0])
    data=store_data_in_variables()
    business_data_entry(data[0], cursor_connection)
    people_data_entry(data[1], cursor_connection)
    populate_location_with_postcodes_from_businesses(cursor_connection)
    populate_location_with_postcodes_from_people(cursor_connection)

def connection_factory(environment):
    """
    This takes an environment variable and returns a cursor c and connection conn.
    """
    conn=sqlite3.connect("{}_phoneBookProject.db".format(environment))
    c=conn.cursor()
    return c, conn

def create_table(database_cursor):
    """
    This function takes one argument, database_cursor and has no output.
    It creates three tables in the database called businesses, people and location.
    """
    database_cursor.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    database_cursor.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    database_cursor.execute("CREATE TABLE IF NOT EXISTS location(postcode TEXT , latitude TEXT, longitude TEXT)")
   
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


def business_data_entry(business_data, database_connection):   
    """
    This function takes two arguments: data from a json file and an argument containing the cursor and connection to the database.
    It inserts this data into a table called businesses.
    """
    for item in business_data:
        values_list=list(item.values())
        #print(values_list)
        database_connection[0].execute("INSERT INTO businesses(business_name, adress_line_1,adress_line_2, adress_line_3,postcode, country,telephone_number,business_category) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        database_connection[1].commit()

def people_data_entry(people_data, database_connection):
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
        database_connection[0].execute("INSERT INTO people(first_name,last_name,adress_line_1,adress_line_2,adress_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        database_connection[1].commit()
    
    


def populate_location_with_postcodes_from_businesses(cursor_connection):
    """
    This function has one argument cursor_connection and has no output. It checks if the postcodes from 
    businesses table are already in the location table and if not, it retrieves the coordinates and inserts
    both into the location table.
    """
    cursor_connection[0].execute("SELECT postcode FROM businesses ") 
    for row in cursor_connection[0].fetchall():
        results=check_if_postcode_exists_in_location(row,cursor_connection)
        if len(results[0])<1:
            retrieve_coordinates_and_insert_into_location(results[1],cursor_connection)
        else:
            print("Results has a len larger than 1, businesses")
            
def populate_location_with_postcodes_from_people(cursor_connection):
    """
    This function has one argument cursor_connection and has no output. It checks if the postcodes from 
    people table are already in the location table and if not, it retrieves the coordinates and inserts
    both into the location table.
    """
    cursor_connection[0].execute("SELECT postcode FROM people ") 
    for row in cursor_connection[0].fetchall():
        results = check_if_postcode_exists_in_location(row,cursor_connection)
        if len(results[0])<1:
            retrieve_coordinates_and_insert_into_location(results[1],cursor_connection)
        else:
            print("Results has a len larger than 1, or people")
                

    
def check_if_postcode_exists_in_location(row,database_cursor):
    """
    This function has 2 arguments row and database_cursor, it has one output, a tuple containing results and a postcode.???????????????????????????????????????????????????????????????????????????????????how to describe results?
    
    """
    postcode= row[0] 
    postcode=postcode.replace(" ","")
    database_cursor[0].execute("SELECT postcode FROM location WHERE postcode = ?", (postcode,))
    results=database_cursor[0].fetchall()
#    print(results)
    return results, postcode  
    

def retrieve_coordinates_and_insert_into_location(postcode,cursor_connection):
    """
    This function takes 2 arguments: a postcode and cursor_connection and returns  a tuple containing longitude and latitude.
    """
    endpoint_postcode="https://api.postcodes.io/postcodes/"
    postcode_response=requests.get(endpoint_postcode+postcode)
    data_postcode=postcode_response.json()
    if data_postcode['status'] ==200:         
        latitude=data_postcode['result']['latitude']
        longitude=data_postcode["result"]["longitude"]
        cursor_connection[0].execute("INSERT INTO location(postcode,latitude,longitude) VALUES(?,?,?)", (postcode,latitude,longitude))
        cursor_connection[1].commit()
        return longitude, latitude
    else:
        print("Your postcode status is not 200!")
    
    
    





    
