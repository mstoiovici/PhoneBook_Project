# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:14:30 2019

@author: maria
"""

import sqlite3

def getdb(environment):
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
