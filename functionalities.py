# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:14:30 2019

@author: maria
"""

import sqlite3
import os
from PhoneBook_Project_functions import *

def check_if_db_exists(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
def getCursor(environment):
    conn=sqlite3.connect("{}_phoneBookProject.db".format(environment))
    cursor=conn.cursor()
    return cursor
def findBusinessType(c):
    """returns all businessType, businessName and location True
    """
    result= input("what do you want? ")
    c.execute('SELECT * FROM businesses WHERE business_category=? ', (result,))
    for row in c.fetchall():
        print(row)



#findBusinessType(getdb("mariana"))


